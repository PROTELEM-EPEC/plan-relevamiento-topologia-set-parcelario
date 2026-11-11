"""
========================================================================================
SQUAD ARQUETIPO A - GIS, CATASTRO Y TOPOLOGÍA DE RED ELÉCTRICA EPEC
MÓDULO 02: Auditoría Topológica de Subestaciones, Clasificación y Tarifa Social
========================================================================================
"""

import os, sys, time, json
os.environ['PROJ_LIB'] = r'C:\Program Files\QGIS 4.2.0\share\proj'
os.environ['PROJ_DATA'] = r'C:\Program Files\QGIS 4.2.0\share\proj'

import duckdb
import geopandas as gpd
import pandas as pd
import numpy as np
from shapely.geometry import Point, box
from shapely import STRtree

print("=== [OPERADOR 2] INICIANDO AUDITORÍA TOPOLÓGICA Y CLASIFICACIÓN DE SETS ===")
start_time = time.time()

base_dir = r'D:\Proyectos\plan-relevamiento-topologia-set-parcelario'
data_dir = os.path.join(base_dir, 'data')
reports_dir = os.path.join(base_dir, 'reports')

sets_geojson = os.path.join(data_dir, 'vt_subestaciones_poly.geojson')
parcelas_parquet = os.path.join(data_dir, 'capa_parcelas_general_consolidada.parquet')
mzas_parquet = r'D:\Proyectos\antigravity-agents-repository\data\manzanas_alta_resolucion_provincial.parquet'
sumis_padron = r'D:\Proyectos\antigravity-agents-repository\data\summary\padron_nuevas_rutas_provincial_consolidado.parquet'

# 1. Cargar subestaciones
print("1. Cargando y preparando capas de subestaciones...")
gdf_sets = gpd.read_file(sets_geojson)
gdf_sets['geometry'] = gdf_sets['geometry'].buffer(0)
gdf_sets = gdf_sets[gdf_sets['geometry'].is_valid & (~gdf_sets['geometry'].is_empty)].copy()
gdf_sets['set_id'] = gdf_sets['id'].astype(str)
gdf_sets['ctmtbt_clean'] = gdf_sets['ctmtbt'].fillna('').astype(str).str.strip()

print(f"   Subestaciones operativas válidas: {len(gdf_sets):,}")

# 2. Cargar parcelas consolidadas
print("2. Cargando capa de parcelas general consolidada...")
df_parc = pd.read_parquet(parcelas_parquet)
# Filtrar aquellas con coordenadas válidas de Córdoba (aprox lat -35 a -29, lon -66 a -61)
df_parc = df_parc[
    (df_parc['centroide_lat'].between(-35.0, -29.0)) &
    (df_parc['centroide_lon'].between(-66.0, -61.0))
].copy()
print(f"   Parcelas con coordenadas válidas: {len(df_parc):,}")

# Convertir parcelas a puntos Shapely para spatial join eficiente
print("3. Indexando espacialmente parcelas y cruzando con polígonos de subestaciones...")
parc_points = [Point(xy) for xy in zip(df_parc['centroide_lon'], df_parc['centroide_lat'])]
gdf_parc = gpd.GeoDataFrame(df_parc, geometry=parc_points, crs="EPSG:4326")

# Spatial join: asignar cada parcela a la subestación que la contiene
joined_parc = gpd.sjoin(gdf_parc, gdf_sets[['id', 'ctmtbt', 'agf_codigo', 'estado', 'geometry']], how='left', predicate='within')
print(f"   Parcelas cruzadas espacialmente: {len(joined_parc):,}")

# Conteo de parcelas ubicadas dentro de alguna SET
parc_en_set = joined_parc[joined_parc['id'].notna()].copy()
parc_fuera_set = joined_parc[joined_parc['id'].isna()].copy()

print(f"   Parcelas dentro de polígonos de SET: {len(parc_en_set):,} ({len(parc_en_set)/len(joined_parc)*100:.1f}%)")
print(f"   Parcelas fuera de polígonos de SET (a verificar/expandir): {len(parc_fuera_set):,}")

# 4. Cargar Manzanas como Fallback para suministros/parcelas huérfanas
print("4. Cargando capa de manzanas de alta resolución para asignación por proximidad/fallback...")
df_mzas = pd.read_parquet(mzas_parquet)
df_mzas_val = df_mzas[
    (df_mzas['centro_lat'].between(-35.0, -29.0)) &
    (df_mzas['centro_lon'].between(-66.0, -61.0))
].copy()
mza_points = [Point(xy) for xy in zip(df_mzas_val['centro_lon'], df_mzas_val['centro_lat'])]
gdf_mzas = gpd.GeoDataFrame(df_mzas_val, geometry=mza_points, crs="EPSG:4326")

joined_mzas = gpd.sjoin(gdf_mzas, gdf_sets[['id', 'ctmtbt', 'geometry']], how='left', predicate='within')
print(f"   Manzanas asociadas a SET: {joined_mzas['id'].notna().sum():,} de {len(gdf_mzas):,}")

# 5. Detección de parcelas cortadas por los límites (Frontera de SET)
print("5. Auditando parcelas cortadas por las líneas perimetrales de las subestaciones...")
# Para detectar si la frontera de la SET corta la parcela:
# Creamos un buffer representativo del radio medio parcelario (~15 metros = ~0.00015 grados)
# Si el buffer intersecta la frontera (boundary) de la SET, la parcela queda cortada al medio.
sets_boundary = gdf_sets[['id', 'ctmtbt', 'geometry']].copy()
sets_boundary['geometry'] = sets_boundary['geometry'].boundary

# Cruce con parcelas cercanas a la frontera
# Hacemos sjoin con buffer de 15m (aprox 0.00015 deg)
gdf_parc_buffer = gdf_parc.copy()
gdf_parc_buffer['geometry'] = gdf_parc_buffer['geometry'].buffer(0.00015)

parc_cortadas = gpd.sjoin(gdf_parc_buffer, sets_boundary, how='inner', predicate='intersects')
print(f"   Parcelas que intersectan la línea perimetral de SET: {len(parc_cortadas):,}")

# Exportar log de excepciones de parcelas cortadas
if len(parc_cortadas) > 0:
    log_cortadas_path = os.path.join(reports_dir, 'log_excepciones_parcelas_cortadas_frontera.csv')
    df_cortadas_exp = parc_cortadas[[
        'nomenclatura', 'nomenclatura_manzana', 'nro_parcela', 'distrito', 'distrito_descripcion',
        'localidad', 'barrio', 'cant_suministros', 'cant_tarifa_social', 'ctmtbt', 'centroide_lat', 'centroide_lon'
    ]].rename(columns={'ctmtbt': 'set_ctmtbt_frontera'}).drop_duplicates(subset=['nomenclatura'])
    df_cortadas_exp.to_csv(log_cortadas_path, index=False)
    print(f"   -> Log de excepciones guardado en: {log_cortadas_path} ({len(df_cortadas_exp):,} parcelas únicas)")

# 6. Agregación y Clasificación de Subestaciones
print("6. Clasificando subestaciones según cantidad de suministros y Tarifa Social...")
set_stats = joined_parc.groupby(['id', 'ctmtbt']).agg(
    cant_parcelas=('nomenclatura', 'count'),
    cant_suministros=('cant_suministros', 'sum'),
    cant_tarifa_social=('cant_tarifa_social', 'sum'),
    distrito_principal=('distrito_descripcion', lambda x: x.mode()[0] if not x.empty else 'N/A'),
    localidad_principal=('localidad', lambda x: x.mode()[0] if not x.empty else 'N/A')
).reset_index()

# Mergear con el total de SETs para incluir las que tienen 0 suministros
df_sets_all = gdf_sets[['id', 'ctmtbt', 'agf_codigo', 'estado']].copy()
df_clasif = pd.merge(df_sets_all, set_stats, on=['id', 'ctmtbt'], how='left')
df_clasif['cant_parcelas'] = df_clasif['cant_parcelas'].fillna(0).astype(int)
df_clasif['cant_suministros'] = df_clasif['cant_suministros'].fillna(0).astype(int)
df_clasif['cant_tarifa_social'] = df_clasif['cant_tarifa_social'].fillna(0).astype(int)

# Calcular % Tarifa Social
df_clasif['pct_tarifa_social'] = np.where(
    df_clasif['cant_suministros'] > 0,
    (df_clasif['cant_tarifa_social'] / df_clasif['cant_suministros']) * 100.0,
    0.0
).round(2)

# Segmentación de Subestaciones
def categorizar_set(row):
    s = row['cant_suministros']
    if s >= 1000:
        return 'MEGA_SET (>=1000 sumis)'
    elif s >= 500:
        return 'GRANDE (500-999 sumis)'
    elif s >= 150:
        return 'MEDIANA (150-499 sumis)'
    elif s > 0:
        return 'PEQUEÑA (1-149 sumis)'
    else:
        return 'SIN_SUMINISTROS (0 sumis)'

df_clasif['categoria_set'] = df_clasif.apply(categorizar_set, axis=1)

# Flag de Alta Sensibilidad Social (>= 20% Tarifa Social)
df_clasif['sensibilidad_social_alta'] = df_clasif['pct_tarifa_social'] >= 20.0

print("\n--- DISTRIBUCIÓN DE SUBESTACIONES POR CATEGORÍA ---")
dist_cat = df_clasif['categoria_set'].value_counts()
for cat, count in dist_cat.items():
    print(f"   * {cat}: {count:,} SETs")

print(f"\n--- SUBESTACIONES CON ALTA SENSIBILIDAD SOCIAL (>=20% Tarifa Social): {df_clasif['sensibilidad_social_alta'].sum():,} SETs ---")

# Exportar resultados
clasif_path = os.path.join(reports_dir, 'resumen_clasificacion_subestaciones.csv')
df_clasif.to_csv(clasif_path, index=False)
print(f"   -> Clasificación guardada en: {clasif_path}")

clasif_parquet = os.path.join(data_dir, 'subestaciones_clasificadas.parquet')
df_clasif.to_parquet(clasif_parquet, index=False)
print(f"   -> Capa parquet guardada en: {clasif_parquet}")

print(f"=== AUDITORÍA TOPOLÓGICA Y CLASIFICACIÓN COMPLETADA EN {time.time() - start_time:.2f}s ===")
