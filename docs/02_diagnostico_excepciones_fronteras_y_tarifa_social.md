# 🔍 Diagnóstico de Límites de Subestaciones, Parcelas Cortadas y Tarifa Social

## 1. El Problema de las Parcelas Cortadas por Fronteras de SET
En los relevamientos de campo de cuadrillas comerciales y técnicas de EPEC, la delimitación de una **Subestación Transformadora (SET)** mediante polígonos rígidos (`vt_subestaciones_poly`) genera un dilema operativo recurrente:
- **Ambigüedad de asignación**: Si la línea perimetral de la SET corta un lote o inmueble por el medio, no se sabe a qué cuadrilla o alimentador corresponde relevar dicho suministro.
- **Riesgo de omisión o doble relevamiento**: El medidor puede quedar sin inspeccionar o ser relevado por dos cuadrillas distintas con reportes contradictorios.

Conforme a la decisión acordada en la **Compuerta de Clarificación (Respuesta A3)**:
> *"Mantener la frontera rígida de la SET y reportar la lista de parcelas cortadas en un log de excepciones para revisión manual"*.

Se identificaron **110,230 parcelas únicas** cuya geometría intersecta la frontera perimetral de los polígonos de SET. Todas han sido catalogadas con sus coordenadas exactas, distrito, barrio, CTMTBT de frontera y cantidad de suministros en [`reports/log_excepciones_parcelas_cortadas_frontera.csv`](../reports/log_excepciones_parcelas_cortadas_frontera.csv).

---

## 2. Marco Regulatorio y Diagnóstico de Tarifa Social (Decreto Provincial 43/2019)

EPEC estructura sus tarifas sociales bajo los lineamientos del **Decreto Provincial N° 43/2019** del Gobierno de la Provincia de Córdoba:
1. **Residencial Tarifa Social Provincial - Carenciados (`Resid TSP Caren Dto. 43/19`)**: 46,941 suministros.
2. **Residencial Tarifa Social Provincial - Indigentes (`Resid TSP Indig Dto. 43/19`)**: 38,244 suministros.
3. **Tarifa Social Provincial sin Medición (`Social Prov. sin medición`)**: 9,065 suministros.
4. **Tarifa Residencial Social Indigentes Histórica**: 6 suministros.

**Total Consolidado Provincial**: **94,256 suministros con Tarifa Social Oficial (7.80% del padrón provincial)**.

### Subestaciones con Alta Sensibilidad Social:
Se detectaron **621 subestaciones** donde la Tarifa Social representa **$\ge 20\%$ del total de suministros servidos**. En estos polígonos rige la directriz de la Compuerta de Clarificación (Respuesta A2):
> *"Identificar y clasificar con flag especial `TARIFA_SOCIAL = TRUE`, relevando con protocolo de sensibilidad comercial pero sin excluirlas del padrón"*.

---

## 3. Matriz de Clasificación de Subestaciones por Volumen

| Categoría de Subestación | Criterio de Suministros | Cantidad de SETs | % del Parque SET | Características Operativas |
| :--- | :---: | :---: | :---: | :--- |
| **MEGA_SET** | $\ge 1.000$ suministros | `1` | 0.02% | Centro de altísima densidad urbana / torres masivas |
| **GRANDE** | $500 - 999$ suministros | `31` | 0.59% | Barrios densos y corredores comerciales mixtos |
| **MEDIANA** | $150 - 499$ suministros | `1,226` | 23.15% | Sector residencial consolidado estándar |
| **PEQUEÑA** | $1 - 149$ suministros | `3,164` | 59.74% | Loteos suburbanos, zonas rurales o transformadores aéreos |
| **SIN_SUMINISTROS** | $0$ suministros en polígono | `874` | 16.50% | Polígonos de reserva, industriales puros o sin cruce espacial |
| **TOTAL** | - | **5,296** | **100.0%** | **Parque Provincial Analizado** |

