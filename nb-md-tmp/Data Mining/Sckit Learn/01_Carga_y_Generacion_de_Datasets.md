# 01_Carga_y_Generacion_de_Datasets

<table style="width: 100%; border-collapse: collapse; border: none; background: #f8fafc; border-left: 6px solid #1e3a8a; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #0f172a; font-size: 2.1em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        Carga y Generación de Datasets en Scikit-Learn 📦
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
        Módulo 01
      </span><br>
      <span style="color: #64748b; font-size: 0.85em;">Docente: Santiago A. Zúñiga M.</span><br>
      <a href="mailto:gestorvirtualcienciadatos@ustatunja.edu.co" style="color: #2563eb; font-size: 0.8em; text-decoration: none; font-weight: 500;">gestorvirtualcienciadatos@ustatunja.edu.co</a>
    </td>
  </tr>
</table>

<div align="center" style="margin-top: 15px; margin-bottom: 15px;">
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Mining/Sckit%20Learn/01_Carga_y_Generacion_de_Datasets.ipynb" target="_parent">
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

En este cuaderno aprenderás a gestionar conjuntos de datos con el submódulo `sklearn.datasets` para prototipado, pruebas de estrés y benchmarking:

* **1. Estructura `Bunch`:** Acceso a `data`, `target`, `feature_names` y conversión directa con `as_frame=True`.
* **2. Toy Datasets Canónicos:** Exploración profunda de `load_iris`, `load_breast_cancer`, `load_wine` y `load_digits`.
* **3. Datasets Reales a Gran Escala:** Descarga con `fetch_california_housing` y gestión de caché local.
* **4. Generación Sintética Controlada:** Uso de `make_classification`, `make_regression`, `make_blobs` y `make_moons`.
* **5. Simulación de Desafíos Reales:** Inyección de ruido gaussiano, multicolinealidad y desbalance severo de clases.

---
### 1. El Objeto `Bunch` y Carga de Datasets Clásicos 🌺

Los *Toy Datasets* vienen embebidos directamente en la librería y se entregan como un objeto diccionario extendido llamado `Bunch`:

```python
from sklearn.datasets import load_iris, load_breast_cancer, load_digits

# 1. Carga de Iris con DataFrame integrado
iris = load_iris(as_frame=True)
df_iris = iris.frame

print("🌺 DATASET IRIS:")
print(f"  Dimensiones       : {df_iris.shape[0]} muestras x {df_iris.shape[1]} columnas")
print(f"  Variables ($X$)    : {iris.feature_names}")
print(f"  Clases ($y$)       : {list(iris.target_names)}")
df_iris.head(3)
```

```python
# 2. Visualización del Dataset Digits (Imágenes de 8x8 píxeles)
digits = load_digits()

fig, axes = plt.subplots(1, 5, figsize=(12, 3))
for i, ax in enumerate(axes):
    ax.imshow(digits.images[i], cmap='binary', interpolation='nearest')
    ax.set_title(f"Dígito: {digits.target[i]}", fontweight='bold')
    ax.axis('off')
plt.suptitle("Muestras de Dígitos Escritos a Mano (sklearn.datasets.load_digits)", fontsize=12, fontweight='bold')
plt.tight_layout()
plt.show()
```

---
### 2. Generación Controlada de Datos Sintéticos 🔬

En Minería de Datos, probar algoritmos en datasets sintéticos permite aislar el impacto de variables redundantes, ruido y no linealidad geométrica:

| Función Generadora | Dominio Analítico | Parámetros Clave |
|---|---|---|
| `make_classification` | Clasificación supervisada | `n_informative`, `n_redundant`, `weights`, `flip_y` |
| `make_regression` | Regresión lineal/polinómica | `n_informative`, `noise`, `coef`, `bias` |
| `make_blobs` | Clustering no supervisado | `centers`, `cluster_std`, `center_box` |
| `make_moons` | Manifolds no lineales | `noise` |

```python
from sklearn.datasets import make_classification, make_regression, make_blobs, make_moons

fig, axes = plt.subplots(2, 2, figsize=(12, 9))

# 1. Clasificación con variables redundantes
X_c, y_c = make_classification(n_samples=300, n_features=2, n_informative=2, n_redundant=0, flip_y=0.03, random_state=42)
axes[0, 0].scatter(X_c[:, 0], X_c[:, 1], c=y_c, cmap='coolwarm', edgecolors='k', alpha=0.8)
axes[0, 0].set_title("make_classification (2 Clases con Ruido)", fontweight='bold')

# 2. Regresión con dispersión gaussiana
X_r, y_r, coef = make_regression(n_samples=300, n_features=1, noise=15.0, coef=True, random_state=42)
axes[0, 1].scatter(X_r, y_r, color='#0284c7', edgecolors='k', alpha=0.7)
axes[0, 1].plot(X_r, X_r * coef, color='#dc2626', lw=2, label=f'Pendiente: {coef:.2f}')
axes[0, 1].set_title(r"make_regression (1D con Ruido \sigma=15)", fontweight='bold')
axes[0, 1].legend()

# 3. Clustering con 4 centros
X_b, y_b = make_blobs(n_samples=300, centers=4, cluster_std=0.8, random_state=42)
axes[1, 0].scatter(X_b[:, 0], X_b[:, 1], c=y_b, cmap='viridis', edgecolors='k', alpha=0.8)
axes[1, 0].set_title("make_blobs (4 Clusters Gaussianos)", fontweight='bold')

# 4. Manifold No Lineal
X_m, y_m = make_moons(n_samples=300, noise=0.12, random_state=42)
axes[1, 1].scatter(X_m[:, 0], X_m[:, 1], c=y_m, cmap='plasma', edgecolors='k', alpha=0.8)
axes[1, 1].set_title("make_moons (Separabilidad No Lineal)", fontweight='bold')

for ax in axes.flat:
    ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

---
#### 🛠️ Práctica: Datasets en Scikit-Learn

**Ejercicio 1:**
Utiliza `load_wine(as_frame=True)` para extraer los nombres de las 13 características químicas y calcula la media de `alcohol` para cada una de las 3 clases de vino.

```python
# Ejercicio 1
# Escribe tu código aquí
from sklearn.datasets import load_wine

# wine = load_wine(as_frame=True)
# ...
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
# Solución Ejercicio 1
wine = load_wine(as_frame=True)
df_wine = wine.frame

print("Características químicas:", wine.feature_names)
media_alcohol_por_clase = df_wine.groupby('target')['alcohol'].mean()
print("\nMedia de Alcohol por Clase de Vino:")
print(media_alcohol_por_clase)
```
</details>

**Ejercicio 2:**
Genera un dataset sintético con `make_classification` que simule un caso de detección de transacciones fraudulentas:
* 1000 muestras, 10 características (4 informativas, 2 redundantes, 4 repetidas o de ruido).
* Desbalance de clases severo: 95% normales, 5% fraudulentas (`weights=[0.95, 0.05]`).
* Comprueba la proporción real de clases generadas mediante `pd.Series(y).value_counts(normalize=True)`.

```python
# Ejercicio 2
# Escribe tu código aquí

# X_fraude, y_fraude = make_classification(...)
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
# Solución Ejercicio 2
X_fraude, y_fraude = make_classification(
    n_samples=1000,
    n_features=10,
    n_informative=4,
    n_redundant=2,
    n_repeated=4,
    weights=[0.95, 0.05],
    random_state=42
)

proporciones = pd.Series(y_fraude).value_counts(normalize=True)
print("Proporción de Clases Obtenida:")
print(proporciones)
print(f"Total transacciones normales (0): {(y_fraude == 0).sum()}")
print(f"Total fraudes detectados (1)    : {(y_fraude == 1).sum()}")
```
</details>

---
### Resumen y Preguntas de Autoevaluación 🧠

1. **¿Qué ventaja ofrece `as_frame=True` en `load_*`?**  
   *Respuesta:* Retorna directamente DataFrames y Series de Pandas con los nombres de variables ya mapeados, facilitando el análisis exploratorio inmediato.
2. **¿Por qué es útil el parámetro `n_redundant` en `make_classification`?**  
   *Respuesta:* Genera variables que son combinaciones lineales de las informativas, permitiendo simular problemas de multicolinealidad y evaluar algoritmos de selección de variables.
3. **¿Cómo se almacenan los datasets descargados con `fetch_*`?**  
   *Respuesta:* Se guardan automáticamente en la caché local del usuario (`~/scikit_learn_data/`) para no requerir descargas repetitivas por internet.

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Minería de Datos (Data Mining)</i>
  </p>
</div>
