# Cronograma de Despliegue Mensual de Relevamiento Catastral (10.000 casos / mes)

**Proyecto:** PROTELEM - Auditoría Topológica de Subestaciones & Plan de Relevamiento Futuro  
**Entidad:** EPEC (Empresa Provincial de Energía de Córdoba)  
**Fecha de Emisión:** Noviembre 2026  
**Capacidad Operativa:** 10.000 relevamientos mensuales sostenidos  
**Herramienta Interactiva:** [viewer/index.html](file:///D:/Proyectos/plan-relevamiento-topologia-set-parcelario/viewer/index.html)

---

## 1. Resumen Ejecutivo & Premisas Operativas

A partir del requerimiento de planificación de cuadrillas para Córdoba Capital (Distrito 1) con una capacidad sostenida de **10.000 relevamientos por mes**, se estructuró un modelo de asignación secuencial estricto que respeta las siguientes condiciones operativas:

1. **Mes de Inicio (Noviembre 2026):**
   - Se integraron los registros reales asentados en la tabla `georef.relevamiento` durante noviembre 2026 (911 suministros relevados entre el 1 y el 12 de noviembre).
   - Se priorizó la culminación definitiva del **Plan 05**, el cual contaba con 22.155 suministros históricos relevados de un total de 27.593 (avance del 80.29%). 
   - Durante noviembre 2026 se ejecutan **6.122 casos del Plan 05** (684 ya registrados en noviembre + 5.438 remanentes para completar el 100% del plan) junto con **126 casos ya registrados del Plan 07**, totalizando **6.248 casos** para el mes en curso.

2. **Arranque en Diciembre 2026:**
   - En diciembre 2026 se da inicio formal al despliegue masivo a ritmo pleno (10.000 casos/mes) comenzando por el **Plan 08** (Prioridad 1).

3. **Secuencia de Prioridad Oficial:**
   - La asignación de meses sigue el orden de prioridad definido en la tabla oficial de relevamiento:
     - **Prioridad 1:** Plan 08
     - **Prioridad 2:** Plan 12
     - **Prioridad 3:** Plan 17
     - **Prioridad 4:** Plan 07
     - **Prioridad 5:** Plan 09
     - **Prioridad 6:** Plan 10
     - **Prioridad 7:** Plan 11
     - **Prioridad 8:** Plan 14
     - **Prioridad 9:** Plan 15

4. **Horizontes de Finalización:**
   - **9 Planes Prioritarios Clave:** **22 meses** de ejecución (Noviembre 2026 a **Agosto 2028**), cubriendo **210.296 casos**.
   - **Universo Completo de 20 Planes:** **25 meses** de ejecución (Noviembre 2026 a **Noviembre 2028**), absorbiendo los 10 planes remanentes (27.660 casos pendientes) y totalizando **237.956 casos**.

---

## 2. Tabla Oficial de Prioridades de Relevamiento

La siguiente tabla consolida los 9 planes prioritarios en su orden estricto de ejecución, incorporando las métricas de parcelas a analizar en frontera de subestación y total de parcelas:

| Prioridad | Plan | Suministros Totales | Parcelas a Analizar (Frontera) | Total Parcelas | Relevados Nov-26 | Pendientes Reales | Periodo Estimado en Cronograma | Color Asignado |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **En Curso** | **Plan 05** | 27.593 | 4.711 | 16.371 | 684 | 5.438 | Nov-2026 (Completado al 100%) | `#10b981` (Esmeralda) |
| **1** | **Plan 08** | 27.622 | 4.682 | 10.871 | 0 | 27.535 | Dic-2026 a Feb-2027 (2.8 meses) | `#6366f1` (Índigo) |
| **2** | **Plan 12** | 22.098 | 3.525 | 12.474 | 0 | 10.452 | Feb-2027 a Mar-2027 (1.0 meses) | `#3b82f6` (Azul) |
| **3** | **Plan 17** | 34.787 | 4.011 | 13.440 | 1 | 19.496 | Mar-2027 a May-2027 (1.9 meses) | `#06b6d4` (Cian) |
| **4** | **Plan 07** | 25.216 | 7.140 | 19.241 | 126 | 24.348 | May-2027 a Ago-2027 (2.4 meses) | `#f59e0b` (Ámbar) |
| **5** | **Plan 09** | 16.863 | 6.043 | 14.229 | 0 | 16.047 | Ago-2027 a Sep-2027 (1.6 meses) | `#ec4899` (Rosa) |
| **6** | **Plan 10** | 17.360 | 4.867 | 16.988 | 0 | 4.503 | Sep-2027 a Oct-2027 (0.5 meses) | `#8b5cf6` (Púrpura) |
| **7** | **Plan 11** | 24.233 | 7.051 | 18.223 | 0 | 23.793 | Oct-2027 a Dic-2027 (2.4 meses) | `#f43f5e` (Rojo Carmesí) |
| **8** | **Plan 14** | 47.912 | 1.070 | 3.192 | 0 | 47.879 | Dic-2027 a May-2028 (4.8 meses) | `#14b8a6` (Teal) |
| **9** | **Plan 15** | 30.593 | 1.132 | 4.059 | 0 | 29.995 | May-2028 a Ago-2028 (3.0 meses) | `#eab308` (Amarillo) |
| **—** | **Remanentes (10)**| 318.542| 48.012 | 147.932| 100 | 27.660 | Ago-2028 a Nov-2028 (2.8 meses) | `#64748b` (Pizarra) |

---

## 3. Desglose Mes a Mes del Cronograma (10.000 casos/mes)

A continuación se detalla la asignación exacta mes por mes:

| Mes - Año | Distribución de Casos por Plan | Total Casos Mes | Casos Acumulados | Hito Operativo / Transición |
| :--- | :--- | :---: | :---: | :--- |
| **Nov-2026** | **Plan 05:** 6.122 &bull; **Plan 07:** 126 | **6.248** | 6.248 | 🟢 **Cierre Plan 05** (100% completado con registros Nov) |
| **Dic-2026** | **Plan 08:** 10.000 | **10.000** | 16.248 | 🚀 **Arranque Plan 08** (Prioridad 1) |
| **Ene-2027** | **Plan 08:** 10.000 | **10.000** | 26.248 | Continuidad cuadrillas Plan 08 |
| **Feb-2027** | **Plan 08:** 7.535 &bull; **Plan 12:** 2.465 | **10.000** | 36.248 | 🏁 **Fin Plan 08** ➔ Arranque **Plan 12** (Prioridad 2) |
| **Mar-2027** | **Plan 12:** 7.987 &bull; **Plan 17:** 2.013 | **10.000** | 46.248 | 🏁 **Fin Plan 12** ➔ Arranque **Plan 17** (Prioridad 3) |
| **Abr-2027** | **Plan 17:** 10.000 | **10.000** | 56.248 | Continuidad cuadrillas Plan 17 |
| **May-2027** | **Plan 17:** 7.483 &bull; **Plan 07:** 2.517 | **10.000** | 66.248 | 🏁 **Fin Plan 17** ➔ Arranque **Plan 07** (Prioridad 4) |
| **Jun-2027** | **Plan 07:** 10.000 | **10.000** | 76.248 | Continuidad cuadrillas Plan 07 |
| **Jul-2027** | **Plan 07:** 10.000 | **10.000** | 86.248 | Continuidad cuadrillas Plan 07 |
| **Ago-2027** | **Plan 07:** 1.831 &bull; **Plan 09:** 8.169 | **10.000** | 96.248 | 🏁 **Fin Plan 07** ➔ Arranque **Plan 09** (Prioridad 5) |
| **Sep-2027** | **Plan 09:** 7.878 &bull; **Plan 10:** 2.122 | **10.000** | 106.248 | 🏁 **Fin Plan 09** ➔ Arranque **Plan 10** (Prioridad 6) |
| **Oct-2027** | **Plan 10:** 2.381 &bull; **Plan 11:** 7.619 | **10.000** | 116.248 | 🏁 **Fin Plan 10** ➔ Arranque **Plan 11** (Prioridad 7) |
| **Nov-2027** | **Plan 11:** 10.000 | **10.000** | 126.248 | Continuidad cuadrillas Plan 11 |
| **Dic-2027** | **Plan 11:** 6.174 &bull; **Plan 14:** 3.826 | **10.000** | 136.248 | 🏁 **Fin Plan 11** ➔ Arranque **Plan 14** (Prioridad 8) |
| **Ene-2028** | **Plan 14:** 10.000 | **10.000** | 146.248 | Continuidad cuadrillas Plan 14 |
| **Feb-2028** | **Plan 14:** 10.000 | **10.000** | 156.248 | Continuidad cuadrillas Plan 14 |
| **Mar-2028** | **Plan 14:** 10.000 | **10.000** | 166.248 | Continuidad cuadrillas Plan 14 |
| **Abr-2028** | **Plan 14:** 10.000 | **10.000** | 176.248 | Continuidad cuadrillas Plan 14 |
| **May-2028** | **Plan 14:** 4.053 &bull; **Plan 15:** 5.947 | **10.000** | 186.248 | 🏁 **Fin Plan 14** ➔ Arranque **Plan 15** (Prioridad 9) |
| **Jun-2028** | **Plan 15:** 10.000 | **10.000** | 196.248 | Continuidad cuadrillas Plan 15 |
| **Jul-2028** | **Plan 15:** 10.000 | **10.000** | 206.248 | Continuidad cuadrillas Plan 15 |
| **Ago-2028** | **Plan 15:** 4.048 *(Fin 9 Planes)* &bull; *Remanentes: 5.952* | **10.000** | 216.248 | 🎯 **Fin 9 Planes Prioritarios** (Ago-2028: 210.296 casos) |
| **Sep-2028** | **Remanentes (10 Planes):** 10.000 | **10.000** | 226.248 | Despliegue en planes con avance intermedio |
| **Oct-2028** | **Remanentes (10 Planes):** 10.000 | **10.000** | 236.248 | Despliegue en planes con avance intermedio |
| **Nov-2028** | **Remanentes (10 Planes):** 1.708 | **1.708** | 237.956 | 🏆 **Cierre Universo 20 Planes Completo** (Noviembre 2028) |

---

## 4. Visualización Interactiva en el Dashboard

En el visor web [viewer/index.html](file:///D:/Proyectos/plan-relevamiento-topologia-set-parcelario/viewer/index.html) se incorporaron las siguientes capacidades interactivas:

1. **Gráfica de Columnas Apiladas (Chart.js):**
   - Eje X: Meses proyectados (desde Nov-2026 hasta Ago-2028 / Nov-2028).
   - Eje Y: Casos mensuales (tope mensual de 10.000 casos con desglose por plan).
   - Paleta de color independiente por plan.
   - Tooltips enriquecidos con el detalle exacto de suministros aportados por cada plan y la suma total del mes.

2. **Selectores de Modo de Visualización:**
   - `[9 Planes Prioritarios (22 meses)]`: Visualiza la meta principal hasta Agosto 2028 (210.296 casos).
   - `[Universo 20 Planes (25 meses)]`: Incorpora los 10 planes remanentes hasta Noviembre 2028 (237.956 casos).
   - `[Suministros Totales (26 meses)]`: Proyecta considerando los totales nominales de la tabla.

3. **Pestaña Dedicada "Tabla Prioridades & Cronograma":**
   - Contiene la **Tabla Oficial de Prioridades** (con el orden del 1 al 9 y Plan 05 en curso).
   - Contiene el **Desglose Mes a Mes** con badges de colores para cada plan y el hito de finalización de cada etapa.

---

## 5. Archivos de Datos y Reportes Generados

- **Reporte CSV Prioridades:** `reports/tabla_prioridad_relevamiento_9_planes.csv`
- **Reporte CSV Cronograma Mes a Mes:** `reports/cronograma_despliegue_mensual_10k.csv`
- **Dataset JavaScript del Dashboard:** `viewer/data/dashboard_data.js`
- **Script Generador de Datos y Auditoría:** `src/03_analisis_calidad_poligonos_y_plan_futuro.py`

