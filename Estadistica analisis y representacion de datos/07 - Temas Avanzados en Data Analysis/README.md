# Módulo 07: Temas Avanzados en Data Analysis 🚀📈

<p align="center">
  <img src="https://img.shields.io/badge/Discipline-Estad%C3%ADstica-ea580c?style=for-the-badge&logo=scipy&logoColor=white" alt="Estadística"/>
  <img src="https://img.shields.io/badge/Topics-Series%20de%20Tiempo%20%7C%20Clustering%20%7C%20%C3%81rboles%20%7C%20At%C3%ADpicos-0ea5e9?style=for-the-badge" alt="Topics"/>
  <img src="https://img.shields.io/badge/Course-Estad%C3%ADstica%2C%20An%C3%A1lisis%20y%20Representaci%C3%B3n%20de%20Datos-6366f1?style=for-the-badge" alt="Course"/>
  <img src="https://img.shields.io/badge/Institution-USTA%20Tunja-1e3a8a?style=for-the-badge" alt="USTA"/>
</p>

Bienvenido al **Módulo 07**, el **último** de la asignatura **Estadística, Análisis y Representación de Datos** de la *Especialización en Ciencia de Datos* de la **Universidad Santo Tomás — Seccional Tunja**. Este módulo **cierra el curso**: además de sus seis cuadernos, reúne al final los **Recursos Complementarios**, el **Glosario** y las **Referencias Bibliográficas** de todo el curso.

---

## 🧭 ¿De qué trata este módulo?

Este módulo desarrolla la sección **2.5** del libro de la asignatura (*Temas avanzados en Data Analysis*) y cierra el **Capítulo 2**. Después de **explorar y limpiar** (Módulo 05) y de **modelar con rigor** (Módulo 06), aquí se estudian cuatro familias de técnicas que aparecen en casi todo proyecto real: **series de tiempo** (datos con orden temporal), ***clustering*** (agrupar sin etiquetas), **árboles de decisión** (reglas legibles) y **detección de datos atípicos**; y dos cuadernos de **integración** que juntan las bibliotecas del curso (*pandas*, *NumPy*, *statsmodels*, *scikit-learn*) en un flujo completo y lo aplican a una tabla con la **estructura de un censo agropecuario**.

El módulo **no** repite lo que ya existe en el repositorio: el desarrollo extenso de árboles y bosques está en [Data Mining, Módulo 04](../../Data%20Mining/04%20-%20Arboles%20de%20Decision%20y%20Bosques%20Aleatorios/README.md); el *clustering* en [Machine Learning, Módulo 04](../../Machine%20Learning/04%20-%20Clustering%20No%20Supervisado/README.md) y [Data Mining, Módulo 03](../../Data%20Mining/03%20-%20Clustering%20y%20Mineria%20Reglas%20de%20Asociacion/README.md); y el EDA con *pandas* en [Data Science programming, Módulo 04](../../Data%20Science%20programming/04%20-%20EDA/README.md). Aquí el enfoque es el del libro: **rigor estadístico** (supuestos, interpretación, intervalos, tamaños del efecto) con **implementaciones desde cero en NumPy contrastadas con `assert` contra SciPy, statsmodels y scikit-learn**, simulaciones con semilla fija y **resultados reportados con honestidad**: un intervalo «del 95 %» de un pronóstico que cubre 79 %, una validación aleatoria que «mejora» 31 % un pronóstico por fuga de información, una regla Z que **no halla ninguno** de 24 atípicos que una regla basada en la mediana halla todos, o un detector LOF cuyo AUC pasa de 0.343 a 0.994 solo por cambiar el parámetro $k$.

> 🗺️ **Mapa del curso (ocho módulos):** **00** Fundamentos → **01** Estadística Descriptiva y Visualización → **02** Probabilidad y Distribuciones → **03** Inferencia Estadística → **04** No Paramétrica, Regresión y Ética → **05** Exploración y Limpieza de Datos → **06** Modelamiento Estadístico → **07** Temas Avanzados en *Data Analysis* *(este módulo; cierra el curso)*. El [README del curso](../README.md) contiene el índice completo.

> 🛠️ **Ponlo en práctica:** todos los cuadernos (estándar y *Para Dummies*) incluyen secciones **«🛠️ Práctica»**: una celda de código para que escribas tu solución y, justo debajo, la **solución guiada desplegable** (`💡 Haz clic aquí para ver la solución guiada...`). Inténtalo primero y abre la solución solo para comparar.

---

## 📚 Estructura Curricular del Módulo

### 🎓 1. Cuadernos Académicos Estándar:
| # | Cuaderno | Tema |
|:---:|:---|:---|
| 00 | [**00_Series_de_Tiempo.ipynb**](00_Series_de_Tiempo.ipynb) | Componentes y descomposición, estacionariedad (ADF y KPSS) y autocorrelación (ACF y PACF), suavizado exponencial y Holt–Winters, ARIMA y SARIMA, **validación temporal y origen móvil** frente a la validación aleatoria, *baselines*, MASE y **cobertura real** de los intervalos de pronóstico. 2 prácticas |
| 01 | [**01_Clustering.ipynb**](01_Clustering.ipynb) | ***k-means*** desde cero (óptimos locales), elección de $k$ (codo, silueta, Calinski–Harabasz, BIC), **clustering jerárquico**, **DBSCAN**, **mezclas gaussianas (EM)** y las limitaciones: escalado, ruido, validez y estabilidad. 2 prácticas |
| 02 | [**02_Arboles_de_Decision.ipynb**](02_Arboles_de_Decision.ipynb) | **CART** desde cero (Gini, entropía, varianza), compromiso sesgo–varianza, **poda por complejidad de costo**, importancia **MDI frente a permutación**, **inestabilidad** del árbol y comparación con un bosque aleatorio con prueba corregida. 2 prácticas |
| 03 | [**03_Ejercicios_Practicos_Pandas_NumPy_Sklearn_Statsmodels.ipynb**](03_Ejercicios_Practicos_Pandas_NumPy_Sklearn_Statsmodels.ipynb) | *Sección 2.5.1 (integración).* Una cooperativa **sintética** (400 fincas, 1 021 cosechas). ***pandas***: `merge(validate="m:1")`, `groupby` con `agg`/`transform`, `pivot_table` y rezagos (ninguna fila duplicada por el *join*, cada media verificada con `np.bincount`). ***NumPy***: *bootstrap* vectorizado idéntico al bucle y **por conglomerados** (el IC sale 18 % más ancho que el ingenuo, [1.294, 2.212] frente a [1.369, 2.145], porque las cosechas de una finca no son independientes) y *broadcasting* de distancias contra `cdist`. ***statsmodels***: ANOVA ($F=121.0$, $\eta^2=0.192$) y Tukey, regresión con **errores robustos por finca** (el error estándar del riego pasa de 0.158 a 0.200) y regresión logística (OR por 100 mm de lluvia de 3.46) **idéntica a *scikit-learn* sin penalización**. ***scikit-learn***: *pipelines*, validación por grupos, *baseline* (el modelo lineal con $R^2=0.39$ supera al bosque, 0.34, cuando la verdad es lineal), AUC 0.80 y el compromiso precisión–sensibilidad del umbral. 2 prácticas |
| 04 | [**04_Aplicacion_EDA_Censo_Nacional_Agropecuario.ipynb**](04_Aplicacion_EDA_Censo_Nacional_Agropecuario.ipynb) | *Sección 2.5.2.* **EDA de un archivo SINTÉTICO con la estructura de un censo agropecuario** (6 000 UPA, departamento y municipio, área total y sembrada, cultivo, tenencia, riego, maquinaria, crédito) con defectos plausibles. **No son datos del DANE.** Perfilado, normalización (16 → 8 departamentos, 15 → 6 formas de tenencia), reglas de consistencia con bitácora (90 UPA con área sembrada mayor que el total), **faltantes estructurales frente a MAR** y su efecto sobre la media (verdad 2.281 ha, sin limpiar 3.704, casos completos 2.385, imputada 2.276), **curva de Lorenz y coeficiente de Gini** desde cero (10 % de las UPA con 61.9 % del área sintética) con IC *bootstrap*, $\chi^2$, V de Cramér, intervalos de Wilson y **asociación cruda frente a ajustada** (OR 3.60 frente a 2.70), más una **guía para descargar y adaptar el censo real** con un validador de esquema. 2 prácticas |
| 05 | [**05_Deteccion_de_Datos_Atipicos_Simulacion_Multivariada.ipynb**](05_Deteccion_de_Datos_Atipicos_Simulacion_Multivariada.ipynb) | *Sección 2.5.3.* **Simulación multivariada** con `multivariate_normal` y **contaminación controlada** (marginal, correlación invertida y grupo desplazado). Reglas **Z, IQR y MAD** desde cero con sus falsas alarmas teóricas y el **enmascaramiento** (con 12 % de contaminación la desviación pasa de 1 a 2.82 y Z halla 0 de 24). **Mahalanobis clásica y robusta (MCD)** contra SciPy y scikit-learn, con un **oráculo** que marca el techo. ***Isolation Forest*** y **LOF** (el AUC de LOF cambia de 0.343 a 0.994 con $k$) y **evaluación** con AUC, AP y precisión/recall, repitiendo la simulación. **Equivalente en R** (`MASS::mvrnorm`, `mahalanobis`, `cov.rob`) como bloque de texto no ejecutado y guía de decisión. 2 prácticas |

---

### 📝 2. Taller Práctico Evaluativo (*Hands-On*):
* [**../homeworks/07_Temas_Avanzados_Hands_On.ipynb**](../homeworks/07_Temas_Avanzados_Hands_On.ipynb): Taller evaluativo que integra series de tiempo, *clustering*, árboles de decisión, el flujo con las cuatro bibliotecas, el EDA del censo y la detección de atípicos. Versión guiada: [`../homeworks/Para Dummies/07_Temas_Avanzados_Hands_On_Dummies.ipynb`](../homeworks/Para%20Dummies/07_Temas_Avanzados_Hands_On_Dummies.ipynb).

---

### 🧸 3. Ruta Didáctica: Para Dummies:
Ubicada en la subcarpeta [`Para Dummies/`](Para%20Dummies/). **Sin jerga ni fórmulas**, con analogías cotidianas de Boyacá (acopio de leche, cooperativa, plaza de mercado, libreta de la vereda):
1. [**00_Series_Tiempo_Dummies.ipynb**](Para%20Dummies/00_Series_Tiempo_Dummies.ipynb): **La leche del centro de acopio:** separar lo que sube, lo que se repite y el azar, y por qué el pronóstico «igual que el año pasado» es el rival a vencer.
2. [**01_Clustering_Dummies.ipynb**](Para%20Dummies/01_Clustering_Dummies.ipynb): **Agrupar las fincas de la cooperativa:** formar grupos de fincas parecidas sin que nadie diga cuáles son, y cuántos grupos tiene sentido hacer.
3. [**02_Arboles_Decision_Dummies.ipynb**](Para%20Dummies/02_Arboles_Decision_Dummies.ipynb): **El juego de las veinte preguntas en la papa:** un árbol de preguntas de sí/no, el peligro de memorizar y el truco de votar entre muchos árboles.
4. [**03_Ejercicios_Practicos_Dummies.ipynb**](Para%20Dummies/03_Ejercicios_Practicos_Dummies.ipynb): **La libreta, el contador y el adivino:** pegar dos listas sin contar doble (10 fincas repetidas añaden 13 cosechas fantasma), el contador que explica con margen de error (+1.39 t por cada 100 kg de abono) y el adivino que se prueba con fincas que no vio (error 1.26 t frente a 1.50 de «siempre el promedio»).
5. [**04_Aplicacion_EDA_Censo_Dummies.ipynb**](Para%20Dummies/04_Aplicacion_EDA_Censo_Dummies.ipynb): **El cuaderno de la vereda:** nueve «veredas» que en realidad son tres, cinco edades «999» que mueven la edad promedio de 51 a 67 años y quién tiene la tierra (el 10 % de las fincas, el 40 %).
6. [**05_Atipicos_Dummies.ipynb**](Para%20Dummies/05_Atipicos_Dummies.ipynb): **Los costales con piedras:** la regla del promedio que se deja engañar (0 de 24) frente a la del valor del medio (24 de 24) y los casos que **solo son raros al mirar dos medidas juntas** (0 de 8 por separado, 8 de 8 juntas).

---

## 🎯 Objetivos de Aprendizaje del Módulo

Al terminar el módulo podrás:
1. **Descomponer y pronosticar** series de tiempo (suavizado exponencial, ARIMA/SARIMA), **validar sin fuga** con partición temporal y origen móvil, compararlas con *baselines* y **medir la cobertura** de los intervalos.
2. **Agrupar sin etiquetas** con *k-means*, jerárquico, DBSCAN y mezclas gaussianas, elegir el número de grupos con criterios y **reconocer los límites** (escalado, formas, ruido, estabilidad).
3. **Construir, podar e interpretar** árboles de decisión, medir la importancia de las variables sin caer en el sesgo de la MDI y comparar con un bosque con incertidumbre.
4. **Integrar** *pandas*, *NumPy*, *statsmodels* y *scikit-learn* en un flujo con uniones seguras, remuestreo vectorizado, inferencia con errores por conglomerado y predicción validada por grupos.
5. **Aplicar un EDA completo** a una tabla de tipo censo: perfilar, normalizar, validar con reglas, evaluar el efecto de los faltantes, medir la concentración (Lorenz y Gini) y distinguir asociación cruda de ajustada, y **adaptar** el flujo a datos reales.
6. **Detectar atípicos** (Z, IQR, MAD, Mahalanobis robusta, *Isolation Forest*, LOF), **simular** contaminación controlada para evaluar detectores (AUC, precisión, *recall*) y decidir qué hacer con un dato marcado.

---

## 💾 Datos Utilizados

Todos los datos son **sintéticos o hipotéticos, con semilla fija, generados por código dentro de cada cuaderno**; **no hay descargas** y **no se necesita ninguna carpeta `data/`**, de modo que cada cuaderno es autocontenido en Google Colab. Las únicas excepciones son datos **incluidos en bibliotecas** que se leen sin red (los conjuntos *wine* y *breast_cancer* de scikit-learn).

| Conjunto | Origen | Dónde se usa |
|---|---|---|
| **Serie mensual de leche acopiada** (144 meses, tendencia, estacionalidad y ruido conocidos) | `default_rng` con semilla fija | Cuaderno 00 |
| **Grupos sintéticos** (`make_blobs`, `make_moons`) y el conjunto ***wine*** | scikit-learn | Cuaderno 01 |
| **Parcelas sintéticas con enfermedad** (humedad, pH, temperatura, interacción conocida) y ***breast_cancer*** | `default_rng`; `sklearn.datasets` | Cuaderno 02 |
| **Cooperativa sintética:** 400 fincas, 1 021 cosechas (3 duplicados y 12 faltantes añadidos), con mecanismo verdadero conocido (efecto de finca no observado) | `default_rng(2026)` | Cuaderno 03 |
| **Censo agropecuario SINTÉTICO:** 6 000 UPA (más 40 filas repetidas) en 8 departamentos, con errores de digitación, centinelas, categorías mal escritas y faltantes MAR | `default_rng(1964)` | Cuaderno 04 |
| **Normales multivariadas contaminadas** (marginal, correlación invertida, grupo desplazado) | `default_rng` con semillas fijas | Cuaderno 05 |
| **Mini-ejemplos de juguete** (leche, fincas, costales, libreta de la vereda) | Tablas y simulaciones con semillas fijas | Los seis *Dummies* |

> ⚠️ **Los datos son inventados** (fincas, censo, cosechas, series, personas): los resultados describen el **mecanismo**, **no** el rendimiento ni la situación de un caso real. **El archivo del cuaderno 04 NO contiene datos del DANE** ni de ninguna fuente oficial; su estructura se inspira en la de un censo agropecuario y ninguna cifra debe compararse con estadísticas oficiales. Los nombres de Boyacá y demás departamentos solo ambientan los ejemplos.

## ⚙️ Requisitos

`numpy`, `pandas` (≥ 2.1, < 3), `matplotlib`, `scipy`, `statsmodels` y `scikit-learn` (todos preinstalados en Google Colab). `seaborn` no se usa. **No se necesita red.** R **no** se ejecuta: su equivalente (cuaderno 05) es un bloque de texto.

Se ejecutó de verdad, de arriba abajo y sin errores, con **Python 3.12**, **NumPy 2.5**, **pandas 2.3**, **SciPy 1.18**, **statsmodels 0.15**, **scikit-learn 1.9** y **Matplotlib 3.11** en Linux (con los *starters* de las prácticas tal cual —solo comentarios— y con una copia donde cada *starter* se reemplazó por su solución). *No se probó en Google Colab ni en Windows/macOS.* Tiempos aproximados en un equipo de escritorio (varían con la carga del equipo): cuadernos 00, 01 y 02 ≈ 26-33 s, cuaderno 03 ≈ 16-20 s, cuaderno 04 ≈ 5-6 s y cuaderno 05 ≈ 22-32 s; los *Dummies* tardan ≈ 2-5 s.

---

## 🌐 Recursos Complementarios del Capítulo 2 y de Todo el Curso

Estas lecturas, fuentes de datos abiertos y herramientas amplían los Módulos 05 a 07 (y, junto con los [Recursos del Capítulo 1](../04%20-%20No%20Parametrica%20Regresion%20y%20Etica/README.md#-recursos-complementarios-del-capítulo-1), todo el curso). **No** contienen cifras: cada fuente es una referencia para consultar. Los libros y artículos que no están en el repositorio se citan **de memoria** y conviene verificar edición, año y capítulos; los enlaces deben comprobarse antes de usarlos en clase, porque los sitios cambian.

### 📖 Lecturas
| Tema | Referencia |
|---|---|
| Exploración y limpieza de datos | *Exploratory Data Analysis* — Tukey (1977); *Tidy data* — Wickham (2014); *Introduction to Data Mining* (capítulos 2 y 3) — Tan, Steinbach & Kumar y *Data Mining: The Textbook* (capítulo 2, sección 2.3) — Aggarwal, **ambos disponibles en `Data Mining/Libros/`** (verificados contra el índice); *Statistical Analysis with Missing Data* — Little & Rubin *(citado de memoria, verificar)* |
| Reducción de dimensionalidad | *The Elements of Statistical Learning* — Hastie, Tibshirani & Friedman; *An Introduction to Statistical Learning with Python* — James *et al.*; van der Maaten & Hinton (2008), *Visualizing data using t-SNE*, **JMLR** 9 *(citados de memoria, verificar)* |
| Modelamiento estadístico | *Generalized Linear Models* — McCullagh & Nelder; *Applied Linear Statistical Models* — Kutner *et al.*; *Data Analysis Using Regression and Multilevel/Hierarchical Models* — Gelman & Hill *(citados de memoria, verificar)* |
| Series de tiempo | *Forecasting: Principles and Practice* — Hyndman & Athanasopoulos (texto abierto en línea); *Time Series Analysis: Forecasting and Control* — Box, Jenkins, Reinsel & Ljung *(citados de memoria, verificar)* |
| *Clustering* | *Finding Groups in Data* — Kaufman & Rousseeuw; Ester *et al.* (1996), *A density-based algorithm for discovering clusters* (DBSCAN), **KDD**; Rousseeuw (1987), *Silhouettes*, **Journal of Computational and Applied Mathematics** 20 *(citados de memoria, verificar)* |
| Árboles y bosques | *Classification and Regression Trees* — Breiman *et al.*; Breiman (2001), *Random Forests*, **Machine Learning** 45; Strobl *et al.* (2007), **BMC Bioinformatics** 8; **disponibles en el repositorio:** `Data Mining/Libros/` (Tan, Steinbach & Kumar, capítulo 4) y [Data Mining, Módulo 04](../../Data%20Mining/04%20-%20Arboles%20de%20Decision%20y%20Bosques%20Aleatorios/README.md) *(citados de memoria, verificar)* |
| Atípicos y robustez | *Data Mining: The Textbook* (capítulo 8) y *Introduction to Data Mining* (capítulo 10), **en `Data Mining/Libros/`**; *Fundamentals of Robust Machine Learning* — Saleh, Majzoub & Saleh, **en `Machine Learning/Libros/`** (todos verificados contra el índice); Rousseeuw & Van Driessen (1999), **Technometrics** 41(3); Liu, Ting & Zhou (2008), *Isolation Forest*; Breunig *et al.* (2000), *LOF* *(citados de memoria, verificar)* |
| Programación científica con Python | *Python Data Science Handbook* — VanderPlas (**en `Data Science programming/Libros/Python/`**, verificado contra el índice) y *Hands-On Machine Learning with Scikit-Learn and PyTorch* — Géron (**en `Machine Learning/Libros/`**, verificado que trata el *toolkit* de scikit-learn) |
| Desigualdad y encuestas | *On Economic Inequality* — Sen (1973); *Sampling: Design and Analysis* — Lohr *(citados de memoria, verificar)* |

### 🗂️ Datos abiertos (para practicar el Capítulo 2)
| Fuente | Qué ofrece | Enlace *(verificar disponibilidad)* |
|---|---|---|
| **DANE** | Estadísticas oficiales, fichas metodológicas y microdatos anonimizados; **aquí se busca el Censo Nacional Agropecuario real** (la ruta cambia: ubícalo desde el portal y revisa fecha, licencia y diccionario) | <https://www.dane.gov.co> |
| **Datos Abiertos Colombia** | Portal nacional de datos abiertos del Estado colombiano | <https://www.datos.gov.co> |
| **IDEAM** | Series hidrometeorológicas (útiles para series de tiempo) | <http://www.ideam.gov.co> |
| **UPRA** y **Agronet** | Información de planificación rural y del sector agropecuario | <https://www.upra.gov.co> · <https://www.agronet.gov.co> |
| **Banco Mundial** y **Our World in Data** | Series de largo plazo con documentación | <https://data.worldbank.org> · <https://ourworldindata.org> |
| **UCI Machine Learning Repository**, **OpenML** y **Kaggle** | Conjuntos de datos para *clustering*, clasificación y detección de anomalías | <https://archive.ics.uci.edu> · <https://www.openml.org> · <https://www.kaggle.com/datasets> |
| **Datos incluidos sin red** | `sklearn.datasets` (iris, wine, diabetes, breast_cancer) y `statsmodels.datasets` (incluye series clásicas) | Documentación de [scikit-learn](https://scikit-learn.org/stable/datasets.html) y [statsmodels](https://www.statsmodels.org/stable/datasets/index.html) |

> 🔐 **Antes de usar datos reales:** revisa la **licencia**, la **finalidad** con que se recogieron, si contienen **datos personales** (Ley 1581 de 2012 de Colombia) y si hay riesgo de **reidentificación** (cuaderno 03 del Módulo 04). Cita siempre la fuente y la fecha de descarga, y **no compares** resultados reales con las cifras sintéticas del curso.

### 🧰 Herramientas
| Herramienta | Para qué sirve |
|---|---|
| **Python científico:** NumPy, SciPy, pandas, statsmodels, scikit-learn y matplotlib | Todo lo del curso; ver la [documentación de SciPy](https://docs.scipy.org/doc/scipy/), de [statsmodels](https://www.statsmodels.org/stable/) y de [scikit-learn](https://scikit-learn.org/stable/) |
| **R** (paquetes base `stats`, `MASS`, `robustbase`) | Alternativa para estadística y para covarianza robusta; el cuaderno 05 muestra el equivalente de `mvrnorm`, `mahalanobis` y `cov.rob` *(bloque de texto, no ejecutado; verificar versiones)* |
| **pmdarima**, **sktime** y **Prophet** | Pronóstico automático de series de tiempo *(no se usan aquí; el cuaderno 00 implementa los métodos desde cero)* |
| **hdbscan** y **PyOD** | *Clustering* jerárquico por densidad y colección de detectores de atípicos *(no se usan aquí; consulta su documentación)* |
| **pingouin**, **Fairlearn**, **OpenDP** | Pruebas estadísticas con salida resumida, equidad y privacidad diferencial *(no se usan aquí)* |
| **JASP** y **jamovi** | Programas gratuitos de estadística con interfaz gráfica, útiles para contrastar resultados |
| **Jupyter** y **Google Colab** | Cuadernos reproducibles; cada cuaderno del curso tiene su botón de Colab |

---

## 📖 Glosario del Curso

Definiciones breves de los términos que aparecen a lo largo de los ocho módulos (la columna **Mód.** indica dónde se trabaja con más detalle).

| Término | Definición | Mód. |
|---|---|:---:|
| **Población** | Conjunto completo de unidades sobre el que se quiere concluir (todas las fincas, todos los productores) | 00 |
| **Muestra** | Subconjunto observado de la población; permite estimar con incertidumbre | 00 |
| **Parámetro y estadístico** | El parámetro es una cantidad fija de la población ($\mu$, $\sigma$); el estadístico es una función de la muestra ($\bar x$, $s$) | 00 |
| **Escalas de medición** | Nominal, ordinal, de intervalo y de razón (Stevens): determinan qué operaciones tienen sentido (20 °C no es «el doble» de 10 °C) | 00 |
| **Sesgo** | Diferencia sistemática entre el valor esperado de un estimador y el parámetro; **no** disminuye al aumentar $n$ si viene del diseño | 00 |
| **Error estándar** | Desviación estándar de la distribución de muestreo de un estimador; para la media, $\sigma/\sqrt n$ | 00 |
| **Confusor** | Variable que afecta a la «causa» y al «efecto» y fabrica o esconde una asociación | 00 |
| **Paradoja de Simpson** | Una tendencia que aparece en cada subgrupo se invierte o desaparece en el total | 00 |
| **Media y mediana** | Medidas de tendencia central; la mediana es **robusta** a valores extremos, la media no | 01 |
| **Cuantil / percentil** | Valor bajo el cual queda una proporción dada de los datos; base de los diagramas de caja y de la regla del IQR | 01 |
| **Desviación estándar y varianza** | Medidas de dispersión alrededor de la media (varianza = promedio de las desviaciones al cuadrado, con divisor $n-1$ en la muestral) | 01 |
| **Asimetría y curtosis** | Forma de la distribución: simetría y peso de las colas | 01 |
| **Covarianza y correlación** | Medidas de asociación lineal; la correlación (Pearson) está acotada entre −1 y 1; **correlación no implica causalidad** | 01 |
| **Probabilidad condicional y teorema de Bayes** | $P(A\mid B)=P(A\cap B)/P(B)$; Bayes invierte el condicionamiento: $P(A\mid B)\propto P(B\mid A)P(A)$ | 02 |
| **Independencia** | $P(A\cap B)=P(A)P(B)$: saber $B$ no cambia la probabilidad de $A$ | 02 |
| **Variable aleatoria, esperanza y varianza** | Función que asigna un número a cada resultado; la esperanza es su promedio teórico y la varianza mide su dispersión | 02 |
| **Distribución normal** | Distribución simétrica en forma de campana, definida por $\mu$ y $\sigma$; base de muchos métodos de inferencia | 02 |
| **Ley de los grandes números** | El promedio muestral converge al valor esperado al crecer $n$ | 02 |
| **Teorema central del límite (TLC)** | La distribución de la media muestral se aproxima a una normal al crecer $n$, casi sin importar la distribución original | 02 |
| **Intervalo de confianza** | Rango construido con un procedimiento que, repetido, cubre el parámetro con la frecuencia nominal (p. ej., 95 %); **no** es «95 % de probabilidad de contener el parámetro» | 03 |
| **Valor p** | Probabilidad, bajo $H_0$, de obtener un resultado al menos tan extremo como el observado; **no** es la probabilidad de que $H_0$ sea cierta | 03 |
| **Error tipo I y tipo II; potencia** | Rechazar una $H_0$ cierta (tasa $\alpha$) y no rechazar una $H_0$ falsa (tasa $\beta$); la potencia es $1-\beta$ | 03 |
| **Tamaño del efecto** | Magnitud de una diferencia o asociación, independiente de $n$ (d de Cohen, $\eta^2$, V de Cramér); **significancia estadística ≠ relevancia práctica** | 03 |
| **Pruebas $t$ y $Z$** | Contrastes sobre medias: $Z$ si $\sigma$ es conocida o $n$ grande, $t$ (con $s$) en general; Welch no supone varianzas iguales | 03 |
| **Chi-cuadrado ($\chi^2$)** | Prueba de independencia o bondad de ajuste con tablas de frecuencias observadas y esperadas | 03 |
| **ANOVA** | Compara medias de $k$ grupos con la razón $F$ entre la variación entre grupos y dentro de ellos; se complementa con comparaciones *post hoc* (Tukey) | 03 |
| **Comparaciones múltiples** | Al hacer muchas pruebas crece la probabilidad de falsos «hallazgos»; se controla con Bonferroni, Holm o Benjamini–Hochberg (FDR) | 04 |
| **Estadística no paramétrica** | Métodos que no suponen una distribución concreta (rangos): Mann–Whitney, Wilcoxon, Kruskal–Wallis | 04 |
| **Regresión lineal y mínimos cuadrados** | Modelo $y=X\beta+\varepsilon$ cuyos coeficientes minimizan la suma de residuos al cuadrado; el coeficiente es el efecto *ceteris paribus* | 04 |
| **$R^2$** | Proporción de la varianza de $y$ explicada por el modelo; sube siempre al añadir variables (por eso existe el $R^2$ ajustado) | 04, 06 |
| **Multicolinealidad y VIF** | Predictores muy correlacionados inflan los errores estándar; el VIF cuantifica la inflación | 04 |
| **Apalancamiento y distancia de Cook** | Medidas de cuánto influye una observación en el ajuste de una regresión | 04 |
| **Heterocedasticidad y errores HC3** | Varianza del error no constante; los errores estándar robustos (HC) corrigen la inferencia | 04 |
| **Privacidad diferencial** | Garantía formal de que el resultado de un análisis casi no cambia por la presencia de un individuo; se logra añadiendo ruido (mecanismo de Laplace) | 04 |
| **$k$-anonimato** | Cada combinación de cuasi-identificadores se repite al menos en $k$ registros | 04 |
| **Análisis exploratorio de datos (EDA)** | Resumir y visualizar los datos para entenderlos y detectar problemas antes de modelar (Tukey) | 05 |
| **MCAR, MAR y MNAR** | Mecanismos de datos faltantes: completamente al azar, al azar condicionado a lo observado y no al azar | 05 |
| **Imputación** | Reemplazar datos faltantes por valores plausibles (media, regresión, múltiple con reglas de Rubin) | 05 |
| **PCA** | Análisis de componentes principales: proyecta en las direcciones de máxima varianza (vía SVD) | 05 |
| **t-SNE** | Técnica no lineal para visualizar datos de alta dimensión; útil para mirar, peligrosa para interpretar distancias | 05 |
| **Maldición de la dimensionalidad** | Al crecer el número de variables, los datos se vuelven dispersos y las distancias pierden contraste | 05 |
| **Codificación *one-hot*** | Representar una categoría con columnas indicadoras 0/1 (eliminando una para evitar la trampa de la variable ficticia) | 06 |
| **Modelo lineal generalizado (GLM)** | Extiende la regresión a respuestas no normales (Poisson, binomial, gamma) mediante una familia y una función de enlace | 06 |
| **Sobredispersión** | Varianza de los conteos mayor que la que implica el modelo (Poisson); se corrige con casi-Poisson o binomial negativa | 06 |
| **AIC y BIC** | Criterios de información que penalizan la complejidad al comparar modelos | 06 |
| **Validación cruzada** | Estimar el error fuera de muestra repitiendo ajuste y prueba en particiones de los datos (*k-fold*, *leave-one-out*, por grupos, temporal) | 06 |
| **Sobreajuste** | El modelo aprende el ruido del entrenamiento y generaliza mal | 06, 07 |
| **Fuga de datos (*leakage*)** | Información de prueba que se cuela en el entrenamiento (preprocesar antes de validar, mezclar filas dependientes, usar el futuro) | 06, 07 |
| ***Pipeline*** | Secuencia de pasos de preprocesamiento y modelo que se ajusta solo con el entrenamiento de cada pliegue | 06, 07 |
| ***Bootstrap*** | Remuestreo con reemplazo para estimar la variabilidad de un estadístico; el de conglomerados remuestrea grupos completos | 03, 06, 07 |
| **Serie de tiempo** | Observaciones ordenadas en el tiempo; se descompone en tendencia, estacionalidad y ruido | 07 |
| **Estacionariedad** | Propiedades estadísticas que no cambian con el tiempo; se contrasta con ADF y KPSS | 07 |
| **ACF y PACF** | Autocorrelación y autocorrelación parcial; identifican el orden de modelos AR y MA | 07 |
| **ARIMA / SARIMA** | Modelos autorregresivos integrados de medias móviles (con componente estacional) para pronosticar | 07 |
| **MASE** | Error de pronóstico escalado por el de un método ingenuo; menor que 1 = mejor que el *baseline* | 07 |
| ***Clustering* y *k-means*** | Agrupar sin etiquetas; *k-means* minimiza la inercia (suma de distancias cuadradas al centroide) y converge a óptimos locales | 07 |
| **Coeficiente de silueta** | Mide cuán bien separado está cada punto de los otros grupos (entre −1 y 1) | 07 |
| **DBSCAN y GMM** | Grupos por densidad (con ruido explícito) y mezclas gaussianas ajustadas con el algoritmo EM | 07 |
| **Árbol de decisión (CART)** | Partición recursiva del espacio con cortes que reducen la impureza (Gini, entropía, varianza); se poda para controlar el sobreajuste | 07 |
| **Bosque aleatorio** | Conjunto de árboles entrenados con remuestras y subconjuntos de variables, cuyo voto estabiliza la predicción | 07 |
| **Importancia por permutación** | Caída del desempeño al desordenar una variable; corrige el sesgo de la importancia MDI | 07 |
| **Curva de Lorenz y coeficiente de Gini** | Medidas de concentración (de la tierra, del ingreso): 0 = igualdad, cercano a 1 = máxima concentración | 07 |
| **Dato atípico (*outlier*)** | Observación que se aparta del patrón del resto; puede ser error, caso real raro o señal de otro proceso | 07 |
| **MAD** | Mediana de las desviaciones absolutas respecto a la mediana; escalada por 1.4826 estima $\sigma$ con datos normales | 07 |
| **Distancia de Mahalanobis y MCD** | Lejanía que tiene en cuenta la forma de la nube; el MCD estima media y covarianza con el subconjunto de menor determinante para resistir contaminación | 07 |
| ***Isolation Forest* y LOF** | Detectores de anomalías: aislamiento con cortes aleatorios y comparación de densidad local con los vecinos | 07 |
| **Precisión, sensibilidad (*recall*) y AUC** | Proporción de alertas correctas, proporción de casos reales hallados y área bajo la curva ROC (probabilidad de ordenar bien un par atípico–normal) | 07 |
| **Faltante estructural** | Dato que no existe por diseño (monto de crédito si no hay crédito), distinto de uno perdido; **no** se imputa | 07 |

---

## 📚 Referencias Bibliográficas

Formato APA 7. Las referencias marcadas con ✅ se **verificaron contra el PDF disponible en este repositorio** (portada y créditos); **todas las demás se citan de memoria** y llevan la marca *(citado de memoria, verificar)*: conviene comprobar edición, año, editorial y páginas antes de citarlas en un trabajo.

### Libros y artículos disponibles en el repositorio ✅
- Aggarwal, C. C. (2015). *Data mining: The textbook*. Springer. ✅ (`Data Mining/Libros/`)
- Géron, A. (2026). *Hands-on machine learning with Scikit-Learn and PyTorch*. O'Reilly Media. ✅ (`Machine Learning/Libros/`)
- Nisbet, R., Elder, J., & Miner, G. (2009). *Handbook of statistical analysis and data mining applications*. Academic Press. ✅ (`Data Mining/Libros/`)
- Saleh, R., Majzoub, S., & Saleh, A. K. Md. E. (2025). *Fundamentals of robust machine learning: Handling outliers and anomalies in data science*. Wiley. ✅ (`Machine Learning/Libros/`)
- Tan, P.-N., Steinbach, M., & Kumar, V. (2006). *Introduction to data mining*. Pearson Education. ✅ (`Data Mining/Libros/`)
- VanderPlas, J. (2017). *Python data science handbook*. O'Reilly Media. ✅ (`Data Science programming/Libros/Python/`)

### Estadística, probabilidad e inferencia
- Anscombe, F. J. (1973). Graphs in statistical analysis. *The American Statistician, 27*(1), 17–21. *(citado de memoria, verificar)*
- Benjamini, Y., & Hochberg, Y. (1995). Controlling the false discovery rate. *Journal of the Royal Statistical Society: Series B, 57*(1), 289–300. *(citado de memoria, verificar)*
- Cohen, J. (1988). *Statistical power analysis for the behavioral sciences* (2.ª ed.). Lawrence Erlbaum. *(citado de memoria, verificar)*
- Devore, J. L. (s. f.). *Probability and statistics for engineering and the sciences*. Cengage. *(citado de memoria, verificar edición y año)*
- Efron, B., & Hastie, T. (2016). *Computer age statistical inference*. Cambridge University Press. *(citado de memoria, verificar)*
- Efron, B., & Tibshirani, R. J. (1993). *An introduction to the bootstrap*. Chapman & Hall. *(citado de memoria, verificar)*
- Holm, S. (1979). A simple sequentially rejective multiple test procedure. *Scandinavian Journal of Statistics, 6*(2), 65–70. *(citado de memoria, verificar)*
- Huff, D. (1954). *How to lie with statistics*. W. W. Norton. *(citado de memoria, verificar)*
- Ioannidis, J. P. A. (2005). Why most published research findings are false. *PLoS Medicine, 2*(8), e124. *(citado de memoria, verificar)*
- Little, R. J. A., & Rubin, D. B. (2019). *Statistical analysis with missing data* (3.ª ed.). Wiley. *(citado de memoria, verificar)*
- Lohr, S. L. (2022). *Sampling: Design and analysis* (3.ª ed.). CRC Press. *(citado de memoria, verificar)*
- Montgomery, D. C., & Runger, G. C. (s. f.). *Applied statistics and probability for engineers*. Wiley. *(citado de memoria, verificar edición y año)*
- Newcombe, R. G. (1998). Two-sided confidence intervals for the single proportion: Comparison of seven methods. *Statistics in Medicine, 17*(8), 857–872. *(citado de memoria, verificar)*
- Reinhart, A. (2015). *Statistics done wrong*. No Starch Press. *(citado de memoria, verificar)*
- Rubin, D. B. (1987). *Multiple imputation for nonresponse in surveys*. Wiley. *(citado de memoria, verificar)*
- Sen, A. (1973). *On economic inequality*. Oxford University Press. *(citado de memoria, verificar)*
- Spiegelhalter, D. (2019). *The art of statistics: How to learn from data*. Basic Books. *(citado de memoria, verificar)*
- Tukey, J. W. (1977). *Exploratory data analysis*. Addison-Wesley. *(citado de memoria, verificar)*
- Wackerly, D. D., Mendenhall, W., & Scheaffer, R. L. (2008). *Mathematical statistics with applications* (7.ª ed.). Cengage. *(citado de memoria, verificar)*
- Walpole, R. E., Myers, R. H., Myers, S. L., & Ye, K. (s. f.). *Probability and statistics for engineers and scientists*. Pearson. *(citado de memoria, verificar edición y año)*
- Wasserman, L. (2004). *All of statistics: A concise course in statistical inference*. Springer. *(citado de memoria, verificar)*
- Wasserstein, R. L., & Lazar, N. A. (2016). The ASA statement on p-values: Context, process, and purpose. *The American Statistician, 70*(2), 129–133. *(citado de memoria, verificar)*
- Wickham, H. (2014). Tidy data. *Journal of Statistical Software, 59*(10), 1–23. *(citado de memoria, verificar)*
- Wilson, E. B. (1927). Probable inference, the law of succession, and statistical inference. *Journal of the American Statistical Association, 22*(158), 209–212. *(citado de memoria, verificar)*

### No paramétrica, regresión y modelamiento
- Conover, W. J. (1999). *Practical nonparametric statistics* (3.ª ed.). Wiley. *(citado de memoria, verificar)*
- Gelman, A., & Hill, J. (2007). *Data analysis using regression and multilevel/hierarchical models*. Cambridge University Press. *(citado de memoria, verificar)*
- Hollander, M., Wolfe, D. A., & Chicken, E. (2014). *Nonparametric statistical methods* (3.ª ed.). Wiley. *(citado de memoria, verificar)*
- Koenker, R., & Bassett, G. (1978). Regression quantiles. *Econometrica, 46*(1), 33–50. *(citado de memoria, verificar)*
- Kutner, M. H., Nachtsheim, C. J., Neter, J., & Li, W. (2005). *Applied linear statistical models* (5.ª ed.). McGraw-Hill/Irwin. *(citado de memoria, verificar)*
- McCullagh, P., & Nelder, J. A. (1989). *Generalized linear models* (2.ª ed.). Chapman & Hall. *(citado de memoria, verificar)*
- Montgomery, D. C., Peck, E. A., & Vining, G. G. (s. f.). *Introduction to linear regression analysis*. Wiley. *(citado de memoria, verificar edición y año)*

### Ética, privacidad y equidad
- Barocas, S., Hardt, M., & Narayanan, A. (2023). *Fairness and machine learning: Limitations and opportunities*. MIT Press. (Texto abierto en fairmlbook.org.) *(citado de memoria, verificar)*
- Dwork, C., & Roth, A. (2014). The algorithmic foundations of differential privacy. *Foundations and Trends in Theoretical Computer Science, 9*(3–4), 211–407. *(citado de memoria, verificar)*
- National Commission for the Protection of Human Subjects of Biomedical and Behavioral Research. (1979). *The Belmont report*. *(citado de memoria, verificar)*
- O'Neil, C. (2016). *Weapons of math destruction*. Crown. *(citado de memoria, verificar)*
- República de Colombia. (2012). *Ley Estatutaria 1581 de 2012, por la cual se dictan disposiciones generales para la protección de datos personales*. *(citado de memoria, verificar texto y vigencia)*

### Aprendizaje estadístico, series de tiempo, *clustering*, árboles y atípicos
- Box, G. E. P., Jenkins, G. M., Reinsel, G. C., & Ljung, G. M. (2015). *Time series analysis: Forecasting and control* (5.ª ed.). Wiley. *(citado de memoria, verificar)*
- Breiman, L. (2001). Random forests. *Machine Learning, 45*(1), 5–32. *(citado de memoria, verificar)*
- Breiman, L., Friedman, J. H., Olshen, R. A., & Stone, C. J. (1984). *Classification and regression trees*. Wadsworth. *(citado de memoria, verificar)*
- Breunig, M. M., Kriegel, H.-P., Ng, R. T., & Sander, J. (2000). LOF: Identifying density-based local outliers. *Proceedings of the ACM SIGMOD International Conference on Management of Data*, 93–104. *(citado de memoria, verificar)*
- Dempster, A. P., Laird, N. M., & Rubin, D. B. (1977). Maximum likelihood from incomplete data via the EM algorithm. *Journal of the Royal Statistical Society: Series B, 39*(1), 1–38. *(citado de memoria, verificar)*
- Ester, M., Kriegel, H.-P., Sander, J., & Xu, X. (1996). A density-based algorithm for discovering clusters in large spatial databases with noise. *Proceedings of the 2nd International Conference on Knowledge Discovery and Data Mining (KDD)*, 226–231. *(citado de memoria, verificar)*
- Hastie, T., Tibshirani, R., & Friedman, J. (2009). *The elements of statistical learning* (2.ª ed.). Springer. *(citado de memoria, verificar)*
- Hyndman, R. J., & Athanasopoulos, G. (2021). *Forecasting: Principles and practice* (3.ª ed.). OTexts. (Texto abierto en línea.) *(citado de memoria, verificar)*
- Hyndman, R. J., & Koehler, A. B. (2006). Another look at measures of forecast accuracy. *International Journal of Forecasting, 22*(4), 679–688. *(citado de memoria, verificar)*
- James, G., Witten, D., Hastie, T., Tibshirani, R., & Taylor, J. (2023). *An introduction to statistical learning with applications in Python*. Springer. *(citado de memoria, verificar)*
- Kaufman, L., & Rousseeuw, P. J. (1990). *Finding groups in data: An introduction to cluster analysis*. Wiley. *(citado de memoria, verificar)*
- Liu, F. T., Ting, K. M., & Zhou, Z.-H. (2008). Isolation forest. *Proceedings of the 8th IEEE International Conference on Data Mining (ICDM)*, 413–422. *(citado de memoria, verificar)*
- Mahalanobis, P. C. (1936). On the generalised distance in statistics. *Proceedings of the National Institute of Sciences of India, 2*(1), 49–55. *(citado de memoria, verificar)*
- Nadeau, C., & Bengio, Y. (2003). Inference for the generalization error. *Machine Learning, 52*(3), 239–281. *(citado de memoria, verificar)*
- Rousseeuw, P. J. (1987). Silhouettes: A graphical aid to the interpretation and validation of cluster analysis. *Journal of Computational and Applied Mathematics, 20*, 53–65. *(citado de memoria, verificar)*
- Rousseeuw, P. J., & Van Driessen, K. (1999). A fast algorithm for the minimum covariance determinant estimator. *Technometrics, 41*(3), 212–223. *(citado de memoria, verificar)*
- Strobl, C., Boulesteix, A.-L., Zeileis, A., & Hothorn, T. (2007). Bias in random forest variable importance measures: Illustrations, sources and a solution. *BMC Bioinformatics, 8*, 25. *(citado de memoria, verificar)*
- van der Maaten, L., & Hinton, G. (2008). Visualizing data using t-SNE. *Journal of Machine Learning Research, 9*, 2579–2605. *(citado de memoria, verificar)*

### Software
- Harris, C. R., Millman, K. J., van der Walt, S. J., *et al.* (2020). Array programming with NumPy. *Nature, 585*, 357–362. *(citado de memoria, verificar)*
- Hunter, J. D. (2007). Matplotlib: A 2D graphics environment. *Computing in Science & Engineering, 9*(3), 90–95. *(citado de memoria, verificar)*
- McKinney, W. (2010). Data structures for statistical computing in Python. *Proceedings of the 9th Python in Science Conference*, 56–61. *(citado de memoria, verificar)*
- Pedregosa, F., Varoquaux, G., Gramfort, A., *et al.* (2011). Scikit-learn: Machine learning in Python. *Journal of Machine Learning Research, 12*, 2825–2830. *(citado de memoria, verificar)*
- Seabold, S., & Perktold, J. (2010). statsmodels: Econometric and statistical modeling with Python. *Proceedings of the 9th Python in Science Conference*, 92–96. *(citado de memoria, verificar)*
- Venables, W. N., & Ripley, B. D. (2002). *Modern applied statistics with S* (4.ª ed.). Springer. *(citado de memoria, verificar)*
- Virtanen, P., Gommers, R., Oliphant, T. E., *et al.* (2020). SciPy 1.0: Fundamental algorithms for scientific computing in Python. *Nature Methods, 17*, 261–272. *(citado de memoria, verificar)*

---

<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Asignatura: Estadística, Análisis y Representación de Datos</i>
  </p>
</div>
