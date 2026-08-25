# Módulo 07: Regresión (Regression) 📈

> **Especialización en Ciencia de Datos**  
> **Universidad Santo Tomás — Seccional Tunja**  
> **Docente:** Santiago A. Zúñiga M.  
> **Contacto:** [gestorvirtualcienciadatos@ustatunja.edu.co](mailto:gestorvirtualcienciadatos@ustatunja.edu.co)

---

## 📌 Descripción General

La **Regresión (*Regression*)** es la rama fundamental del Aprendizaje Automático Supervisado dedicada a predecir variables cuantitativas continuas ($y \in \mathbb{R}$). Comprender los fundamentos matemáticos de la regresión, sus métodos de optimización (Mínimos Cuadrados Ordinarios y Gradiente Descendente), el diagnóstico de supuestos y las técnicas de regularización es indispensable para todo Científico de Datos.

En este módulo aprenderás las metodologías esenciales y avanzadas del modelado predictivo continuo:
* Fundamentos teóricos del Aprendizaje Supervisado y formulación matemática de la Regresión Lineal Simple y Múltiple.
* Solución analítica exacta mediante la **Ecuación Normal de Mínimos Cuadrados (OLS)**.
* Métricas estadísticas de evaluación continua: **MAE**, **MSE**, **RMSE**, **$R^2$** y **$R^2$ Ajustado**.
* Verificación y diagnóstico de los **Cinco Supuestos Clásicos de Gauss-Markov** (Linealidad, Homocedasticidad, Normalidad, Independencia y Multicolinealidad con VIF).
* Captura de curvaturas complejas mediante **Regresión Polinomial** y balance del dilema **Sesgo-Varianza (*Bias-Variance Tradeoff*)**.
* Control del sobreajuste mediante regularización **Ridge ($L_2$)**, **Lasso ($L_1$)** y **ElasticNet**.
* Modelado no paramétrico con **Regresión por $k$-Vecinos Más Cercanos ($k$-NN Regressor)**.
* Validación cruzada (*$k$-Fold Cross-Validation*) e inferencia estadística mediante pruebas de hipótesis.

---

## 🗺️ Estructura y Cuadernos del Módulo

| # | Cuaderno Interactivo | Temas Principales | Dificultad |
|:---:|---|---|:---:|
| **00** | [**Introducción a la Regresión**](00_Introduccion_Regression.ipynb) | Paradigma supervisado, objetivos de aprendizaje, inferencia vs predicción, mapa de ruta del módulo y entorno. | 🟢 Básico |
| **01** | [**Regresión Lineal**](01_Regresion_Lineal.ipynb) | Ecuaciones matemáticas, formulación matricial, derivación analítica de la Ecuación Normal OLS, Scikit-Learn API, caso práctico Advertising, métricas (MSE, R², RMSE, MAE) y diagnóstico de supuestos (Gauss-Markov, Durbin-Watson). | 🟢 Básico-Intermedio |
| **02** | [**Consideraciones de la Regresión Múltiple**](02_Consideraciones_Regresion_Multiple.ipynb) | Sobreajuste (*Overfitting*), subajuste (*Underfitting*), compromiso Sesgo-Varianza (*Bias-Variance Tradeoff*), Multicolinealidad y diagnóstico con el Factor de Inflación de la Varianza (**VIF**). | 🟡 Intermedio |
| **03** | [**Regresión Polinomial y Técnicas de Regularización**](03_Regresion_Polinomial_y_Regularizacion.ipynb) | Transformaciones polinomiales con `PolynomialFeatures`, regularización **Ridge ($L_2$)**, **Lasso ($L_1$)**, **ElasticNet**, estandarización de variables y optimización de hiperparámetros con Validación Cruzada (`RidgeCV` y `LassoCV`). | 🧗 Intermedio-Avanzado |
| **04** | [**Selección de Modelos, Validación Cruzada y k-NN**](04_Seleccion_Modelos_Validacion_Cruzada_y_KNN.ipynb) | Métodos Hold-out vs **$k$-Fold Cross-Validation** (`cross_val_score`, `Pipeline`), pruebas de hipótesis ($t$-test y $F$-test), regresión no paramétrica con **$k$-NN Regressor** y caso práctico con Capital Bikeshare. | 🧗 Intermedio-Avanzado |

---

## 📂 Conjuntos de Datos (*Datasets*)

Los cuadernos interactivos de este módulo emplean conjuntos de datos reales y sintéticos de referencia:

* **`Advertising.csv`**: Inversión publicitaria en TV, Radio y Periódicos vs Ventas (ideal para Regresión Lineal Múltiple, Ecuación Normal y diagnóstico OLS).
* **`bikeshare.csv`**: Demanda diaria de alquiler de bicicletas en Washington D.C. según temperatura y condiciones meteorológicas (731 observaciones, ideal para comparar modelos paramétricos vs no paramétricos $k$-NN).
* **`insurance.csv`**: Gastos médicos individuales según edad, IMC, fumador y región (modelado multivariado con interacciones).
* **`housing.csv`**: Precios de viviendas con múltiples atributos socioeconómicos y geográficos.

---

## 📚 Recursos y Lecturas Recomendadas

### 📖 Libros y Cursos de Referencia
1. **[An Introduction to Statistical Learning with Applications in Python (ISLP)](https://www.statlearning.com/)** — *Gareth James, Daniela Witten, Trevor Hastie, Robert Tibshirani (Capítulos 2 y 3)*.
2. **[STAT 501: Regression Methods](https://online.stat.psu.edu/stat501/)** — *Penn State Department of Statistics*.
3. **[Scikit-Learn Supervised Learning Guide: Linear Models](https://scikit-learn.org/stable/modules/linear_model.html)**.
4. **[Scikit-Learn User Guide: Regression Metrics](https://scikit-learn.org/stable/modules/model_evaluation.html#regression-metrics)**.
5. **[Harvard CS109-A: Introduction to Data Science](https://harvard-iacs.github.io/2021-CS109A/)**.

---

<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos</i>
  </p>
</div>
