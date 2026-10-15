# Talleres Prácticos Evaluativos (Hands-On Homeworks) 📝

> **Especialización en Ciencia de Datos**
> **Universidad Santo Tomás — Seccional Tunja**
> **Docente:** Santiago A. Zúñiga M.
> **Contacto:** [gestorvirtualcienciadatos@ustatunja.edu.co](mailto:gestorvirtualcienciadatos@ustatunja.edu.co)

---

## 📌 Descripción General

Esta carpeta contiene los **Talleres Prácticos Evaluativos (*Hands-On Homeworks*)** del curso **Estadística, Análisis y Representación de Datos**, uno por cada módulo teórico, en dos ediciones:

* **Edición estándar** (esta carpeta): 4 retos integradores con código más un reto final de conclusiones, con problemas **nuevos** (no repiten los datos ni los ejemplos del módulo), rúbrica de evaluación y checklist de entrega.
* **Edición Para Dummies** ([`Para Dummies/`](Para%20Dummies/)): los mismos objetivos con 3 retos muy guiados, en lenguaje cotidiano y con pistas.

A diferencia de los cuadernos de clase, **los talleres no traen soluciones**: el estudiante los resuelve de forma autónoma. Cada reto incluye una celda de **autoverificación** con `assert` que falla con un mensaje claro mientras el reto no esté resuelto y pasa con una solución correcta. Todos los datos son sintéticos, con semilla fija y sin descargas, y el último reto de cada taller estándar exige **interpretar los resultados con rigor estadístico** (valor P bien interpretado, tamaño del efecto frente a significancia, supuestos).

---

## 🗺️ Mapa de Talleres del Curso

| # | Taller Práctico | Módulo Asociado | Retos |
|---|---|---|---|
| **00** | [**00_Fundamentos_Estadistica_Hands_On.ipynb**](00_Fundamentos_Estadistica_Hands_On.ipynb) · [Dummies](Para%20Dummies/00_Fundamentos_Estadistica_Hands_On_Dummies.ipynb) | **Módulo 00: Fundamentos de Estadística y Análisis de Datos** | Muestreo de una cooperativa, encuesta con sesgo de no respuesta, correlación frente a causalidad y dos paradojas del agregado y del azar. |
| **01** | [**01_Descriptiva_Visualizacion_Hands_On.ipynb**](01_Descriptiva_Visualizacion_Hands_On.ipynb) · [Dummies](Para%20Dummies/01_Descriptiva_Visualizacion_Hands_On_Dummies.ipynb) | **Módulo 01: Estadística Descriptiva y Visualización** | Resúmenes robustos de la lluvia, simetrización con Box-Cox, qué ve cada coeficiente de asociación y un gráfico honesto de la temperatura. |
| **02** | [**02_Probabilidad_Distribuciones_Hands_On.ipynb**](02_Probabilidad_Distribuciones_Hands_On.ipynb) · [Dummies](Para%20Dummies/02_Probabilidad_Distribuciones_Hands_On_Dummies.ipynb) | **Módulo 02: Probabilidad y Distribuciones** | Detectores de fraude no independientes, distribución conjunta de incidentes y costos, llamadas con Poisson y exponencial, y el TLC con tiempos asimétricos. |
| **03** | [**03_Inferencia_Hands_On.ipynb**](03_Inferencia_Hands_On.ipynb) · [Dummies](Para%20Dummies/03_Inferencia_Hands_On_Dummies.ipynb) | **Módulo 03: Inferencia Estadística** | Intervalos de la proporción a la mediana, una prueba A/B, Chi-cuadrado de independencia y un ANOVA con comparaciones múltiples. |
| **04** | [**04_NoParametrica_Regresion_Etica_Hands_On.ipynb**](04_NoParametrica_Regresion_Etica_Hands_On.ipynb) · [Dummies](Para%20Dummies/04_NoParametrica_Regresion_Etica_Hands_On_Dummies.ipynb) | **Módulo 04: No Paramétrica, Regresión y Ética** | Pruebas por rangos con un dato mal digitado, regresión simple y predicción, regresión múltiple con colinealidad y datos de personas con privacidad, multiplicidad y equidad. |
| **05** | [**05_Exploracion_Limpieza_Hands_On.ipynb**](05_Exploracion_Limpieza_Hands_On.ipynb) · [Dummies](Para%20Dummies/05_Exploracion_Limpieza_Hands_On_Dummies.ipynb) | **Módulo 05: Exploración y Limpieza de Datos** | EDA antes de calcular, datos faltantes con reglas de Rubin, limpieza con un recibo que cuadra y PCA sin trampas. |
| **06** | [**06_Modelamiento_Estadistico_Hands_On.ipynb**](06_Modelamiento_Estadistico_Hands_On.ipynb) · [Dummies](Para%20Dummies/06_Modelamiento_Estadistico_Hands_On_Dummies.ipynb) | **Módulo 06: Modelamiento Estadístico** | Codificación sin inventar un orden, GLM de conteo con regresión robusta, evaluación sin engañarse y un informe con statsmodels y scikit-learn. |
| **07** | [**07_Temas_Avanzados_Hands_On.ipynb**](07_Temas_Avanzados_Hands_On.ipynb) · [Dummies](Para%20Dummies/07_Temas_Avanzados_Hands_On_Dummies.ipynb) | **Módulo 07: Temas Avanzados en Data Analysis** | Series de tiempo, *clustering*, árboles de decisión, un flujo integrado de análisis, EDA tipo censo agropecuario y detección de atípicos multivariados. |

---

## 📋 Instrucciones y Criterios de Entrega

1. **Entorno de Ejecución:** Python 3.10+ con NumPy, Pandas, SciPy, statsmodels, Scikit-Learn y Matplotlib. No hace falta conexión a internet.
2. **Ejecución Completa:** antes de la entrega, reinicia el kernel y ejecuta todas las celdas (*Restart Kernel and Run All Cells*). No deben quedar `# TODO` ni `...` pendientes y todas las celdas de autoverificación deben pasar.
3. **Autonomía:** los talleres no incluyen soluciones; consulta los cuadernos del módulo correspondiente como material de apoyo.
4. **Honestidad estadística:** reporta los resultados tal como salen. Un valor P no es la probabilidad de que $H_0$ sea cierta, y que una prueba no rechace $H_0$ no demuestra que sea cierta.
5. **Conclusiones:** el último reto de cada taller estándar es una reflexión escrita (5 a 8 líneas) que interpreta tus resultados.
6. **Evaluación:** cada taller suma 100 puntos; la rúbrica por criterio está al final de cada cuaderno.
7. **Tiempos:** todos corren en menos de 60 segundos.

---

<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Estadística, Análisis y Representación de Datos</i>
  </p>
</div>
