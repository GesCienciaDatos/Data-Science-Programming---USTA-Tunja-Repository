# 00_Introduccion_Regression

<table style="width: 100%; border-collapse: collapse; border: none; background: #f8fafc; border-left: 6px solid #1e3a8a; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #0f172a; font-size: 2.1em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        Introducción a la Regresión en Ciencia de Datos 📈
      </h1>
      <p style="margin: 6px 0 0 0; color: #1e3a8a; font-size: 1.15em; font-weight: 600; font-family: system-ui, -apple-system, sans-serif;">
        Especialización en Ciencia de Datos | Programación para Ciencia de Datos
      </p>
      <p style="margin: 4px 0 0 0; color: #64748b; font-size: 0.95em; font-family: system-ui, -apple-system, sans-serif;">
        Universidad Santo Tomás — Seccional Tunja
      </p>
    </td>
    <td style="text-align: right; vertical-align: middle; border: none; padding: 15px 20px; width: 30%;">
      <span style="background: #1e3a8a; color: #ffffff; padding: 6px 14px; border-radius: 20px; font-size: 0.85em; font-weight: 700; display: inline-block; margin-bottom: 8px;">
        Módulo 07
      </span><br>
      <span style="color: #64748b; font-size: 0.85em;">Docente: Santiago A. Zúñiga M.</span><br>
      <a href="mailto:gestorvirtualcienciadatos@ustatunja.edu.co" style="color: #2563eb; font-size: 0.8em; text-decoration: none; font-weight: 500;">gestorvirtualcienciadatos@ustatunja.edu.co</a>
    </td>
  </tr>
</table>

<div align="center" style="margin-top: 15px; margin-bottom: 15px;">
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/07%20-%20Regression/00_Introduccion_Regression.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## Objetivos de Aprendizaje (*Learning Outcomes*) 🔎

En este séptimo módulo exploraremos el **Modelado de Regresión**, una de las disciplinas más fundamentales y aplicadas dentro del Machine Learning Supervisado.

El contenido se estructura progresivamente a través de los siguientes cuadernos interactivos:

1. **[Introducción a la Regresión](00_Introduccion_Regression.ipynb)** *(Este cuaderno)*: Paradigma supervisado, inferencia vs predicción, ventajas de la regresión lineal y hoja de ruta del módulo.
2. **[Regresión Lineal Simple y Múltiple](01_Regresion_Lineal.ipynb)**: Formulación matemática, derivación analítica de la Ecuación Normal OLS $\boldsymbol{\theta} = (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{y}$, Scikit-Learn API, caso práctico `Advertising.csv`, métricas ($R^2$, MSE, RMSE, MAE) y diagnóstico de supuestos de Gauss-Markov.
3. **[Consideraciones de la Regresión Múltiple](02_Consideraciones_Regresion_Multiple.ipynb)**: Sobreajuste (*Overfitting*), subajuste (*Underfitting*), compromiso Sesgo-Varianza (*Bias-Variance Tradeoff*), multicolinealidad y diagnóstico con el Factor de Inflación de la Varianza (**VIF**).
4. **[Regresión Polinomial y Técnicas de Regularización](03_Regresion_Polinomial_y_Regularizacion.ipynb)** 🧗: Captura de curvaturas con `PolynomialFeatures`, regularización **Ridge ($L_2$)**, **Lasso ($L_1$)**, **ElasticNet**, estandarización de características y optimización con `RidgeCV` y `LassoCV`.
5. **[Selección de Modelos, Validación Cruzada y k-NN](04_Seleccion_Modelos_Validacion_Cruzada_y_KNN.ipynb)** 🧗: Limitaciones del método Hold-Out, **$k$-Fold Cross-Validation** (`cross_val_score`, `Pipeline`), pruebas de hipótesis estadísticas ($t$-test y $F$-test), regresión no paramétrica con **$k$-NN Regressor** y caso práctico con `bikeshare.csv`.

> 🧗 **Nota:** Los cuadernos identificados con el ícono de escalador abordan técnicas avanzadas de optimización de hiperparámetros y modelado no paramétrico.

---
## Recursos y Referencias Recomendadas 📚

### 📖 Libros de Referencia:
* **[An Introduction to Statistical Learning with Applications in Python (ISLP)](https://www.statlearning.com/)** — *Gareth James, Daniela Witten, Trevor Hastie, Robert Tibshirani (Capítulos 2 y 3)*.
* **[Course Notes for STAT 501: Regression Methods](https://online.stat.psu.edu/stat501/)** — *Penn State Department of Statistics*.
* **[The Elements of Statistical Learning](https://hastie.su.domains/ElemStatLearn/)** — *Trevor Hastie, Robert Tibshirani, Jerome Friedman*.

### 🌐 Enlaces y Documentación Oficial:
* **[Scikit-Learn User Guide: Supervised Learning & Linear Models](https://scikit-learn.org/stable/supervised_learning.html)**.
* **[Scikit-Learn User Guide: Regression Metrics](https://scikit-learn.org/stable/modules/model_evaluation.html#regression-metrics)**.
* **[Harvard CS109-A: Introduction to Data Science](https://harvard-iacs.github.io/2021-CS109A/)** — *Harvard Institute for Applied Computational Science*.

---
## 1. ¿Qué es el Aprendizaje Supervisado y qué es la Regresión? 🧠

En el **Aprendizaje Supervisado (*Supervised Learning*)**, los algoritmos aprenden a partir de datos históricos etiquetados donde cada observación consiste en un vector de características $\mathbf{x} = [x_1, x_2, \dots, x_p]^T$ y una respuesta cuantitativa conocida $y$:

$$\mathcal{D} = \{(\mathbf{x}_1, y_1), (\mathbf{x}_2, y_2), \dots, (\mathbf{x}_n, y_n)\}$$

El objetivo es estimar una función de mapeo $\hat{y} = f(\mathbf{x})$ que describa la esperanza condicional de la variable objetivo:

$$\hat{y} = \mathbb{E}[Y \mid \mathbf{X} = \mathbf{x}]$$

```
                           ┌──────────────────────────────┐
                           │   Aprendizaje Supervisado    │
                           └──────────────┬───────────────┘
                                          │
                  ┌───────────────────────┴───────────────────────┐
                  ▼                                               ▼
      ┌───────────────────────┐                       ┌───────────────────────┐
      │  Regresión (Continuo) │                       │ Clasificación (Categ.)│
      └───────────────────────┘                       └───────────────────────┘
        • Precio de viviendas ($)                       • Detección de Fraude (0 / 1)
        • Temperatura ambiental (°C)                    • Diagnóstico Médico (A / B)
        • Demanda de alquileres (uds)                   • Cancelación de Clientes (Churn)
```

---
## 2. ¿Por qué utilizar Modelos de Regresión? 💡

A pesar de la existencia de modelos complejos tipo caja negra (como redes neuronales profundas o ensambles boosting), la **Regresión** continúa siendo el pilar analítico fundamental en Ciencia de Datos por cuatro motivos clave:

1. **Interpretabilidad Directa:** Los coeficientes $\beta_j$ cuantifican el impacto marginal de cada predictor sobre la respuesta, manteniendo los demás constantes.
2. **Inferencia Estadística Rigurosa:** Permite probar hipótesis ($p$-valores, intervalos de confianza del 95% y pruebas $t$/$F$) para validar si los efectos observados son significativos.
3. **Eficiencia Computacional:** Su solución analítica mediante la Ecuación Normal OLS se ejecuta de forma casi instantánea.
4. **Modelo Base Indispensable (*Baseline*):** Establece el umbral mínimo de precisión que cualquier técnica más sofisticada está obligada a superar.

---
## 3. Mapa Estratégico del Módulo 🗺️

```
┌────────────────────────────────────────────────────────────────────────┐
│                   Pipeline de Modelado de Regresión                    │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
    ┌───────────────────────────────┼───────────────────────────────┐
    ▼                               ▼                               ▼
┌────────────────────────┐      ┌────────────────────────┐      ┌────────────────────────┐
│ 01. Regresión Lineal   │      │ 02. Consideraciones    │      │ 03. Regresión Polin.   │
│     Simple y Múltiple  │ ───► │     Regresión Múltiple │ ───► │     y Regularización   │
│ • Ecuación Normal OLS  │      │ • Sesgo-Varianza       │      │ • PolynomialFeatures   │
│ • Diagnóstico Supuestos│      │ • VIF y Colinealidad   │      │ • Ridge, Lasso, Elastic│
└────────────────────────┘      └────────────────────────┘      └───────────┬────────────┘
                                                                            │
                                                                            ▼
                                                                ┌────────────────────────┐
                                                                │ 04. Validación Cruzada │
                                                                │     y Regresión k-NN   │
                                                                │ • cross_val_score & PL │
                                                                │ • k-NN Regressor       │
                                                                │ • Caso Bikeshare       │
                                                                └────────────────────────┘
```

---
## Configuración del Entorno 🛠️

Para el desarrollo práctico de este módulo utilizaremos las bibliotecas estándar del ecosistema científico de Python: `numpy`, `pandas`, `scikit-learn`, `statsmodels`, `matplotlib` y `seaborn`.

```python
try:
    from IPython.core.interactiveshell import InteractiveShell
    InteractiveShell.ast_node_interactivity = 'all'
except Exception:
    pass
try:
    from IPython.display import display
except Exception:
    pass

# Módulos numéricos, tabulares y estadísticos
import numpy as np
import pandas as pd
import statsmodels.api as sm

# Visualización gráfica
import matplotlib.pyplot as plt
import seaborn as sns

# Modelado y evaluación de regresión con Scikit-Learn
import sklearn
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Configuración visual institucional
sns.set_theme(style="whitegrid")
plt.rcParams["figure.figsize"] = (8, 4.5)
plt.rcParams["font.size"] = 10

import warnings
warnings.filterwarnings("ignore")

print("✅ Entorno preparado exitosamente para el Módulo 07: Regresión.")
print(f"📦 Versiones cargadas: Scikit-Learn {sklearn.__version__} | Pandas {pd.__version__} | NumPy {np.__version__}")
```

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos</i>
  </p>
</div>
