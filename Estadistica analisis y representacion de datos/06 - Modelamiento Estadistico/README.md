# Módulo 06: Modelamiento Estadístico 📐🧮

<p align="center">
  <img src="https://img.shields.io/badge/Discipline-Estad%C3%ADstica-ea580c?style=for-the-badge&logo=scipy&logoColor=white" alt="Estadística"/>
  <img src="https://img.shields.io/badge/Topics-Codificaci%C3%B3n%20%7C%20GLM%20%7C%20Validaci%C3%B3n%20Cruzada%20%7C%20Pipelines-0ea5e9?style=for-the-badge" alt="Topics"/>
  <img src="https://img.shields.io/badge/Course-Estad%C3%ADstica%2C%20An%C3%A1lisis%20y%20Representaci%C3%B3n%20de%20Datos-6366f1?style=for-the-badge" alt="Course"/>
  <img src="https://img.shields.io/badge/Institution-USTA%20Tunja-1e3a8a?style=for-the-badge" alt="USTA"/>
</p>

Bienvenido al **Módulo 06**, el **séptimo** de la asignatura **Estadística, Análisis y Representación de Datos** de la *Especialización en Ciencia de Datos* de la **Universidad Santo Tomás — Seccional Tunja**.

---

## 🧭 ¿De qué trata este módulo?

Este módulo corresponde a la sección **2.4** del libro de la asignatura (*Modelamiento estadístico*) y reúne las cuatro piezas de un análisis predictivo/inferencial serio: **representar** las variables categóricas como números (*one-hot*, *label*, ordinal y *target encoding*), **ampliar** el modelo lineal a respuestas que no son normales (**modelos lineales generalizados**) y protegerse de los atípicos (**métodos robustos y no paramétricos**), **evaluar** con honestidad (R², RMSE, AIC/BIC y **validación cruzada** de varios tipos) y **juntar todo** en un flujo de trabajo con *statsmodels* (inferir) y *scikit-learn* (predecir).

El módulo **no** repite lo que ya existe en el repositorio: la regresión lineal y su diagnóstico están en el [Módulo 04 de este curso](../04%20-%20No%20Parametrica%20Regresion%20y%20Etica/README.md); la ingeniería de características orientada a ML, en [Data Science programming, Módulo 06](../../Data%20Science%20programming/06%20-%20Feature%20Engineering/README.md); y las métricas y la validación cruzada orientadas a ML, en [Machine Learning, Módulo 03](../../Machine%20Learning/03%20-%20Metricas%20y%20Ajuste%20de%20Hiperparametros/README.md). Aquí el enfoque es el del libro: **rigor estadístico** (supuestos, interpretación, intervalos), con **implementaciones desde cero en NumPy contrastadas por `assert` contra `statsmodels`, `SciPy` y `scikit-learn`**, **simulaciones** que miden qué promete cada método y **resultados reportados con honestidad** (cuando un modelo más complejo no mejora, cuando un método «robusto» pierde eficiencia, cuando una codificación filtra la respuesta).

> 🗺️ **Mapa del curso (ocho módulos):** **00** Fundamentos de Estadística y Análisis de Datos → **01** Estadística Descriptiva y Visualización → **02** Probabilidad y Distribuciones → **03** Inferencia Estadística → **04** No Paramétrica, Regresión y Ética → **05** Exploración y Limpieza de Datos → **06** Modelamiento Estadístico *(este módulo)* → **07** Temas Avanzados en *Data Analysis*. El [README del curso](../README.md) se actualizará con el índice completo.

> 🔗 **Conexión con otros cursos:** la selección y reducción previa de variables está en el [Módulo 05](../05%20-%20Exploracion%20y%20Limpieza%20de%20Datos/02_Seleccion_y_Reduccion_de_Dimensionalidad_PCA_tSNE.ipynb); los modelos de regresión y la validación cruzada de *Machine Learning* en [Modelos Lineales Supervisados](../../Machine%20Learning/01%20-%20Modelos%20Lineales%20Supervisados/README.md) y [Selección de Modelos y Optimización](../../Machine%20Learning/07%20-%20Seleccion%20de%20Modelos%20y%20Optimizacion/README.md).

> 🛠️ **Ponlo en práctica:** todos los cuadernos (estándar y *Para Dummies*) incluyen secciones **«🛠️ Práctica»**: una celda de código para que escribas tu solución y, justo debajo, la **solución guiada desplegable** (`💡 Haz clic aquí para ver la solución guiada...`). Inténtalo primero y abre la solución solo para comparar.

---

## 🎯 Objetivos de Aprendizaje del Módulo

1. **Representar categorías sin inventar supuestos:** elegir entre *label*, ordinal, *one-hot* y *target encoding*, evitar la **trampa de la variable ficticia** y la **fuga de información**.
2. **Modelar respuestas no normales:** ajustar GLM (Poisson, Binomial, Gamma, binomial negativa) con el algoritmo **IRLS**, interpretar los coeficientes como razones de tasas, *odds ratios* o razones de medias y **diagnosticar la sobredispersión**.
3. **Resistir a los atípicos:** aplicar regresión por **cuantiles**, **Huber**, **Theil–Sen** y el ***bootstrap* de pares**, conociendo su costo de eficiencia.
4. **Evaluar con honestidad:** calcular $R^2$, $R^2$ ajustado, MSE/RMSE/MAE, AIC/BIC; usar *hold-out*, ***k-fold***, ***leave-one-out***, validación **repetida**, **por grupos** y **temporal**, y reconocer el sobreajuste y la fuga al seleccionar variables.
5. **Integrar `statsmodels` y `scikit-learn`:** fórmulas de *patsy*, `summary()`, diagnósticos (VIF, Breusch–Pagan, Cook) y *pipelines* con `ColumnTransformer`, comprobando que ambas bibliotecas producen el mismo modelo.

---

## 📚 Estructura Curricular del Módulo

### 🎓 1. Cuadernos Académicos Estándar:
1. [**00_Representacion_de_Datos_OneHot_y_Label_Encoding.ipynb**](00_Representacion_de_Datos_OneHot_y_Label_Encoding.ipynb): *Sección 2.4.1.* La **matriz de diseño** y las escalas de medición. ***Label encoding*** desde cero (igual a `LabelEncoder`/`OrdinalEncoder`) y su **riesgo de orden falso**: el $R^2$ de validación cruzada va de −0.04 a 0.36 según el orden arbitrario de las 24 asignaciones posibles de códigos, frente a 0.395 con *one-hot*. **Codificación ordinal** con orden explícito y prueba $F$ anidada (pasos 1.71 y 0.72 t/ha, $p=0.19$). ***One-hot*** con NumPy (igual a `get_dummies` y `OneHotEncoder`), **trampa de la variable ficticia** (rango 4 de 5 columnas, número de condición $\approx10^{15}$), categoría de referencia (coeficientes = diferencias de medias; las predicciones no cambian) y equivalencia con los contrastes de *patsy*. ***Target encoding*** suavizado y *out-of-fold*: con una variable sin efecto real, el ingenuo sube el $R^2$ de entrenamiento (0.359 → 0.437) y **baja** el de prueba (0.362 → 0.261); validado contra `TargetEncoder`. Categorías nuevas, infrecuentes y columnas desalineadas. 2 prácticas (otra categoría de referencia; suavizar el codificador).
2. [**01_Modelos_Lineales_Generalizados_y_No_Parametricos.ipynb**](01_Modelos_Lineales_Generalizados_y_No_Parametricos.ipynb): *Sección 2.4.2.* Los tres componentes del GLM, la tabla de familias/enlaces y el algoritmo **IRLS** desde cero, **idéntico a `statsmodels.GLM`** para **Poisson con *offset*** (plagas por hectárea), **Binomial** (logística, *odds ratios* y razón de verosimilitudes) y **Gamma** (frente a MCO sobre $y$ y sobre $\log y$: la retransformación ingenua subestima la media, ≈ 0.89). **Sobredispersión:** $\hat\phi=3.83$, prueba de Cameron–Trivedi, sándwich HC0, casi-Poisson y **binomial negativa** por máxima verosimilitud de perfil (igual a `statsmodels.NegativeBinomial`); el IC «95 %» de Poisson ingenuo cubre solo 63.2 %. **Métodos robustos y no paramétricos:** regresión por **cuantiles** (programación lineal), **Huber** (IRLS) y **Theil–Sen** (iguales a `QuantReg`, `RLM` y `theilslopes`), con su costo de eficiencia medido por simulación; ***bootstrap* de pares** (cobertura 92.2 % frente a 69.0 % del IC $t$ clásico con varianza creciente). 2 prácticas (razón de tasas y razón de verosimilitudes; la recta del cuantil 0.75).
3. [**02_Evaluacion_del_Modelo_R2_MSE_y_Validacion_Cruzada.ipynb**](02_Evaluacion_del_Modelo_R2_MSE_y_Validacion_Cruzada.ipynb): *Sección 2.4.3.* $R^2$, $R^2$ ajustado, MSE, RMSE y MAE desde $\text{SST}=\text{SSR}+\text{SSE}$ (igual a `sklearn` y `statsmodels`); con 80 variables de ruido el $R^2$ de entrenamiento sube de 0.44 a 0.82 y el de **prueba cae a −0.90**. **AIC/BIC** desde la verosimilitud gaussiana y su comparación (simulada, 300 réplicas) con $R^2$ ajustado y validación cruzada para elegir el grado de un polinomio. ***k-fold*** y ***leave-one-out*** desde cero (con el atajo de la matriz sombrero $e_i/(1-h_{ii})$), **sesgo y varianza según $k$** (2-fold: sesgo +5.9; 10-fold: +0.5), variabilidad del *hold-out* frente a la validación repetida, IC *bootstrap* del RMSE. **Validación por grupos** (el bosque aleatorio pasa de $R^2=0.67$ con `KFold` a −0.85 con `GroupKFold`) y **temporal** (0.94 frente a 0.27 con *forward chaining*), estratificada, y la **fuga al seleccionar variables** (ruido puro: $R^2=0.23$ con fuga, −0.61 con *pipeline*). 2 prácticas (una variable de ruido y el BIC; selección dentro del *pipeline*).
4. [**03_Ejercicio_Practico_Scikit_Learn_y_Statsmodels.ipynb**](03_Ejercicio_Practico_Scikit_Learn_y_Statsmodels.ipynb): *Sección 2.4.4.* Flujo completo con el **conjunto de diabetes real de scikit-learn** (442 pacientes): fórmulas de *patsy*, `summary()` **reconstruido con álgebra matricial**, diagnósticos (VIF de 59 y 39 para `s1`/`s2`, Breusch–Pagan, Jarque–Bera, Durbin–Watson, apalancamiento y Cook) y errores estándar HC3, modelo reducido por prueba $F$, AIC y BIC. **Puente entre bibliotecas:** `LinearRegression` = `OLS` y `GammaRegressor(alpha=0)` = `GLM Gamma`; validación cruzada repetida (los cuatro modelos empatan en RMSE ≈ 54.6; $R^2$ honesto 0.49 frente a 0.518 dentro de muestra). ***Pipeline*** con `ColumnTransformer` (imputación, escalado, *one-hot*, ordinal y *splines*) sobre fincas **sintéticas** con datos mixtos y faltantes: los *splines* en la altitud mejoran ≈ 20 % el RMSE, cambiar de modelo casi nada; evaluación única en la prueba con IC *bootstrap* e inferencia con `statsmodels` (razones de medias). 3 prácticas (VIF a mano; distancia de Cook a mano; finca nueva con categoría desconocida y dato faltante).

---

### 📝 2. Taller Práctico Evaluativo (*Hands-On*):
* [**../homeworks/06_Modelamiento_Estadistico_Hands_On.ipynb**](../homeworks/06_Modelamiento_Estadistico_Hands_On.ipynb): Taller evaluativo que integra la codificación de variables, los GLM y métodos robustos, la evaluación con validación cruzada y el flujo `statsmodels` + `scikit-learn` en ejercicios prácticos. Versión guiada: [`../homeworks/Para Dummies/06_Modelamiento_Estadistico_Hands_On_Dummies.ipynb`](../homeworks/Para%20Dummies/06_Modelamiento_Estadistico_Hands_On_Dummies.ipynb).

---

### 🧸 3. Ruta Didáctica: Para Dummies:
Ubicada en la subcarpeta [`Para Dummies/`](Para%20Dummies/). **Sin jerga ni fórmulas**, con analogías cotidianas (plaza de mercado, colegio, cocina) y simulaciones sencillas con *NumPy*, *pandas*, *Matplotlib* y, donde hace falta, *scikit-learn* y *statsmodels*:
1. [**00_Codificacion_Variables_Dummies.ipynb**](Para%20Dummies/00_Codificacion_Variables_Dummies.ipynb): **El traductor de la plaza**: por qué numerar las variedades de papa (0, 1, 2, 3) le inventa un orden al modelo, las casillas de sí/no (y la que sobra) y por qué traducir una categoría con la respuesta de la misma finca es «copiar de la hoja de respuestas».
2. [**01_Modelos_GLM_Robustos_Dummies.ipynb**](Para%20Dummies/01_Modelos_GLM_Robustos_Dummies.ipynb): **Contar, decidir y resistir**: la recta que predice plagas negativas y probabilidades fuera de 0 a 1, los modelos de conteo y de sí/no, y el vendedor tramposo que arrastra al promedio pero no a la mediana.
3. [**02_Evaluacion_Modelo_Dummies.ipynb**](Para%20Dummies/02_Evaluacion_Modelo_Dummies.ipynb): **El examen sorpresa**: el estudiante que memoriza el simulacro, cinco exámenes en lugar de uno (validación cruzada) y por qué agregar columnas de lotería sube el R² del entrenamiento y hunde el del examen.
4. [**03_Receta_Pipeline_Dummies.ipynb**](Para%20Dummies/03_Receta_Pipeline_Dummies.ipynb): **La receta de la plaza**: lavar, pelar, cortar y cocinar en orden (*pipeline*), el examen de la receta completa y los dos cocineros —el que **explica** (statsmodels) y el que **predice** (scikit-learn)— que dan los mismos números.

---

## 💾 Datos Utilizados

Todos los datos son **sintéticos con semilla fija, generados por código dentro de cada cuaderno**, salvo el conjunto de diabetes, que **viene incluido en scikit-learn** (`load_diabetes`; no requiere red). **No hay descargas**, **no se necesita ninguna carpeta `data/`** ni se escribe ningún archivo. Como en los datos sintéticos se conoce el mecanismo verdadero, se puede **comprobar** que cada método hace lo que promete.

| Conjunto | Origen | Dónde se usa |
|---|---|---|
| **400 fincas** (variedad, manejo, fertilizante, rendimiento) | `default_rng(42)` | Cuaderno 00 (*label*, ordinal, *one-hot*, referencia) |
| **600 observaciones con 60 veredas** (sin efecto y con efecto real) | `default_rng(3)` | Cuaderno 00 (*target encoding* y fuga) |
| **400 parcelas con conteos de plagas** (con *offset* de área) | `default_rng(7)` | Cuaderno 01 (Poisson, IRLS) |
| **500 observaciones de hongo sí/no**; **400 ingresos por finca** (Gamma, millones de pesos **inventados**) | `default_rng(21)` y `default_rng(5)` | Cuaderno 01 (logística, Gamma) |
| **400 conteos sobredispersos** ($\alpha=0.8$) y 1 000 réplicas de $n=100$ | `default_rng(11)` y `default_rng(0)` | Cuaderno 01 (sobredispersión, NB, cobertura) |
| **150 puntos con 8 atípicos** y réplicas contaminadas/limpias; muestras de $n=40$ con varianza creciente | `default_rng(11)`, `(0)` y `(1)` | Cuaderno 01 (cuantiles, Huber, Theil–Sen, *bootstrap*) |
| **200 observaciones con 3 predictores reales** y hasta 80 de ruido; polinomio cúbico ($n=60$) | `default_rng(1)`, semillas 100+ y `(0)` | Cuaderno 02 (métricas, AIC/BIC) |
| **40 fincas × 10 mediciones**, **serie mensual de 240 meses** y **60 × 500 de ruido puro** | `default_rng(2)`, `(4)` y `(0)` | Cuaderno 02 (grupos, tiempo, fuga por selección) |
| **Diabetes** (442 pacientes, **real**, incluido en scikit-learn) | `sklearn.datasets.load_diabetes` | Cuaderno 03 (`statsmodels`, diagnósticos, comparación) |
| **500 fincas con datos mixtos y faltantes** | `default_rng(8)` | Cuaderno 03 (*pipeline*) |
| **Mini-ejemplos de juguete** (variedades, plagas, hongo, precios, plantas, fincas con faltantes) | `default_rng` con semilla fija | Los cuatro *Dummies* |

> ⚠️ **Los datos sintéticos son inventados** (cultivos, parcelas, fincas, ingresos y cifras): los resultados describen el **mecanismo estadístico**, **no** la realidad agropecuaria. El conjunto de diabetes es real, pero se usa solo para **ilustrar el flujo de modelamiento**, sin pretensión causal ni clínica.

## ⚙️ Requisitos

`numpy`, `pandas`, `matplotlib`, **`scipy`** (≥ 1.11), **`statsmodels`** (≥ 0.14) y **`scikit-learn`** (≥ 1.3; los cuadernos 00 y 03 usan `TargetEncoder` con suavizado numérico y `GammaRegressor(solver="newton-cholesky")`, que requieren ≥ 1.3 y ≥ 1.2 respectivamente), todos preinstalados en Google Colab. **No se necesita red.**

Se ejecutó de verdad, de arriba abajo y sin errores, con **Python 3.12**, **NumPy 2.5**, **pandas 2.3**, **SciPy 1.18**, **statsmodels 0.15**, **scikit-learn 1.9** y **Matplotlib 3.11** en Linux (con los *starters* de las prácticas tal cual —solo comentarios— y con una copia donde cada *starter* se reemplazó por su solución). *No se probó en Google Colab ni en Windows/macOS.* Tiempos aproximados en un equipo de escritorio (varían con la carga): cuaderno 00 ≈ 11 s, 01 ≈ 17 s, 02 ≈ 35 s y 03 ≈ 40 s; los *Dummies* tardan ≈ 3–7 s cada uno.

---

<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Asignatura: Estadística, Análisis y Representación de Datos</i>
  </p>
</div>
