"""
========================================================================================
SQUAD ARQUETIPO A - GIS, CATASTRO Y TOPOLOGÍA DE RED ELÉCTRICA EPEC
MÓDULO 03: Generación de Datos para Visor Web Interactivo de Subestaciones
========================================================================================
"""

import os, json
import pandas as pd
import duckdb

print("=== [OPERADOR 3] GENERANDO DATASET PARA VISOR WEB INTERACTIVO ===")

base_dir = r'D:\Proyectos\plan-relevamiento-topologia-set-parcelario'
reports_dir = os.path.join(base_dir, 'reports')
viewer_dir = os.path.join(base_dir, 'viewer')
viewer_data_dir = os.path.join(viewer_dir, 'data')
os.makedirs(viewer_data_dir, exist_ok=True)

# 1. Cargar subestaciones clasificadas
clasif_csv = os.path.join(reports_dir, 'resumen_clasificacion_subestaciones.csv')
df_sets = pd.read_csv(clasif_csv)

# 2. Resumen métricas globales
total_sets = len(df_sets)
total_sumis = int(df_sets['cant_suministros'].sum())
total_social = int(df_sets['cant_tarifa_social'].sum())
total_parcelas_set = int(df_sets['cant_parcelas'].sum())
sets_con_social_alta = int(df_sets['sensibilidad_social_alta'].sum())

# Distribución por categoría
cat_counts = df_sets['categoria_set'].value_counts().to_dict()

# Top 50 Subestaciones por suministro
top_sets = df_sets.sort_values(by='cant_suministros', ascending=False).head(100)[
    ['id', 'ctmtbt', 'agf_codigo', 'estado', 'cant_parcelas', 'cant_suministros', 'cant_tarifa_social', 'pct_tarifa_social', 'categoria_set', 'localidad_principal', 'distrito_principal']
].to_dict(orient='records')

# Top 50 Subestaciones con mayor Tarifa Social
top_social = df_sets[df_sets['cant_tarifa_social'] > 0].sort_values(by=['cant_tarifa_social', 'pct_tarifa_social'], ascending=[False, False]).head(50)[
    ['id', 'ctmtbt', 'cant_suministros', 'cant_tarifa_social', 'pct_tarifa_social', 'localidad_principal', 'distrito_principal']
].to_dict(orient='records')

# 3. Cargar muestra de parcelas cortadas (primeras 500 para visualización ágil en tabla interactiva)
log_cortadas_csv = os.path.join(reports_dir, 'log_excepciones_parcelas_cortadas_frontera.csv')
df_cortadas = pd.read_csv(log_cortadas_csv)
total_cortadas = len(df_cortadas)

muestra_cortadas = df_cortadas.head(300)[
    ['nomenclatura', 'nomenclatura_manzana', 'nro_parcela', 'set_ctmtbt_frontera', 'cant_suministros', 'cant_tarifa_social', 'distrito_descripcion', 'barrio', 'centroide_lat', 'centroide_lon']
].to_dict(orient='records')

# 4. Cargar anomalías de parcelas duplicadas
dup_csv = os.path.join(reports_dir, 'anomalias_parcelas_duplicadas_en_manzana.csv')
df_dups = pd.read_csv(dup_csv)
total_dups = len(df_dups)
muestra_dups = df_dups.head(150)[
    ['nomenclatura', 'nomenclatura_manzana', 'nro_parcela', 'distrito_descripcion', 'cant_suministros']
].to_dict(orient='records')

payload = {
    "metadata": {
        "fecha": "2026-11-11",
        "proyecto": "PROTELEM-EPEC/plan-relevamiento-topologia-set-parcelario",
        "descripcion": "Tablero Integral de Auditoría Topológica de Subestaciones, Fusión Parcelaria y Tarifa Social EPEC",
        "autor": "Squad Ágil PM-Operadores (Arquetipo A: GIS, Catastro y Redes Eléctricas)"
    },
    "kpis": {
        "total_subestaciones": total_sets,
        "total_suministros_en_set": total_sumis,
        "total_tarifa_social_en_set": total_social,
        "total_parcelas_en_set": total_parcelas_set,
        "sets_sensibilidad_social_alta": sets_con_social_alta,
        "total_parcelas_cortadas_frontera": total_cortadas,
        "total_parcelas_duplicadas_manzana": total_dups
    },
    "distribucion_categorias": cat_counts,
    "top_subestaciones": top_sets,
    "top_tarifa_social": top_social,
    "muestra_parcelas_cortadas": muestra_cortadas,
    "muestra_parcelas_duplicadas": muestra_dups
}

out_js = os.path.join(viewer_data_dir, 'dashboard_data.js')
with open(out_js, 'w', encoding='utf-8') as f:
    f.write(f"window.DASHBOARD_DATA = {json.dumps(payload, ensure_ascii=False, indent=2)};\n")

print(f"   -> Dataset generado exitosamente en: {out_js} ({os.path.getsize(out_js)/(1024):.1f} KB)")
