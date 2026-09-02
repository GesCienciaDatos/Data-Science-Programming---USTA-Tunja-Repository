# 01_Regresion_Logistica_Simple_y_Multiple

<table style="width: 100%; border-collapse: collapse; border: none; background: #f8fafc; border-left: 6px solid #1e3a8a; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #0f172a; font-size: 2.1em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        Regresión Logística Simple y Múltiple 🎯
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
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/08%20-%20Classification/01_Regresion_Logistica_Simple_y_Multiple.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
### 1. ¿Qué es la Regresión Logística? 🧠

La **Regresión Logística (*Logistic Regression*)** es el modelo lineal clásico por excelencia para problemas de **clasificación binaria** ($y \in \{0, 1\}$). A pesar de conservar la denominación histórica de "regresión", su función objetivo es modelar la probabilidad condicional a posteriori:

$$p(X) = P(Y = 1 \mid X)$$

---
### 2. Formulación Matemática del Modelo Logit y Razón de Momios (*Odds Ratio*) 📐

Para transformar la probabilidad $p(X) \in (0, 1)$ a la escala lineal de los números reales $\mathbb{R}$, aplicamos la transformación **Logit** (logaritmo de la razón de momios o *log-odds*):

$$\text{logit}(p) = \ln\left(\frac{p(X)}{1 - p(X)}\right) = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \dots + \beta_p x_p = \mathbf{w}^T \mathbf{x} + b$$

Despejando la probabilidad $p(X)$ obtenemos la expresión sigmoidal cerrada:

$$p(X) = \sigma(\mathbf{w}^T \mathbf{x} + b) = \frac{1}{1 + e^{-(\mathbf{w}^T \mathbf{x} + b)}}$$

#### 🎲 Concepto de Odds y Odds Ratio ($e^{\beta_j}$):
* **Odds (*Razón de Momios*):** $\text{Odds} = \frac{p}{1-p}$. Si $p = 0.75$, $\text{Odds} = \frac{0.75}{0.25} = 3$ (la probabilidad a favor es el triple que en contra).
* **Odds Ratio (OR):** $e^{\beta_j}$ representa el cambio multiplicativo en las odds por cada incremento unitario en la variable $x_j$, manteniendo constantes los demás predictores (*ceteris paribus*).

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
### 3. Carga y Exploración del Dataset de Riesgo Cardiovascular (`heart_disease.csv`) 📊

```python
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Cargar dataset
file_path = load_dataset('heart_disease.csv', '08 - Classification')
df_heart = pd.read_csv(file_path)

display(df_heart.head())
print("Dimensiones del dataset:", df_heart.shape)
print("Distribución de la clase objetivo (0: Sano, 1: Cardiopatía):")
print(df_heart['target'].value_counts(normalize=True))
```

---
### 4. Regresión Logística Simple (Univariada) 📈

Modelamos el riesgo cardiaco en función exclusivamente de la frecuencia cardiaca máxima (`thalach`).

```python
X_simple = df_heart[['thalach']]
y_simple = df_heart['target']

X_train, X_test, y_train, y_test = train_test_split(
    X_simple, y_simple, test_size=0.25, random_state=42, stratify=y_simple
)

# Ajuste con regularización mínima para ver parámetros puros
model_simple = LogisticRegression(C=1e5, solver='lbfgs')
model_simple.fit(X_train, y_train)

b0 = model_simple.intercept_[0]
b1 = model_simple.coef_[0][0]
or_val = np.exp(b1)

print(f"Intersección (β₀): {b0:.4f}")
print(f"Pendiente (β₁):    {b1:.4f}")
print(f"Odds Ratio (e^β₁): {or_val:.4f} (Factor multiplicativo por cada lpm adicional)")
```

```python
# Visualización de la sigmoide ajustada
x_grid = np.linspace(df_heart['thalach'].min() - 5, df_heart['thalach'].max() + 5, 300).reshape(-1, 1)
y_probs = model_simple.predict_proba(x_grid)[:, 1]

plt.figure(figsize=(9, 4.5))
plt.scatter(X_train, y_train, color='#0284c7', alpha=0.45, s=50, edgecolors='k', label='Datos Entrenamiento')
plt.plot(x_grid, y_probs, color='#dc2626', lw=2.8, label=r'Sigmoide Ajustada: $P(Y=1 \mid thalach)$')
plt.axhline(0.5, color='gray', linestyle='--', label='Umbral Estándar ($	au = 0.5$)')
plt.title("Curva de Probabilidad Logística Simple: Frecuencia Cardiaca vs Riesgo", fontweight='bold')
plt.xlabel("Frecuencia Cardiaca Máxima (thalach)")
plt.ylabel("Probabilidad Estimada")
plt.legend()
plt.show()
```

---
### 5. Regresión Logística Múltiple (Multivariada) y Función de Pérdida Log-Loss 🧮

En la práctica clínica, combinamos múltiples predictores: `age`, `sex`, `trestbps`, `chol`, `thalach`, `oldpeak`.

#### Función de Pérdida (*Binary Cross-Entropy / Log-Loss*):
$$\mathcal{L}(\mathbf{w}, b) = -\frac{1}{N} \sum_{i=1}^N \left[ y_i \ln(p_i) + (1 - y_i) \ln(1 - p_i) \right]$$

```python
features = ['age', 'sex', 'trestbps', 'chol', 'thalach', 'oldpeak']
X_mult = df_heart[features]
y_mult = df_heart['target']

X_tr_m, X_te_m, y_tr_m, y_te_m = train_test_split(
    X_mult, y_mult, test_size=0.25, random_state=42, stratify=y_mult
)

model_multi = LogisticRegression(max_iter=1000, random_state=42)
model_multi.fit(X_tr_m, y_tr_m)

coef_summary = pd.DataFrame({
    'Variable': features,
    'Coeficiente (β)': model_multi.coef_[0],
    'Odds Ratio (e^β)': np.exp(model_multi.coef_[0]),
    'Efecto Clínico': ['Riesgo Aumentado (+)' if c > 0 else 'Factor Protector (-)' for c in model_multi.coef_[0]]
}).sort_values(by='Odds Ratio (e^β)', ascending=False)

display(coef_summary)
```

---
### 6. Probabilidades vs Clases Predichas (`predict_proba` vs `predict`) y Calibración de Umbral $\tau$ ⚖️

```python
probs_test = model_multi.predict_proba(X_te_m)[:, 1]
preds_50 = (probs_test >= 0.5).astype(int)
preds_30 = (probs_test >= 0.3).astype(int)

df_comparison = pd.DataFrame({
    'P(Y=1)': probs_test[:10].round(4),
    'Pred (τ=0.5)': preds_50[:10],
    'Pred (τ=0.3)': preds_30[:10],
    'Real': y_te_m.values[:10]
})
display(df_comparison)
```

---
##### 🛠️ Práctica 1: Modelado de Retención de Clientes (*Customer Churn*) con Odds Ratio

**Contexto:** En el sector de telecomunicaciones, predecir qué clientes cancelarán su servicio (`churn = 1`) permite desplegar campañas de fidelización preventivas.

**Instrucciones:**
1. Carga el dataset `customer_churn.csv` utilizando `load_dataset('customer_churn.csv')`.
2. Define las variables numéricas explicativas: `features = ['tenure', 'monthly_charges', 'support_calls']` y la variable objetivo `y = df_churn['churn']`.
3. Divide los datos en Train (75%) y Test (25%) con `random_state=42` y `stratify=y`.
4. Ajusta un modelo `LogisticRegression(random_state=42)`.
5. Construye una tabla con los Coeficientes $(\beta)$ y los **Odds Ratios** ($e^\beta$).
6. Responde: ¿Qué variable ejerce la mayor presión de abandono en el cliente?

```python
# =========================================================================
# TU SOLUCIÓN: Práctica 1 - Modelo Predictivo de Churn
# =========================================================================

# 1. Cargar datos
# file_churn = load_dataset('customer_churn.csv', '08 - Classification')
# df_churn_pr = pd.read_csv(file_churn)

# 2. Definir variables X e y
# features_churn = ['tenure', 'monthly_charges', 'support_calls']
# X_churn = ...
# y_churn = ...

# 3. Train / Test Split
# X_tr_c, X_te_c, y_tr_c, y_te_c = ...

# 4. Ajuste del modelo
# log_churn = ...

# 5. Tabla de Odds Ratio
# df_or = pd.DataFrame({...})
# display(df_or)
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
# 1. Cargar datos
file_churn = load_dataset('customer_churn.csv', '08 - Classification')
df_churn_pr = pd.read_csv(file_churn)

# 2. Definir variables X e y
features_churn = ['tenure', 'monthly_charges', 'support_calls']
X_churn = df_churn_pr[features_churn]
y_churn = df_churn_pr['churn']

# 3. Train / Test Split
X_tr_c, X_te_c, y_tr_c, y_te_c = train_test_split(
    X_churn, y_churn, test_size=0.25, random_state=42, stratify=y_churn
)

# 4. Ajuste del modelo
log_churn = LogisticRegression(random_state=42)
log_churn.fit(X_tr_c, y_tr_c)

# 5. Tabla de Odds Ratio
df_or = pd.DataFrame({
    'Predictor': features_churn,
    'Coeficiente (β)': log_churn.coef_[0],
    'Odds Ratio (e^β)': np.exp(log_churn.coef_[0]),
    'Interpretación': ['Mayor antigüedad retiene al cliente (OR < 1)' if c < 0 else 'Aumenta riesgo de cancelación (OR > 1)' for c in log_churn.coef_[0]]
}).sort_values(by='Odds Ratio (e^β)', ascending=False)

print("=" * 65)
print("📊 RESULTADOS DEL MODELO DE CHURN (ODDS RATIOS):")
print("=" * 65)
display(df_or)

# Exactitud en Test
acc_churn = log_churn.score(X_te_c, y_te_c)
print(f"
Exactitud global en conjunto de prueba: {acc_churn*100:.2f}%")
```
</details>

---
### 7. Resumen y Conclusiones del Cuaderno 01 📌

1. **Transformación Logit:** Modela el log-odds de la probabilidad, convirtiendo un problema de rango acotado $(0, 1)$ en una combinación lineal sobre $\mathbb{R}$.
2. **Odds Ratio ($e^{\beta_j}$):** Permite cuantificar el efecto marginal de cada predictor: $OR > 1$ indica incremento del riesgo, mientras que $OR < 1$ señala un factor protector.
3. **Calibración de Umbral:** Modificar $\tau$ permite alinear el modelo con las prioridades del negocio (ej. aumentar la detección de casos positivos reduciendo $\tau$).

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos</i>
  </p>
</div>
