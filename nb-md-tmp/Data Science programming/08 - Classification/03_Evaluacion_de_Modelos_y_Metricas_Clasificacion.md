# 03_Evaluacion_de_Modelos_y_Metricas_Clasificacion

<table style="width: 100%; border-collapse: collapse; border: none; background: #f8fafc; border-left: 6px solid #1e3a8a; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #0f172a; font-size: 2.1em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        Evaluación de Modelos y Métricas de Clasificación 🎯
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
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/08%20-%20Classification/03_Evaluacion_de_Modelos_y_Metricas_Clasificacion.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
### 1. La Matriz de Confusión (*Confusion Matrix*) 📊

En problemas de clasificación, la **Exactitud (*Accuracy*)** puede resultar engañosa ante clases desbalanceadas. La **Matriz de Confusión** desglosa el rendimiento en cuatro cuadrantes fundamentales:

| | Predicción Negativa ($\hat{Y}=0$) | Predicción Positiva ($\hat{Y}=1$) |
|---|:---:|:---:|
| **Real Negativo ($Y=0$)** | **Verdadero Negativo (TN)** | **Falso Positivo (FP)** *(Error Tipo I)* |
| **Real Positivo ($Y=1$)** | **Falso Negativo (FN)** *(Error Tipo II)* | **Verdadero Positivo (TP)** |

---
### 2. Definiciones Matemáticas de las Métricas Clave 📐

1. **Exactitud (*Accuracy*):** $\text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN}$
2. **Precisión (*Precision / PPV*):** $\text{Precision} = \frac{TP}{TP + FP}$
3. **Exhaustividad / Sensibilidad (*Recall / TPR*):** $\text{Recall} = \frac{TP}{TP + FN}$
4. **Especificidad (*Specificity / TNR*):** $\text{Specificity} = \frac{TN}{TN + FP} \quad \implies \quad \text{FPR} = 1 - \text{Specificity} = \frac{FP}{TN + FP}$
5. **$F_1$-Score (Media Armónica):** $F_1 = 2 \cdot \frac{\text{Precision} \cdot \text{Recall}}{\text{Precision} + \text{Recall}}$

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
### 3. Carga y Modelado en el Dataset de Retención de Clientes (`customer_churn.csv`) 📂

```python
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (confusion_matrix, ConfusionMatrixDisplay,
                             classification_report, roc_curve, auc,
                             precision_recall_curve)

# Cargar dataset
file_path = load_dataset('customer_churn.csv', '08 - Classification')
df_churn = pd.read_csv(file_path)

display(df_churn.head())
print("Distribución de la clase Churn (Fuga):")
print(df_churn['churn'].value_counts(normalize=True))
```

---
### 4. Matriz de Confusión Gráfica y Reporte de Clasificación 📈

```python
# Preprocesamiento y división
df_enc = pd.get_dummies(df_churn, columns=['contract'], drop_first=True)
X = df_enc.drop(columns=['churn'])
y = df_enc['churn']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=42, stratify=y
)

model = LogisticRegression(max_iter=1000, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
y_proba = model.predict_proba(X_test)[:, 1]

# Matriz de Confusión
cm = confusion_matrix(y_test, y_pred)
fig, ax = plt.subplots(figsize=(5.5, 4.5))
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['No Churn (0)', 'Churn (1)'])
disp.plot(cmap='Blues', ax=ax, values_format='d')
plt.title("Matriz de Confusión: Detección de Fuga de Clientes", fontweight='bold')
plt.grid(False)
plt.show()

print("\nReporte de Clasificación Detallado:")
print(classification_report(y_test, y_pred, target_names=['No Churn', 'Churn']))
```

---
### 5. Curva ROC (*Receiver Operating Characteristic*) y Área Bajo la Curva (**AUC-ROC**) 📉

La curva ROC evalúa la capacidad discriminativa del modelo en todos los umbrales de decisión $\tau \in [0, 1]$ posibles.
* **$AUC = 0.5$:** Modelo sin capacidad discriminativa (equivalente al azar).
* **$AUC = 1.0$:** Clasificador perfecto.

```python
fpr, tpr, thresholds = roc_curve(y_test, y_proba)
roc_auc = auc(fpr, tpr)

plt.figure(figsize=(7.5, 5))
plt.plot(fpr, tpr, color='#0284c7', lw=2.5, label=f'Curva ROC (AUC = {roc_auc:.3f})')
plt.plot([0, 1], [0, 1], color='gray', linestyle='--', label='Azar (AUC = 0.50)')
plt.xlim([-0.02, 1.02])
plt.ylim([-0.02, 1.02])
plt.xlabel('Tasa de Falsos Positivos (1 - Especificidad)')
plt.ylabel('Tasa de Verdaderos Positivos (Sensibilidad / Recall)')
plt.title('Curva ROC - Capacidad de Separabilidad Global', fontweight='bold')
plt.legend(loc='lower right')
plt.show()
```

---
### 6. Calibración Óptima del Umbral de Decisión con el Índice de Youden 🎯

```python
# Índice de Youden: J = TPR - FPR
youden_j = tpr - fpr
opt_idx = np.argmax(youden_j)
opt_tau = thresholds[opt_idx]

print(f"Umbral óptimo según Youden: τ = {opt_tau:.4f}")
print(f"En este umbral -> Sensibilidad: {tpr[opt_idx]:.4f} | Especificidad: {1 - fpr[opt_idx]:.4f}")
```

---
##### 🛠️ Práctica 3: Compensación Precisión-Recall (*Precision-Recall Tradeoff*) y Curva PR

**Contexto:** En detección de clientes en riesgo de cancelación, a menudo nos interesa asegurar un **Recall mínimo del 85%** sin degradar excesivamente la Precisión.

**Instrucciones:**
1. Calcula la curva Precision-Recall usando `precision_recall_curve(y_test, y_proba)`.
2. Encuentra el umbral $\tau$ que garantiza un **Recall $\ge 0.85$** con la mayor Precisión posible.
3. Grafica simultáneamente la Precisión y el Recall en función del umbral $\tau \in [0.1, 0.9]$.
4. Evalúa la nueva Matriz de Confusión aplicando dicho umbral calibrado.

```python
# =========================================================================
# TU SOLUCIÓN: Práctica 3 - Precision-Recall Tradeoff y Calibración
# =========================================================================

# 1. Curva Precision-Recall
# precisions, recalls, pr_thresholds = precision_recall_curve(...)

# 2. Identificar umbral con Recall >= 0.85
# idx_target = ...
# target_tau = ...

# 3. Graficar Precision y Recall vs Umbral
# plt.figure(...)
# ...

# 4. Matriz de confusión calibrada
# y_pred_calibrated = (y_proba >= target_tau).astype(int)
# cm_calibrated = confusion_matrix(y_test, y_pred_calibrated)
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
precisions, recalls, pr_thresholds = precision_recall_curve(y_test, y_proba)

# 1. Encontrar umbral donde Recall >= 0.85 con mayor Precision
valid_indices = np.where(recalls[:-1] >= 0.85)[0]
best_pr_idx = valid_indices[np.argmax(precisions[:-1][valid_indices])]
target_tau = pr_thresholds[best_pr_idx]

print("=" * 65)
print(f"🎯 UMBRAL CALIBRADO PARA RECALL >= 85%: τ = {target_tau:.4f}")
print(f"• Sensibilidad (Recall) alcanzada: {recalls[best_pr_idx]*100:.2f}%")
print(f"• Precisión correspondiente:       {precisions[best_pr_idx]*100:.2f}%")
print("=" * 65)

# 2. Visualización de curvas Precision y Recall vs Umbral
plt.figure(figsize=(8.5, 4.5))
plt.plot(pr_thresholds, precisions[:-1], color='#0284c7', lw=2.5, label='Precisión')
plt.plot(pr_thresholds, recalls[:-1], color='#10b981', lw=2.5, label='Sensibilidad (Recall)')
plt.axvline(target_tau, color='#dc2626', linestyle='--', label=f'Umbral Elegido (τ = {target_tau:.2f})')
plt.title('Compromiso Precisión-Recall en función del Umbral de Decisión', fontweight='bold')
plt.xlabel('Umbral de Probabilidad (τ)')
plt.ylabel('Puntaje de la Métrica')
plt.legend()
plt.show()

# 3. Matriz de confusión con umbral calibrado
y_pred_calib = (y_proba >= target_tau).astype(int)
cm_calib = confusion_matrix(y_test, y_pred_calib)

fig, ax = plt.subplots(figsize=(5.5, 4.5))
ConfusionMatrixDisplay(cm_calib, display_labels=['No Churn (0)', 'Churn (1)']).plot(cmap='Greens', ax=ax, values_format='d')
plt.title(f"Matriz de Confusión Calibrada (τ = {target_tau:.2f})", fontweight='bold')
plt.grid(False)
plt.show()
```
</details>

---
### 7. Resumen y Conclusiones del Cuaderno 03 📌

1. **Más allá de la Exactitud:** En conjuntos de datos desbalanceados, evaluar Precisión, Recall y $F_1$-score es indispensable para no enmascarar errores críticos.
2. **Curva ROC-AUC:** Evalúa la robustez del modelo independientemente de la escala o umbral seleccionado ($AUC > 0.8$ denota buena discriminación).
3. **Calibración de Umbrales:** Ajustar $\tau$ mediante Youden o la curva PR permite alinear las predicciones con los costos asimétricos del negocio.

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos</i>
  </p>
</div>
