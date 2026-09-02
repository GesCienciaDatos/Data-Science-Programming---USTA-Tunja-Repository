# 00_Introduccion_Classification

<table style="width: 100%; border-collapse: collapse; border: none; background: #f8fafc; border-left: 6px solid #1e3a8a; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #0f172a; font-size: 2.1em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        Introducción a la Clasificación en Ciencia de Datos 🎯
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
        Módulo 08
      </span><br>
      <span style="color: #64748b; font-size: 0.85em;">Docente: Santiago A. Zúñiga M.</span><br>
      <a href="mailto:gestorvirtualcienciadatos@ustatunja.edu.co" style="color: #2563eb; font-size: 0.8em; text-decoration: none; font-weight: 500;">gestorvirtualcienciadatos@ustatunja.edu.co</a>
    </td>
  </tr>
</table>

<div align="center" style="margin-top: 15px; margin-bottom: 15px;">
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/08%20-%20Classification/00_Introduccion_Classification.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## Objetivos de Aprendizaje (*Learning Outcomes*) 🔎

En este octavo módulo abordaremos el **Modelado de Clasificación**, la disciplina del Machine Learning Supervisado dedicada a predecir variables cualitativas discretas ($y \in \{C_1, C_2, \dots, C_K\}$).

El contenido se estructura progresivamente a través de los siguientes cuadernos interactivos:

1. **[Introducción a la Clasificación](00_Introduccion_Classification.ipynb)** *(Este cuaderno)*: Paradigma supervisado cualitativo, probabilidades acotadas, función Sigmoide $\sigma(z)$, limitaciones insalvables de la regresión lineal en clasificación y mapa de ruta del módulo.
2. **[Regresión Logística Simple y Múltiple](01_Regresion_Logistica_Simple_y_Multiple.ipynb)**: Formulación analítica del Logit, razón de momios (*Odds Ratio* $e^\beta$), estimación por Máxima Verosimilitud (MLE), función de pérdida *Binary Cross-Entropy / Log-Loss*, `predict_proba` vs `predict` y umbrales de decisión con `heart_disease.csv`.
3. **[Clasificación Multiclase y Fronteras de Decisión](02_Clasificacion_Multiclase_y_Fronteras_Decision.ipynb)** 🌸: Estrategias One-vs-Rest (OvR) y Multinomial Softmax, visualización 2D de regiones de decisión sobre el conjunto botánico de Fisher `Iris`, transformaciones polinomiales no lineales y regularización $L_1$ (Lasso) / $L_2$ (Ridge) con el parámetro $C$.
4. **[Evaluación de Modelos y Métricas de Clasificación](03_Evaluacion_de_Modelos_y_Metricas_Clasificacion.ipynb)** 📊: Diagnóstico exhaustivo más allá de la exactitud: Matriz de Confusión (VP, VN, FP, FN), Precisión, Sensibilidad (*Recall*), Especificidad, $F_1$-Score, Curva ROC-AUC, Curva Precision-Recall (PR-AUC) y calibración de umbrales con el índice de Youden en `customer_churn.csv`.
5. **[k-NN Clasificación y Selección de Modelos](04_KNN_Clasificacion_y_Seleccion_Modelos.ipynb)** 🧗: Algoritmo no paramétrico basado en instancias $k$-Nearest Neighbors ($k$-NN), métricas de distancia ($\mathbb{R}^p$), demostración del **impacto crítico de `StandardScaler`**, compromiso Sesgo-Varianza, `StratifiedKFold`, `Pipeline` y optimización sistemática con `GridSearchCV`.

---
## Recursos y Referencias Recomendadas 📚

### 📖 Libros de Referencia:
* **[An Introduction to Statistical Learning with Applications in Python (ISLP)](https://www.statlearning.com/)** — *Gareth James, Daniela Witten, Trevor Hastie, Robert Tibshirani (Capítulo 4: Classification)*.
* **[The Elements of Statistical Learning](https://hastie.su.domains/ElemStatLearn/)** — *Trevor Hastie, Robert Tibshirani, Jerome Friedman (Capítulo 4)*.
* **[Pattern Recognition and Machine Learning](https://www.microsoft.com/en-us/research/people/cmbishop/prml-book/)** — *Christopher M. Bishop*.

### 🌐 Enlaces y Documentación Oficial:
* **[Scikit-Learn User Guide: Supervised Learning & Logistic Regression](https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression)**.
* **[Scikit-Learn User Guide: Nearest Neighbors](https://scikit-learn.org/stable/modules/neighbors.html)**.
* **[Scikit-Learn User Guide: Classification Metrics](https://scikit-learn.org/stable/modules/model_evaluation.html#classification-metrics)**.
* **[Harvard CS109-A: Introduction to Data Science](https://harvard-iacs.github.io/2021-CS109A/)** — *Harvard University*.

---
## 1. ¿Qué es el Aprendizaje Supervisado y qué es la Clasificación? 🧠

En el **Aprendizaje Supervisado (*Supervised Learning*)**, los algoritmos aprenden a partir de datos etiquetados $\mathcal{D} = \{(\mathbf{x}_1, y_1), \dots, (\mathbf{x}_n, y_n)\}$.
* En **Regresión**, la salida es continua ($y \in \mathbb{R}$).
* En **Clasificación**, la respuesta es cualitativa o categórica ($y \in \{0, 1\}$ o $\{C_1, \dots, C_K\}$).

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
        • Demanda de alquileres (uds)                   • Diagnóstico Cardiopatía (0 / 1)
        • Temperatura ambiental (°C)                    • Especies de Flor (Setosa / ...)
```

---
## Configuración del Entorno de Trabajo 🛠️

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

import os
import urllib.parse
import urllib.request
import warnings
warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn

# Configuración visual institucional
sns.set_theme(style="whitegrid")
plt.rcParams["figure.figsize"] = (8, 4.5)
plt.rcParams["font.size"] = 10

# 🚀 Función de utilidad para cargar datasets de forma segura (Local o Google Colab)
def load_dataset(filename, module_name="08 - Classification"):
    candidates = [
        f"data/{filename}",
        f"{module_name}/data/{filename}",
        filename
    ]
    for path in candidates:
        if os.path.exists(path):
            return path
            
    os.makedirs("data", exist_ok=True)
    target_path = f"data/{filename}"
    encoded_module = urllib.parse.quote(module_name)
    encoded_file = urllib.parse.quote(filename)
    url_main = f"https://raw.githubusercontent.com/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/main/{encoded_module}/data/{encoded_file}"
    url_master = f"https://raw.githubusercontent.com/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/master/{encoded_module}/data/{encoded_file}"
    
    print(f"📥 Descargando dataset '{filename}' desde el repositorio oficial...")
    try:
        urllib.request.urlretrieve(url_main, target_path)
    except Exception:
        urllib.request.urlretrieve(url_master, target_path)
    print(f"✅ Dataset '{filename}' cargado exitosamente.")
    return target_path

print("✅ Entorno preparado exitosamente para el Módulo 08: Clasificación.")
print(f"📦 Versiones: Scikit-Learn {sklearn.__version__} | Pandas {pd.__version__} | NumPy {np.__version__}")
```

---
## 2. Demostración Visual: ¿Por qué la Regresión Lineal OLS falla en Clasificación? ⚠️

Si intentamos ajustar una recta de mínimos cuadrados ordinarios $\hat{y} = \beta_0 + \beta_1 x$ para modelar probabilidades:
1. **Predicciones Inválidas:** Produce probabilidades fuera del rango axiomático: $\hat{y} < 0$ o $\hat{y} > 1$.
2. **Sensibilidad a Valores Atípicos (*Outliers*):** Observaciones alejadas distorsionan la pendiente y desplazan el umbral de decisión.

```python
np.random.seed(42)
x_normal = np.linspace(10, 50, 25)
y_normal = (x_normal > 30).astype(int)

# Añadimos un valor extremo (outlier) con y=1 en x=120
x_outlier = np.append(x_normal, [105, 120])
y_outlier = np.append(y_normal, [1, 1])

# Ajustes OLS
b1_norm, b0_norm = np.polyfit(x_normal, y_normal, 1)
b1_out, b0_out = np.polyfit(x_outlier, y_outlier, 1)

fig, ax = plt.subplots(1, 2, figsize=(14, 4.5))

ax[0].scatter(x_normal, y_normal, color='#0284c7', s=55, edgecolors='black', label=r'Datos reales ($y \in \{0, 1\}$)')
ax[0].plot(x_normal, b0_norm + b1_norm * x_normal, color='#dc2626', lw=2.5, label='Recta OLS')
ax[0].axhline(0.5, color='gray', linestyle='--', label='Umbral $\tau = 0.5$')
ax[0].set_title("Regresión Lineal en Datos Binarios (Sin Outliers)", fontweight='bold')
ax[0].set_xlabel("Biomarcador ($x$)")
ax[0].set_ylabel("Probabilidad Estimada")
ax[0].legend()

ax[1].scatter(x_outlier, y_outlier, color='#0284c7', s=55, edgecolors='black', label='Datos con Outliers')
ax[1].plot(x_outlier, b0_out + b1_out * x_outlier, color='#dc2626', lw=2.5, label='Recta OLS Desplazada')
ax[1].axhline(0.5, color='gray', linestyle='--', label='Umbral $\tau = 0.5$')
ax[1].set_title("Distorsión Severa del Umbral por Outliers", fontweight='bold')
ax[1].set_xlabel("Biomarcador ($x$)")
ax[1].legend()

plt.tight_layout()
plt.show()
```

---
## 3. La Solución: La Función Sigmoide Logística (*Logistic Function*) 📐

Para mapear la combinación lineal $z = \mathbf{w}^T \mathbf{x} + b \in \mathbb{R}$ estrictamente dentro del intervalo de probabilidad $(0, 1)$, aplicamos la **Función Sigmoide**:

$$\sigma(z) = \frac{1}{1 + e^{-z}} = \frac{e^z}{1 + e^z}$$

### Propiedades Fundamentales:
* $\lim_{z \to +\infty} \sigma(z) = 1$
* $\lim_{z \to -\infty} \sigma(z) = 0$
* $\sigma(0) = 0.5$ (Punto de inflexión simétrico)
* Derivada cerrada: $\sigma'(z) = \sigma(z)(1 - \sigma(z))$

```python
z = np.linspace(-7, 7, 200)
sigma_z = 1 / (1 + np.exp(-z))

plt.figure(figsize=(8.5, 4.2))
plt.plot(z, sigma_z, color='#7c3aed', lw=3, label=r'$\sigma(z) = \frac{1}{1 + e^{-z}}$')
plt.axhline(0.5, color='#f59e0b', linestyle='--', label='Punto de Inflexión (p = 0.5)')
plt.axvline(0, color='gray', linestyle=':', alpha=0.7)
plt.title(r"Función Sigmoide Logística: Mapeo de $\mathbb{R} \to (0, 1)$", fontsize=12, fontweight='bold')
plt.xlabel("Combinación Lineal: $z = \beta_0 + \beta_1 x$")
plt.ylabel(r"Probabilidad: $P(Y=1 \mid X)$")
plt.legend()
plt.show()
```

---
##### 🛠️ Práctica 0: Demostración Numérica del Falso Rango de OLS frente a la Sigmoide

**Objetivo:** Comparar matemáticamente las predicciones generadas por una recta de regresión lineal frente a un modelo logístico en valores normales y valores extremos.

**Instrucciones:**
1. Define un conjunto de biomarcadores $x = [5, 25, 45, 65, 85, 120, 150]$.
2. Con los coeficientes ajustados de OLS ($b_0 = -0.22, b_1 = 0.024$), calcula las predicciones lineales $\hat{y}_{ols} = b_0 + b_1 x$.
3. Con una función sigmoide ($z = -3.0 + 0.08 x$), calcula las probabilidades $\hat{y}_{log} = \sigma(z)$.
4. Imprime una tabla comparativa y resalta los valores inválidos ($\hat{y} < 0$ o $\hat{y} > 1$).

```python
# =========================================================================
# TU SOLUCIÓN: Práctica 0 - Demostración Numérica OLS vs Sigmoide
# =========================================================================

# 1. Definir valores de prueba
# x_test_vals = np.array([5, 25, 45, 65, 85, 120, 150])

# 2. Predicciones lineales OLS
# y_ols = ...

# 3. Predicciones logísticas Sigmoide
# z_vals = ...
# y_log = ...

# 4. Construir y mostrar DataFrame comparativo
# df_reto0 = pd.DataFrame({...})
# display(df_reto0)
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
x_test_vals = np.array([5, 25, 45, 65, 85, 120, 150])

# 1. Predicciones OLS
b0_ols, b1_ols = -0.22, 0.024
y_ols = b0_ols + b1_ols * x_test_vals

# 2. Predicciones Sigmoide
z_vals = -3.0 + 0.08 * x_test_vals
y_log = 1 / (1 + np.exp(-z_vals))

# 3. Tabla comparativa
df_reto0 = pd.DataFrame({
    'Biomarcador (x)': x_test_vals,
    'Predicción OLS': y_ols.round(4),
    '¿Válido en OLS?': ['✅ Válido' if 0 <= val <= 1 else '❌ INVÁLIDO' for val in y_ols],
    'Predicción Sigmoide': y_log.round(4),
    '¿Válido en Sigmoide?': ['✅ Válido (0, 1)' for _ in y_log]
})

print("=" * 60)
print("📊 COMPARACIÓN NUMÉRICA: OLS LINEAL vs SIGMOIDE LOGÍSTICA")
print("=" * 60)
display(df_reto0)
```
</details>

---
### 4. Resumen y Conclusiones del Cuaderno 00 📌

1. **Naturaleza Categórica:** La clasificación modela variables cualitativas discretas estimando probabilidades a posteriori $P(Y=1|X)$.
2. **Falla de OLS en Clasificación:** La regresión lineal genera valores de probabilidad imposibles ($<0$ o $>1$) y es altamente susceptible a valores atípicos distantes.
3. **Función Sigmoide $\sigma(z)$:** Mapea el espacio $\mathbb{R} \to (0, 1)$, garantizando probabilidades válidas y matemáticamente coherentes.

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos</i>
  </p>
</div>
