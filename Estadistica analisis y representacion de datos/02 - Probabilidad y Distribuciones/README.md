# Módulo 02: Probabilidad y Distribuciones 🎲🔔

<p align="center">
  <img src="https://img.shields.io/badge/Discipline-Estad%C3%ADstica-ea580c?style=for-the-badge&logo=scipy&logoColor=white" alt="Estadística"/>
  <img src="https://img.shields.io/badge/Topics-Probabilidad%20%7C%20Distribuciones%20%7C%20TLC-0ea5e9?style=for-the-badge" alt="Topics"/>
  <img src="https://img.shields.io/badge/Course-Estad%C3%ADstica%2C%20An%C3%A1lisis%20y%20Representaci%C3%B3n%20de%20Datos-6366f1?style=for-the-badge" alt="Course"/>
  <img src="https://img.shields.io/badge/Institution-USTA%20Tunja-1e3a8a?style=for-the-badge" alt="USTA"/>
</p>

Bienvenido al **Módulo 02** de la asignatura **Estadística, Análisis y Representación de Datos** de la *Especialización en Ciencia de Datos* de la **Universidad Santo Tomás — Seccional Tunja**.

---

## 🧭 ¿De qué trata este módulo?

Este módulo desarrolla la sección **1.3.4** del libro de la asignatura (*Probabilidad: teoría básica, independencia, variables aleatorias y distribuciones*). La estadística descriptiva (Módulo 01) **resume lo que ya pasó**; la probabilidad es el lenguaje para **razonar sobre lo que puede pasar** y, sobre todo, para saber **qué tan creíble es una conclusión obtenida de una muestra**. La pregunta que responde es **¿cómo se modela y se cuantifica la incertidumbre?**, antes de pasar a la inferencia (intervalos de confianza y pruebas de hipótesis).

El módulo **no** repite lo que ya existe en el repositorio (el resumen de datos con *pandas* y el EDA están en [Data Science programming, Módulo 04](../../Data%20Science%20programming/04%20-%20EDA/README.md); las métricas de clasificación, que son probabilidades condicionales disfrazadas, en [Machine Learning, Módulo 03](../../Machine%20Learning/03%20-%20Metricas%20y%20Ajuste%20de%20Hiperparametros/00_Metricas_de_Clasificacion.ipynb)). Aquí el enfoque es el del libro: **rigor estadístico** (definiciones, supuestos, interpretación) con **implementaciones desde cero** (enumeración exacta con `Fraction`, funciones de masa y densidad con la biblioteca estándar, transformada inversa, integración numérica) **contrastadas con `assert` contra SciPy**, simulaciones con semilla fija y **resultados reportados con honestidad**: la normal que **no** aproxima bien una binomial con $np=1$, la Poisson que **se rechaza** ante conteos sobredispersos, el intervalo «95 %» que cubre solo ≈ 88 % con $n=30$ en una población asimétrica.

> 🗺️ **Mapa del curso:** **00** Fundamentos → **01** Estadística Descriptiva y Visualización → **02** Probabilidad y Distribuciones *(este módulo)* → **03** Inferencia Estadística → **04** No Paramétrica, Regresión y Ética → **05** Exploración y Limpieza de Datos → **06** Modelamiento Estadístico → **07** Temas Avanzados. El [README del curso](../README.md) contiene el índice completo.

> 🛠️ **Ponlo en práctica:** todos los cuadernos (estándar y *Para Dummies*) incluyen secciones **«🛠️ Práctica»**: una celda de código para que escribas tu solución y, justo debajo, la **solución guiada desplegable** (`💡 Haz clic aquí para ver la solución guiada...`). Inténtalo primero y abre la solución solo para comparar.

---

## 📚 Estructura Curricular del Módulo

### 🎓 1. Cuadernos Académicos Estándar:
1. [**00_Probabilidad_Basica_Condicional_Bayes_e_Independencia.ipynb**](00_Probabilidad_Basica_Condicional_Bayes_e_Independencia.ipynb): *Sección 1.3.4 (parte 1).* **Espacio muestral, eventos y axiomas de Kolmogorov** verificados con fracciones exactas (inclusión-exclusión, complemento, monotonía) y la **convergencia de la frecuencia relativa**; **conteo** (permutaciones y combinaciones) y el **problema de los cumpleaños** (exacto: 0.5073 con 23 personas; la simulación coincide). **Probabilidad condicional, probabilidad total y Bayes** en una planta de empaque **hipotética** (la línea C produce el 20 % pero aporta el 38.7 % de los defectuosos) y en una **prueba de detección** (con prevalencia 1 %, sensibilidad 90 % y especificidad 95 %, el VPP es solo 15.4 %; un segundo positivo independiente lo sube a 76.6 %; en frecuencias naturales y en *odds*; con prevalencia baja manda la especificidad). **Independencia:** por parejas frente a mutua (X, Y, X xor Y), excluyentes frente a independientes y una **causa común** que multiplica por ≈ 160 la probabilidad de falla de un sistema «redundante». **Monty Hall** con presentador informado (2/3) frente a ignorante (1/2): el mecanismo que genera el dato importa. 2 prácticas (VPP y especificidad mínima de una prueba de plaga; fiabilidad de un sistema serie-paralelo).
2. [**01_Variables_Aleatorias_Esperanza_y_Varianza.ipynb**](01_Variables_Aleatorias_Esperanza_y_Varianza.ipynb): *Sección 1.3.4 (parte 2).* Variable aleatoria como función; **masa, densidad y acumulada**; una clase `VADiscreta` desde cero con fracciones exactas contrastada con `scipy.stats.rv_discrete`. **Esperanza y varianza:** linealidad (aun con dependencia), $\text{Var}(aX+b)=a^2\text{Var}(X)$, **Jensen**, y una **rifa** hipotética con esperanza de −2 000 pesos por boleta pero $\sigma \approx 94\,800$. **Continuas:** integración numérica (trapecio escrito desde cero frente a `quad`), asimetría 2 y curtosis en exceso 6 de la exponencial, y **transformada inversa**. **Conjuntas:** marginales, covarianza y correlación (verificadas con `numpy.cov`) y el contraejemplo $Y=X^2$ (correlación 0, dependencia total). **Markov y Chebyshev** (holgadas, pero una distribución de tres puntos alcanza la cota) y **esperanza y varianza totales** (con dos fincas sintéticas, el 49.9 % de la varianza es variación *entre* fincas: la idea del ANOVA). 2 prácticas (valor esperado de una decisión comercial; transformada inversa de una densidad).
3. [**02_Distribuciones_Discretas_y_Continuas.ipynb**](02_Distribuciones_Discretas_y_Continuas.ipynb): *Sección 1.3.4 (parte 3).* La **galería de familias** (Bernoulli, binomial, geométrica, Poisson, hipergeométrica, uniforme, normal, exponencial, gamma, beta, lognormal, $\chi^2$ y $t$) elegida por **mecanismo**; masas escritas desde cero (con `math.comb`, `lgamma`, `erf`) y comprobadas contra `scipy.stats`. **Aproximaciones** medidas con la distancia de variación total: Poisson a binomial (error de 0.056 a 0.001, bajo la cota $np^2$), normal con **corrección de continuidad** (y su fallo con $np=1$) e hipergeométrica a binomial. **Normal** (cuantiles por bisección, regla 68-95-99.7), **falta de memoria** de la exponencial, relación **Poisson-exponencial** y gamma, $\chi^2$ y $t$ fabricadas por sumas y razones (la $t(5)$ tiene colas más del doble de pesadas). **Ajuste y diagnóstico:** conteos de plagas **sobredispersos** ($D=2.21$: se rechaza la Poisson y gana la binomial negativa por 152 puntos de AIC), tiempos de atención (exponencial, gamma y lognormal por máxima verosimilitud, gráfico Q-Q) y por qué los valores $p$ de KS con parámetros estimados son optimistas. 3 prácticas (control de calidad con la binomial; Poisson y exponencial; cuantiles de la normal).
4. [**03_Muestreo_Ley_de_los_Grandes_Numeros_y_TLC.ipynb**](03_Muestreo_Ley_de_los_Grandes_Numeros_y_TLC.ipynb): *Sección 1.3.4 (parte 4).* **Distribución muestral de la media** (EE $=\sigma/\sqrt n$ verificado con pendiente −0.497 en escala log-log), **factor de población finita** y **corrección de Bessel** ($(n-1)/n=0.8$ medido: 0.798). **Ley de los grandes números** (Chebyshev, trayectorias, el contraejemplo de **Cauchy** y la **falacia del apostador**: la proporción converge pero $\lvert S_n-n/2\rvert$ crece como $\sqrt n$). **Teorema del límite central:** distancia KS a la normal para cuatro poblaciones (la exponencial sigue en 0.023 con $n=30$), asimetría de $\bar X$ igual a $\gamma_1/\sqrt n$ y cota de Berry-Esseen. **Aplicaciones:** **cobertura real** de $\bar x \pm 1.96\,s/\sqrt n$ en una población lognormal (74 % con $n=5$, 88 % con $n=30$, 94 % con $n=400$), **tamaño de muestra** para una proporción (385 para ±5 %) y **Monte Carlo** para $\pi$ (error $\propto 1/\sqrt n$). 3 prácticas (media frente a umbral: TLC contra simulación; factor de población finita; tamaño de muestra de una encuesta).

---

### 📝 2. Taller Práctico Evaluativo (*Hands-On*):
* [**../homeworks/02_Probabilidad_Distribuciones_Hands_On.ipynb**](../homeworks/02_Probabilidad_Distribuciones_Hands_On.ipynb): Taller evaluativo que integra probabilidad, variables aleatorias, distribuciones y muestreo en ejercicios prácticos.

---

### 🧸 3. Ruta Didáctica: Para Dummies:
Ubicada en la subcarpeta [`Para Dummies/`](Para%20Dummies/). Sin jerga ni fórmulas, con analogías cotidianas de Boyacá; solo requieren `NumPy`, `pandas` y `matplotlib`:
1. [**00_Probabilidad_Dummies.ipynb**](Para%20Dummies/00_Probabilidad_Dummies.ipynb): **Paraguas, dados y detectores:** la probabilidad como fracción (contar y luego simular), **el detector de plaga** que se equivoca casi siempre que suena (de 116 alarmas solo 18 son ciertas) y **dos buses que fallan juntos** cuando llueve.
2. [**01_Variables_Aleatorias_Dummies.ipynb**](Para%20Dummies/01_Variables_Aleatorias_Dummies.ipynb): **El promedio del tendero y la rifa de la vereda:** el promedio a la larga (cada boleta cuesta \$2 500 en promedio), **dos fincas lecheras** con el mismo promedio y distinta variación, y el número que mide cuándo **dos cosas suben juntas** (y no ve una relación curva).
3. [**02_Distribuciones_Dummies.ipynb**](Para%20Dummies/02_Distribuciones_Dummies.ipynb): **Los moldes del azar:** cuántas de 10 semillas brotan, **buses por hora** y el bus que «no tiene memoria», y **la campana** de las papas (68 %, 95 % y 99.7 %).
4. [**03_Muestreo_y_TLC_Dummies.ipynb**](Para%20Dummies/03_Muestreo_y_TLC_Dummies.ipynb): **La olla de sopa:** probar una cucharada (muestras de 5 frente a 100 bultos), **los promedios forman una campana** aunque los datos sean torcidos, y por qué **cuadruplicar** la muestra reduce el error **a la mitad**.

---

## 💾 Datos Utilizados

Todos los datos son **sintéticos o hipotéticos, con semilla fija, generados por código dentro de cada cuaderno**; **no hay descargas** y **no se necesita ninguna carpeta `data/`**, de modo que cada cuaderno es autocontenido en Google Colab y el repositorio no acumula archivos.

| Conjunto | Origen | Dónde se usa |
|---|---|---|
| **Dos dados** (36 resultados) y 20 000 lanzamientos | `itertools.product`, `default_rng(42)` | Cuaderno 00 |
| **Planta de empaque** (3 líneas, tasas de defecto **inventadas**) y **prueba de detección** (prevalencia, sensibilidad y especificidad **hipotéticas**) | Tablas escritas a mano + simulación de 1 y 2 millones de casos | Cuaderno 00 |
| **Variable «suma de dos dados»**, **rifa** de una ternera (cifras inventadas) y **quejas/devoluciones** (tabla conjunta inventada) | `VADiscreta`, `default_rng(42)` | Cuaderno 01 |
| **Rendimiento de parcelas en dos fincas** (medias 20 y 28 kg, sintético) | `rng.normal` por grupo | Cuaderno 01 |
| **Proporción de papa de primera** (Beta(2,2)), **minutos entre buses** (exponencial 0.5) | Modelos hipotéticos, integración numérica y transformada inversa | Cuaderno 01 |
| **Pesos de papas** N(180 g, 25 g), **conteos de plagas** (400 parcelas, binomial negativa) y **tiempos de atención** (500, gamma) | `default_rng(42)`, `scipy.stats.rvs` | Cuaderno 02 |
| **Población de 5 000 bultos de papa** (lognormal, asimétrica), poblaciones uniforme, exponencial, Bernoulli y bimodal, lognormal($\sigma=1$) | `default_rng(42)` | Cuaderno 03 |
| **Mini-ejemplos de juguete** (detector de plaga, rifa de la vereda, fincas lecheras, semillas, buses, papas, bodega de 5 000 bultos) | Tablas y simulaciones con semilla 42 | Los cuatro *Dummies* |

> ⚠️ **Los datos son inventados** (fincas, líneas de producción, tasas, pruebas y precios): los resultados describen el **mecanismo**, **no** el rendimiento de un caso real. Ninguna cifra del libro ni de fuentes oficiales se reproduce aquí. Los nombres de Boyacá solo ambientan los ejemplos.

## ⚙️ Requisitos

`numpy`, `pandas` (≥ 2.1, por `DataFrame.map`), `matplotlib` y `scipy` (todos preinstalados en Google Colab). `itertools`, `fractions` y `math` son de la **biblioteca estándar**. **No se necesita red.** Los cuatro **Dummies** usan solo `NumPy`, `pandas` y `matplotlib`.

Se ejecutó de verdad, de arriba abajo y sin errores, con **Python 3.12**, **NumPy 2.5**, **pandas 2.3**, **SciPy 1.18** y **Matplotlib 3.11** en Linux (de verdad: con los *starters* de las prácticas tal cual —solo comentarios— y con una copia donde cada *starter* se reemplazó por su solución). *No se probó en Google Colab ni en Windows/macOS.* Tiempos aproximados en un equipo de escritorio (varían con la carga): cuadernos 00, 01 y 02 ≈ 6-8 s y cuaderno 03 ≈ 13-15 s; los *Dummies* tardan 4-6 s.

---

<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Asignatura: Estadística, Análisis y Representación de Datos</i>
  </p>
</div>
