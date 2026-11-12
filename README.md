# ⚡ Plan de Relevamiento, Topología de Subestaciones & Fusión Parcelaria EPEC

Repositorio técnico y geoespacial dedicado de **PROTELEM-EPEC** para la consolidación del parcelario provincial, auditoría de fronteras de Subestaciones Transformadoras (SET), control de excepciones de relevamiento y análisis de sensibilidad de Tarifa Social (Decreto Provincial 43/2019).

---

## 🎯 Objetivos del Proyecto

1. **Fusión Jerárquica Parcelaria Multifuente**:
   - Consolidar las tres fuentes cartográficas oficiales bajo estricta prioridad de conservación en caso de superposición:
     1. **Prioridad 1 (Máxima)**: `EPEC:parcelas_union` (`vt_parcelas_union` / `vm_vt_parcelas_union`).
     2. **Prioridad 2 (Media)**: Municipalidad de Córdoba (`parcelas_muni` / `parcelas_muni_4326`).
     3. **Prioridad 3 (Base)**: Provincia de Córdoba - IDECOR (`parcelas_idecor`).
   - Garantizar la unicidad del número de parcela dentro de la misma manzana y eliminar solapamientos geométricos.

2. **Auditoría Topológica de Subestaciones (`EPEC:vt_subestaciones_poly`)**:
   - Cruzar los 5.296 polígonos de subestaciones provinciales contra las parcelas y suministros normalizados.
   - Detectar parcelas que son cortadas por las líneas perimetrales de la SET (evitando ambigüedad operativa de relevamiento en campo).
   - Generar el **Log de Excepciones** con fronteras rígidas para revisión y control manual de cuadrillas.

3. **Mapeo y Sensibilidad de Tarifa Social**:
   - Identificar suministros con Tarifa Social Oficial de Córdoba (Decreto 43/19: *TSP Carenciados*, *TSP Indigentes*, *Social Prov. sin medición*).
   - Identificar las **621 Subestaciones con Alta Sensibilidad Social ($\ge 20\%$)** para aplicar protocolos de atención comercial diferenciados.

4. **Clasificación de Subestaciones**:
   - Segmentar las SETs según volumen de suministros asociados (vía centroide de parcela o centroide de manzana sintética de alta resolución).

---

## 📊 Métricas Clave y Resultados de la Auditoría

| Indicador Técnico | Valor Obtenido | Descripción |
| :--- | :---: | :--- |
| **Subestaciones Poligonales Válidas** | `5,296` | Polígonos de `EPEC:vt_subestaciones_poly` en EPSG:4326 |
| **Parcelas Consolidadas Saneadas** | `386,005` | Capa maestra unificada sin duplicados por manzana |
| **Parcelas contenidas dentro de SET** | `311,912` | Cobertura neta del 80.9% del universo parcelario |
| **Parcelas fuera del perímetro de SET** | `73,852` | Parcelas a evaluar para expansión de límites de SET |
| **Parcelas Cortadas por Frontera de SET** | `110,230` | Casos de excepción registrados en log para revisión manual |
| **SETs con Alta Sensibilidad ($\ge 20\%$ Tarifa Social)** | `621` | Subestaciones con alta concentración de usuarios vulnerables |
| **Duplicados Internos en Manzana Saneados** | `69,011` | Inconsistencias catastrales detectadas y depuradas |

---

## 🗂️ Estructura del Repositorio

```text
plan-relevamiento-topologia-set-parcelario/
├── data/
│   ├── vt_subestaciones_poly.geojson            # Polígonos WFS oficiales de 5.3k SETs
│   ├── capa_parcelas_general_consolidada.parquet # Capa maestra de 386k parcelas saneadas
│   └── subestaciones_clasificadas.parquet       # Dataset de SETs con KPIs y métricas sociales
├── reports/
│   ├── resumen_clasificacion_subestaciones.csv  # Clasificación completa de las 5.3k SETs
│   ├── log_excepciones_parcelas_cortadas_frontera.csv # 110k parcelas que intersectan perímetro
│   └── anomalias_parcelas_duplicadas_en_manzana.csv   # 69k inconsistencias de duplicación
├── src/
│   ├── 01_fusion_jerarquica_parcelaria.py       # Pipeline de fusión y deduplicación
│   ├── 02_auditoria_subestaciones_topologia.py   # Cruce espacial, SET cutting y Tarifa Social
│   └── 03_generar_viewer_data.py                # Generador de datos para el visor web
├── viewer/
│   ├── index.html                               # Tablero web interactivo responsivo
│   └── data/dashboard_data.js                   # JSON data estructurado para visualización
├── docs/                                        # Monografías técnicas y de arquitectura
└── README.md                                    # Ficha técnica ejecutiva
```

---

## 🚀 Uso Rápido

### Ejecución de Pipelines:
```powershell
# 1. Fusión y saneamiento parcelario
python src/01_fusion_jerarquica_parcelaria.py

# 2. Auditoría de límites de subestaciones y clasificación
python src/02_auditoria_subestaciones_topologia.py

# 3. Exportación para visor interactivo
python src/03_generar_viewer_data.py
```

### Visualización del Tablero:
Abrir [`viewer/index.html`](viewer/index.html) directamente en cualquier navegador web moderno para explorar métricas, filtrar subestaciones por tamaño y consultar el log de parcelas cortadas.

---

## 👥 Gobernanza y Squad Ágil (Arquetipo A: GIS & Redes EPEC)
- **Project Manager**: `Gemini 2.5 Pro` (Top-1) - Planificación WBS, arbitraje de contratos y Stage-Gate Triple QA.
- **Operador 1 (Core GIS)**: `Gemini 2.5 Flash` (Top-2) - Geoprocesamiento Shapely / GeoPandas y pipeline de fusión.
- **Operador 2 (Dominio Catastro & SET)**: `Gemini 2.5 Flash` (Top-2) - Cruce topológico de subestaciones y Tarifa Social.
- **Operador 3 (QA & UX)**: `Gemini 2.5 Flash` (Top-2) - Auditoría de excepciones, backups y visor interactivo.

