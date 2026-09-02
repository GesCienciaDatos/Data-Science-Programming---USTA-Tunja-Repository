# 03_Particion_y_Estrategias_de_Validacion

<table style="width: 100%; border-collapse: collapse; border: none; background: #f8fafc; border-left: 6px solid #1e3a8a; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #0f172a; font-size: 2.1em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        Partición y Estrategias de Validación Cruzada 🧪
      </h1>
      <p style="margin: 6px 0 0 0; color: #1e3a8a; font-size: 1.15em; font-weight: 600; font-family: system-ui, -apple-system, sans-serif;">
        Especialización en Ciencia de Datos | Minería de Datos (Data Mining)
      </p>
      <p style="margin: 4px 0 0 0; color: #64748b; font-size: 0.95em; font-family: system-ui, -apple-system, sans-serif;">
        Universidad Santo Tomás — Seccional Tunja
      </p>
    </td>
    <td style="text-align: right; vertical-align: middle; border: none; padding: 15px 20px; width: 30%;">
      <span style="background: #1e3a8a; color: #ffffff; padding: 6px 14px; border-radius: 20px; font-size: 0.85em; font-weight: 700; display: inline-block; margin-bottom: 8px;">
        Módulo 03
      </span><br>
      <span style="color: #64748b; font-size: 0.85em;">Docente: Santiago A. Zúñiga M.</span><br>
      <a href="mailto:gestorvirtualcienciadatos@ustatunja.edu.co" style="color: #2563eb; font-size: 0.8em; text-decoration: none; font-weight: 500;">gestorvirtualcienciadatos@ustatunja.edu.co</a>
    </td>
  </tr>
</table>

<div align="center" style="margin-top: 15px; margin-bottom: 15px;">
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Mining/Sckit%20Learn/03_Particion_y_Estrategias_de_Validacion.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

```python
# Configuración del entorno interactivo
try:
    from IPython.core.interactiveshell import InteractiveShell
    InteractiveShell.ast_node_interactivity = "all"
except ImportError:
    pass

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn

print(f"🚀 Entorno listo con Scikit-Learn versión: {sklearn.__version__}")
```

---
## Objetivos de Aprendizaje 🎯

En este cuaderno aprenderás a evaluar y validar modelos cuantitativamente mediante `sklearn.model_selection` y `sklearn.metrics`:

* **1. Partición Train/Test:** Partición estratificada con `train_test_split` y control de aleatoriedad.
* **2. Validación Cruzada ($K$-Fold):** `KFold`, `StratifiedKFold`, `TimeSeriesSplit` y `GroupKFold`.
* **3. Métricas de Clasificación:** Matriz de confusión, *Accuracy*, *Precision*, *Recall*, *F1-Score*, *ROC-AUC*.
* **4. Métricas de Regresión:** *MSE*, *RMSE*, *MAE*, $R^2$.
* **5. Automatización:** Evaluación multifactorial con `cross_val_score` y `cross_validate`.

---
### 1. Partición de Datos y Validación Cruzada Estratificada 🔄

$$\text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN}, \quad \text{Precision} = \frac{TP}{TP + FP}, \quad \text{Recall} = \frac{TP}{TP + FN}, \quad F_1 = 2 \cdot \frac{P \cdot R}{P + R}$$

```python
from sklearn.model_selection import train_test_split, StratifiedKFold
from sklearn.datasets import load_breast_cancer
from sklearn.metrics import classification_report, confusion_matrix

cancer = load_breast_cancer(as_frame=True)
X, y = cancer.data, cancer.target

# Partición 80/20 Estratificada
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, stratify=y, random_state=42
)

print(f"Muestras Train: {len(X_train)} | Muestras Test: {len(X_test)}")
print(f"Prevalencia Clase Positiva en Train: {y_train.mean():.4f}")
print(f"Prevalencia Clase Positiva en Test : {y_test.mean():.4f}")
```

---
#### 🛠️ Práctica: Partición y Validación de Modelos

**Ejercicio 1:**
Simula etiquetas reales `y_true = [1, 0, 1, 1, 0, 1, 0, 0, 1, 0]` y predicciones `y_pred = [1, 0, 1, 0, 0, 1, 1, 0, 1, 0]`. Calcula la matriz de confusión, precisión, recall y f1-score usando `sklearn.metrics`.

```python
# Ejercicio 1
# Escribe tu código aquí
from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score

y_true = [1, 0, 1, 1, 0, 1, 0, 0, 1, 0]
y_pred = [1, 0, 1, 0, 0, 1, 1, 0, 1, 0]

# cm = ...
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
# Solución Ejercicio 1
cm = confusion_matrix(y_true, y_pred)
p = precision_score(y_true, y_pred)
r = recall_score(y_true, y_pred)
f1 = f1_score(y_true, y_pred)

print("Matriz de Confusión:\n", cm)
print(f"Precision : {p:.4f}")
print(f"Recall    : {r:.4f}")
print(f"F1-Score  : {f1:.4f}")
```
</details>

**Ejercicio 2:**
En problemas de series temporales, las observaciones futuras no deben usarse para predecir el pasado. Instancia un `TimeSeriesSplit(n_splits=3)` sobre 10 periodos y muestra los índices asignados a cada fold.

```python
# Ejercicio 2
# Escribe tu código aquí
from sklearn.model_selection import TimeSeriesSplit

periodos = np.arange(1, 11)

# tscv = TimeSeriesSplit(n_splits=3)
# ...
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
# Solución Ejercicio 2
tscv = TimeSeriesSplit(n_splits=3)
for fold, (tr_idx, te_idx) in enumerate(tscv.split(periodos)):
    print(f"Fold {fold+1} -> Train: {periodos[tr_idx]} | Test: {periodos[te_idx]}")
```
</details>

---
### Resumen y Preguntas de Autoevaluación 🧠

1. **¿Por qué la estratificación es crítica en clasificación desbalanceada?**  
   *Respuesta:* Porque asegura que cada subconjunto (train, test o fold) mantenga la proporción exacta de clases positivas y negativas de la población general.
2. **¿Cuándo se debe priorizar Recall sobre Precision?**  
   *Respuesta:* En problemas donde omitir un caso positivo es crítico (ej. diagnóstico de enfermedades o detección de fraude), tolerando más falsas alarmas con tal de no perder positivos reales.
3. **¿Por qué no se debe usar K-Fold estándar en series de tiempo?**  
   *Respuesta:* Porque violaría la causalidad temporal al entrenar con datos del futuro para predecir el pasado (*Look-ahead bias*).

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Minería de Datos (Data Mining)</i>
  </p>
</div>
