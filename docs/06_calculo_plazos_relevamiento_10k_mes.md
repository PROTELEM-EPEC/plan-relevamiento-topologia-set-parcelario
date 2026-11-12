# ⏱️ Estimación de Plazos: Plan de Relevamiento de Córdoba a Régimen de 10.000 Relevamientos/Mes

## 1. Parámetros Operativos del Modelo

* **Tasa de Producción Nominal**: **10.000 relevamientos / mes**
* **Días Hábiles Mensuales**: 21 días laborables promedio.
* **Ritmo Diario Requerido**: **~476 suministros / día hábil**.
* **Dimensionamiento de Cuadrillas**:
  * Zonas Urbanas Densas (CC en Centro/Nueva Cba - 30 sumis/día/cuadrilla): **16 cuadrillas activas**.
  * Zonas Mixtas / Periféricas (25 sumis/día/cuadrilla): **19 cuadrillas activas**.
  * Zonas con Sensibilidad Social / Tarifa Social (20 sumis/día/cuadrilla con mediación): **24 cuadrillas activas**.
* **Fecha Base de Arranque Simulada**: **1° de Diciembre de 2026** (o 1° de Enero de 2027).

---

## 2. Definición de Escenarios de Alcance ("Planes sin Relevamiento")

| Escenario de Alcance | Criterio de Selección | Planes Incluidos | Suministros Pendientes | Meses Estimados | Tiempo Calendario | Fecha Estimada de Finalización |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: |
| **Escenario A: Planes Vírgenes (Sin Relevamiento)** | **Avance histórico $< 5\%$** | **Planes 14, 15, 08, 07, 11 y 09** (6 planes) | **169.597** | **16,96 meses** | **~1 año y 5 meses** | **Fines de Abril 2028** |
| **Escenario B: Planes con Déficit Estructural** | **Avance histórico $< 80\%$** | Escenario A + **Planes 17, 12 y 10** (9 planes) | **204.048** | **20,40 meses** | **~1 año y 8,5 meses** | **Agosto 2028** |
| **Escenario C: Universo Consolidado Completo** | **20 Planes (100% Capital)** | Todos los planes (incluyendo barrido residual) | **237.146** | **23,71 meses** | **~2 años exactos** | **Noviembre 2028** |

---

## 3. Cronograma Detallado y Secuenciación Óptima (Escenario A: 6 Planes Vírgenes)

El orden de avance propuesto prioriza primero los distritos con **$\ge 98\%$ de Clientes Comunes (CC)** y alta densidad para asegurar la curva de aprendizaje y máxima velocidad de captura, permitiendo que el equipo de GIS sanee los polígonos de subestaciones con conflicto topológico antes de que las cuadrillas ingresen a las zonas periféricas y vulnerables.

| Secuencia | Plan de Lectura | Barrio / Zona Referencia | Total Pendientes | Pendientes CC | Pendientes Tarifa Social | Duración (Meses) | Duración Acumulada | Ventana Calendario Estimada | Perfil de Ejecución |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **1°** | **Plan 14** | Centro, Nueva Córdoba, Güemes Norte | **47.879** | 47.764 | 26 | **4,79 m** | 4,79 m | Dic-2026 a Abr-2027 | **Arranque Máxima Densidad**: 99,8% CC en edificios y medidores accesibles. |
| **2°** | **Plan 15** | Alta Córdoba, Cofico, Gral. Bustos | **29.995** | 29.751 | 68 | **3,00 m** | 7,79 m | May-2027 a Jul-2027 | **Continuidad Centro-Norte**: 99,2% CC homogéneo. |
| **3°** | **Plan 08** | San Vicente, Pueyrredón, Juniors | **27.535** | 27.061 | 404 | **2,75 m** | 10,54 m | Ago-2027 a Oct-2027 | **Corredor Este Residencial**: 98,3% CC. |
| **4°** | **Plan 07** | Empalme, Ferreyra, Cno. 60 Cuadras | **24.348** | 20.982 | 3.285 | **2,43 m** | 12,98 m | Nov-2027 a Ene-2028 | **Transición Mixta**: Cuadrillas estándar + 1 cuadrilla con protocolo social. |
| **5°** | **Plan 11** | Villa El Libertador, Comercial, Suroeste | **23.793** | 18.336 | 5.335 | **2,38 m** | 15,36 m | Feb-2028 a Mar-2028 | **Sensibilidad Crítica**: 22,4% Tarifa Social con mediación vecinal previa. |
| **6°** | **Plan 09** | Guiñazú, Liceo, Periferia Norte | **16.047** | 13.466 | 2.507 | **1,60 m** | 16,96 m | Abr-2028 a May-2028 | **Cierre Periférico**: Cuadrillas de cierre territorial. |
| **TOTAL** | **6 PLANES** | **Córdoba Capital Consolidado** | **169.597** | **157.360** | **11.625** | **16,96 m** | **16,96 m** | **17 meses corridos** | **1 año y 5 meses a 10.000/mes** |

---

## 4. Estrategia de Coordinación Técnica con Calidad de Polígonos de SETs

* **Ventana de Saneamiento GIS de 10 Meses**:
  * Durante los primeros **10 meses y medio** (Dic-2026 a Oct-2027), las cuadrillas estarán concentradas exclusivamente en **Planes 14, 15 y 08** (zonas urbanas centrales con polígonos limpios de subestaciones).
  * Esta ventana temporal brinda al equipo de gabinete de GIS el tiempo necesario para **redefinir y corregir los límites perimetrales de las 449 subestaciones en conflicto topológico** (Cuadrante 3, con 78.898 suministros) en los Planes 07, 11 y 09.
  * Cuando las cuadrillas lleguen en Noviembre de 2027 al Plan 07 y en Febrero de 2028 al Plan 11, los planos y polígonos de las subestaciones estarán 100% saneados, **eliminando el riesgo de imputaciones erróneas de medidores a transformadores**.

