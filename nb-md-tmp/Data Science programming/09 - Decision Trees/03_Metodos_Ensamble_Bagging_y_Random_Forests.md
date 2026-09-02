# 03_Metodos_Ensamble_Bagging_y_Random_Forests

<table style="width: 100%; border-collapse: collapse; border: none; background: #f8fafc; border-left: 6px solid #1e3a8a; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #0f172a; font-size: 2.1em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        Métodos de Ensamble: Bagging y Random Forests
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
        Módulo 09
      </span><br>
      <span style="color: #64748b; font-size: 0.85em;">Docente: Santiago A. Zúñiga M.</span><br>
      <a href="mailto:gestorvirtualcienciadatos@ustatunja.edu.co" style="color: #2563eb; font-size: 0.8em; text-decoration: none; font-weight: 500;">gestorvirtualcienciadatos@ustatunja.edu.co</a>
    </td>
  </tr>
</table>

<div align="center" style="margin-top: 15px; margin-bottom: 15px;">
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/09%20-%20Decision%20Trees/03_Metodos_Ensamble_Bagging_y_Random_Forests.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
### 1. El Dilema de los Árboles Individuales y el Principio de Ensamble 👥🌲

Un árbol de decisión individual sufre de **alta varianza e inestabilidad**: una pequeña perturbación en los datos de entrenamiento puede alterar drásticamente la estructura de todos los nodos subsiguientes.

Para superar esta limitación, surge el **Aprendizaje por Ensamble (*Ensemble Learning*)** basado en la *"Sabiduría de las Masas"* (*Wisdom of Crowds*):
> *"El promedio o voto mayoritario de un comité de modelos diversos e independientes supera sistemáticamente a cualquier modelo individual aislado."*

<div align="center">
  <table style="border:none; background:transparent;">
    <tr style="border:none;">
      <td style="border:none; text-align:center; padding:8px;">
        <img src="images/bias_variance.png" width="280" alt="Sesgo y Varianza" style="border-radius:8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);"/>
        <p style="font-size:0.8em; color:#64748b;"><b>Compensación Sesgo-Varianza</b></p>
      </td>
      <td style="border:none; text-align:center; padding:8px;">
        <img src="images/bagging_array.png" width="300" alt="Bagging" style="border-radius:8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);"/>
        <p style="font-size:0.8em; color:#64748b;"><b>Remuestreo Bootstrap en Paralelo</b></p>
      </td>
      <td style="border:none; text-align:center; padding:8px;">
        <img src="images/trees.png" width="260" alt="Bosque Aleatorio" style="border-radius:8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);"/>
        <p style="font-size:0.8em; color:#64748b;"><b>Comité de Árboles Descorrelacionados</b></p>
      </td>
    </tr>
  </table>
</div>

---
### 2. Bootstrap Aggregating (Bagging) y Error Out-of-Bag (OOB) 🎲

1. Genera $B$ muestras con reemplazo (*Bootstrap samples*) a partir del conjunto original de tamaño $N$.
2. Entrena un árbol profundo no restringido $f^{*b}(x)$ sobre cada muestra $b$.
3. Agrega las predicciones promediando (regresión) o por votación mayoritaria (clasificación):

$$\hat{f}_{\text{bag}}(x) = \frac{1}{B} \sum_{b=1}^B \hat{f}^{*b}(x)$$

* **Evaluación Out-of-Bag (OOB):** En promedio, cada muestra bootstrap omite aproximadamente el 36.8% de los datos ($1 - 1/e \approx 63.2\%$). Estas muestras excluidas permiten calcular una estimación no sesgada del error de generalización sin requerir un set de validación cruzada explícito (`oob_score=True`).

---
### 3. Random Forests: Descorrelación de Árboles con Subespacios Aleatorios 🌳

Si existe una variable muy dominante en el dataset, todos los árboles de Bagging la elegirán en el nodo raíz, generando árboles altamente correlacionados (limitando la reducción de varianza).

**Random Forests** introduce un segundo nivel de aleatoriedad:
* En cada división de nodo, solo se permite seleccionar la mejor variable entre un **subconjunto aleatorio de $m$ predictores**:
  * Para Clasificación: $m \approx \sqrt{p}$
  * Para Regresión: $m \approx p / 3$

#### Importancia de Características (*Feature Importance*):
Mide la reducción acumulada promedio de la impureza de Gini atribuible a cada característica en todo el bosque.

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os, urllib.request
import warnings
warnings.filterwarnings('ignore')

from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

sns.set_theme(style="whitegrid", palette="muted")
plt.rcParams['figure.figsize'] = (8.5, 4.5)
plt.rcParams['font.size'] = 10

def load_dataset(filename, module_folder="09 - Decision Trees"):
    local_path = os.path.join(os.getcwd(), "data", filename)
    if os.path.exists(local_path):
        return local_path
    
    parent_path = os.path.join(os.getcwd(), "..", module_folder, "data", filename)
    if os.path.exists(parent_path):
        return parent_path

    raw_url = f"https://raw.githubusercontent.com/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/main/Data%20Science%20programming/{module_folder.replace(' ', '%20')}/data/{filename}"
    os.makedirs("data", exist_ok=True)
    target_path = os.path.join("data", filename)
    if not os.path.exists(target_path):
        urllib.request.urlretrieve(raw_url, target_path)
    return target_path

print("🚀 Entorno configurado exitosamente para el Módulo 09: Árboles de Decisión.")
```

---
### 4. Implementación y Comparativa: Árbol Simple vs Bagging vs Random Forest 📊

```python
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier, RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, roc_auc_score

# 1. Cargar dataset de spam
file_spam = load_dataset('spam.csv', '09 - Decision Trees')
df_spam = pd.read_csv(file_spam, header=None)
X = df_spam.iloc[:, :-1]
y = df_spam.iloc[:, -1]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42, stratify=y)

# 2. Árbol Simple (Baseline)
single_tree = DecisionTreeClassifier(max_depth=10, random_state=42)
single_tree.fit(X_train, y_train)

# 3. Bagging de 100 Árboles
bagging_model = BaggingClassifier(
    estimator=DecisionTreeClassifier(),
    n_estimators=100,
    oob_score=True,
    random_state=42,
    n_jobs=-1
)
bagging_model.fit(X_train, y_train)

# 4. Random Forest de 100 Árboles
rf_model = RandomForestClassifier(
    n_estimators=100,
    max_features='sqrt',
    oob_score=True,
    random_state=42,
    n_jobs=-1
)
rf_model.fit(X_train, y_train)

print("=" * 65)
print("🌲 COMPARATIVA DE MODELOS SOBRE EL DATASET DE SPAM:")
print("=" * 65)
print(f"• Árbol Simple (Depth=10):  Exactitud Test = {single_tree.score(X_test, y_test)*100:.2f}% | AUC = {roc_auc_score(y_test, single_tree.predict_proba(X_test)[:,1]):.4f}")
print(f"• Bagging (100 Árboles):     Exactitud Test = {bagging_model.score(X_test, y_test)*100:.2f}% | OOB = {bagging_model.oob_score_*100:.2f}%")
print(f"• Random Forest (100 Árboles): Exactitud Test = {rf_model.score(X_test, y_test)*100:.2f}% | OOB = {rf_model.oob_score_*100:.2f}% | AUC = {roc_auc_score(y_test, rf_model.predict_proba(X_test)[:,1]):.4f}")
print("=" * 65)
```

---
##### 🛠️ Práctica 3: Extracción e Inspección de Importancia de Variables en Random Forest

**Objetivo:** Extraer las 10 características más determinantes para clasificar correo Spam mediante el atributo `feature_importances_` de Random Forest y representarlas en un gráfico de barras horizontal.

**Instrucciones:**
1. Extrae las importancias relativas `importances = rf_model.feature_importances_`.
2. Crea un `pd.Series` con los nombres de columnas `Feature_1, ..., Feature_57` y ordénalas de mayor a menor.
3. Filtra las 10 características principales.
4. Grafica un diagrama de barras horizontal con Seaborn / Matplotlib.

```python
# =========================================================================
# TU SOLUCIÓN: Práctica 3 - Importancia de Características
# =========================================================================

# 1. Extraer importancias
# top10_features = ...

# 2. Gráfico de barras horizontal
# plt.figure(figsize=(9, 5))
# ...
# plt.show()
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
# 1. Crear serie de importancias
feature_names = [f"F_{i+1}" for i in range(X.shape[1])]
feat_imp = pd.Series(rf_model.feature_importances_, index=feature_names)
top10 = feat_imp.sort_values(ascending=False).head(10)

# 2. Visualización
plt.figure(figsize=(9, 4.8), dpi=110)
sns.barplot(x=top10.values, y=top10.index, palette='crest')
plt.title('Top 10 Características Más Importantes (Random Forest - Spam Dataset)', fontweight='bold')
plt.xlabel('Reducción Promedio de Impureza de Gini (Importancia Relativa)')
plt.ylabel('Característica (Frecuencia de Palabra / Carácter)')
for i, v in enumerate(top10.values):
    plt.text(v + 0.001, i, f"{v*100:.2f}%", va='center', fontsize=9, fontweight='bold', color='#1e293b')
plt.xlim(0, top10.max() * 1.18)
plt.show()
```
</details>

---
### 5. Resumen y Conclusiones del Cuaderno 03 📌

1. **Bagging:** Reduce la varianza promediando modelos idénticos sobre muestras bootstrap independientes.
2. **Random Forest:** Descorrelaciona los árboles restringiendo los predictores elegibles a $m = \sqrt{p}$, logrando mayor estabilidad y menor error de generalización.
3. **Out-of-Bag (OOB):** Permite validar el modelo internamente sin necesidad de un set de validación cruzada adicional.

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos</i>
  </p>
</div>
