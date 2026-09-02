# 01_Criterios_Division_y_Arboles_Clasificacion

<table style="width: 100%; border-collapse: collapse; border: none; background: #f8fafc; border-left: 6px solid #1e3a8a; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #0f172a; font-size: 2.1em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        Criterios de División y Árboles de Clasificación
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
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/09%20-%20Decision%20Trees/01_Criterios_Division_y_Arboles_Clasificacion.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
### 1. ¿Cómo se construye un Árbol de Clasificación? (Algoritmo Voraz CART) 📐

El algoritmo estándar **CART (*Classification and Regression Trees*)** construye el árbol de forma recursiva descendente (*Top-Down Greedy Approach*):
1. Comienza en el **nodo raíz** con todas las observaciones $D$.
2. En cada nodo, evalúa todas las variables predictoras $X_j$ y todos los posibles umbrales de corte $t$.
3. Selecciona la partición $(X_j, t)$ que **maximiza la pureza** (o minimiza la impureza) de los nodos hijos resultantes ($D_L$ y $D_R$).
4. Repite el proceso recursivamente hasta alcanzar una condición de parada.

<div align="center">
  <table style="border:none; background:transparent;">
    <tr style="border:none;">
      <td style="border:none; text-align:center; padding:10px;">
        <img src="images/split1.png" width="340" alt="Primera división" style="border-radius:8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);"/>
        <p style="font-size:0.85em; color:#64748b;"><b>División Inicial del Espacio 2D</b></p>
      </td>
      <td style="border:none; text-align:center; padding:10px;">
        <img src="images/split2.png" width="340" alt="Segunda división" style="border-radius:8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);"/>
        <p style="font-size:0.85em; color:#64748b;"><b>Partición Recursiva en Hiper-rectángulos</b></p>
      </td>
    </tr>
  </table>
</div>

---
### 2. Criterios Matemáticos de Impureza: Gini vs Entropía 🧮

Sea $p_k$ la proporción de muestras en el nodo pertenecientes a la clase $k \in \{1, 2, \dots, K\}$:

#### 1. Índice de Impureza de Gini (*Gini Impurity*):
Mide la probabilidad de clasificar erróneamente un elemento elegido al azar si se etiqueta según la distribución de clases del nodo:

$$	ext{Gini}(p) = \sum_{k=1}^K p_k (1 - p_k) = 1 - \sum_{k=1}^K p_k^2$$

* $	ext{Gini} = 0$: Nodo **completamente puro** (todas las muestras pertenecen a una sola clase).
* $	ext{Gini} = 0.5$ (en binario): Máxima impureza (50% clase 0, 50% clase 1).

#### 2. Entropía y Ganancia de Información (*Entropy & Information Gain*):
Basada en la teoría de la información de Shannon:

$$H(p) = -\sum_{k=1}^K p_k \log_2(p_k)$$

$$	ext{Ganancia\ de\ Información (IG)} = H(D) - \left( \frac{|D_L|}{|D|} H(D_L) + \frac{|D_R|}{|D|} H(D_R) \right)$$

<div align="center">
  <img src="images/tree_loss.png" width="450" alt="Comparativa de funciones de pérdida" style="border-radius:8px; box-shadow: 0 4px 6px rgba(0,0,0,0.12); margin: 10px 0;"/>
  <p style="font-size: 0.85em; color: #64748b;">
    <i>Figura: Comparación de la Entropía escalada, el Índice de Gini y el Error de Clasificación frente a la probabilidad $p$.</i>
  </p>
</div>

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
### 3. Carga del Dataset de Detección de Correo Spam (`spam.csv`) 📧

El dataset contiene 4,601 correos electrónicos y 57 características continuas (frecuencias de palabras clave y caracteres especiales como `!`, `$`), más la variable objetivo binaria `Spam` (0: Correo Legítimo, 1: Spam).

```python
# Cargar dataset de spam
file_spam = load_dataset('spam.csv', '09 - Decision Trees')
spam_df = pd.read_csv(file_spam, header=None)

# Asignar nombres de columnas
cols = [f"Feature_{i+1}" for i in range(spam_df.shape[1] - 1)] + ['Spam']
spam_df.columns = cols

display(spam_df.head())
print("Dimensiones del dataset de spam:", spam_df.shape)
print("Distribución de clases:")
print(spam_df['Spam'].value_counts(normalize=True))
```

---
### 4. Partición Train / Test y Ajuste con Criterio Gini vs Entropía 🌲

```python
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score

X = spam_df.drop(columns=['Spam'])
y = spam_df['Spam']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=42, stratify=y
)

# Modelo con Gini
tree_gini = DecisionTreeClassifier(criterion='gini', max_depth=6, random_state=42)
tree_gini.fit(X_train, y_train)

# Modelo con Entropía
tree_entropy = DecisionTreeClassifier(criterion='entropy', max_depth=6, random_state=42)
tree_entropy.fit(X_train, y_train)

print(f"Exactitud Test (Criterio Gini):     {tree_gini.score(X_test, y_test)*100:.2f}%")
print(f"Exactitud Test (Criterio Entropía): {tree_entropy.score(X_test, y_test)*100:.2f}%")
```

---
##### 🛠️ Práctica 1: Cálculo Analítico y Verificación de Ganancia de Información

**Objetivo:** Calcular paso a paso la Entropía inicial de un grupo de datos, la Entropía ponderada tras una división binaria y verificar la Ganancia de Información obtenida.

**Contexto:** Un nodo contiene 40 correos: 15 son Spam ($p_1 = 15/40 = 0.375$) y 25 son No-Spam ($p_0 = 25/40 = 0.625$).
* Un corte en la palabra `free` divide el grupo en:
  * **Hijo Izquierdo ($D_L$):** 10 correos (8 Spam, 2 No-Spam).
  * **Hijo Derecho ($D_R$):** 30 correos (7 Spam, 23 No-Spam).

**Instrucciones:**
1. Define la función matemática de entropía: $H(p) = -p_0 \log_2(p_0) - p_1 \log_2(p_1)$.
2. Calcula la entropía del nodo padre $H(D)$.
3. Calcula las entropías de los nodos hijos $H(D_L)$ y $H(D_R)$.
4. Calcula la Ganancia de Información $	ext{IG} = H(D) - \left( \frac{10}{40} H(D_L) + \frac{30}{40} H(D_R) 
\right)$.
5. Imprime los resultados con formato numérico.

```python
# =========================================================================
# TU SOLUCIÓN: Práctica 1 - Cálculo de Entropía y Ganancia de Información
# =========================================================================

# def entropia(p1):
#     if p1 == 0 or p1 == 1:
#         return 0
#     p0 = 1 - p1
#     return - (p0 * np.log2(p0) + p1 * np.log2(p1))

# 1. Entropía Padre
# h_padre = entropia(15 / 40)

# 2. Entropías Hijos
# h_izq = ...
# h_der = ...

# 3. Ganancia de Información
# ig = ...
# print(...)
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
def calcular_entropia(pos, total):
    if pos == 0 or pos == total:
        return 0.0
    p1 = pos / total
    p0 = 1 - p1
    return -(p0 * np.log2(p0) + p1 * np.log2(p1))

# 1. Entropía del nodo padre (15 spam de 40)
H_padre = calcular_entropia(15, 40)

# 2. Entropía hijo izquierdo (8 spam de 10)
H_izq = calcular_entropia(8, 10)

# 3. Entropía hijo derecho (7 spam de 30)
H_der = calcular_entropia(7, 30)

# 4. Entropía ponderada de los hijos
H_ponderada = (10 / 40) * H_izq + (30 / 40) * H_der

# 5. Ganancia de Información (IG)
info_gain = H_padre - H_ponderada

print("=" * 60)
print("📊 CÁLCULO FORMAL DE GANANCIA DE INFORMACIÓN (CART):")
print("=" * 60)
print(f"• Entropía del Nodo Padre H(D):      {H_padre:.4f} bits")
print(f"• Entropía Hijo Izquierdo H(D_L):     {H_izq:.4f} bits")
print(f"• Entropía Hijo Derecho H(D_R):       {H_der:.4f} bits")
print(f"• Entropía Ponderada Hijos:          {H_ponderada:.4f} bits")
print(f"• Ganancia de Información (IG):      {info_gain:.4f} bits (¡Reducción positiva!)")
print("=" * 60)
```
</details>

---
### 5. Resumen y Conclusiones del Cuaderno 01 📌

1. **Criterios de Corte:** Gini computa más rápido (evita cálculos logarítmicos), mientras que la Entropía favorece ligeramente particiones más balanceadas. En la práctica, sus exactitudes son prácticamente idénticas.
2. **Inducción Voraz:** CART evalúa en cada nodo la mejor división inmediata sin considerar el impacto global en niveles posteriores.
3. **Fronteras Ortogonales:** Las decisiones dividen el espacio en planos perpendiculares a los ejes de las variables ($X_j \le t$).

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos</i>
  </p>
</div>
