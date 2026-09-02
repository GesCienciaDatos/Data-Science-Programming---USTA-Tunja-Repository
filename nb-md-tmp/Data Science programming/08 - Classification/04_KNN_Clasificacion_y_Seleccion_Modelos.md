# 04_KNN_Clasificacion_y_Seleccion_Modelos

<table style="width: 100%; border-collapse: collapse; border: none; background: #f8fafc; border-left: 6px solid #1e3a8a; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #0f172a; font-size: 2.1em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        k-NN Clasificación y Selección de Modelos 🎯
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
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/08%20-%20Classification/04_KNN_Clasificacion_y_Seleccion_Modelos.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
### 1. El Algoritmo no Paramétrico $k$-Nearest Neighbors ($k$-NN) 👥

El algoritmo **$k$-Nearest Neighbors** es un método de aprendizaje no paramétrico y basado en instancias (*Instance-Based / Lazy Learning*). No asume una forma funcional fija sobre los datos.

#### Principio de Votación Mayoritaria:
Para clasificar un nuevo punto de consulta $\mathbf{x}_0$:
1. Calcula la distancia métrica $d(\mathbf{x}_0, \mathbf{x}_i)$ a todas las observaciones de entrenamiento.
2. Encuentra los $k$ vecinos más cercanos $\mathcal{N}_0$.
3. Asigna la clase mayoritaria:

$$P(Y = j \mid \mathbf{x}_0) = \frac{1}{k} \sum_{i \in \mathcal{N}_0} \mathbb{I}(y_i = j)$$

---
### 2. Métricas de Distancia en $\mathbb{R}^p$ y la Necesidad Crítica de `StandardScaler` 📏
* **Euclidiana ($L_2$):** $d(\mathbf{u}, \mathbf{v}) = \sqrt{\sum_{j=1}^p (u_j - v_j)^2}$
* **Manhattan ($L_1$):** $d(\mathbf{u}, \mathbf{v}) = \sum_{j=1}^p |u_j - v_j|$

> ⚠️ **REGLA IMPERATIVA:** Si las variables tienen escalas distintas (ej. Salario de millones vs Edad en decenas), la distancia quedará dominada por la variable mayor. **El escalado (`StandardScaler`) es obligatorio en $k$-NN**.

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
### 3. Demostración Práctica: $k$-NN SIN Escalado vs CON `StandardScaler` ⚖️

```python
from sklearn.model_selection import train_test_split, StratifiedKFold, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report, accuracy_score

file_path = load_dataset('heart_disease.csv', '08 - Classification')
df_h = pd.read_csv(file_path)

X = df_h.drop(columns=['target'])
y = df_h['target']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

# 1. k-NN SIN escalar
knn_raw = KNeighborsClassifier(n_neighbors=5)
knn_raw.fit(X_train, y_train)
acc_raw = accuracy_score(y_test, knn_raw.predict(X_test))

# 2. k-NN CON StandardScaler en Pipeline
knn_pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('knn', KNeighborsClassifier(n_neighbors=5))
])
knn_pipe.fit(X_train, y_train)
acc_pipe = accuracy_score(y_test, knn_pipe.predict(X_test))

print(f"Exactitud k-NN SIN Escalado:  {acc_raw*100:.2f}%")
print(f"Exactitud k-NN CON StandardScaler: {acc_pipe*100:.2f}%")
print(f"Ganancia de Rendimiento: +{(acc_pipe - acc_raw)*100:.2f}% gracias al escalado métrico.")
```

---
### 4. Compromiso Sesgo-Varianza y Elección del Hiperparámetro $k$ 📈

```python
k_values = range(1, 35, 2)
train_accs, test_accs = [], []

scaler = StandardScaler()
X_tr_s = scaler.fit_transform(X_train)
X_te_s = scaler.transform(X_test)

for k in k_values:
    clf = KNeighborsClassifier(n_neighbors=k)
    clf.fit(X_tr_s, y_train)
    train_accs.append(accuracy_score(y_train, clf.predict(X_tr_s)))
    test_accs.append(accuracy_score(y_test, clf.predict(X_te_s)))

plt.figure(figsize=(9, 4.5))
plt.plot(k_values, train_accs, marker='o', label='Exactitud Entrenamiento', color='#0284c7')
plt.plot(k_values, test_accs, marker='s', label='Exactitud Prueba (Generalización)', color='#10b981', lw=2.5)
plt.title('Dilema Sesgo-Varianza en función de k', fontweight='bold')
plt.xlabel('Número de Vecinos (k)')
plt.ylabel('Exactitud')
plt.xticks(list(k_values))
plt.legend()
plt.show()
```

---
### 5. Construcción de Pipeline Profesional y Búsqueda con `GridSearchCV` 🚀

```python
full_pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('knn', KNeighborsClassifier())
])

param_grid = {
    'knn__n_neighbors': [3, 5, 7, 9, 11, 15, 21],
    'knn__weights': ['uniform', 'distance'],
    'knn__metric': ['euclidean', 'manhattan']
}

cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

grid = GridSearchCV(full_pipe, param_grid, cv=cv, scoring='roc_auc', n_jobs=-1)
grid.fit(X_train, y_train)

print(f"Mejores Hiperparámetros: {grid.best_params_}")
print(f"Mejor ROC-AUC en Validación Cruzada: {grid.best_score_:.4f}")

best_knn = grid.best_estimator_
y_pred_opt = best_knn.predict(X_test)
print("\nReporte en Conjunto de Prueba:")
print(classification_report(y_test, y_pred_opt))
```

---
##### 🛠️ Práctica 4 (Gran Desafío Integrador): Benchmark Comparativo k-NN vs Regresión Logística

**Objetivo:** Desarrollar un banco de pruebas exhaustivo comparando el mejor modelo de **$k$-NN Optimizado** frente a una **Regresión Logística Regularizada (L2)** sobre el dataset `customer_churn.csv`.

**Instrucciones:**
1. Carga `customer_churn.csv`, aplica One-Hot Encoding a variables categóricas y separa Train (75%) y Test (25%) con `random_state=42`.
2. Ajusta un Pipeline de $k$-NN optimizado con `GridSearchCV(cv=5)`.
3. Ajusta un Pipeline de `LogisticRegression()` con `StandardScaler()`.
4. Evalúa ambos modelos sobre el conjunto de prueba independiente calculando: **ROC-AUC**, **$F_1$-Score** y **Exactitud**.
5. Muestra una tabla comparativa y justifica cuál desplegarías en producción.

```python
# =========================================================================
# TU SOLUCIÓN: Práctica 4 - Benchmark Comparativo k-NN vs Regresión Logística
# =========================================================================

# 1. Cargar y procesar datos
# df_churn_bench = pd.read_csv(load_dataset('customer_churn.csv', '08 - Classification'))
# df_bench_enc = pd.get_dummies(df_churn_bench, columns=['contract'], drop_first=True)
# X_b = df_bench_enc.drop(columns=['churn'])
# y_b = df_bench_enc['churn']

# 2. Train / Test Split
# X_tr_b, X_te_b, y_tr_b, y_te_b = train_test_split(X_b, y_b, test_size=0.25, random_state=42, stratify=y_b)

# 3. Modelos y Evaluación
# ...
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
from sklearn.metrics import roc_auc_score, f1_score

# 1. Cargar y preparar datos
df_churn_bench = pd.read_csv(load_dataset('customer_churn.csv', '08 - Classification'))
df_bench_enc = pd.get_dummies(df_churn_bench, columns=['contract'], drop_first=True)
X_b = df_bench_enc.drop(columns=['churn'])
y_b = df_bench_enc['churn']

X_tr_b, X_te_b, y_tr_b, y_te_b = train_test_split(
    X_b, y_b, test_size=0.25, random_state=42, stratify=y_b
)

# 2. Pipeline k-NN con GridSearchCV
pipe_knn = Pipeline([('scaler', StandardScaler()), ('knn', KNeighborsClassifier())])
grid_knn = GridSearchCV(pipe_knn, {'knn__n_neighbors': [5, 9, 15, 21], 'knn__weights': ['uniform', 'distance']}, cv=5, scoring='roc_auc')
grid_knn.fit(X_tr_b, y_tr_b)
best_knn_model = grid_knn.best_estimator_

# 3. Pipeline Regresión Logística
pipe_log = Pipeline([('scaler', StandardScaler()), ('log', LogisticRegression(C=1.0, random_state=42))])
pipe_log.fit(X_tr_b, y_tr_b)

# 4. Predicciones en Test
y_pred_knn = best_knn_model.predict(X_te_b)
y_prob_knn = best_knn_model.predict_proba(X_te_b)[:, 1]

y_pred_log = pipe_log.predict(X_te_b)
y_prob_log = pipe_log.predict_proba(X_te_b)[:, 1]

# 5. Tabla Resumen del Benchmark
df_benchmark = pd.DataFrame({
    'Modelo': ['k-Nearest Neighbors (Optimizado)', 'Regresión Logística (L2 Ridge)'],
    'Mejor Configuración': [str(grid_knn.best_params_), 'C=1.0, solver=lbfgs'],
    'Exactitud (Accuracy)': [accuracy_score(y_te_b, y_pred_knn), accuracy_score(y_te_b, y_pred_log)],
    'F1-Score (Clase Churn)': [f1_score(y_te_b, y_pred_knn), f1_score(y_te_b, y_pred_log)],
    'ROC-AUC': [roc_auc_score(y_te_b, y_prob_knn), roc_auc_score(y_te_b, y_prob_log)]
})

print("=" * 80)
print("🏆 TABLA COMPARATIVA FINAL DE RENDIMIENTO (BENCHMARK):")
print("=" * 80)
display(df_benchmark.round(4))
```
</details>

---
### 6. Resumen y Conclusiones del Cuaderno 04 📌

1. **Naturaleza no Paramétrica:** $k$-NN clasifica por parecido geométrico en lugar de ajustar coeficientes analíticos.
2. **Escalado Obligatorio:** Sin estandarización previa (`StandardScaler`), las variables de mayor rango distorsionan por completo el cálculo de distancias euclidianas.
3. **Optimización con Pipeline:** Encapsular transformadores y estimadores previene la fuga de información (*Data Leakage*) durante la validación cruzada con `GridSearchCV`.

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos</i>
  </p>
</div>
