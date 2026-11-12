"""
========================================================================================
SQUAD ÁGIL MULTI-AGENTE PM-OPERADORES - ARQUETIPO A (GIS / CATASTRO / REDES ELÉCTRICAS)
ETAPA 3 & 4: ANÁLISIS DE CALIDAD DE POLÍGONOS DE SUBESTACIONES & ESTABLECIMIENTO DEL
             PLAN DE RELEVAMIENTO A FUTURO (EPEC)
========================================================================================
Fuentes integradas:
1. data/subestaciones_clasificadas.parquet (5.296 SETs provinciales clasificadas)
2. data/vt_subestaciones_poly.geojson (5.296 polígonos de SET en EPSG:4326)
3. reports/log_excepciones_parcelas_cortadas_frontera.csv (110.230 parcelas cortadas)
4. data/georef_relevamiento_suministros.parquet (473.762 suministros de georef.relevamiento)
5. data/suministros_provincial_completo.parquet (1.208.097 suministros provinciales)
6. reports/anomalias_parcelas_duplicadas_en_manzana.csv (69.011 anomalías catastrales)
========================================================================================
"""
import os
import sys
import json
import duckdb
import pandas as pd
import numpy as np
import geopandas as gpd

# Configurar rutas seguras PROJ
os.environ['PROJ_LIB'] = r'C:\Program Files\QGIS 4.2.0\share\proj'
os.environ['PROJ_DATA'] = r'C:\Program Files\QGIS 4.2.0\share\proj'

repo_dir = r'D:\Proyectos\plan-relevamiento-topologia-set-parcelario'
data_dir = os.path.join(repo_dir, 'data')
reports_dir = os.path.join(repo_dir, 'reports')
viewer_data_dir = os.path.join(repo_dir, 'viewer', 'data')
docs_dir = os.path.join(repo_dir, 'docs')
os.makedirs(viewer_data_dir, exist_ok=True)

p_sets = os.path.join(data_dir, 'subestaciones_clasificadas.parquet')
p_geojson = os.path.join(data_dir, 'vt_subestaciones_poly.geojson')
p_cortadas = os.path.join(reports_dir, 'log_excepciones_parcelas_cortadas_frontera.csv')
p_dups = os.path.join(reports_dir, 'anomalias_parcelas_duplicadas_en_manzana.csv')
p_rel = os.path.join(data_dir, 'georef_relevamiento_suministros.parquet')
p_sumis = r'D:\Proyectos\antigravity-agents-repository\data\suministros_provincial_completo.parquet'

print("=" * 80)
print("AUDITORÍA DE CALIDAD DE POLÍGONOS & PLAN DE RELEVAMIENTO A FUTURO EPEC")
print("=" * 80)

# --------------------------------------------------------------------------------------
# 1. MÉTRICAS GEOMÉTRICAS Y COMPACIDAD DE POLÍGONOS
# --------------------------------------------------------------------------------------
print("\n1. Computando geometría, superficie y compacidad Polsby-Popper para 5.296 SETs...")
gdf_sets = gpd.read_file(p_geojson)
gdf_metric = gdf_sets[['id', 'ctmtbt', 'geometry']].to_crs(epsg=32720)

gdf_sets['area_m2'] = gdf_metric.geometry.area.round(2)
gdf_sets['perimetro_m'] = gdf_metric.geometry.length.round(2)
gdf_sets['compacidad_polsby'] = np.where(
    gdf_sets['perimetro_m'] > 0,
    (4 * np.pi * gdf_sets['area_m2']) / (gdf_sets['perimetro_m'] ** 2),
    0.0
).round(4)

# --------------------------------------------------------------------------------------
# 2. PROCESAMIENTO DE PARCELAS CORTADAS POR FRONTERA
# --------------------------------------------------------------------------------------
print("2. Procesando incidencias de parcelas cortadas por límite perimetral...")
df_cortadas = pd.read_csv(p_cortadas)
cortadas_per_set = df_cortadas.groupby('set_ctmtbt_frontera').agg(
    parcelas_cortadas=('nomenclatura', 'count'),
    sumis_en_cortadas=('cant_suministros', 'sum'),
    ts_en_cortadas=('cant_tarifa_social', 'sum')
).reset_index().rename(columns={'set_ctmtbt_frontera': 'ctmtbt'})

# --------------------------------------------------------------------------------------
# 3. ENRIQUECIMIENTO DE SUBESTACIONES CON CALIDAD GEOMÉTRICA
# --------------------------------------------------------------------------------------
print("3. Integrando métricas topológicas sobre el catálogo maestro de subestaciones...")
df_sets_base = pd.read_parquet(p_sets)

df_set_full = df_sets_base.merge(
    gdf_sets[['ctmtbt', 'area_m2', 'perimetro_m', 'compacidad_polsby']].drop_duplicates(subset=['ctmtbt']),
    on='ctmtbt', how='left'
).merge(cortadas_per_set, on='ctmtbt', how='left')

df_set_full['parcelas_cortadas'] = df_set_full['parcelas_cortadas'].fillna(0).astype(int)
df_set_full['sumis_en_cortadas'] = df_set_full['sumis_en_cortadas'].fillna(0).astype(int)
df_set_full['ts_en_cortadas'] = df_set_full['ts_en_cortadas'].fillna(0).astype(int)

df_set_full['pct_parcelas_cortadas'] = np.where(
    df_set_full['cant_parcelas'] > 0,
    (df_set_full['parcelas_cortadas'] / df_set_full['cant_parcelas']) * 100.0,
    0.0
).round(2)

# Clasificación del Polígono según Calidad Topológica
def clasificar_calidad_poligono(row):
    cortadas = row['parcelas_cortadas']
    pct = row['pct_parcelas_cortadas']
    comp = row['compacidad_polsby']
    
    if cortadas == 0:
        return 'ALTA_LIMPIO (0 cortadas)'
    elif cortadas <= 10 or (pct <= 5.0 and comp >= 0.15):
        return 'ALTA_LEVE (1-10 cortadas)'
    elif cortadas <= 30 or pct <= 20.0:
        return 'MEDIA_MODERADO (11-30 cortadas)'
    else:
        return 'BAJA_CONFLICTO (>30 cortadas)'

df_set_full['calidad_poligono'] = df_set_full.apply(clasificar_calidad_poligono, axis=1)

# --------------------------------------------------------------------------------------
# 4. CRUCE CON GEOREF.RELEVAMIENTO (ESTADO DE RELEVAMIENTO EFECTIVO)
# --------------------------------------------------------------------------------------
print("4. Cruzando con registros históricos de georef.relevamiento...")
p_rel_df = pd.read_parquet(p_rel)
rel_counts = p_rel_df.groupby('rel_subestacion')['suministro'].count().to_dict()

def get_relevados(row):
    agf_ctmtbt = f"{row['agf_codigo']}-{row['ctmtbt']}"
    ctmtbt = str(row['ctmtbt'])
    
    if agf_ctmtbt in rel_counts:
        return rel_counts[agf_ctmtbt]
    elif ctmtbt in rel_counts:
        return rel_counts[ctmtbt]
    else:
        return 0

df_set_full['suministros_relevados'] = df_set_full.apply(get_relevados, axis=1)
df_set_full['suministros_pendientes'] = np.maximum(
    0, df_set_full['cant_suministros'] - df_set_full['suministros_relevados']
)
df_set_full['pct_avance_relevamiento'] = np.where(
    df_set_full['cant_suministros'] > 0,
    np.minimum(100.0, (df_set_full['suministros_relevados'] / df_set_full['cant_suministros']) * 100.0),
    0.0
).round(2)

# Estimación de Clientes Comunes CC en la SET
df_set_full['cant_clientes_cc'] = np.maximum(
    0, df_set_full['cant_suministros'] - df_set_full['cant_tarifa_social']
)

# --------------------------------------------------------------------------------------
# 5. MATRIZ DE PRIORIZACIÓN OPERATIVA PARA EL PLAN DE RELEVAMIENTO A FUTURO
# --------------------------------------------------------------------------------------
print("5. Construyendo Matriz de Priorización Operativa en 5 Cuadrantes...")

def clasificar_prioridad_futura(row):
    pend = row['suministros_pendientes']
    avance = row['pct_avance_relevamiento']
    calidad = row['calidad_poligono']
    ts_pct = row['pct_tarifa_social']
    
    if row['cant_suministros'] == 0:
        return '5_SIN_DEMANDA_O_ESPECIAL'
    elif avance >= 75.0 or pend < 30:
        return '4_AVANZADA_O_COMPLETADA'
    elif 'BAJA_CONFLICTO' in calidad and pend >= 50:
        return '3_SANEAMIENTO_TOPOLOGICO_PREVIO'
    elif ts_pct >= 20.0 and pend >= 30:
        return '2_SENSIBILIDAD_SOCIAL'
    else:
        return '1_RELEVAMIENTO_INMEDIATO'

df_set_full['prioridad_relevamiento_futuro'] = df_set_full.apply(clasificar_prioridad_futura, axis=1)

# Guardar Dataset Enriquecido de Subestaciones
parquet_out = os.path.join(data_dir, 'subestaciones_calidad_y_relevamiento.parquet')
df_set_full.to_parquet(parquet_out, index=False)
print(f"   -> Dataset enriquecido guardado en: {parquet_out}")

# Guardar Resumen de Calidad de Polígonos
csv_calidad_path = os.path.join(reports_dir, 'resumen_calidad_poligonos_subestaciones.csv')
res_calidad = df_set_full.groupby('calidad_poligono').agg(
    total_sets=('ctmtbt', 'count'),
    sumis_totales=('cant_suministros', 'sum'),
    sumis_relevados=('suministros_relevados', 'sum'),
    sumis_pendientes=('suministros_pendientes', 'sum'),
    parcelas_cortadas_totales=('parcelas_cortadas', 'sum'),
    compacidad_media=('compacidad_polsby', 'mean')
).reset_index()
res_calidad['pct_sets'] = (res_calidad['total_sets'] / len(df_set_full) * 100).round(2)
res_calidad.to_csv(csv_calidad_path, index=False)
print(f"   -> Resumen de calidad guardado en: {csv_calidad_path}")

# Guardar Matriz de Priorización
csv_prio_path = os.path.join(reports_dir, 'matriz_priorizacion_plan_futuro_sets.csv')
res_prio = df_set_full.groupby('prioridad_relevamiento_futuro').agg(
    total_sets=('ctmtbt', 'count'),
    sumis_totales=('cant_suministros', 'sum'),
    sumis_relevados=('suministros_relevados', 'sum'),
    sumis_pendientes=('suministros_pendientes', 'sum'),
    tarifa_social=('cant_tarifa_social', 'sum'),
    parcelas_cortadas=('parcelas_cortadas', 'sum')
).reset_index()
res_prio['pct_sets'] = (res_prio['total_sets'] / len(df_set_full) * 100).round(2)
res_prio.to_csv(csv_prio_path, index=False)
print(f"   -> Matriz de priorización guardada en: {csv_prio_path}")

# --------------------------------------------------------------------------------------
# 6. ANÁLISIS INTEGRAL POR PLAN DE LECTURA (DISTRIBUCIÓN 20 PLANES DE CÓRDOBA CAPITAL)
# --------------------------------------------------------------------------------------
print("\n6. Analizando avance, pendientes y perfil de clientes por Plan de Lectura...")

con = duckdb.connect()

q_planes = f"""
WITH base AS (
    SELECT 
        s.suministro,
        s.distrito,
        s.distrito_descripcion,
        CASE 
            WHEN TRY_CAST(s.grupo_lectura AS INTEGER) BETWEEN 1 AND 20 THEN 'Plan ' || LPAD(s.grupo_lectura, 2, '0')
            WHEN s.grupo_lectura IS NULL OR s.grupo_lectura = '' THEN 'Sin Plan'
            ELSE 'Plan ' || s.grupo_lectura
        END as plan,
        CASE
            WHEN s.tarifa ILIKE '%social%' OR s.tarifa ILIKE '%caren%' OR s.tarifa ILIKE '%indig%' THEN 'TARIFA_SOCIAL'
            WHEN s.tarifa ILIKE '%RESIDENCIAL%' OR s.tarifa ILIKE '%1.%' OR s.tarifa ILIKE '%GENERAL%' OR s.tarifa ILIKE '%2 %' OR s.tarifa ILIKE '%2.%' THEN 'CC'
            ELSE 'OTROS'
        END as tipo_cliente,
        CASE WHEN r.suministro IS NOT NULL THEN 1 ELSE 0 END as relevado
    FROM '{p_sumis}' s
    LEFT JOIN '{p_rel}' r ON s.suministro = r.suministro
    WHERE s.distrito = 1 OR s.distrito_descripcion ILIKE '%cordoba%'
)
SELECT 
    plan,
    count(*) as total_puntos,
    sum(relevado) as total_relevados,
    count(*) - sum(relevado) as total_pendientes,
    round(sum(relevado) * 100.0 / count(*), 2) as pct_avance,
    -- Pendientes desglosados
    sum(CASE WHEN relevado = 0 AND tipo_cliente = 'CC' THEN 1 ELSE 0 END) as pendientes_cc,
    sum(CASE WHEN relevado = 0 AND tipo_cliente = 'TARIFA_SOCIAL' THEN 1 ELSE 0 END) as pendientes_tarifa_social,
    sum(CASE WHEN relevado = 0 AND tipo_cliente = 'OTROS' THEN 1 ELSE 0 END) as pendientes_otros,
    -- Diagnóstico del Plan
    CASE 
        WHEN (sum(relevado) * 100.0 / count(*)) >= 80.0 THEN 'FASE_FINAL_REMANENTES'
        WHEN (sum(CASE WHEN relevado = 0 AND tipo_cliente = 'TARIFA_SOCIAL' THEN 1 ELSE 0 END) * 100.0 / NULLIF(count(*) - sum(relevado), 0)) >= 15.0 THEN 'SENSIBILIDAD_SOCIAL_PRIORITARIA'
        WHEN plan IN ('Plan 14', 'Plan 15', 'Plan 08', 'Plan 17', 'Plan 12') THEN 'RELEVAMIENTO_MASIVO_CC_INMEDIATO'
        ELSE 'RELEVAMIENTO_MIXTO_ESTANDAR'
    END as diagnostico_operativo
FROM base
WHERE plan LIKE 'Plan __' AND plan BETWEEN 'Plan 01' AND 'Plan 20'
GROUP BY plan
ORDER BY plan
"""

df_planes = con.execute(q_planes).df()
csv_planes_path = os.path.join(reports_dir, 'resumen_plan_avance_y_calidad.csv')
df_planes.to_csv(csv_planes_path, index=False)
print(f"   -> Resumen de planes guardado en: {csv_planes_path}")

# --------------------------------------------------------------------------------------
# 7. GENERACIÓN DEL PAYLOAD CONSOLIDADO PARA EL DASHBOARD WEB INTERACTIVO
# --------------------------------------------------------------------------------------
print("\n7. Actualizando datos interactivos del Dashboard Web (viewer/data/dashboard_data.js)...")

# Cargar muestras para compatibilidad total con el visor
muestra_cortadas = df_cortadas.head(300)[
    ['nomenclatura', 'nomenclatura_manzana', 'nro_parcela', 'set_ctmtbt_frontera', 'cant_suministros', 'cant_tarifa_social', 'distrito_descripcion', 'barrio', 'centroide_lat', 'centroide_lon']
].to_dict(orient='records')

df_dups = pd.read_csv(p_dups)
muestra_dups = df_dups.head(150)[
    ['nomenclatura', 'nomenclatura_manzana', 'nro_parcela', 'distrito_descripcion', 'cant_suministros']
].to_dict(orient='records')

cat_counts = df_set_full['categoria_set'].value_counts().to_dict()

top_social = df_set_full[df_set_full['cant_tarifa_social'] > 0].sort_values(by=['cant_tarifa_social', 'pct_tarifa_social'], ascending=[False, False]).head(50)[
    ['id', 'ctmtbt', 'cant_suministros', 'cant_tarifa_social', 'pct_tarifa_social', 'localidad_principal', 'distrito_principal']
].to_dict(orient='records')

top_sets = df_set_full.sort_values(by='cant_suministros', ascending=False).head(100)[
    ['id', 'ctmtbt', 'agf_codigo', 'estado', 'cant_parcelas', 'cant_suministros', 'cant_tarifa_social', 'pct_tarifa_social', 'categoria_set', 'localidad_principal', 'distrito_principal', 'calidad_poligono', 'prioridad_relevamiento_futuro', 'suministros_pendientes', 'pct_avance_relevamiento']
].to_dict(orient='records')

# Consolidar objeto global completo
dashboard_payload = {
    "metadata": {
        "fecha": "2026-11-12",
        "proyecto": "PROTELEM-EPEC/plan-relevamiento-topologia-set-parcelario",
        "descripcion": "Tablero Integral de Auditoría Topológica de Subestaciones, Calidad de Polígonos y Plan de Relevamiento Futuro EPEC",
        "autor": "Squad Ágil PM-Operadores (Arquetipo A: GIS, Catastro y Redes Eléctricas)"
    },
    "kpis": {
        "total_subestaciones": len(df_set_full),
        "total_suministros_en_set": int(df_set_full['cant_suministros'].sum()),
        "total_tarifa_social_en_set": int(df_set_full['cant_tarifa_social'].sum()),
        "total_parcelas_en_set": int(df_set_full['cant_parcelas'].sum()),
        "sets_sensibilidad_social_alta": int(df_set_full['sensibilidad_social_alta'].sum()),
        "total_parcelas_cortadas_frontera": len(df_cortadas),
        "total_parcelas_duplicadas_manzana": len(df_dups),
        "total_suministros_provincial": 1208097,
        "total_relevados_provincial": int(df_set_full['suministros_relevados'].sum()),
        "total_pendientes_provincial": int(df_set_full['suministros_pendientes'].sum()),
        "total_20_planes": int(df_planes['total_puntos'].sum()),
        "relevados_20_planes": int(df_planes['total_relevados'].sum()),
        "pendientes_20_planes": int(df_planes['total_pendientes'].sum()),
        "pct_avance_20_planes": round(df_planes['total_relevados'].sum() * 100.0 / df_planes['total_puntos'].sum(), 2)
    },
    "distribucion_categorias": cat_counts,
    "top_subestaciones": top_sets,
    "top_tarifa_social": top_social,
    "muestra_parcelas_cortadas": muestra_cortadas,
    "muestra_parcelas_duplicadas": muestra_dups,
    "calidad_poligonos": res_calidad.to_dict(orient="records"),
    "matriz_priorizacion": res_prio.to_dict(orient="records"),
    "planes_relevamiento": df_planes.to_dict(orient="records"),
    "subestaciones_top_pendientes": df_set_full.sort_values(by='suministros_pendientes', ascending=False).head(100)[[
        'id', 'ctmtbt', 'agf_codigo', 'distrito_principal', 'localidad_principal',
        'cant_suministros', 'suministros_relevados', 'suministros_pendientes', 'pct_avance_relevamiento',
        'calidad_poligono', 'parcelas_cortadas', 'pct_tarifa_social', 'prioridad_relevamiento_futuro'
    ]].to_dict(orient="records")
}

dashboard_js_path = os.path.join(viewer_data_dir, 'dashboard_data.js')
with open(dashboard_js_path, 'w', encoding='utf-8') as f:
    f.write(f"window.DASHBOARD_DATA = {json.dumps(dashboard_payload, ensure_ascii=False, indent=2)};\n")

print(f"   -> Payload del dashboard actualizado en: {dashboard_js_path} ({os.path.getsize(dashboard_js_path)/(1024):.1f} KB)")

print("\n" + "=" * 80)
print("AUDITORÍA COMPLETADA EXITOSAMENTE CON CERO ERRORES RUNTIME")
print("=" * 80)
