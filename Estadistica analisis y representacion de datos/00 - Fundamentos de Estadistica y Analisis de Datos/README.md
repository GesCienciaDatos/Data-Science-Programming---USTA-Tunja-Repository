# Módulo 00: Fundamentos de Estadística y Análisis de Datos 📊🧭

<p align="center">
  <img src="https://img.shields.io/badge/Discipline-Estad%C3%ADstica-1e3a8a?style=for-the-badge&logo=scipy&logoColor=white" alt="Estadística"/>
  <img src="https://img.shields.io/badge/Topics-Fundamentos%20de%20Estad%C3%ADstica-0ea5e9?style=for-the-badge" alt="Topics"/>
  <img src="https://img.shields.io/badge/Course-Estad%C3%ADstica%2C%20An%C3%A1lisis%20y%20Representaci%C3%B3n%20de%20Datos-6366f1?style=for-the-badge" alt="Course"/>
  <img src="https://img.shields.io/badge/Institution-USTA%20Tunja-1e3a8a?style=for-the-badge" alt="USTA"/>
</p>

Bienvenido al **Módulo 00**, el **primero** de la asignatura **Estadística, Análisis y Representación de Datos** de la *Especialización en Ciencia de Datos* de la **Universidad Santo Tomás — Seccional Tunja**.

---

## 🧭 ¿De qué trata este módulo?

Este módulo abre el **Capítulo 1** del libro de la asignatura y corresponde a las secciones **1.1 (*Introducción*)**, **1.2 (*Resumen*)**, **1.3 (*Conceptos fundamentales*)** y **1.3.1 (*Generalidades de los conceptos estadísticos y sus aplicaciones en ciencia de datos*)**. La pregunta que responde es **¿qué se mide, cómo se obtuvieron los datos y qué trampas conceptuales hay que evitar antes de calcular nada?** Los errores más graves en ciencia de datos casi nunca están en la fórmula final: están en la **muestra**, en la **escala de la variable** o en la **interpretación**.

El módulo **no** repite lo que ya existe en el repositorio: el cálculo de estadísticos descriptivos con *pandas* y el análisis exploratorio están en [Programación para Ciencia de Datos, Módulo 04 (EDA)](../../Data%20Science%20programming/04%20-%20EDA/README.md); aquí el enfoque es el del libro: **rigor estadístico** (supuestos, interpretación, intervalos, tamaños del efecto), con **implementaciones desde cero en NumPy contrastadas por `assert`** contra SciPy, *statsmodels* y *scikit-learn*, con **semillas fijas** y **resultados reportados con honestidad** (por ejemplo, un intervalo «del 95 %» que en la práctica cubre el 89 %, o un bosque aleatorio que **no** supera al modelo lineal cuando la verdad es lineal).

> 🗺️ **Mapa del curso (ocho módulos):** **00** Fundamentos *(este módulo)* → **01** Estadística Descriptiva y Visualización → **02** Probabilidad y Distribuciones → **03** Inferencia Estadística → **04** No Paramétrica, Regresión y Ética → **05** Exploración y Limpieza de Datos → **06** Modelamiento Estadístico → **07** Temas Avanzados en *Data Analysis*. El [README del curso](../README.md) se actualizará con el índice completo.

> 🔗 **Conexión con otros cursos:** la regresión y los bosques aleatorios que aparecen en el cuaderno 01 como vehículo para contrastar *inferencia frente a predicción* se desarrollan en [Machine Learning, Módulo 01 (modelos lineales)](../../Machine%20Learning/01%20-%20Modelos%20Lineales%20Supervisados/README.md), [Machine Learning, Módulo 02 (árboles y bosques)](../../Machine%20Learning/02%20-%20Arboles%20Bosques%20y%20Redes%20Neuronales/README.md) y [Programación para Ciencia de Datos, Módulo 07 (regresión)](../../Data%20Science%20programming/07%20-%20Regression/README.md); la ética de datos se profundiza en [Introducción a la IA, Módulo 03 (ética)](../../Introduccion%20a%20la%20Inteligencia%20Artificial/03%20-%20Etica%20y%20el%20Nuevo%20Paradigma%20de%20la%20IA/README.md).

> 🛠️ **Ponlo en práctica:** todos los cuadernos (estándar y *Para Dummies*) incluyen secciones **«🛠️ Práctica»**: una celda de código para que escribas tu solución y, justo debajo, la **solución guiada desplegable** (`💡 Haz clic aquí para ver la solución guiada...`). Inténtalo primero y abre la solución solo para comparar.

---

## 📚 Estructura Curricular del Módulo

### 🎓 1. Cuadernos Académicos Estándar:
1. [**00_Introduccion_y_Resumen_del_Curso.ipynb**](00_Introduccion_y_Resumen_del_Curso.ipynb): *Secciones 1.1, 1.2 y 1.3.* **Qué es la estadística** (descriptiva, probabilidad e inferencial) y el **resumen del Capítulo 1 con el mapa de los ocho módulos**. **Población, muestra, parámetro y estadístico:** una población **sintética** de 20 000 parcelas, media y varianza **desde cero** (contrastadas con NumPy), la **distribución de muestreo** de $\bar{x}$ con 5 000 muestras (el error estándar observado coincide con $\sigma/\sqrt{n}$ y la corrección de Bessel se **demuestra**: dividir entre $n$ da un factor ≈ 0.963 frente al 0.967 teórico). **Tipos de variables y escalas de Stevens** (nominal, ordinal, de intervalo y de razón): la media de códigos nominales **depende de la codificación**, la mediana ordinal **sobrevive a transformaciones crecientes** y 20 °C no es «el doble» de 10 °C (en kelvin la razón es 1.035). **Cinco métodos de muestreo** implementados desde cero y comparados por simulación con $n=200$ (aleatorio simple, sistemático, estratificado, por conglomerados y por conveniencia): estratificar baja la desviación estándar de 0.59 a 0.43 t/ha, conglomerar la **multiplica por ≈ 5** (efecto de diseño ≈ 28), el sistemático **hereda** la estratificación del orden de la lista (y falla con una lista periódica) y la conveniencia **sesga** ≈ 2.9 t/ha; las varianzas teóricas coinciden con las simuladas y se compara la **asignación de Neyman** con la proporcional. **Un primer intervalo de confianza** y su **cobertura real** (≈ 95 % con la población gamma; **82–92 %** con una lognormal muy asimétrica) y el **ciclo de vida de un proyecto de datos** dibujado con `matplotlib`. 2 prácticas (Bessel con $n=5$; Neyman frente a proporcional).
2. [**01_Conceptos_Estadisticos_en_Ciencia_de_Datos.ipynb**](01_Conceptos_Estadisticos_en_Ciencia_de_Datos.ipynb): *Sección 1.3.1.* **Sesgo de muestreo:** $\text{ECM}=\text{varianza}+\text{sesgo}^2$ verificado; en una encuesta en línea **ficticia** el sesgo del estimador ingenuo (≈ −0.49 puntos) **no se mueve** al pasar de 200 a 20 000 invitados, la **ponderación por el inverso de la probabilidad de respuesta** lo elimina cuando la respuesta depende solo del grupo, y **no lo elimina del todo** cuando depende de la propia satisfacción. **Variabilidad:** el error estándar sigue $1/\sqrt{n}$ (pendiente log-log ≈ −0.50) y, **bajo $H_0$ sin efecto real**, 20 métricas dan al menos un «descubrimiento» en el **64 %** de los experimentos (Bonferroni lo baja al ≈ 5 %). **Correlación frente a causalidad:** Pearson y Spearman desde cero, una dependencia perfecta con $r\approx 0$, un **confusor** (correlación 0.65 que cae a ≈ 0 al controlar la temperatura), el efecto causal verdadero $\beta=0.5$ estimado como 1.1 (ingenuo), 0.51 (ajustado) y 0.50 (**aleatorizado**), y un **colisionador** que crea una correlación de −0.63. **Paradoja de Simpson:** el método A gana en cada terreno y pierde en el total (56 % frente a 79 %); la estandarización lo corrige, y una versión continua con pendientes positivas dentro y negativa global. **Estadística frente a *machine learning*:** mínimos cuadrados desde cero iguales a *statsmodels* (coeficientes, errores estándar y valores p) y a *scikit-learn*, **el modelo lineal iguala o supera al bosque cuando la verdad es lineal** ($R^2$ 0.42 frente a 0.39) y **pierde cuando no lo es** (0.51 frente a 0.94), y un efecto **«significativo» pero irrelevante** ($p\approx 7\times10^{-6}$ con $R^2\approx 0.0001$). 3 prácticas (corrección con pesos; correlación parcial; estandarización de tasas).

---

### 📝 2. Taller Práctico Evaluativo (*Hands-On*):
* [**../homeworks/00_Fundamentos_Estadistica_Hands_On.ipynb**](../homeworks/00_Fundamentos_Estadistica_Hands_On.ipynb): Taller evaluativo que integra población y muestra, escalas de medición, muestreo y las trampas del análisis en ejercicios prácticos.
* [**../homeworks/Para Dummies/00_Fundamentos_Estadistica_Hands_On_Dummies.ipynb**](../homeworks/Para%20Dummies/00_Fundamentos_Estadistica_Hands_On_Dummies.ipynb): versión guiada del taller.

---

### 🧸 3. Ruta Didáctica: Para Dummies:
Ubicada en la subcarpeta [`Para Dummies/`](Para%20Dummies/). Sin jerga ni fórmulas, con analogías cotidianas de Boyacá:
1. [**00_Introduccion_Estadistica_Dummies.ipynb**](Para%20Dummies/00_Introduccion_Estadistica_Dummies.ipynb): **La sopa y la cucharada**: probar una cucharada de la olla (1 000 costales de papa: las cucharadas grandes se parecen más a la olla), **contar, ordenar o promediar** según el tipo de dato (y por qué 20 °C no es «el doble» de 10 °C) y **la puerta de la tienda**: preguntar solo a las familias de la carretera sesga el promedio de leche, el sorteo no.
2. [**01_Conceptos_Estadisticos_Dummies.ipynb**](Para%20Dummies/01_Conceptos_Estadisticos_Dummies.ipynb): **El paraguas, la lluvia y las trampas de los números**: 7 caras de 10 monedas buenas le pasa al 17 % de las personas, **ruanas y gripa** suben juntas por el frío (y la relación casi desaparece al comparar días igual de fríos) y **dos flotas de buses** donde la ganadora en cada tipo de día pierde en el total (paradoja de Simpson).

---

## 💾 Datos Utilizados

Todos los datos son **sintéticos con semilla fija, generados por código dentro de cada cuaderno**; **no hay descargas** y **no se necesita ninguna carpeta `data/`**: cada cuaderno es autocontenido en Google Colab y el repositorio no acumula archivos.

| Conjunto | Origen | Dónde se usa |
|---|---|---|
| **Población de 20 000 parcelas** (rendimiento en t/ha, distribución gamma) y una población **lognormal** de 200 000 | `default_rng(42)` | Cuaderno 00 (muestreo, error estándar, intervalos y cobertura) |
| **Encuesta de 500 fincas** (municipio, educación, satisfacción, temperatura, altitud, trabajadores) | `default_rng(42)` | Cuaderno 00 (escalas de medición) |
| **8 000 parcelas en 160 veredas y 4 zonas**, con distancia a la vía | `default_rng(42)` | Cuaderno 00 (comparación de métodos de muestreo y Neyman) |
| **100 000 clientes** con tres grupos de edad y dos mecanismos de no respuesta | `default_rng(42)` | Cuaderno 01 (sesgo de muestreo y ponderación) |
| **Temperatura, helado, insolación**, un efecto causal $\beta=0.5$ con confusor, talento y esfuerzo | `default_rng(42)` | Cuaderno 01 (correlación y causalidad) |
| **Tabla de riego** (conteos inventados) y tres grupos con pendiente invertida | tabla escrita a mano y `default_rng(42)` | Cuaderno 01 (paradoja de Simpson) |
| **Regresión de 1 000 filas** (verdad lineal y no lineal) y de 200 000 filas (efecto minúsculo) | `default_rng(41)` | Cuaderno 01 (inferencia frente a predicción) |
| **Mini-ejemplos de juguete** (1 000 costales, tres veredas de leche, tienda de don José, ruanas y gripa, dos flotas de buses) | Tablas y generadores con semilla fija | Los dos *Dummies* |

> ⚠️ **Los datos son inventados** (nombres, cifras, flotas y veredas): los resultados describen el **mecanismo**, **no** valores esperables en un caso real. Los nombres de municipios de Boyacá solo ambientan los ejemplos. **No se usa ninguna cifra real** de población, censos o estudios.

## ⚙️ Requisitos

`numpy`, `pandas`, `scipy`, `statsmodels`, `scikit-learn` y `matplotlib` (todos preinstalados en Google Colab, salvo que conviene tener una versión reciente de *statsmodels*). **No se necesita red.** Los dos **Dummies** usan solo `NumPy`, `pandas` y `matplotlib`.

Se ejecutó de verdad, de arriba abajo y sin errores, con **Python 3.12**, **NumPy 2.5**, **pandas 2.3**, **SciPy 1.18**, ***statsmodels* 0.15**, ***scikit-learn* 1.9** y **Matplotlib 3.11** en Linux (de verdad: con los *starters* de las prácticas tal cual —solo comentarios— y con una copia donde cada *starter* se reemplazó por su solución). *No se probó en Google Colab ni en Windows/macOS.* Tiempos aproximados en un equipo de escritorio (varían con la carga): cuaderno 00 ≈ 10 s, 01 ≈ 12–14 s y los *Dummies* ≈ 4 s.

---

<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Asignatura: Estadística, Análisis y Representación de Datos</i>
  </p>
</div>
