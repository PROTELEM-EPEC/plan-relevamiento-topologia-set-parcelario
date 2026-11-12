# 🎯 Plan de Relevamiento a Futuro & Auditoría de Calidad de Polígonos de Subestaciones (EPEC)

## 1. Resumen Ejecutivo y Diagnóstico Global

A partir de la integración de la tabla histórica de relevamiento en campo (`georef.relevamiento` con 473.762 suministros procesados), el padrón provincial consolidado (1.208.097 suministros) y la auditoría topológica de los 5.296 polígonos de subestaciones transformadoras (`EPEC:vt_subestaciones_poly`), se estructuró el **Plan de Relevamiento a Futuro** para el **Distrito 1 (Córdoba Capital)**.

### Balance de Relevamiento en los 20 Planes de Córdoba Capital:
- **Universo Total de Puntos**: **585.819 suministros**.
- **Relevamiento Histórico Efectivo**: **348.673 suministros (59,52% de avance)**.
- **Backlog Total a Relevar a Futuro**: **237.146 suministros (40,48% remanente)**.
  - **Clientes Comunes (CC)**: **220.395 suministros (92,94% del backlog)**.
  - **Tarifa Social Provincial (Decreto 43/2019)**: **15.947 suministros (6,72% del backlog)**.
  - **Otros Clientes (Oficial, AP, Especiales)**: **804 suministros (0,34% del backlog)**.

---

## 2. Auditoría de Calidad Geométrica de los Polígonos de Subestaciones

La calidad geométrica del polígono de una Subestación Transformadora (SET) determina la viabilidad operativa del relevamiento en campo: cuando una frontera atraviesa manzanas o divide parcelas al medio, los relevadores dudan sobre qué medidor corresponde a cuál transformador, generando errores de imputación y retrabajos costosos.

| Calidad Geométrica del Polígono | Criterio Topológico | Subestaciones (SET) | % del Total | Suministros Totales | Suministros Pendientes | Parcelas Cortadas | Diagnóstico Operativo |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **ALTA_LIMPIO** | $0$ parcelas cortadas por frontera | `963` | 18,18% | 12.594 | 5.776 | 0 | **Óptimo**: Límites limpios sobre ejes viales. Salida directa a campo. |
| **ALTA_LEVE** | $1 - 10$ parcelas cortadas | `1.278` | 24,13% | 40.634 | 18.944 | 9.167 | **Favorable**: Afección perimetral mínima. Relevamiento masivo viable. |
| **MEDIA_MODERADO** | $11 - 30$ parcelas cortadas | `973` | 18,37% | 99.947 | 31.294 | 21.127 | **Precaución**: Requiere plano de detalle en bordes para cuadrillas. |
| **BAJA_CONFLICTO** | $> 30$ parcelas cortadas por frontera | `1.923` | 36,31% | 321.611 | 82.453 | 133.457 | **Crítico**: Frontera corta parcelas al medio. Alto riesgo de asignación cruzada. |
| **TOTAL** | - | **5.296** | **100,0%** | **474.786** | **138.467** | **163.751** | Consolidado Provincial en Polígonos |

---

## 3. Matriz de Priorización Operativa para el Plan Futuro (5 Cuadrantes)

Cruzando el volumen pendiente, la calidad del polígono y la concentración de Tarifa Social, se definió la siguiente matriz de asignación para cuadrillas:

| Cuadrante de Priorización | SETs | % SETs | Suministros Pendientes | Tarifa Social | Parcelas Cortadas | Directriz Operativa |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **`1_RELEVAMIENTO_INMEDIATO`** | **387** | 7,31% | **44.699** | 2.264 | 6.482 | **Máxima Productividad**: SETs con alta demanda pendiente ($\ge 50$ sumis), polígono limpio (calidad alta/media) y predominio CC. Asignar cuadrillas estándar de inmediato. |
| **`2_SENSIBILIDAD_SOCIAL`** | **105** | 1,98% | **7.194** | 2.546 | 1.833 | **Atención Comunitaria**: SETs con $\ge 20\%$ Tarifa Social. Relevamiento bajo protocolo con centros vecinales y mediación territorial. |
| **`3_SANEAMIENTO_TOPOLOGICO_PREVIO`** | **449** | 8,48% | **78.898** | 5.822 | 28.767 | **BLOQUEADO EN CAMPO**: Polígonos con severo conflicto perimetral ($>30$ cortadas). **No enviar cuadrillas hasta redefinir el polígono en GIS**, evitando retrabajo o imputación errónea. |
| **`4_AVANZADA_O_COMPLETADA`** | **3.481** | 65,73% | **7.676** | 26.585 | 121.740 | **Remanente Residual**: SETs con avance $\ge 75\%$ o saldo $<30$ sumis (423.101 suministros ya relevados históricamente). Asignar cuadrillas livianas de barrido. |
| **`5_SIN_DEMANDA_O_ESPECIAL`** | **715** | 13,50% | **0** | 0 | 4.929 | **Especiales**: SETs industriales, telemedidas exclusivas o sin suministros activos. |

---

## 4. Estado de Relevamiento por Plan de Lectura (Distrito 1)

| Plan de Lectura | Total Puntos | Relevados Históricos | % Avance | Pendientes Totales | Pendientes CC | Pendientes Tarifa Social | Pendientes Otros | Diagnóstico Operativo y Recomendación |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Plan 14** | 47.912 | 33 | **0,07%** | **47.879** | 47.764 | 26 | 89 | **Prioridad 1 Absoluta**: Centro / Nueva Cba. 99,8% CC. |
| **Plan 15** | 30.593 | 598 | **1,95%** | **29.995** | 29.751 | 68 | 176 | **Prioridad 1 Absoluta**: Centro-Norte residencial masivo CC. |
| **Plan 08** | 27.622 | 87 | **0,31%** | **27.535** | 27.061 | 404 | 70 | **Prioridad 1 Absoluta**: Este masivo residencial CC. |
| **Plan 07** | 25.216 | 868 | **3,44%** | **24.348** | 20.982 | 3.285 | 81 | **Prioridad Mixta**: Relevamiento CC con cuadrilla social de apoyo. |
| **Plan 11** | 24.233 | 440 | **1,82%** | **23.793** | 18.336 | **5.335** | 122 | **Sensibilidad Crítica**: 22,4% Tarifa Social pendiente. |
| **Plan 17** | 34.787 | 15.291 | 43,96% | **19.496** | 19.391 | 53 | 52 | **Prioridad 2 CC**: Corredor Centro-Sur aéreo/subterráneo. |
| **Plan 09** | 16.863 | 816 | **4,84%** | **16.047** | 13.466 | **2.507** | 74 | **Sensibilidad Social**: 15,6% Tarifa Social en periferia. |
| **Plan 12** | 22.098 | 11.646 | 52,70% | **10.452** | 10.323 | 114 | 15 | **Prioridad 2 CC**: Sureste residencial CC remanente. |
| **Plan 05** | 27.593 | 22.155 | 80,29% | **5.438** | 3.820 | 1.589 | 29 | **Fase Final**: Barrido de remanentes con foco en Tarifa Social. |
| **Plan 16** | 47.984 | 43.301 | 90,24% | **4.683** | 4.619 | 55 | 9 | **Fase Final**: Solo barrido residual masivo. |
| **Plan 03** | 38.204 | 33.581 | 87,90% | **4.623** | 4.191 | 416 | 16 | **Fase Final**: Barrido residual de borde. |
| **Plan 10** | 17.360 | 12.857 | 74,06% | **4.503** | 2.966 | 1.515 | 22 | **Fase Final / Social**: Remanentes vulnerables. |
| **Plan 20** | 41.474 | 37.856 | 91,28% | **3.618** | 3.582 | 28 | 8 | **Fase Final**: Barrido de remanentes periféricos. |
| **Plan 01** | 29.910 | 27.053 | 90,45% | **2.857** | 2.845 | 7 | 5 | **Fase Final**: Barrido residual de alta densidad. |
| **Plan 19** | 29.408 | 26.600 | 90,45% | **2.808** | 2.787 | 14 | 7 | **Fase Final**: Barrido residual. |
| **Plan 13** | 34.498 | 31.730 | 91,98% | **2.768** | 2.705 | 54 | 9 | **Fase Final**: Barrido residual comercial. |
| **Plan 18** | 33.248 | 30.741 | 92,46% | **2.507** | 2.083 | 412 | 12 | **Fase Final**: Barrido residual oeste. |
| **Plan 04** | 24.285 | 22.690 | 93,43% | **1.595** | 1.589 | 5 | 1 | **Fase Final**: Barrido residual. |
| **Plan 02** | 19.856 | 18.582 | 93,58% | **1.274** | 1.268 | 4 | 2 | **Fase Final**: Barrido residual. |
| **Plan 06** | 12.675 | 11.748 | 92,69% | **927** | 866 | 56 | 5 | **Fase Final**: Barrido residual noreste. |
| **TOTAL** | **585.819** | **348.673** | **59,52%** | **237.146** | **220.395** | **15.947** | **804** | **Consolidado 20 Planes** |

---

## 5. Hoja de Ruta Operativa y Recomendaciones para Despliegue de Cuadrillas

1. **Etapa 1 - Despliegue Inmediato CC de Máxima Eficiencia (104.910 suministros)**:
   - Planes 14 (Nueva Cba / Centro: 47.879 sumis), 15 (Centro Norte: 29.995 sumis) y 08 (Este: 27.535 sumis).
   - Más del 98% de Clientes Comunes en SETs de polígonos limpios.
   - Máximo rendimiento diario por cuadrilla, medidores en fachada accesibles y bajo tiempo de traslado.

2. **Etapa 2 - Saneamiento Topológico Previo en GIS (449 Subestaciones / 78.898 suministros)**:
   - **Acción Obligatoria**: Antes de activar las cuadrillas en las 449 SETs con conflicto topológico severo (`reports/matriz_priorizacion_plan_futuro_sets.csv`), el equipo de GIS debe ajustar el límite perimetral de la SET a las calles o límites parcelarios reales.
   - **Beneficio**: Evita el 100% de los reclamos y retrabajos por suministros asignados a subestaciones equivocadas.

3. **Etapa 3 - Cuadrillas con Protocolo Comunitario para Tarifa Social (15.947 suministros)**:
   - Planes 11 (5.335 pendientes TSP), 07 (3.285 TSP), 09 (2.507 TSP), 05 (1.589 TSP) y 10 (1.515 TSP).
   - Relevamiento coordinado previamente con centros vecinales y referentes barriales de EPEC Comercial.

4. **Etapa 4 - Barrido Sistemático de Remanentes (12 Planes con > 80% avance)**:
   - Asignar cuadrillas ligeras para el cierre de los 33.376 puntos remanentes en los 12 planes avanzados.

