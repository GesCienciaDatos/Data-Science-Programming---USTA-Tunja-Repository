# Módulo 01: Estadística Descriptiva y Visualización 📊📈

<p align="center">
  <img src="https://img.shields.io/badge/Discipline-Estad%C3%ADstica-0ea5e9?style=for-the-badge&logo=scipy&logoColor=white" alt="Estadística"/>
  <img src="https://img.shields.io/badge/Topics-Descriptiva%20y%20Visualizaci%C3%B3n-16a34a?style=for-the-badge" alt="Topics"/>
  <img src="https://img.shields.io/badge/Course-Estad%C3%ADstica%2C%20An%C3%A1lisis%20y%20Representaci%C3%B3n%20de%20Datos-6366f1?style=for-the-badge" alt="Course"/>
  <img src="https://img.shields.io/badge/Institution-USTA%20Tunja-1e3a8a?style=for-the-badge" alt="USTA"/>
</p>

Bienvenido al **Módulo 01** de la asignatura **Estadística, Análisis y Representación de Datos** de la *Especialización en Ciencia de Datos* de la **Universidad Santo Tomás — Seccional Tunja**.

---

## 🧭 ¿De qué trata este módulo?

Este módulo corresponde a las secciones **1.3.2 (*Estadística descriptiva*)** y **1.3.3 (*Visualización de datos*)** del **Capítulo 1** del libro de la asignatura. La pregunta que responde es **¿cómo resumo y muestro un conjunto de datos sin perder lo importante ni engañar?** Un resumen siempre **descarta información**; el rigor consiste en saber **qué se descarta**, **qué supuestos** hay detrás de cada medida y **cuánto cambia** el resultado si los datos traen errores o una cola larga.

El módulo **no** repite lo que ya existe en el repositorio (el manejo de `describe()`, `groupby` y el flujo de EDA con *pandas* y *seaborn*, los principios de diseño visual y la detección de atípicos en datos reales): lo **enlaza**. Aquí el enfoque es el del libro: **rigor estadístico** (supuestos, interpretación, robustez, definiciones) con **implementaciones desde cero en NumPy contrastadas con `assert` contra NumPy, pandas, SciPy, scikit-learn y Matplotlib**. Como en el resto del repositorio, se usan **semillas fijas** y **resultados reportados con honestidad**, incluidos los casos en que lo «más sofisticado» **no** gana (la mediana frente a la media con datos normales, una V de Cramér que no baja de 0 por azar, una paleta apta para daltonismo con colores ilegibles).

> 🗺️ **Mapa del curso (ocho módulos):** 00 Fundamentos de Estadística y Análisis de Datos → **01 Estadística Descriptiva y Visualización** *(este módulo)* → 02 Probabilidad y Distribuciones → 03 Inferencia Estadística → 04 No Paramétrica, Regresión y Ética → 05 Exploración y Limpieza de Datos → 06 Modelamiento Estadístico → 07 Temas Avanzados en Data Analysis. El [README del curso](../README.md) recoge el índice completo.

> 🔗 **Conexión con otros cursos:** el flujo de EDA con *pandas* y *seaborn* está en [Data Science Programming, Módulo 04 (EDA)](../../Data%20Science%20programming/04%20-%20EDA/README.md); los principios de diseño, los tipos de gráficos y el pensamiento crítico sobre gráficos engañosos, en [Visual Analytics, Módulo 02 (Fundamentos de visualización)](../../Visual%20Analytics%20and%20Critical%20Thinking/02%20-%20Fundamentos%20de%20Visualizacion/README.md), [Módulo 03 (Pensamiento crítico en datos)](../../Visual%20Analytics%20and%20Critical%20Thinking/03%20-%20Pensamiento%20Critico%20en%20Datos/README.md) y [Módulo 05 (Datos numéricos)](../../Visual%20Analytics%20and%20Critical%20Thinking/05%20-%20Visualizacion%20de%20Datos%20Numericos/README.md); el tratamiento de valores atípicos antes de modelar, en [Data Mining, Módulo 01 (Preprocesamiento)](../../Data%20Mining/01%20-%20Preprocesamiento%20de%20los%20Datos/README.md).

> 🛠️ **Ponlo en práctica:** todos los cuadernos (estándar y *Para Dummies*) incluyen secciones **«🛠️ Práctica»**: una celda de código para que escribas tu solución y, justo debajo, la **solución guiada desplegable** (`💡 Haz clic aquí para ver la solución guiada...`). Inténtalo primero y abre la solución solo para comparar.

---

## 🎯 Objetivos del Módulo

Al terminar el módulo podrás:

1. **Elegir** la medida de tendencia central adecuada a la **escala de medición** y a la **forma** de los datos; calcular media (aritmética, ponderada, recortada, winsorizada, geométrica, armónica), mediana y moda, y explicar **qué minimiza** cada una y **cuánto aguanta** frente a datos contaminados (punto de ruptura, eficiencia).
2. **Calcular cuantiles** con las definiciones de Hyndman y Fan, usar la **ECDF**, el rango percentil y el puntaje $z$ (y saber cuándo el $z$ engaña), y resumir datos **agrupados**.
3. **Medir la dispersión** (rango, RIC, varianza con $n-1$, MAD, CV) y la **forma** (asimetría, curtosis, transformaciones de Box-Cox), con cálculo **numéricamente estable** (Welford).
4. **Detectar atípicos** (Tukey, $z$ clásico, $z$ robusto), entender el **enmascaramiento** y distinguir **atípico** de **error**.
5. **Cuantificar la asociación**: covarianza, correlación de Pearson, Spearman y Kendall, V de Cramér, matriz de correlación; saber qué capta cada una y cuándo **un solo punto** la fabrica.
6. **Construir y leer** histogramas (reglas de ancho de clase), KDE, ECDF, diagramas de caja, violines y Q-Q plots; **visualizar** relaciones con muchos puntos y series de tiempo; y **medir el engaño gráfico** (factor de mentira, contraste de colores, luminancia de los mapas de color).

---

## 📚 Estructura Curricular del Módulo

### 🎓 1. Cuadernos Académicos Estándar:
1. [**00_Medidas_de_Tendencia_Central_y_Posicion.ipynb**](00_Medidas_de_Tendencia_Central_y_Posicion.ipynb): *Sección 1.3.2 (primera parte).* **Escalas de medición y medida adecuada** (moda para nominal, mediana para ordinal). **La media y sus variantes desde cero** (ponderada, recortada, winsorizada, geométrica, armónica) contrastadas con NumPy y SciPy, con sus propiedades verificadas (las desviaciones suman cero, linealidad, mínimo de cuadrados, HM ≤ GM ≤ AM) y tres aplicaciones: el **promedio de promedios**, la **tasa media de variación de un precio** (6.92 % la aritmética frente a 4.35 % la que reproduce el precio final) y la **velocidad media** de ida y vuelta (48 km/h, no 50). **Mediana y moda** (qué minimiza cada una: cuadrados frente a valores absolutos; moda continua con KDE). **Robustez y eficiencia:** experimento de contaminación con **punto de ruptura** (con 10 % de errores la media se desplaza +45.0 y la mediana +0.9; la recortada al 10 % se rompe al 12 %; la mediana colapsa recién al 55 %) y razón de errores estándar mediana/media (**1.23** con datos normales, teoría √(π/2) ≈ 1.253; **≈ 0.8** con colas pesadas). **Cuantiles:** los seis tipos de Hyndman y Fan (4 a 9) desde cero en un solo código, verificados contra `np.quantile` (con n = 11 el primer cuartil va de 17.32 a 19.05 según el tipo; con n = 400 casi coinciden), ECDF, rango percentil, resumen de cinco números y **puntaje z frente a percentil** (94.7 si fuera normal frente a 92.0 empírico en datos asimétricos). **Datos agrupados** (media, mediana y moda desde una tabla de frecuencias y error según el ancho de clase). 2 prácticas (recortar o winsorizar; cuantiles con dos definiciones).
2. [**01_Medidas_de_Dispersion_Forma_y_Asociacion.ipynb**](01_Medidas_de_Dispersion_Forma_y_Asociacion.ipynb): *Sección 1.3.2 (segunda parte).* **Dispersión** (rango, RIC, varianza, desviación estándar, MAD escalada, CV con la comprobación de que **exige escala de razón**: °C→K lo cambia de 0.264 a 0.011), **por qué $n-1$** (simulación: 3.19 con $n$ frente a 3.99 con $n-1$ sobre 4; $s$ sigue sesgada), **error numérico de la fórmula ingenua de la varianza** (512.0 frente a 1.005 con un desplazamiento de $10^9$) con el **algoritmo de Welford**, y **Chebyshev frente a la regla empírica**. **Forma:** momentos, asimetría y curtosis (con y sin corrección, contrastadas con SciPy), cinco distribuciones frente a su valor teórico, la **inestabilidad de la curtosis** con colas pesadas (lognormal, n = 1000: rango de 2.0 a 34.0 frente a 7.80 teórico) y transformaciones (**log** y **Box-Cox**, λ̂ ≈ 0.06). **Atípicos:** Tukey, z clásico y z robusto con verdad conocida (el z clásico detecta 4 de 20 por **enmascaramiento**; Tukey y z robusto, 20 de 20) y la advertencia de que **atípico no es error** (Tukey marca 4.17 % de una lognormal sin errores). **Asociación:** covarianza, Pearson, rangos con empates, Spearman y Kendall desde cero (verificadas con SciPy), **cuarteto de Anscombe**, qué capta cada coeficiente (monótona, parábola con **información mutua**, un solo atípico que lleva Pearson de 0.08 a 0.80), invariancias, **matriz de covarianza y de correlación** con los 178 vinos de scikit-learn y **V de Cramér** (con el aviso de su sesgo positivo en tablas pequeñas). 2 prácticas (Box-Cox desde cero; V de Cramér).
3. [**02_Visualizacion_de_Datos_Estadisticos.ipynb**](02_Visualizacion_de_Datos_Estadisticos.ipynb): *Sección 1.3.3.* **Principios** (jerarquía perceptual de Cleveland y McGill, tinta de datos y factor de mentira de Tufte) y una **guía de qué gráfico para qué pregunta**. **Histograma:** reglas de **Sturges, Scott y Freedman-Diaconis** desde cero verificadas contra `np.histogram_bin_edges` (600 ingresos: 11, 20 y 30 clases; 5 000 parcelas: 14, 37 y 49), efecto de pocas o demasiadas clases, **KDE** desde cero verificado contra `gaussian_kde` (ancho de banda) y **ECDF**. **Comparar grupos:** **anatomía del diagrama de caja** calculada a mano y verificada contra `matplotlib.cbook.boxplot_stats`, violín, tira de puntos y **Q-Q plot** con las posiciones de Filliben verificadas contra `scipy.stats.probplot` (correlación 0.9350 para el ingreso, 0.9990 para su logaritmo). **Relaciones:** 5 000 puntos con transparencia, ***hexbin*** (los conteos suman $n$) y **LOWESS**, y **media móvil** con sumas acumuladas verificada contra pandas. **Gráficos honestos:** **factor de mentira** (26 con un eje truncado frente a 1 desde cero), **contraste WCAG** de la paleta de Okabe-Ito (el amarillo solo llega a 1.32) y **luminancia monótona** de *viridis* frente a *jet*. 3 prácticas (número de clases según la regla; Q-Q de tres variables; factor de mentira de una serie de ventas).

---

### 📝 2. Taller Práctico Evaluativo (*Hands-On*):
* [**../homeworks/01_Descriptiva_Visualizacion_Hands_On.ipynb**](../homeworks/01_Descriptiva_Visualizacion_Hands_On.ipynb): Taller evaluativo que integra estadística descriptiva y visualización en ejercicios prácticos.

---

### 🧸 3. Ruta Didáctica: Para Dummies:
Ubicada en la subcarpeta [`Para Dummies/`](Para%20Dummies/). Sin jerga ni fórmulas, con analogías cotidianas; usan solo `NumPy`, `pandas` y `matplotlib`:
1. [**00_Tendencia_Central_Dummies.ipynb**](Para%20Dummies/00_Tendencia_Central_Dummies.ipynb): **El precio justo de la papa**: nueve puestos de la plaza y un puesto turístico con un precio absurdo (el promedio salta de 2 022 a 2 720; la mediana sigue en 2 000), y **la fila de los buses** para entender el percentil 90 (mediana 9 min, promedio 11.4, percentil 90 de 18.7 min).
2. [**01_Dispersion_y_Asociacion_Dummies.ipynb**](Para%20Dummies/01_Dispersion_y_Asociacion_Dummies.ipynb): **Dos fincas, el mismo promedio**: ambas dan 20 litros pero la B varía 12 veces más; **el dato mal digitado** (90 en vez de 19) que dispara unas medidas y no otras; y **la correlación** (lluvia y cosecha 0.97; paraguas y chocolate caliente suben juntos sin causarse; una sola parcela inundada la baja a 0.14).
3. [**02_Graficos_Dummies.ipynb**](Para%20Dummies/02_Graficos_Dummies.ipynb): **Elegir el gráfico correcto**: cuatro preguntas, cuatro gráficos (histograma, cajas, dispersión y línea), **las cajitas del histograma** (3, 8 y 30 sobre los mismos datos) y **la trampa del eje** (520 frente a 550 toneladas parece 2.5 veces con el eje desde 500).

---

## 💾 Datos Utilizados

Todos los datos son **sintéticos con semilla fija, generados por código dentro de cada cuaderno**, salvo dos excepciones **públicas, sin red y de uso didáctico**: el **cuarteto de Anscombe** (Anscombe, 1973; 11 pares × 4 conjuntos, escritos a mano) y el conjunto **`wine`** incluido en scikit-learn (178 vinos, 13 variables químicas, 3 cultivares). **No hay descargas** y **no se necesita ninguna carpeta `data/`**: cada cuaderno es autocontenido en Google Colab y el repositorio no acumula archivos.

| Conjunto | Origen | Dónde se usa |
|---|---|---|
| **400 hogares agrícolas** (`ingreso` lognormal, `rendimiento` normal, `variedad` nominal, `talla` ordinal) | `default_rng(42)`, FICTICIOS | Cuaderno 00 |
| **Pequeños ejemplos de juguete** (veredas, precios de una serie, velocidades) | Listas escritas a mano, FICTICIAS | Cuaderno 00 |
| **Zonas A y B** (misma media, distinta variabilidad), **ingresos** (400), **lecturas de un sensor** (200, 10 % defectuosas, verdad conocida) y **pares de prueba** (lineal, exponencial, parábola, atípico) | `default_rng(42 + k)`, FICTICIOS | Cuaderno 01 |
| **Cuarteto de Anscombe** y **vinos de scikit-learn** | Clásico (1973) y `sklearn.datasets.load_wine` | Cuaderno 01 |
| **600 hogares en tres zonas**, **5 000 parcelas** (lluvia y rendimiento) y **precio semanal** (3 años) | `default_rng(42)`, FICTICIOS | Cuaderno 02 |
| **Mini-ejemplos de juguete** (puestos de la plaza, buses, fincas lecheras, parcelas, cooperativas) | Listas escritas a mano o `default_rng(7)`, FICTICIAS | Los tres *Dummies* |

> ⚠️ **Los datos son inventados** (hogares, ingresos, rendimientos, precios, cooperativas): los resultados describen el **mecanismo**, **no** cifras reales del campo colombiano. Los nombres de variedades de papa y de regiones solo ambientan los ejemplos.

## ⚙️ Requisitos

`numpy`, `pandas`, `scipy`, `matplotlib`, `scikit-learn` y `statsmodels` (este último solo para el suavizado LOWESS del cuaderno 02); todos están preinstalados en Google Colab. **No se necesita red ni GPU.** Los tres **Dummies** usan solo `NumPy`, `pandas` y `matplotlib`.

Se ejecutó de verdad, de arriba abajo y sin errores, con **Python 3.12**, **NumPy 2.5**, **pandas 2.3**, **SciPy 1.18**, **scikit-learn 1.9**, **statsmodels 0.15** y **Matplotlib 3.11** en Linux (de verdad: con los *starters* de las prácticas tal cual —solo comentarios— y con una copia donde cada *starter* se reemplazó por su solución). *No se probó en Google Colab ni en Windows/macOS.* Tiempos aproximados en un equipo de escritorio (varían con la carga): cuadernos estándar de **7 a 19 s** y *Dummies* de **3 a 5 s**. Notas de portabilidad: `np.quantile(..., method=...)` requiere NumPy ≥ 1.22; `stats.median_abs_deviation` y `stats.contingency.association` requieren SciPy ≥ 1.5 y ≥ 1.7; en los diagramas de caja se evitó el argumento `labels`/`tick_labels` (cambió de nombre entre versiones de Matplotlib).

---

<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Asignatura: Estadística, Análisis y Representación de Datos</i>
  </p>
</div>
