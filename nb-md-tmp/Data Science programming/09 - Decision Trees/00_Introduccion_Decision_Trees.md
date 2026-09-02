# 00_Introduccion_Decision_Trees

<table style="width: 100%; border-collapse: collapse; border: none; background: #f8fafc; border-left: 6px solid #1e3a8a; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #0f172a; font-size: 2.1em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        Introducción a los Árboles de Decisión (Decision Trees)
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
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/09%20-%20Decision%20Trees/00_Introduccion_Decision_Trees.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## Objetivos de Aprendizaje (*Learning Outcomes*) 🔎

En este noveno módulo exploraremos los **Modelos Basados en Árboles (*Tree-Based Methods*)** y los **Métodos de Ensamble (*Ensemble Methods*)**, una de las familias más versátiles, intuitivas y competitivas del Machine Learning moderno.

El contenido se estructura progresivamente a través de los siguientes cuadernos interactivos:

1. **[Introducción a los Árboles de Decisión](00_Introduccion_Decision_Trees.ipynb)** *(Este cuaderno)*: Paradigma de segmentación del espacio de características en hiper-rectángulos, analogía del diagrama de flujo, anatomía de nodos (raíz, internos, hojas) y mapa de ruta del módulo.
2. **[Criterios de División y Árboles de Clasificación](01_Criterios_Division_y_Arboles_Clasificacion.ipynb)** 🌲: Algoritmo voraz (*Greedy Top-Down Induction*), criterios matemáticos de impureza: **Índice de Gini** vs **Entropía / Ganancia de Información**, partición binaria óptima y visualización 2D de fronteras ortogonales.
3. **[Árboles de Regresión y Poda Cost-Complexity](02_Arboles_Regresion_y_Poda_Cost_Complexity.ipynb)** ✂️: Árboles continuos con `DecisionTreeRegressor`, criterios MSE/MAE, el dilema del sobreajuste en árboles profundos y técnica formal de **Poda por Complejidad de Costo Mínimo (*Minimal Cost-Complexity Pruning / ccp_alpha*)**.
4. **[Métodos de Ensamble: Bagging y Random Forests](03_Metodos_Ensamble_Bagging_y_Random_Forests.ipynb)** 🌲🌳🌲: Principio de la *Sabiduría de las Masas* (*Wisdom of Crowds*), remuestreo con reemplazo **Bootstrap Aggregating (Bagging)**, error *Out-of-Bag (OOB)*, descorrelación de árboles con **Random Forests** e importancia de características (*Feature Importance*).
5. **[Boosting y Modelado en Datos Desbalanceados](04_Boosting_y_Casos_Estudio_Desbalanceados.ipynb)** 🚀: Aprendizaje secuencial sobre residuos, AdaBoost, Gradient Boosting, XGBoost, ajuste de pesos por desbalance (`class_weight='balanced'`) y benchmark comparativo integral en el dataset de spam (`spam.csv`).

---
## Recursos y Referencias Recomendadas 📚

### 📖 Libros de Referencia:
* **[An Introduction to Statistical Learning with Applications in Python (ISLP)](https://www.statlearning.com/)** — *Gareth James, Daniela Witten, Trevor Hastie, Robert Tibshirani (Capítulo 8: Tree-Based Methods)*.
* **[The Elements of Statistical Learning](https://hastie.su.domains/ElemStatLearn/)** — *Trevor Hastie, Robert Tibshirani, Jerome Friedman (Capítulo 9: Additive Models, Trees, and Related Methods)*.
* **[Classification and Regression Trees (CART)](https://www.routledge.com/Classification-and-Regression-Trees/Breiman-Friedman-Stone-Olshen/p/book/9780412048418)** — *Leo Breiman, Jerome Friedman, Richard Olshen, Charles Stone (1984)*.

### 🌐 Documentación Oficial y Enlaces:
* **[Scikit-Learn User Guide: Decision Trees](https://scikit-learn.org/stable/modules/tree.html)**.
* **[Scikit-Learn: Tips on Practical Use of Trees](https://scikit-learn.org/stable/modules/tree.html#tips-on-practical-use)**.
* **[Harvard CS109-A: Introduction to Data Science](https://harvard-iacs.github.io/2021-CS109A/)** — *Harvard University*.
* **[XGBoost Official Documentation](https://xgboost.readthedocs.io/en/stable/)**.

---
## 1. ¿Qué son los Árboles de Decisión? 🧠

Los métodos basados en árboles segmentan o **estratifican el espacio de predictores en una serie de regiones simples (hiper-rectángulos)** ortogonales.

<div align="center">
  <img src="images/flowchart.png" width="600" alt="Diagrama de Flujo" style="border-radius:8px; box-shadow: 0 4px 6px rgba(0,0,0,0.15); margin: 10px 0;"/>
  <p style="font-size: 0.85em; color: #64748b;">
    <i>Figura: Los árboles de decisión formalizan matemáticamente diagramas de flujo secuenciales e interpretables.</i>
  </p>
</div>

### Propiedades Deseables:
1. **Interpretabilidad Humana:** Su estructura de reglas *"Si [Condición], Entonces [Resultado]"* puede explicarse fácilmente a expertos de dominio y tomadores de decisiones.
2. **Fronteras Locales Lineales:** Cada segmento o corte ortogonal es computacionalmente simple ($x_j \le t$).
3. **Mínimo Preprocesamiento:** No requieren escalado ni normalización de variables (invariantes a transformaciones monótonas).

---
## Configuración del Entorno de Trabajo 🛠️

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
## 2. Anatomía y Terminología de un Árbol de Decisión 🌿

Un árbol de decisión se compone de tres elementos topológicos fundamentales:

```
                            ┌────────────────────────┐
                            │    Nodo Raíz (Root)    │ ◄── Pregunta inicial sobre X_j <= t
                            └───────────┬────────────┘
                                        │
                         ┌──────────────┴──────────────┐
                         ▼                             ▼
              ┌────────────────────┐         ┌────────────────────┐
              │    Nodo Interno    │         │     Hoja (Leaf)    │ ◄── Predicción final
              └─────────┬──────────┘         └────────────────────┘
                        │
                ┌───────┴───────┐
                ▼               ▼
          ┌──────────┐    ┌──────────┐
          │   Hoja   │    │   Hoja   │
          └──────────┘    └──────────┘
```

<div align="center">
  <img src="images/simple_tree.png" width="450" alt="Estructura de Árbol Simple" style="border-radius:8px; box-shadow: 0 4px 6px rgba(0,0,0,0.12); margin: 10px 0;"/>
</div>

1. **Nodo Raíz (*Root Node*):** El punto de entrada superior que contiene el $100\%$ de las observaciones antes del primer corte.
2. **Nodos Internos (*Internal Decision Nodes*):** Evalúan una condición umbral binaria ($x_j \le t$) sobre una variable específica.
3. **Nodos Hoja / Terminales (*Leaf / Terminal Nodes*):** Asignan la etiqueta modal mayoritaria (en clasificación) o el promedio continuo $\bar{y}$ (en regresión).

---
## 3. Implementación Rápida con Scikit-Learn: `DecisionTreeClassifier` ⚡

```python
from sklearn.tree import DecisionTreeClassifier, export_text, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Cargar dataset de diagnóstico cardiaco
file_heart = load_dataset('heart_disease.csv', '08 - Classification')
df_heart = pd.read_csv(file_heart)

X = df_heart[['age', 'trestbps', 'chol', 'thalach', 'oldpeak']]
y = df_heart['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)

# Instanciar y ajustar árbol con profundidad controlada
tree_simple = DecisionTreeClassifier(max_depth=3, random_state=42)
tree_simple.fit(X_train, y_train)

print(f"Exactitud en Entrenamiento: {tree_simple.score(X_train, y_train)*100:.2f}%")
print(f"Exactitud en Prueba:        {tree_simple.score(X_test, y_test)*100:.2f}%")
```

```python
# 1. Representación en texto legible de las reglas del árbol
print("=" * 60)
print("🌲 REGLAS LÓGICAS APRENDIDAS POR EL ÁRBOL:")
print("=" * 60)
print(export_text(tree_simple, feature_names=list(X.columns)))
```

```python
# 2. Representación gráfica del árbol
plt.figure(figsize=(14, 7), dpi=120)
plot_tree(
    tree_simple,
    feature_names=list(X.columns),
    class_names=['Saludable (0)', 'Riesgo (1)'],
    filled=True,
    rounded=True,
    fontsize=10
)
plt.title("Estructura Gráfica del Árbol de Decisión (Profundidad = 3)", fontsize=13, fontweight='bold')
plt.show()
```

---
##### 🛠️ Práctica 0: Inspección e Interpretación de un Árbol Clínico de 2 Niveles

**Objetivo:** Entrenar un árbol de decisión compacto (`max_depth=2`) con solo 2 variables biométricas (`thalach`: Frecuencia cardiaca máxima, `oldpeak`: Depresión del segmento ST) y deducir verbalmente la regla de mayor riesgo.

**Instrucciones:**
1. Filtra las características `X_sub = df_heart[['thalach', 'oldpeak']]` y la clase objetivo `y = df_heart['target']`.
2. Ajusta un `DecisionTreeClassifier(max_depth=2, random_state=42)`.
3. Grafica el árbol con `plot_tree(..., filled=True)`.
4. Responde: ¿Qué combinación de `thalach` y `oldpeak` conduce a la hoja con mayor concentración de pacientes con cardiopatía?

```python
# =========================================================================
# TU SOLUCIÓN: Práctica 0 - Árbol Compacto de 2 Niveles
# =========================================================================

# 1. Definir variables
# X_sub = df_heart[['thalach', 'oldpeak']]
# y_sub = df_heart['target']

# 2. Ajuste del modelo
# tree_p0 = DecisionTreeClassifier(...)
# tree_p0.fit(...)

# 3. Gráfica del árbol
# plt.figure(figsize=(10, 5))
# plot_tree(...)
# plt.show()
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
X_sub = df_heart[['thalach', 'oldpeak']]
y_sub = df_heart['target']

# 1. Ajustar árbol compacto
tree_p0 = DecisionTreeClassifier(max_depth=2, random_state=42)
tree_p0.fit(X_sub, y_sub)

# 2. Visualización
plt.figure(figsize=(10, 5.5), dpi=120)
plot_tree(
    tree_p0,
    feature_names=['thalach', 'oldpeak'],
    class_names=['Sano (0)', 'Cardiopatía (1)'],
    filled=True,
    rounded=True,
    fontsize=11
)
plt.title("Árbol de Decisión Clínico Compacto (Profundidad = 2)", fontweight='bold')
plt.show()

# 3. Interpretación de la regla principal
print("=" * 65)
print("💡 INTERPRETACIÓN CLÍNICA DE LA REGLA:")
print("• Si oldpeak <= 0.7 y thalach > 147.5:")
print("  ──► El 78.6% de los pacientes presenta cardiopatía (Riesgo Alto 🚨)")
print("• Si oldpeak > 0.7 y oldpeak > 1.7:")
print("  ──► El 85.2% de los pacientes está diagnosticado como Sano ✅")
print("=" * 65)
```
</details>

---
### 4. Resumen y Conclusiones del Cuaderno 00 📌

1. **Modelos Basados en Reglas:** Los árboles dividen el espacio de forma jerárquica mediante comparaciones binarias sencillas e intuitivas.
2. **Componentes:** Nodo raíz (inicio), nodos internos (decisiones de corte) y hojas terminales (etiqueta o valor estimado).
3. **Interpretabilidad:** Herramientas como `export_text` y `plot_tree` permiten auditar exactamente cómo y por qué el modelo toma cada decisión.

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos</i>
  </p>
</div>
