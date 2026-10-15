# Módulo 05: Exploración y Limpieza de Datos 🔍🧹

<p align="center">
  <img src="https://img.shields.io/badge/Discipline-Estad%C3%ADstica-ea580c?style=for-the-badge&logo=scipy&logoColor=white" alt="Estadística"/>
  <img src="https://img.shields.io/badge/Topics-EDA%20%7C%20Datos%20Faltantes%20%7C%20PCA%20%7C%20t--SNE-0ea5e9?style=for-the-badge" alt="Topics"/>
  <img src="https://img.shields.io/badge/Course-Estad%C3%ADstica%2C%20An%C3%A1lisis%20y%20Representaci%C3%B3n%20de%20Datos-6366f1?style=for-the-badge" alt="Course"/>
  <img src="https://img.shields.io/badge/Institution-USTA%20Tunja-1e3a8a?style=for-the-badge" alt="USTA"/>
</p>

Bienvenido al **Módulo 05** de la asignatura **Estadística, Análisis y Representación de Datos** de la *Especialización en Ciencia de Datos* de la **Universidad Santo Tomás — Seccional Tunja**.

---

## 🧭 ¿De qué trata este módulo?

Este módulo abre el **Capítulo 2** del libro de la asignatura y desarrolla las secciones **2.1 (*Introducción*)**, **2.2 (*Resumen*)** y **2.3 (*Exploración y limpieza de datos*)**: **2.3.1** resumen estadístico, visualizaciones e ingeniería de características; **2.3.2** datos faltantes, imputación, interpolación y limpieza; y **2.3.3** selección y reducción de dimensionalidad (PCA y t-SNE). El Capítulo 1 dio el lenguaje (variables, probabilidad, inferencia); este módulo lo aplica a datos que **nunca llegan limpios ni listos**. La pregunta que responde es **¿cómo exploro, limpio y reduzco los datos sin engañarme?**, antes de modelar (Módulo 06).

El módulo **no** repite lo que ya existe en el repositorio: el uso de `pandas` para el EDA está en [Data Science programming, Módulo 04](../../Data%20Science%20programming/04%20-%20EDA/README.md); la preparación y la ingeniería de características operativas, en los [módulos 05](../../Data%20Science%20programming/05%20-%20Data%20Preparation/README.md) y [06](../../Data%20Science%20programming/06%20-%20Feature%20Engineering/README.md) de ese curso; la imputación, los atípicos y el PCA dentro de un flujo de minería de datos, en [Data Mining, Módulo 01](../../Data%20Mining/01%20-%20Preprocesamiento%20de%20los%20Datos/README.md); y PCA, t-SNE e Isomap con `scikit-learn`, en [Machine Learning, Módulo 05](../../Machine%20Learning/05%20-%20Reduccion%20de%20Dimensionalidad/README.md). Aquí el enfoque es el del libro: **rigor estadístico** (supuestos, intervalos, honestidad sobre lo que cada resumen puede decir) con **implementaciones desde cero** (resumen estadístico, Box-Cox, KNN y imputación encadenada, imputación múltiple con las reglas de Rubin, PCA con la SVD y t-SNE exacto) **contrastadas con `assert` contra SciPy y scikit-learn**, simulaciones con semilla fija y **resultados reportados con honestidad**: el EDA que «encuentra» ≈ 9.5 correlaciones en puro ruido, el «IC95» que cubre solo el 15 % bajo datos faltantes MAR, el KNN sin escalar que es **peor** que la media, la selección de variables que da 0.91 de exactitud sobre ruido, el PCA que **no** mejora la predicción y el t-SNE que fabrica grupos en el ruido.

> 🗺️ **Mapa del curso:** **00** Fundamentos → **01** Estadística Descriptiva y Visualización → **02** Probabilidad y Distribuciones → **03** Inferencia Estadística → **04** No Paramétrica, Regresión y Ética → **05** Exploración y Limpieza de Datos *(este módulo)* → **06** Modelamiento Estadístico → **07** Temas Avanzados. El [README del curso](../README.md) contiene el índice completo.

> 🛠️ **Ponlo en práctica:** todos los cuadernos (estándar y *Para Dummies*) incluyen secciones **«🛠️ Práctica»**: una celda de código para que escribas tu solución y, justo debajo, la **solución guiada desplegable** (`💡 Haz clic aquí para ver la solución guiada...`). Inténtalo primero y abre la solución solo para comparar.

---

## 📚 Estructura Curricular del Módulo

### 🎓 1. Cuadernos Académicos Estándar:
1. [**00_Introduccion_Cap2_Resumen_y_EDA.ipynb**](00_Introduccion_Cap2_Resumen_y_EDA.ipynb): *Secciones 2.1, 2.2 y 2.3.1.* El **mapa del Capítulo 2** y dos principios (la exploración genera hipótesis; toda transformación se ajusta con el entrenamiento). **Perfil de datos** y **resumen estadístico desde cero** (posición, escala, forma e IC *t* de la media; coincide con `pandas`/`SciPy`) sobre 600 fincas **sintéticas**: el área tiene asimetría 3.38 y curtosis 18.1. **EDA visual** (histograma + densidad, cajas, dispersión con tendencia por deciles, correlaciones de Pearson y Spearman desde cero): la **U invertida** de la altitud tiene $r=-0.10$ pero un ajuste cuadrático explica el 35 % de la variación. **Comparaciones múltiples:** en 190 parejas de ruido salen ≈ 9.6 «hallazgos» a $\alpha=0.05$ (Bonferroni: 0.04). **Ingeniería de características:** **Box-Cox** con $\lambda$ por máxima verosimilitud (coincide con `scipy.stats.boxcox`; IC95 por razón de verosimilitud $[-0.07, 0.09]$ contiene al logaritmo), escaladores desde cero (un solo valor absurdo reduce el ancho P5–P95 del min-max de 0.52 a 0.02; el robusto no cambia), mes **cíclico** y discretización por cuantiles. **Validación cruzada 5×3 sin fugas:** transformar subió el $R^2$ de 0.36 a 0.67 (0.70 con el objetivo en log), el mes cíclico sin señal **no aportó** y el bosque sobre datos crudos llegó a 0.62. 2 prácticas (resumen por variedad con IC; escalado sin fuga de datos).
2. [**01_Datos_Faltantes_e_Inconsistentes.ipynb**](01_Datos_Faltantes_e_Inconsistentes.ipynb): *Sección 2.3.2.* **Mecanismos MCAR, MAR y MNAR** (Rubin, 1976), simulados con la misma proporción de faltantes (30 %) y **diagnosticados** (AUC de predecir la falta, prueba de Welch): un MNAR **se ve como MAR** con lo observado. **Evaluación honesta en 200 réplicas:** borrar filas sesga la media en −0.40 t/ha bajo MAR (−0.75 bajo MNAR); la media encoge la desviación a 0.84 de la real y debilita las correlaciones; la regresión corrige el MAR pero **nada** corrige el MNAR; el **menor RMSE** (regresión determinista, 1.26) **no** es el mejor para inferir (la estocástica conserva sd y correlación con RMSE 1.78). **KNN** e **imputación encadenada** desde cero (coinciden con `KNNImputer` e `IterativeImputer`): la encadenada gana (0.80), **KNN sin escalar (1.02) es peor que la media (0.99)**. **Imputación múltiple con las reglas de Rubin** y **cobertura real** del IC95 (400 réplicas): bajo MAR, casos completos **15 %**, regresión única 87 %, imputación múltiple **94.5 %**; bajo MNAR todo falla. **Interpolación** de series (ffill, lineal, spline, modelo estacional): la lineal gana en huecos cortos, el modelo estacional en largos (cruce entre 7 y 15 días) y el **spline se desboca**. **Inconsistencias:** texto con `difflib`, centinelas, libras y kilos, fechas con formatos explícitos (la lectura `mixed` de pandas equivocó 42 fechas en silencio), duplicados, **cuarentena** y **conservación de filas**. 2 prácticas (diagnosticar un MAR y medir cuánto corrige la regresión; un hueco no basta para elegir un método de interpolación).
3. [**02_Seleccion_y_Reduccion_de_Dimensionalidad_PCA_tSNE.ipynb**](02_Seleccion_y_Reduccion_de_Dimensionalidad_PCA_tSNE.ipynb): *Sección 2.3.3.* **Maldición de la dimensionalidad** (contraste de distancias 66 → 0.11; con $n=60$ el $R^2$ de validación cae a −0.87 al pasar de 3 a 53 variables). **Filtro, envoltura e incrustada** con verdad conocida (lineales, una **cuadrática**, redundantes y ruido): el filtro $F$ repite información y no ve la cuadrática, la información mutua sí la ve pero es ruidosa, la envoltura lineal es limpia pero ciega a lo no lineal, el Lasso deja ruido y el bosque recupera 5 de 6; $F$ y la selección hacia adelante **verificados** contra `f_regression` y `SequentialFeatureSelector`. **Fuga de selección:** 0.91 de exactitud sobre puro ruido frente a 0.46 dentro del *pipeline*. **PCA con la SVD** desde cero (coincide con `PCA`; el error de reconstrucción es $(n-1)\sum_{j>k}\lambda_j$) en los vinos de `load_wine`: **sin estandarizar PC1 explica 99.8 %** (solo `proline`) frente a 36.2 %; $k$ por varianza acumulada (8), Kaiser (3) y **análisis paralelo** (3). **Límites:** PCR no superó a la regresión completa en `load_diabetes` y la señal puede vivir en un componente de baja varianza (PC1 0.52, PC2 0.99). **t-SNE** (confiabilidad 0.98 frente a 0.83 de PCA en `load_digits`) con **tres advertencias medidas** (la razón de dispersión 5.0 pasa a 1.0; el ruido gaussiano produce «grupos» con silueta 0.35 frente a 0.04; ocho grupos equidistantes quedan a distancias con CV 0.35) y **t-SNE exacto desde cero** (perplejidad verificada, KL decreciente, confiabilidad 0.977 frente a 0.982 de `scikit-learn`). 2 prácticas (información mutua y relación no lineal; elegir $k$ y verificar la identidad de la reconstrucción).

---

### 📝 2. Taller Práctico Evaluativo (*Hands-On*):
* [**../homeworks/05_Exploracion_Limpieza_Hands_On.ipynb**](../homeworks/05_Exploracion_Limpieza_Hands_On.ipynb): Taller evaluativo que integra el EDA, la imputación y la reducción de dimensionalidad en ejercicios prácticos.

---

### 🧸 3. Ruta Didáctica: Para Dummies:
Ubicada en la subcarpeta [`Para Dummies/`](Para%20Dummies/). Sin jerga ni fórmulas, con analogías cotidianas de Boyacá; solo requieren `NumPy`, `pandas` y `matplotlib`:
1. [**00_EDA_Dummies.ipynb**](Para%20Dummies/00_EDA_Dummies.ipynb): **Conociendo la finca antes de sembrar:** el vistazo (un solo 21.0 sube el promedio a 7.93 con la mediana en 6.8), el logaritmo para cuando una finca es 120 veces otra y **las monedas** (de 200 personas, varias sacan 5 caras por pura suerte).
2. [**01_Faltantes_Dummies.ipynb**](Para%20Dummies/01_Faltantes_Dummies.ipynb): **El cuaderno con páginas rotas:** tres razones de falta (la lluvia, los domingos, las ventas malas), cómo cambia el promedio en cada una y por qué **rellenar con el promedio no cambia el promedio**.
3. [**02_Reduccion_Dummies.ipynb**](Para%20Dummies/02_Reduccion_Dummies.ipynb): **La sombra de la papa:** una sola «sombra» conserva el 96.8 % de la información de altura y peso, el vendedor que «adivina» entre 200 columnas de ruido (0.85 que se esfuma a 0.14) y el mapa del metro como imagen de t-SNE.

---

## 💾 Datos Utilizados

Todos los datos son **sintéticos con semilla fija, generados por código dentro de cada cuaderno**, salvo tres conjuntos **reales de juguete incluidos en `scikit-learn`** (sin descargas): `load_wine` (178 vinos), `load_diabetes` (442 pacientes) y `load_digits` (1 797 dígitos 8×8). **No hay descargas** y **no se necesita ninguna carpeta `data/`**, de modo que cada cuaderno es autocontenido en Google Colab y el repositorio no acumula archivos.

| Conjunto | Origen | Dónde se usa |
|---|---|---|
| **600 fincas paperas** (zona, altitud, precipitación, área, fertilizante, variedad, fecha, rendimiento; 12 faltantes) | `generar_fincas(semilla=42)`, rendimiento multiplicativo con parábola en la altitud | Cuaderno 00 |
| **Ruido puro** (100 × 20) y **ventanas de CV 5×3** | `default_rng(7)`, `RepeatedKFold` | Cuaderno 00 |
| **Fincas completas** (5 variables correlacionadas) con faltantes MCAR/MAR/MNAR | `generar_completos`, `mascara` | Cuaderno 01 |
| **Temperatura diaria** (730 días: tendencia, estacionalidad y AR(1)) | `serie_sintetica` | Cuaderno 01 |
| **Encuesta sucia** (315 filas, 6 municipios de Boyacá como etiquetas) con centinelas, unidades, fechas y duplicados | `generar_encuesta_sucia` | Cuaderno 01 |
| **Problema de selección** ($n=300$, $p=30$: lineales, cuadrática, redundantes, ruido) y **ruido de 2 000 variables** | `default_rng(3)` y `default_rng(1)` | Cuaderno 02 |
| **Vinos, diabetes y dígitos** (reales, de juguete) | `load_wine`, `load_diabetes`, `load_digits` | Cuaderno 02 |
| **Nubes y simplex sintéticos** para las advertencias de t-SNE | `default_rng(2)`, `default_rng(6)` | Cuaderno 02 |
| **Mini-ejemplos de juguete** (12 fincas, áreas, monedas, ventas de 28 días, plantas, hojas de café) | Tablas y simulaciones con semilla fija | Los tres *Dummies* |

> ⚠️ **Los datos sintéticos son inventados** (fincas, zonas, encuestas, ventas): los resultados describen el **mecanismo**, **no** el rendimiento de un caso real. Los nombres de los municipios de Boyacá solo ambientan los ejemplos de limpieza de texto. Ninguna cifra del libro ni de fuentes oficiales se reproduce aquí.

## ⚙️ Requisitos

`numpy`, `pandas`, `matplotlib`, `scipy` y `scikit-learn` (todos preinstalados en Google Colab). `difflib`, `unicodedata` y `re` son de la **biblioteca estándar**. **No se necesita red.** `IterativeImputer` requiere importar `sklearn.experimental.enable_iterative_imputer` (el cuaderno 01 lo hace); el parámetro `max_iter` de `TSNE` requiere una versión reciente de scikit-learn (≥ 1.5). Los tres **Dummies** usan solo `NumPy`, `pandas` y `matplotlib`.

Se ejecutó de verdad, de arriba abajo y sin errores, con **Python 3.12**, **NumPy 2.5**, **pandas 2.3**, **SciPy 1.18**, **scikit-learn 1.9** y **Matplotlib 3.11** en Linux (de verdad: con los *starters* de las prácticas tal cual —solo comentarios— y con una copia donde cada *starter* se reemplazó por su solución). *No se probó en Google Colab ni en Windows/macOS.* Tiempos aproximados en un equipo de escritorio (varían con la carga): cuaderno 00 ≈ 12–18 s, 01 ≈ 18–30 s y 02 ≈ 35–65 s (el t-SNE y la selección de variables son lo más lento; con la máquina muy cargada llegó a duplicarse); los *Dummies* tardan 4–7 s.

---

<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Asignatura: Estadística, Análisis y Representación de Datos</i>
  </p>
</div>
