import os, sys, json, time

os.environ['PROJ_LIB'] = r'C:\Program Files\QGIS 4.2.0\share\proj'
os.environ['PROJ_DATA'] = r'C:\Program Files\QGIS 4.2.0\share\proj'

import duckdb
import geopandas as gpd
import pandas as pd
from shapely.geometry import shape, Point
from shapely import STRtree

print("=== INICIANDO MOTOR DE ANÁLISIS DE SUBESTACIONES Y PARCELAS ===")
start_time = time.time()

# Rutas
base_dir = r'D:\Proyectos\plan-relevamiento-topologia-set-parcelario'
sets_geojson = os.path.join(base_dir, 'data', 'vt_subestaciones_poly.geojson')
sumis_parquet = r'D:\Proyectos\antigravity-agents-repository\data\suministros_provincial_completo.parquet'
mzas_parquet = r'D:\Proyectos\antigravity-agents-repository\data\manzanas_alta_resolucion_provincial.parquet'

# 1. Cargar subestaciones
print("1. Cargando polígonos de subestaciones...")
gdf_sets = gpd.read_file(sets_geojson)
print(f"   Subestaciones cargadas: {len(gdf_sets):,}")

# Validar y limpiar geometrías
gdf_sets['geometry'] = gdf_sets['geometry'].buffer(0)
gdf_sets = gdf_sets[gdf_sets['geometry'].is_valid & (~gdf_sets['geometry'].is_empty)]
print(f"   Subestaciones válidas: {len(gdf_sets):,}")

# 2. Conectar DuckDB para analizar suministros y tarifas sociales
print("2. Analizando suministros y Tarifa Social en DuckDB...")
con = duckdb.connect()

# Total suministros y tarifa social
ts_query = f"""
    SELECT 
        count(*) as total_sumis,
        sum(CASE WHEN tarifa ILIKE '%social%' OR tarifa ILIKE '%caren%' OR tarifa ILIKE '%indig%' THEN 1 ELSE 0 END) as total_tarifa_social,
        count(DISTINCT distrito) as cant_distritos,
        count(DISTINCT ruta_lectura) as cant_rutas
    FROM '{sumis_parquet}'
"""
ts_res = con.execute(ts_query).fetchone()
print(f"   Total suministros provinciales: {ts_res[0]:,}")
print(f"   Total con Tarifa Social (Dec. 43/19): {ts_res[1]:,} ({ts_res[1]/ts_res[0]*100:.2f}%)")
print(f"   Distritos: {ts_res[2]}, Rutas de lectura: {ts_res[3]}")

# 3. Muestreo espacial para vinculación y clasificación SET
print("3. Indexando espacialmente subestaciones con STRtree...")
sindex = gdf_sets.sindex

print(f"=== TIEMPO PARCIAL: {time.time() - start_time:.2f}s ===")
