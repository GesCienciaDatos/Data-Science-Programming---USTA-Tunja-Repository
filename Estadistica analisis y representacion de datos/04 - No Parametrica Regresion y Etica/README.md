# Módulo 04: No Paramétrica, Regresión y Ética ⚖️📈

<p align="center">
  <img src="https://img.shields.io/badge/Discipline-Estad%C3%ADstica-ea580c?style=for-the-badge&logo=scipy&logoColor=white" alt="Estadística"/>
  <img src="https://img.shields.io/badge/Topics-No%20Param%C3%A9trica%20%7C%20Regresi%C3%B3n%20%7C%20%C3%89tica-0ea5e9?style=for-the-badge" alt="Topics"/>
  <img src="https://img.shields.io/badge/Course-Estad%C3%ADstica%2C%20An%C3%A1lisis%20y%20Representaci%C3%B3n%20de%20Datos-6366f1?style=for-the-badge" alt="Course"/>
  <img src="https://img.shields.io/badge/Institution-USTA%20Tunja-1e3a8a?style=for-the-badge" alt="USTA"/>
</p>

Bienvenido al **Módulo 04** de la asignatura **Estadística, Análisis y Representación de Datos** de la *Especialización en Ciencia de Datos* de la **Universidad Santo Tomás — Seccional Tunja**.

---

## 🧭 ¿De qué trata este módulo?

Este módulo desarrolla las secciones **1.4.2** (*estadística no paramétrica*), **1.4.3** (*regresión y correlación*) y **1.5** (*ética en el uso de datos*) del libro de la asignatura, y **cierra el Capítulo 1**. Después de aprender a describir (Módulo 01), a modelar la incertidumbre (02) y a inferir con pruebas e intervalos (03), aquí se responden tres preguntas: **¿qué hacer cuando los supuestos de la $t$ y del ANOVA no se cumplen?**, **¿cómo se modela y se contrasta la relación entre variables numéricas?** y **¿cómo se usan los datos con integridad, protegiendo a las personas?**

El módulo **no** repite lo que ya existe en el repositorio (la regresión como modelo predictivo, con scikit-learn, regularización y validación cruzada, está en [Data Science programming, Módulo 07](../../Data%20Science%20programming/07%20-%20Regression/README.md) y en [Machine Learning, Módulo 01](../../Machine%20Learning/01%20-%20Modelos%20Lineales%20Supervisados/README.md); la ética a nivel de proceso, en [Data Mining, Módulo 00](../../Data%20Mining/00%20-%20Introduccion%20al%20Data%20Mining/04_Etica_Privacidad_y_Gobernanza_en_Mineria_de_Datos.ipynb)). Aquí el enfoque es el del libro: **rigor estadístico** (supuestos, interpretación, tamaños del efecto, intervalos) con **implementaciones desde cero en NumPy contrastadas con `assert` contra SciPy, statsmodels y scikit-learn**, simulaciones con semilla fija y **resultados reportados con honestidad**: la prueba de Mann-Whitney **tampoco** se salva cuando las varianzas y los tamaños son distintos (rechaza 13.6 % con $H_0$ cierta), la correlación espuria que «rechaza» $\rho=0$ en 75.5 % de los pares de series independientes, el intervalo «95 %» de la pendiente que cubre solo 59.2 % con errores autocorrelacionados, o un modelo de crédito sin la variable de grupo que aprueba al 46.4 % de quienes sí pagarían en el grupo penalizado frente a 75.1 % en el otro.

> 🗺️ **Mapa del curso:** **00** Fundamentos → **01** Estadística Descriptiva y Visualización → **02** Probabilidad y Distribuciones → **03** Inferencia Estadística → **04** No Paramétrica, Regresión y Ética *(este módulo; cierra el Capítulo 1)* → **05** Exploración y Limpieza de Datos → **06** Modelamiento Estadístico → **07** Temas Avanzados. El [README del curso](../README.md) contiene el índice completo.

> 🛠️ **Ponlo en práctica:** todos los cuadernos (estándar y *Para Dummies*) incluyen secciones **«🛠️ Práctica»**: una celda de código para que escribas tu solución y, justo debajo, la **solución guiada desplegable** (`💡 Haz clic aquí para ver la solución guiada...`). Inténtalo primero y abre la solución solo para comparar.

---

## 📚 Estructura Curricular del Módulo

### 🎓 1. Cuadernos Académicos Estándar:
1. [**00_Estadistica_No_Parametrica_Kruskal_Wallis_y_Mann_Whitney.ipynb**](00_Estadistica_No_Parametrica_Kruskal_Wallis_y_Mann_Whitney.ipynb): *Sección 1.4.2.* **Rangos con empates** desde cero (idénticos con y sin un valor extremo: la media pasa de 51.5 a 87.9 con un error de digitación y los rangos no cambian). **Mann-Whitney:** $U$ con varianza corregida por empates, valor $p$ asintótico, **exacto** (recurrencia) y por **permutación**, todos contrastados con SciPy; tamaño del efecto como probabilidad de superioridad (= AUC), correlación biserial por rangos y **Hodges-Lehmann** con IC *bootstrap*. **Simulación honesta** (4 000 experimentos por escenario): con datos normales Mann-Whitney pierde ≈ 2.5 puntos de potencia, con lognormal y colas pesadas gana mucho (0.844 frente a 0.450 y 0.872 frente a 0.604), y con varianzas y tamaños distintos ninguna de las tres pruebas se salva salvo Welch. **Wilcoxon de rangos con signo** exacto por enumeración de $2^n$ signos (una parcela con error de digitación vuelve «no significativa» la $t$ pareada, $p=0.156$, mientras Wilcoxon da $p=0.0015$). **Kruskal-Wallis** con corrección por empates, $\varepsilon^2$ y permutación, y **Dunn + Holm** (con $k=2$, $H=z^2$). 2 prácticas (U y tamaño del efecto en dos lotes; Kruskal-Wallis y Dunn con otra familia de datos).
2. [**01_Regresion_Lineal_Simple_y_Correlacion.ipynb**](01_Regresion_Lineal_Simple_y_Correlacion.ipynb): *Sección 1.4.3 (parte 1).* **Pearson, Spearman y Kendall** desde cero (con IC de Fisher), el **cuarteto de Anscombe** (mismas medias, varianzas, $r=0.816$ y recta en los cuatro) y la **correlación espuria** entre caminatas aleatorias independientes. **MCO** con la descomposición $SCT=SCR+SCE$, errores estándar, IC de la pendiente y **bandas de confianza frente a predicción** (la de predicción es 6 veces más ancha en el ejemplo), verificadas contra SciPy y statsmodels. **Diagnóstico de supuestos** (un $R^2=0.89$ con modelo mal especificado). **Simulación** de insesgadez y cobertura (94.8 %), cobertura del IC con errores autocorrelacionados (59.2 %), **regresión a la media**, **atenuación** por error de medición (1.60 en vez de 2.00), **Theil-Sen** como regresión robusta no paramétrica y **extrapolación**. 2 prácticas (Pearson frente a Spearman con un valor mal digitado; intervalos al 99 % de la media y de predicción).
3. [**02_Regresion_Multiple_y_Diagnostico.ipynb**](02_Regresion_Multiple_y_Diagnostico.ipynb): *Sección 1.4.3 (parte 2).* **Forma matricial** (ecuaciones normales, QR y `lstsq`; matriz sombrero con traza $p$), variables indicadoras y la **trampa de la variable ficticia**, **$F$ parcial** (idéntica a `anova_lm`) y **sesgo por variable omitida** (el efecto del fertilizante sube de 0.0546 a 0.0679 al omitir el riego). **Multicolinealidad:** VIF desde cero, altitud y temperatura con VIF ≈ 73 (errores estándar 8.4 veces mayores) y los VIF del conjunto *diabetes* de scikit-learn. **Influencia:** apalancamiento, residuos studentizados y distancia de Cook (un solo error de digitación hunde el coeficiente de 0.0540 a 0.0370). **Contrastes:** Breusch-Pagan, Durbin-Watson, Shapiro, **errores HC3** (cobertura del IC: 90.0 % clásico frente a 94.6 % con HC3). **Selección:** $R^2$ sube con 40 columnas de ruido (0.618 a 0.719) mientras AIC, BIC y PRESS (LOOCV exacto) empeoran. 2 prácticas (VIF y eliminación de un predictor redundante; distancia de Cook).
4. [**03_Etica_en_el_Uso_de_Datos.ipynb**](03_Etica_en_el_Uso_de_Datos.ipynb): *Sección 1.5.* **Privacidad:** un *hash* de un identificador de 6 dígitos se invierte en 1.8 s (HMAC con clave no), cuasi-identificadores (41.5 % de personas únicas con 4 variables), **ataque de vinculación** (36 % identificadas), **$k$-anonimato** por generalización y supresión y ataque de homogeneidad ($l$-diversidad). **Privacidad diferencial con el mecanismo de Laplace desde cero** (cociente de densidades $\le e^{\varepsilon}$ verificado, error medio $=\Delta f/\varepsilon$, composición del presupuesto y respuesta aleatorizada). **P-hacking y comparaciones múltiples:** 20 desenlaces sin efecto dan 63.7 % de «hallazgos», **Bonferroni, Holm y Benjamini-Hochberg** (contrastados con `statsmodels`; con 1 000 pruebas BH detecta 81.4 % frente a 33.2 % de Bonferroni), detención opcional (23.5 % de error tipo I), el 46.6 % de falsos entre los «significativos» con hipótesis poco probables y la **maldición del ganador** (efecto exagerado 3.2 veces). **Sesgo y equidad** con datos sintéticos: proxies, métricas por grupo, umbrales por grupo y el conflicto entre criterios. **Interpretación responsable:** lista de verificación y desafíos contemporáneos. 3 prácticas (generalización mínima para $k=5$; media de edad con privacidad diferencial; Benjamini-Hochberg a mano).

---

### 📝 2. Taller Práctico Evaluativo (*Hands-On*):
* [**../homeworks/04_NoParametrica_Regresion_Etica_Hands_On.ipynb**](../homeworks/04_NoParametrica_Regresion_Etica_Hands_On.ipynb): Taller evaluativo que integra pruebas no paramétricas, regresión simple y múltiple con diagnóstico, y los mecanismos de ética (privacidad, multiplicidad y equidad) en ejercicios prácticos.

---

### 🧸 3. Ruta Didáctica: Para Dummies:
Ubicada en la subcarpeta [`Para Dummies/`](Para%20Dummies/). Sin jerga ni fórmulas, con analogías cotidianas de Boyacá; solo requieren `NumPy`, `pandas` y `matplotlib`:
1. [**00_NoParametrica_Dummies.ipynb**](Para%20Dummies/00_NoParametrica_Dummies.ipynb): **La carrera de las papas:** una papa gigante engaña al promedio (299 g contra 196 g) pero no al orden, la **carrera de pares** y **barajar** para medir qué tan raro es el resultado (en la finca A, 56 % de duelos ganados *no* es raro: 67 % de las barajadas lo igualan; en las rutas de bus, 86 % sí lo es) y tres fincas a la vez.
2. [**01_Regresion_Simple_Dummies.ipynb**](Para%20Dummies/01_Regresion_Simple_Dummies.ipynb): **La línea que mejor pasa por los puntos:** escoger la línea que menos se equivoca, leer su pendiente («por cada 10 kg de abono, +0.68 t/ha»), la **correlación que engaña** (una curva perfecta da 0.00 y un solo punto raro la dispara) y el peligro de **pasarse del rango**.
3. [**02_Regresion_Multiple_Dummies.ipynb**](Para%20Dummies/02_Regresion_Multiple_Dummies.ipynb): **La receta de la cosecha:** el abono se lleva el crédito del riego (+0.81 frente a +0.61 t/ha por 10 kg), **dos cocineros que dicen lo mismo** (altitud y temperatura: el aporte baila 8.7 veces más) y **un solo dato raro** que mueve la línea.
4. [**03_Etica_Datos_Dummies.ipynb**](Para%20Dummies/03_Etica_Datos_Dummies.ipynb): **El cuaderno de la tienda:** quitar el nombre no basta (77 % de personas únicas con vereda, edad y oficio), el **ruido que protege** y por qué preguntar mil veces lo deshace, **probar veinte colores de camisa** (65 % de «hallazgos» falsos) y **copiar el pasado** castiga a un grupo.

---

## 🎯 Objetivos de Aprendizaje del Módulo

Al terminar el módulo podrás:
1. **Elegir y justificar** entre una prueba paramétrica y una de rangos (Mann-Whitney, Wilcoxon, Kruskal-Wallis + Dunn), **implementarla** y reportar el **tamaño del efecto** y su incertidumbre.
2. **Ajustar e interpretar** una regresión lineal simple y múltiple (coeficientes *ceteris paribus*, $R^2$, IC de la media y de predicción), y **diagnosticar** supuestos, multicolinealidad y observaciones influyentes.
3. **Reconocer** cuándo la correlación o el modelo engañan (Anscombe, espuria, regresión a la media, atenuación, extrapolación) y qué alternativas robustas existen (Spearman, Theil-Sen, errores HC3).
4. **Proteger** datos de personas (seudonimización, $k$-anonimato, privacidad diferencial) y entender sus límites.
5. **Controlar** el *p-hacking* con correcciones por multiplicidad (Bonferroni, Holm, Benjamini-Hochberg) y evitar la detención opcional.
6. **Auditar la equidad** de un modelo con métricas por grupo, y **documentar** y reportar con interpretación responsable.

---

## 💾 Datos Utilizados

Todos los datos son **sintéticos o hipotéticos, con semilla fija, generados por código dentro de cada cuaderno**; **no hay descargas** y **no se necesita ninguna carpeta `data/`**, de modo que cada cuaderno es autocontenido en Google Colab y el repositorio no acumula archivos. Las únicas excepciones son datos **incluidos en bibliotecas** que se leen sin red: el **cuarteto de Anscombe** (4 × 11 pares publicados en 1973, escritos en el cuaderno) y el conjunto ***diabetes*** de scikit-learn (solo para ilustrar la multicolinealidad).

| Conjunto | Origen | Dónde se usa |
|---|---|---|
| **Pesos de parcelas en dos fincas** (lognormales), **conteos de insectos** en tres fincas (binomial negativa), **12 parcelas antes y después** (con un error de digitación) | `default_rng` con semillas fijas | Cuaderno 00 |
| **Respuesta a la dosis de fertilizante**, **fertilizante y rendimiento de papa** (40 parcelas, modelo verdadero conocido), caminatas aleatorias, series AR(1) | `default_rng` con semillas fijas | Cuaderno 01 |
| **Cuarteto de Anscombe** | Datos clásicos publicados (Anscombe, 1973) | Cuaderno 01 |
| **200 fincas de papa sintéticas** (fertilizante, lluvia, riego, altitud, temperatura, variedad) con modelo verdadero conocido; conjunto ***diabetes*** | `default_rng(2024)`; `sklearn.datasets.load_diabetes` | Cuaderno 02 |
| **Registro de salud de 5 000 personas** (cuasi-identificadores y diagnóstico), **identificadores de 6 dígitos**, **20 000 solicitantes de crédito** agrícola (grupos A y B, proxy de zona, decisiones históricas sesgadas) | `default_rng` con semillas fijas | Cuaderno 03 |
| **Mini-ejemplos de juguete** (papas, rutas de bus, abono y cosecha, tienda de vereda) | Tablas y simulaciones con semillas fijas | Los cuatro *Dummies* |

> ⚠️ **Los datos son inventados** (fincas, personas, créditos, diagnósticos, pruebas): los resultados describen el **mecanismo**, **no** el rendimiento ni la situación de un caso real. Ninguna cifra de fuentes oficiales ni del libro se reproduce aquí. Los nombres de Boyacá solo ambientan los ejemplos.

## ⚙️ Requisitos

`numpy`, `pandas` (≥ 2.1), `matplotlib`, `scipy`, `statsmodels` y `scikit-learn` (todos preinstalados en Google Colab). `hashlib`, `hmac`, `itertools` y `functools` son de la **biblioteca estándar**. **No se necesita red.** Los cuatro **Dummies** usan solo `NumPy`, `pandas` y `matplotlib`.

Se ejecutó de verdad, de arriba abajo y sin errores, con **Python 3.12**, **NumPy 2.5**, **pandas 2.3**, **SciPy 1.18**, **statsmodels 0.15**, **scikit-learn 1.9** y **Matplotlib 3.11** en Linux (con los *starters* de las prácticas tal cual —solo comentarios— y con una copia donde cada *starter* se reemplazó por su solución). *No se probó en Google Colab ni en Windows/macOS.* Tiempos aproximados en un equipo de escritorio (varían con la carga): cuadernos 00, 01 y 02 ≈ 6-9 s y cuaderno 03 ≈ 13-17 s; los *Dummies* tardan ≈ 4-24 s (los tiempos más altos se midieron con el equipo ocupado).

---

## 🌐 Recursos Complementarios del Capítulo 1

Este módulo cierra el Capítulo 1. Estas lecturas, fuentes de datos abiertos y herramientas amplían los Módulos 00 a 04. **No** contienen cifras: cada fuente es una referencia para consultar. Los libros y artículos se citan **de memoria** y conviene verificar edición, año y capítulos; los enlaces deben comprobarse antes de usarlos en clase, porque los sitios cambian.

### 📖 Lecturas
| Tema | Referencia |
|---|---|
| Visión general de la estadística moderna | *All of Statistics* — Wasserman (Springer, 2004); *Computer Age Statistical Inference* — Efron & Hastie (Cambridge, 2016); *The Art of Statistics* — Spiegelhalter (2019) *(citados de memoria, verificar)* |
| Probabilidad e inferencia con ingeniería | *Applied Statistics and Probability for Engineers* — Montgomery & Runger (Wiley); *Probability and Statistics for Engineering and the Sciences* — Devore (Cengage); *Mathematical Statistics with Applications* — Wackerly *et al.* (Cengage) *(citados de memoria, verificar)* |
| Exploración y visualización | *Exploratory Data Analysis* — Tukey (1977); *How to Lie with Statistics* — Huff (1954) *(citados de memoria, verificar)* |
| Regresión y diagnóstico | *Applied Linear Statistical Models* — Kutner *et al.*; *Introduction to Linear Regression Analysis* — Montgomery, Peck & Vining; *Data Analysis Using Regression and Multilevel/Hierarchical Models* — Gelman & Hill; *An Introduction to Statistical Learning (ISLP)* — James *et al.* *(citados de memoria, verificar)* |
| No paramétrica | *Nonparametric Statistical Methods* — Hollander, Wolfe & Chicken; *Practical Nonparametric Statistics* — Conover *(citados de memoria, verificar)* |
| Series de tiempo (Módulo 07) | *Forecasting: Principles and Practice* — Hyndman & Athanasopoulos (texto abierto en línea) *(citado de memoria, verificar)* |
| Uso correcto de los valores $p$ | Wasserstein & Lazar (2016), *The ASA statement on p-values*, **The American Statistician** 70(2); Ioannidis (2005), **PLoS Medicine** 2(8); *Statistics Done Wrong* — Reinhart (2015) *(citados de memoria, verificar)* |
| Privacidad, equidad y ética | *The Algorithmic Foundations of Differential Privacy* — Dwork & Roth (2014); *Fairness and Machine Learning* — Barocas, Hardt & Narayanan (texto abierto en fairmlbook.org); *Weapons of Math Destruction* — O'Neil (2016); *Informe Belmont* (1979); guías de ética estadística de la ASA; Ley Estatutaria 1581 de 2012 de Colombia *(citados de memoria, verificar texto y vigencia)* |
| Libros disponibles en este repositorio | *Handbook of Statistical Analysis and Data Mining Applications* — Nisbet, Miner & Elder (en `Data Mining/Libros/`), *Python Data Science Handbook* — VanderPlas (en `Data Science programming/Libros/`): **no verificados** capítulo por capítulo para estos temas |

### 🗂️ Datos abiertos (para practicar el Capítulo 1)
| Fuente | Qué ofrece | Enlace *(verificar disponibilidad)* |
|---|---|---|
| **Datos Abiertos Colombia** | Portal nacional de datos abiertos del Estado colombiano | <https://www.datos.gov.co> |
| **DANE** | Estadísticas oficiales y microdatos (incluye el Censo Nacional Agropecuario, que se trabaja en el Módulo 07) | <https://www.dane.gov.co> |
| **IDEAM** | Datos hidrometeorológicos y ambientales | <http://www.ideam.gov.co> |
| **UPRA** y **Agronet** | Información de planificación rural y del sector agropecuario | <https://www.upra.gov.co> · <https://www.agronet.gov.co> |
| **Banco Mundial** y **Our World in Data** | Indicadores de desarrollo y series de largo plazo con documentación | <https://data.worldbank.org> · <https://ourworldindata.org> |
| **Gapminder** | Series de indicadores con herramientas de visualización | <https://www.gapminder.org/data> |
| **UCI Machine Learning Repository**, **OpenML** y **Kaggle** | Conjuntos de datos para análisis y modelamiento | <https://archive.ics.uci.edu> · <https://www.openml.org> · <https://www.kaggle.com/datasets> |
| **Datos incluidos sin red** | `sklearn.datasets` (iris, wine, diabetes, breast_cancer) y los conjuntos de `statsmodels.datasets` | Documentación de [scikit-learn](https://scikit-learn.org/stable/datasets.html) y [statsmodels](https://www.statsmodels.org/stable/datasets/index.html) |

> 🔐 **Antes de usar datos reales:** revisa la **licencia**, la **finalidad** con que se recogieron, si contienen **datos personales** (Ley 1581 de 2012) y si hay riesgo de **reidentificación** (cuaderno 03). Cita siempre la fuente y la fecha de descarga.

### 🧰 Herramientas
| Herramienta | Para qué sirve |
|---|---|
| **Python científico:** NumPy, SciPy, pandas, statsmodels, scikit-learn, matplotlib y seaborn | Todo lo de este módulo; ver la [documentación de SciPy](https://docs.scipy.org/doc/scipy/) y de [statsmodels](https://www.statsmodels.org/stable/) |
| **pingouin** y **scikit-posthocs** | Pruebas estadísticas con salida resumida y pruebas *post hoc* (Dunn, Conover) *(no se usan aquí; el cuaderno 00 implementa Dunn desde cero)* |
| **Fairlearn**, **AIF360** | Métricas y mitigación de sesgo en modelos *(no se usan aquí; consulta su documentación)* |
| **OpenDP**, **diffprivlib** y la biblioteca de privacidad diferencial de Google | Mecanismos de privacidad diferencial listos para producción *(no se usan aquí; el cuaderno 03 implementa Laplace desde cero)* |
| **ARX** | Herramienta de anonimización ($k$-anonimato, $l$-diversidad) con interfaz gráfica *(no se usa aquí)* |
| **R** (paquetes base `stats` y `MASS`) | Alternativa para estadística; se usará como referencia en el Módulo 07 |
| **JASP** y **jamovi** | Programas gratuitos de estadística con interfaz gráfica, útiles para contrastar resultados |
| **Jupyter** y **Google Colab** | Cuadernos reproducibles; cada cuaderno del curso tiene su botón de Colab |

---

<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Asignatura: Estadística, Análisis y Representación de Datos</i>
  </p>
</div>
