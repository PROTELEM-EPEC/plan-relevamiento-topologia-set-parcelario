# 🗺️ Análisis por Plan: Parcelario, Fronteras de SET a Analizar y Parcelas a Dibujar

## 1. Resumen Ejecutivo

En el marco del **Plan de Relevamiento, Topología de Subestaciones y Fusión Parcelaria de EPEC (Córdoba Capital - Distrito 1)**, se profundizó la caracterización técnica y catastral de los 20 Planes de Lectura, vinculando de forma multidimensional el universo de suministros (585.819 puntos), las parcelas vectoriales consolidadas, las excepciones de frontera de subestaciones y las parcelas catastrales sin representación gráfica vectorial que requieren digitalización.

### Métricas Consolidadas del Universo de los 20 Planes:
- **Total de Puntos de Suministro**: `585.819`
- **Relevados Históricos (`georef.relevamiento`)**: `348.673` (59,52% de avance)
- **Pendientes Totales a Relevar**: `237.146` (220.395 CC, 15.947 Tarifa Social, 804 Otros)
- **Total de Parcelas Dibujadas con Suministros**: `266.755` parcelas únicas
- **Parcelas en Frontera de SET a Analizar**: `88.205` parcelas (33,07% del parcelario activo)
- **Parcelas Catastrales a Dibujar (Faltantes en Cartografía)**: `26.736` parcelas identificadas a partir de la descripción catastral normalizada (`dc` / `id_suministro_catastral`)

---

## 2. Matriz Consolidada por Plan de Lectura

| Plan | Puntos Totales | Relevados | % Avance | Pendientes | Total Parcelas | Frontera SET (Analizar) | % Frontera | A Dibujar (Faltantes) | % A Dibujar | Diagnóstico Operativo |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Plan 01** | 29.910 | 27.053 | 90,45% | 2.857 | 17.931 | 5.325 | 29,70% | 1.040 | 5,80% | `FASE_FINAL_REMANENTES` |
| **Plan 02** | 19.856 | 18.582 | 93,58% | 1.274 | 9.773 | 3.935 | 40,26% | 452 | 4,62% | `FASE_FINAL_REMANENTES` |
| **Plan 03** | 38.204 | 33.581 | 87,90% | 4.623 | 24.245 | 7.343 | 30,29% | 1.531 | 6,31% | `FASE_FINAL_REMANENTES` |
| **Plan 04** | 24.285 | 22.690 | 93,43% | 1.595 | 8.348 | 4.002 | 47,94% | 477 | 5,71% | `FASE_FINAL_REMANENTES` |
| **Plan 05** | 27.593 | 22.155 | 80,29% | 5.438 | 16.371 | 4.703 | 28,73% | 3.017 | 18,43% | `FASE_FINAL_REMANENTES` |
| **Plan 06** | 12.675 | 11.748 | 92,69% | 927 | 8.808 | 3.231 | 36,68% | 349 | 3,96% | `FASE_FINAL_REMANENTES` |
| **Plan 07** | 25.216 | 868 | 3,44% | 24.348 | 12.101 | 4.584 | 37,88% | 2.555 | 21,11% | `RELEVAMIENTO_MIXTO_ESTANDAR` |
| **Plan 08** | 27.622 | 87 | 0,31% | 27.535 | 6.189 | 3.396 | 54,87% | 1.279 | 20,67% | `RELEVAMIENTO_MASIVO_CC_INMEDIATO` |
| **Plan 09** | 16.863 | 816 | 4,84% | 16.047 | 8.186 | 3.178 | 38,82% | 2.872 | 35,08% | `SENSIBILIDAD_SOCIAL_PRIORITARIA` |
| **Plan 10** | 17.360 | 12.857 | 74,06% | 4.503 | 12.121 | 4.185 | 34,53% | 691 | 5,70% | `SENSIBILIDAD_SOCIAL_PRIORITARIA` |
| **Plan 11** | 24.233 | 440 | 1,82% | 23.793 | 11.172 | 4.338 | 38,83% | 2.719 | 24,34% | `SENSIBILIDAD_SOCIAL_PRIORITARIA` |
| **Plan 12** | 22.098 | 11.646 | 52,70% | 10.452 | 8.949 | 2.939 | 32,84% | 581 | 6,49% | `RELEVAMIENTO_MASIVO_CC_INMEDIATO` |
| **Plan 13** | 34.498 | 31.730 | 91,98% | 2.768 | 18.399 | 5.199 | 28,26% | 1.153 | 6,27% | `FASE_FINAL_REMANENTES` |
| **Plan 14** | 47.912 | 33 | 0,07% | 47.879 | 2.122 | 21 | 0,99% | 1.047 | 49,34% | `RELEVAMIENTO_MASIVO_CC_INMEDIATO` |
| **Plan 15** | 30.593 | 598 | 1,95% | 29.995 | 2.927 | 106 | 3,62% | 1.030 | 35,19% | `RELEVAMIENTO_MASIVO_CC_INMEDIATO` |
| **Plan 16** | 47.984 | 43.301 | 90,24% | 4.683 | 33.638 | 10.039 | 29,84% | 2.834 | 8,42% | `FASE_FINAL_REMANENTES` |
| **Plan 17** | 34.787 | 15.291 | 43,96% | 19.496 | 9.429 | 3.211 | 34,05% | 800 | 8,48% | `RELEVAMIENTO_MASIVO_CC_INMEDIATO` |
| **Plan 18** | 33.248 | 30.741 | 92,46% | 2.507 | 24.759 | 7.620 | 30,78% | 533 | 2,15% | `FASE_FINAL_REMANENTES` |
| **Plan 19** | 29.408 | 26.600 | 90,45% | 2.808 | 10.016 | 4.066 | 40,60% | 529 | 5,28% | `FASE_FINAL_REMANENTES` |
| **Plan 20** | 41.474 | 37.856 | 91,28% | 3.618 | 21.271 | 6.784 | 31,89% | 1.247 | 5,86% | `FASE_FINAL_REMANENTES` |
| **TOTAL** | **585.819** | **348.673** | **59,52%** | **237.146** | **266.755** | **88.205** | **33,07%** | **26.736** | **10,02%** | **-** |

---

## 3. Diagnóstico de Parcelas en Frontera de Subestación (88.205 casos)

### Definición y Criterio Técnico:
Las parcelas en frontera son aquellas cuyo polígono catastral es **cortado por el límite perimetral de un polígono de subestación transformadora (`EPEC:vt_subestaciones_poly`)**.
- **Riesgo Operativo**: Si un cuadrillero releva la parcela, existe ambigüedad respecto a si los suministros deben imputarse eléctricamente al Centro de Transformación (CT) de la SET A o de la SET B.
- **Protocolo Acordado**: En cumplimiento de la decisión A3 de la Compuerta de Clarificación, se mantiene la **frontera rígida** en el visor y se entrega el listado nominal de parcelas cortadas a cuadrilla para control manual en terreno mediante inspección de acometida y línea de baja tensión.

### Distribución por Tipología Urbana:
1. **Zonas de Mínimo Conflicto Perimetral (< 5% frontera)**:
   - **Plan 14** (Centro / Casco Histórico): Apenas **21 parcelas** (0,99%) cortadas.
   - **Plan 15** (Nueva Córdoba / Güemes): **106 parcelas** (3,62%) cortadas.
   - *Causa*: Red predominantemente subterránea con cámaras transformadoras de límites perfectamente encuadrados en parcelas o veredas.
2. **Zonas de Alto Conflicto Perimetral (> 40% frontera)**:
   - **Plan 08** (54,87% - 3.396 parcelas), **Plan 04** (47,94% - 4.002 parcelas), **Plan 19** (40,60% - 4.066 parcelas), **Plan 02** (40,26% - 3.935 parcelas).
   - *Causa*: Trazados de distribución aérea antiguos donde los polígonos de SET fueron digitalizados englobando manzanas de forma irregular o cortando manzanas por la línea de fondo de lote.
3. **Mayor Volumen Absoluto de Parcelas a Analizar**:
   - **Plan 16**: **10.039 parcelas cortadas**.
   - **Plan 18**: **7.620 parcelas cortadas**.
   - **Plan 03**: **7.343 parcelas cortadas**.
   - **Plan 20**: **6.784 parcelas cortadas**.

---

## 4. Diagnóstico de Parcelas a Dibujar (26.736 casos)

### Definición y Criterio Técnico:
Corresponden a parcelas donde existen suministros legalmente constituidos y activos en la base comercial de EPEC (`suministros_provincial_completo`), con **descripción catastral completa y válida** (`distrito-seccion-manzana-parcela`), pero que **carecen de un polígono vectorial dibujado** en la capa unificada de parcelas (`parcelas_union` / Municipalidad / IDECOR).

### Top 5 Planes con Mayor Demanda de Digitalización Vectorial:
1. **Plan 05**: `3.017 parcelas a dibujar` (18,43% del volumen del plan).
2. **Plan 09**: `2.872 parcelas a dibujar` (35,08% del volumen del plan).
3. **Plan 16**: `2.834 parcelas a dibujar` (8,42% del volumen del plan).
4. **Plan 11**: `2.719 parcelas a dibujar` (24,34% del volumen del plan).
5. **Plan 07**: `2.555 parcelas a dibujar` (21,11% del volumen del plan).

### Caso Singular en Planes de Alta Densidad (Planes 14 y 15):
- En **Plan 14** y **Plan 15**, aunque el porcentaje relativo parece alto (~35-49%), se debe a que son distritos céntricos con muy baja cantidad de parcelas territoriales (2.122 y 2.927) pero altísima concentración de Propiedad Horizontal (PH). Las ~1.000 parcelas a dibujar en cada uno corresponden principalmente a nuevas torres residenciales o subdivisiones en PH que aún no tenían incorporada su geometría subdividida en la base cartográfica municipal/provincial.

---

## 5. Hoja de Ruta para Cuadrillas y Gabinete GIS

1. **Prioridad 1 - Gabinete GIS (Meses 1 a 10)**:
   - Mientras las cuadrillas de campo ejecutan el relevamiento masivo de Clientes Comunes en **Plan 14, Plan 15 y Plan 08** (que tienen un avance histórico prácticamente nulo pero límites perimetrales muy claros en el centro), el equipo de Gabinete GIS digitaliza las **26.736 parcelas faltantes** en los Planes 05, 07, 09 y 11.
2. **Prioridad 2 - Corrección de Fronteras SET**:
   - Ajustar el perímetro de las subestaciones en los Planes 07, 08 y 11 para que sigan las líneas divisorias de parcelas (ejes de calle o fondos de lote), reduciendo drásticamente las 88.205 parcelas cortadas antes de que las cuadrillas inicien el barrido en dichos distritos.
3. **Prioridad 3 - Cierre de Remanentes**:
   - En los 12 planes con más del 80% de avance, utilizar el mapa del visor para asignar rutas directas a las parcelas específicas con suministros pendientes.

