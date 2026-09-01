# Módulo 07: Modelado de Regresión (Regression) 📈

> **Especialización en Ciencia de Datos**  
> **Universidad Santo Tomás — Seccional Tunja**  
> **Docente:** Santiago A. Zúñiga M.  
> **Contacto:** [gestorvirtualcienciadatos@ustatunja.edu.co](mailto:gestorvirtualcienciadatos@ustatunja.edu.co)

---

## 📌 Descripción General

El **Modelado de Regresión (*Regression Modeling*)** constituye el pilar fundamental del Aprendizaje Automático Supervisado para la predicción de variables cuantitativas continuas ($y \in \mathbb{R}$).

En este módulo estudiarás desde la deducción matemática de la **Ecuación Normal de Mínimos Cuadrados Ordinarios (OLS)** hasta modelos avanzados con regularización:
* Diagnóstico riguroso de los **supuestos del Teorema de Gauss-Markov** (Linealidad, Homocedasticidad, Normalidad de residuos e Independencia).
* Modelos multivariados, **términos de interacción sinérgicos** y detección de multicolinealidad con el factor **VIF (*Variance Inflation Factor*)**.
* Regresión Polinomial y técnicas de contracción de coeficientes: **Ridge ($L_2$)**, **Lasso ($L_1$)** y **ElasticNet**.
* Estrategias de **Validación Cruzada (*K-Fold Cross Validation*)**, ajuste sistemático de hiperparámetros con **`GridSearchCV`** y regresores no paramétricos basados en instancias (**$k$-NN Regressor**).

---

## 🗺️ Estructura del Módulo

| # | Cuaderno Interactivo | Temas Principales | Dificultad |
|:---:|---|---|:---:|
| **00** | [**Introducción a la Regresión**](00_Introduccion_Regression.ipynb) | Paradigma del aprendizaje supervisado cuantitativo, formulación de la función de costo MSE y mapa de ruta del módulo. | 🟢 Básico |
| **01** | [**Regresión Lineal Simple**](01_Regresion_Lineal.ipynb) | Deducción matricial de la Ecuación Normal OLS $\boldsymbol{\theta} = (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{y}$, métricas $R^2$ / MSE y diagnóstico de supuestos de Gauss-Markov en `Advertising.csv`. | 🟢 Básico-Intermedio |
| **02** | [**Consideraciones en Regresión Múltiple**](02_Consideraciones_Regresion_Multiple.ipynb) | Regresión multivariada, interpretación de coeficientes parciales, términos de interacción cruzada, multicolinealidad y cálculo de VIF en `USA_Housing.csv`. | 🟡 Intermedio |
| **03** | [**Regresión Polinomial y Regularización**](03_Regresion_Polinomial_y_Regularizacion.ipynb) | Expansión polinomial, compromiso Sesgo-Varianza (*Bias-Variance Tradeoff*), sobreajuste y regularización analítica: Ridge ($L_2$), Lasso ($L_1$) y ElasticNet. | 🧗 Intermedio-Avanzado |
| **04** | [**Selección de Modelos, Validación Cruzada y k-NN**](04_Seleccion_Modelos_Validacion_Cruzada_y_KNN.ipynb) | Validación cruzada $K$-Fold, búsqueda exhaustiva con `GridSearchCV`, regresión no paramétrica $k$-NN y comparativa de modelos. | 🧗 Intermedio-Avanzado |

---

## 💡 Guías "Para Dummies" (Explicaciones Intuitivas Sin Jerga Compleja)

* [**00. Introducción a la Regresión (Dummies)**](Para%20Dummies/00_Introduccion_Regression_Dummies.ipynb): ¿Qué es predecir un número? La regla para estimar precios y demandas.
* [**01. Regresión Lineal (Dummies)**](Para%20Dummies/01_Regresion_Lineal_Dummies.ipynb): Trazar la mejor línea recta a través de una nube de puntos.
* [**02. Regresión Múltiple (Dummies)**](Para%20Dummies/02_Consideraciones_Regresion_Multiple_Dummies.ipynb): El perito avaluador que suma el efecto de las habitaciones, el barrio y los metros cuadrados.
* [**03. Polinomios y Regularización (Dummies)**](Para%20Dummies/03_Regresion_Polinomial_y_Regularizacion_Dummies.ipynb): La cuerda flexible (Lasso y Ridge) que frena al modelo para no memorizar el ruido.
* [**04. Validación Cruzada y k-NN (Dummies)**](Para%20Dummies/04_Seleccion_Modelos_Validacion_Cruzada_y_KNN_Dummies.ipynb): Probar el modelo con diferentes exámenes sorpresa y consultar a los vecinos más parecidos.

---

## 📂 Conjuntos de Datos (*Datasets*)

En este módulo se emplean los siguientes datasets ubicados en la carpeta `data/`:
- `Advertising.csv`: Inversiones publicitarias en TV, Radio y Periódicos frente a ventas generadas.
- `USA_Housing.csv`: Características demográficas y precios de venta de viviendas en Estados Unidos.

---

<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos</i>
  </p>
</div>
