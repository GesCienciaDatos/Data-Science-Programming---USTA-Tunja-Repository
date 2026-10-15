# Módulo 03: Inferencia Estadística 🎯📐

<p align="center">
  <img src="https://img.shields.io/badge/Discipline-Estad%C3%ADstica-ea580c?style=for-the-badge&logo=scipy&logoColor=white" alt="Estadística"/>
  <img src="https://img.shields.io/badge/Topics-IC%20%7C%20Pruebas%20de%20Hip%C3%B3tesis%20%7C%20Chi%C2%B2%20%7C%20ANOVA-0ea5e9?style=for-the-badge" alt="Topics"/>
  <img src="https://img.shields.io/badge/Course-Estad%C3%ADstica%2C%20An%C3%A1lisis%20y%20Representaci%C3%B3n%20de%20Datos-6366f1?style=for-the-badge" alt="Course"/>
  <img src="https://img.shields.io/badge/Institution-USTA%20Tunja-1e3a8a?style=for-the-badge" alt="USTA"/>
</p>

Bienvenido al **Módulo 03**, el **cuarto** de la asignatura **Estadística, Análisis y Representación de Datos** de la *Especialización en Ciencia de Datos* de la **Universidad Santo Tomás — Seccional Tunja**.

---

## 🧭 ¿De qué trata este módulo?

Este módulo corresponde a la sección **1.4.1** del libro de la asignatura (*Estadística inferencial: intervalos de confianza y pruebas de hipótesis, con valor p, pruebas T, Z, Chi-cuadrado y ANOVA*). La estadística descriptiva resume **la muestra que tenemos**; la inferencia responde a la pregunta que de verdad importa: **¿qué podemos decir de la población de la que salió, y con cuánta incertidumbre?** El módulo recorre las dos caras de esa pregunta: **estimar** (intervalos de confianza, *bootstrap*) y **decidir** (pruebas de hipótesis, potencia, tamaño del efecto, comparaciones múltiples), primero para **medias y proporciones** y luego para **frecuencias** (chi-cuadrado) y **varios grupos** (ANOVA).

El módulo **no** repite lo que ya existe en el repositorio: la estadística descriptiva con *pandas* está en [Data Science programming, Módulo 04 (EDA)](../../Data%20Science%20programming/04%20-%20EDA/README.md) y el uso del remuestreo para **validar modelos** en [Machine Learning, Módulo 03 (métricas, validación cruzada)](../../Machine%20Learning/03%20-%20Metricas%20y%20Ajuste%20de%20Hiperparametros/README.md). Aquí el enfoque es el del libro: **rigor estadístico** (supuestos, interpretación correcta del valor p y del «95 %», tamaños del efecto, potencia), con **implementaciones desde cero en NumPy contrastadas por `assert` contra SciPy y statsmodels**, **simulaciones** que muestran qué promete cada método y **resultados reportados con honestidad** (cuando un método «más moderno» no gana, cuando una prueba no rechaza $H_0$, cuando el estudio no tiene potencia).

> 🗺️ **Mapa del curso (ocho módulos):** **00** Fundamentos de Estadística y Análisis de Datos → **01** Estadística Descriptiva y Visualización → **02** Probabilidad y Distribuciones → **03** Inferencia Estadística *(este módulo)* → **04** No Paramétrica, Regresión y Ética → **05** Exploración y Limpieza de Datos → **06** Modelamiento Estadístico → **07** Temas Avanzados en *Data Analysis*. El [README del curso](../README.md) se actualizará con el índice completo.

> 🔗 **Conexión con otros cursos:** el diagnóstico de supuestos conecta con la regresión de [Data Science programming, Módulo 07](../../Data%20Science%20programming/07%20-%20Regression/README.md); la comparación de grupos y la limpieza previa, con [Data Mining, Módulo 01 (preprocesamiento)](../../Data%20Mining/01%20-%20Preprocesamiento%20de%20los%20Datos/README.md).

> 🛠️ **Ponlo en práctica:** todos los cuadernos (estándar y *Para Dummies*) incluyen secciones **«🛠️ Práctica»**: una celda de código para que escribas tu solución y, justo debajo, la **solución guiada desplegable** (`💡 Haz clic aquí para ver la solución guiada...`). Inténtalo primero y abre la solución solo para comparar.

---

## 🎯 Objetivos de Aprendizaje del Módulo

1. **Estimar con incertidumbre:** construir e **interpretar** intervalos de confianza para medias, proporciones, diferencias y varianzas, y verificar por simulación su **cobertura**.
2. **Elegir el método correcto:** $z$ frente a $t$, Wald frente a Wilson frente a Clopper–Pearson, percentil frente a BCa, Student frente a Welch, y saber **cuándo** el método elegido falla.
3. **Decidir con datos:** formular $H_0$ y $H_1$, calcular el **valor p** (y entender qué **no** es), controlar los **errores tipo I y II** y calcular la **potencia** y el **tamaño de muestra**.
4. **Ir más allá de la significancia:** reportar **tamaño del efecto con su intervalo**, distinguir significancia de relevancia práctica y reconocer la «maldición del ganador».
5. **Comparar frecuencias y varios grupos:** pruebas **chi-cuadrado** (ajuste e independencia, V de Cramér, Yates, Fisher) y **ANOVA** (tabla, $\eta^2$/$\omega^2$, supuestos, **Tukey**, **Welch**), controlando las **comparaciones múltiples**.

---

## 📚 Estructura Curricular del Módulo

### 🎓 1. Cuadernos Académicos Estándar:
1. [**00_Intervalos_de_Confianza.ipynb**](00_Intervalos_de_Confianza.ipynb): *Sección 1.4.1.* **Estimación puntual y por intervalo:** parámetro, estimador, error estándar y la **interpretación correcta** del «95 %». **IC de la media** con $z$ (σ conocida) y $t$ de Student (σ desconocida), con funciones propias iguales a SciPy y statsmodels; **intervalo de predicción** (solo ≈ 35 % de las observaciones nuevas cae en el IC de la media frente a 95 % en el de predicción) y **tamaño de muestra** (62 parcelas para ±1 t/ha con σ = 4; cuadruplicar $n$ reduce el ancho a la mitad). **Simulación de cobertura:** el IC $t$ cubre ≈ 95 % para todo $n$, mientras que el error común «$z$ con $s$» cubre 81 % con $n = 3$. **Proporciones:** Wald, Wilson, Agresti–Coull y Clopper–Pearson desde cero, con **cobertura exacta** para $n = 30$ (Wald: mínimo 0.14 y media 0.882; Wilson: media 0.953; Clopper–Pearson: nunca baja de 0.954), corrección por población finita. **Diferencia de medias (Welch)**, dualidad IC ↔ prueba (el IC incluye al 0 y $p = 0.147$: «sin evidencia» no es «sin efecto») y **IC de la varianza** (cubre 95 % con datos normales pero 72 % con exponenciales). ***Bootstrap*** percentil y **BCa** vectorizados desde cero y contrastados con `scipy.stats.bootstrap` sobre una muestra asimétrica, mediana sin fórmula y una **cobertura honesta**: con $n = 25$ y asimetría fuerte ningún método llega al 95 % (el IC $t$ 89.6 %, percentil y BCa 88.5 %). 2 prácticas (pocos defectuosos: ¿qué intervalo conviene?; *bootstrap* del coeficiente de variación).
2. [**01_Pruebas_de_Hipotesis_Valor_P_Z_y_T.ipynb**](01_Pruebas_de_Hipotesis_Valor_P_Z_y_T.ipynb): *Sección 1.4.1.* El protocolo de seis pasos, la definición correcta del **valor p** y la tabla de lo que **no** significa (Declaración de la ASA). **Prueba Z** con región crítica dibujada (z = −1.957, $p = 0.0504$ bilateral frente a 0.0252 unilateral: la decisión **cambia** y por eso la cola se elige antes de ver los datos) y **pruebas t** (una muestra, **Welch**, Student y **pareada**) iguales a SciPy en las tres alternativas; ignorar el emparejamiento sube el valor p de 0.003 a 0.357. **Simulación del valor p:** uniforme bajo $H_0$ (4.7 % de rechazos con α = 0.05) y apilado cerca de 0 bajo $H_1$ (solo 25 % de rechazos con $n = 15$ y un efecto de 0.5 desviaciones), y **prueba de permutación** desde cero. **Potencia** exacta con la $t$ no central (idéntica a statsmodels y a Monte Carlo), tamaño de muestra (64 por grupo para $d = 0.5$ frente a 394 para $d = 0.2$), **$d$ de Cohen y $g$ de Hedges** con IC. **Significancia frente a relevancia** (con $n = 20\,000$ por grupo: $p \approx 10^{-9}$ y $d = 0.06$) y la **«maldición del ganador»** (con poca potencia, los éxitos exageran el efecto ≈ 1.9 veces), y **pruebas múltiples** (FWER ≈ 0.64 con 20 pruebas; Bonferroni, Holm y Benjamini–Hochberg desde cero, iguales a `multipletests`). 2 prácticas (permutación para medianas; ¿cuántas parcelas hacen falta?).
3. [**02_Chi_Cuadrado_y_ANOVA.ipynb**](02_Chi_Cuadrado_y_ANOVA.ipynb): *Sección 1.4.1.* La **distribución chi-cuadrado** (suma de normales al cuadrado) y la **bondad de ajuste** con dados sintéticos: calibración (5.0 % de rechazos con dados justos) y potencia (82 % contra un dado cargado), y el efecto de las **esperadas pequeñas** (nivel real 8.2 % en vez de 5 % con probabilidades muy desiguales). **Independencia en tablas de contingencia** desde cero (esperadas, **V de Cramér**, **residuos ajustados**, mapa de calor) con una encuesta sintética de 400 fincas ($\chi^2 = 18.16$, $p = 0.0001$, pero $V = 0.21$: asociación modesta), verificada contra SciPy y contra una **prueba de permutación**; **Yates y Fisher** en una tabla 2×2 pequeña (la decisión cambia). **ANOVA de un factor** desde cero (SCE, SCD, SCT, $F$; $F = 6.455$, $\eta^2 = 0.31$, $\omega^2 = 0.25$) igual a `f_oneway` y a `anova_lm`, con $F = t^2$ para dos grupos y diagnóstico de supuestos con los residuos. **Comparaciones múltiples:** 6 pruebas $t$ sin corregir dan 20 % de falsos positivos con $H_0$ cierta; **Tukey HSD** (Tukey–Kramer desde cero, igual a SciPy y a statsmodels) y Bonferroni los controlan. **ANOVA de Welch** desde cero: con varianzas y tamaños desiguales el $F$ clásico rechaza 28.6 % (o 0.7 %) con $H_0$ cierta, mientras Welch se mantiene en 5 %. 2 prácticas (Yates, Fisher y chi-cuadrado en una tabla pequeña; $\eta^2$, $\omega^2$ y su relación con $F$).

---

### 📝 2. Taller Práctico Evaluativo (*Hands-On*):
* [**../homeworks/03_Inferencia_Hands_On.ipynb**](../homeworks/03_Inferencia_Hands_On.ipynb): Taller evaluativo que integra los intervalos de confianza, las pruebas de hipótesis y las pruebas chi-cuadrado y ANOVA en ejercicios prácticos. Versión guiada: [`../homeworks/Para Dummies/03_Inferencia_Hands_On_Dummies.ipynb`](../homeworks/Para%20Dummies/03_Inferencia_Hands_On_Dummies.ipynb).

---

### 🧸 3. Ruta Didáctica: Para Dummies:
Ubicada en la subcarpeta [`Para Dummies/`](Para%20Dummies/). **Sin jerga ni fórmulas**, con analogías cotidianas y simulaciones sencillas con *NumPy*, *pandas* y *Matplotlib* (no requieren SciPy ni statsmodels):
1. [**00_Intervalos_Confianza_Dummies.ipynb**](Para%20Dummies/00_Intervalos_Confianza_Dummies.ipynb): **La red de pesca**: un camión con 2 000 bultos de papa, cinco muestras de 10 que dan cinco promedios distintos, qué significa «95 %» (946 de 1 000 vendedores atrapan el promedio real), por qué cuadruplicar los bultos solo reduce el intervalo a la mitad y el *bootstrap* como «volver a sacar de la bolsa».
2. [**01_Pruebas_Hipotesis_Dummies.ipynb**](Para%20Dummies/01_Pruebas_Hipotesis_Dummies.ipynb): **El juicio del dato**: una moneda con 62 caras (el valor p como «qué tan seguido pasa algo así por pura suerte»), dos abonos comparados revolviendo etiquetas (p ≈ 7 %: **no** se puede descartar la suerte, pero tampoco se prueba que sean iguales) y por qué «muy significativo» no es «muy importante».
3. [**02_Chi_Cuadrado_ANOVA_Dummies.ipynb**](Para%20Dummies/02_Chi_Cuadrado_ANOVA_Dummies.ipynb): **¿Tiene que ver?**: la encuesta de cultivo y riego con lo observado frente a lo esperado, cuatro variedades de papa con un «contraste» y la trampa de comparar muchas parejas (≈ 20 % de falsas alarmas con variedades idénticas).

---

## 💾 Datos Utilizados

Todos los datos son **sintéticos con semilla fija, generados por código dentro de cada cuaderno**; **no hay descargas** y **no se necesita ninguna carpeta `data/`** ni se escribe ningún archivo. Como se conoce el parámetro verdadero, se puede **comprobar** que cada método hace lo que promete.

| Conjunto | Origen | Dónde se usa |
|---|---|---|
| **Rendimiento de 30 parcelas** de papa (normal, μ = 22, σ = 4 t/ha) | `default_rng(42)` | Cuaderno 00 (IC $z$/$t$, predicción, *bootstrap* de la práctica 2) |
| **Ingreso de 40 hogares** (lognormal, asimétrico) y 1 000 muestras lognormales de 25 | `default_rng` | Cuaderno 00 (*bootstrap* percentil/BCa y su cobertura) |
| **Dos fertilizantes** (18 y 14 parcelas, varianzas distintas) | `default_rng` | Cuaderno 00 (Welch, dualidad) |
| **36 bultos de papa** (etiqueta de 50 kg, σ = 1.5 kg conocida) | `default_rng` | Cuaderno 01 (prueba Z) |
| **Dos variedades** (20 y 24 parcelas) y **15 parcelas antes/después** de un riego | `default_rng` | Cuaderno 01 (t, Welch, pareada, permutación, potencia, tamaño del efecto) |
| **Estudios A y B** (20 000 y 8 por grupo) y 20 hipótesis (5 con efecto real) | `default_rng(5)` y global | Cuaderno 01 (significancia y relevancia, pruebas múltiples) |
| **Dados justo y cargado** (300 tiros) | `default_rng(42)` | Cuaderno 02 (bondad de ajuste) |
| **Encuesta de 400 fincas** (cultivo × riego) y tabla 2×2 de 20 parcelas | `default_rng` | Cuaderno 02 (independencia, Yates, Fisher) |
| **4 variedades de papa** (12 parcelas cada una, semilla propia) | `default_rng(12)` | Cuaderno 02 (ANOVA, Tukey) |
| **Mini-ejemplos de juguete** (camión de papa, monedas, abonos, encuesta, variedades) | `default_rng(42)` y tablas escritas a mano | Los tres *Dummies* |

> ⚠️ **Los datos son inventados** (cultivos, parcelas, fincas, ingresos y cifras): los resultados describen el **mecanismo estadístico**, **no** el rendimiento ni la realidad agropecuaria. En el cuaderno 02 la semilla del ANOVA se eligió entre las 12 primeras por dar un caso «típico» (con otras semillas el $F$ va de ≈ 1.2 a ≈ 9.4 con los mismos parámetros), y así se declara en el cuaderno.

## ⚙️ Requisitos

`numpy`, `pandas`, `matplotlib`, **`scipy`** (≥ 1.11: se usan `stats.bootstrap`, `permutation_test`, `tukey_hsd`, `studentized_range` y el atributo `df` de `ttest_ind`) y **`statsmodels`** (≥ 0.14), todos preinstalados en Google Colab. Los tres **Dummies** usan solo `NumPy`, `pandas` y `Matplotlib`. **No se necesita red.**

Se ejecutó de verdad, de arriba abajo y sin errores, con **Python 3.12**, **NumPy 2.5**, **pandas 2.3**, **SciPy 1.18**, **statsmodels 0.15** y **Matplotlib 3.11** en Linux (de verdad: con los *starters* de las prácticas tal cual —solo comentarios— y con una copia donde cada *starter* se reemplazó por su solución). *No se probó en Google Colab ni en Windows/macOS.* Tiempos aproximados en un equipo de escritorio (varían con la carga): cuaderno 00 ≈ 8–9 s, 01 ≈ 6 s y 02 ≈ 17–29 s; los *Dummies* tardan ≈ 3–9 s.

---

<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Asignatura: Estadística, Análisis y Representación de Datos</i>
  </p>
</div>
