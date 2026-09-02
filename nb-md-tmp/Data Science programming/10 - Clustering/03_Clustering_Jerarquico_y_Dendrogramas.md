# 03_Clustering_Jerarquico_y_Dendrogramas

<table style="width: 100%; border-collapse: collapse; border: none; background: #f8fafc; border-left: 6px solid #1e3a8a; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #0f172a; font-size: 2.1em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        Clustering Jerárquico Aglomerativo y Dendrogramas 🌳
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
        Módulo 10 • Cuaderno 03
      </span><br>
      <span style="color: #64748b; font-size: 0.85em;">Docente: Santiago A. Zúñiga M.</span><br>
      <a href="mailto:gestorvirtualcienciadatos@ustatunja.edu.co" style="color: #2563eb; font-size: 0.8em; text-decoration: none; font-weight: 500;">gestorvirtualcienciadatos@ustatunja.edu.co</a>
    </td>
  </tr>
</table>

<div align="center" style="margin-top: 15px; margin-bottom: 15px;">
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/10%20-%20Clustering/03_Clustering_Jerarquico_y_Dendrogramas.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Abrir en Google Colab" style="vertical-align: middle;"/>
  </a>
</div>

```python
# Configuración del entorno interactivo para visualización múltiple
try:
    from IPython.core.interactiveshell import InteractiveShell
    InteractiveShell.ast_node_interactivity = "all"
except ImportError:
    pass
```

---
## Objetivos de Aprendizaje 🎯

| # | Objetivo |
|:---:|---|
| 1 | Comprender el enfoque aglomerativo ascendente (*Bottom-up*) para clustering jerárquico. |
| 2 | Interpretar la Matriz de Enlace (*Linkage Matrix* $Z$) de SciPy. |
| 3 | Trazar e interpretar Dendrogramas para determinar el número natural de clusters mediante cortes de altura. |
| 4 | Comparar los cuatro métodos de enlace: Single, Average, Complete y Ward. |

---
## Fundamentos del Clustering Jerárquico Aglomerativo 🌳

El clustering aglomerativo construye una jerarquía completa de agrupamiento siguiendo una estrategia ascendente:
1. Inicia asignando cada una de las $n$ observaciones a su propio cluster individual ($n$ clusters de tamaño 1).
2. Calcula la matriz de distancias inter-cluster $D$.
3. Encuentra los dos clusters más cercanos y los fusiona en uno solo.
4. Actualiza la matriz de distancias entre el nuevo cluster y los restantes según el método de enlace elegido.
5. Repite los pasos 3 y 4 hasta que todas las muestras queden unidas en un único gran cluster raíz.

### La Matriz de Enlace (*Linkage Matrix* $Z$) con SciPy

SciPy almacena la historia secuencial de fusiones en una matriz $Z$ de dimensiones $(n-1) \times 4$:

| Columna | Descripción |
|:---:|---|
| `Z[i, 0]` | Identificador del primer cluster fusionado en el paso $i$ |
| `Z[i, 1]` | Identificador del segundo cluster fusionado en el paso $i$ |
| `Z[i, 2]` | Distancia inter-cluster a la cual se unieron |
| `Z[i, 3]` | Número total de observaciones contenidas en el nuevo cluster formado |

```python
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.datasets import load_digits
from sklearn.preprocessing import StandardScaler
import numpy as np
import matplotlib.pyplot as plt

digits = load_digits()
X, y = digits.data, digits.target
X_std = StandardScaler().fit_transform(X)

# Cálculo de la matriz de enlace con el método de Ward (mínima varianza)
Z = linkage(X_std, method="ward")

print(f"Dimensiones de la matriz de enlace Z: {Z.shape} -> ({X.shape[0]-1} fusiones x 4 columnas)")
print("\nPrimera fusión realizada (paso 0):", Z[0])
print("Última fusión realizada (raíz del árbol):", Z[-1])
```

```python
# Graficación del Dendrograma Truncado a los últimos 30 nodos de fusión
plt.figure(figsize=(13, 5))
dendrogram(
    Z,
    truncate_mode="lastp",
    p=30,
    leaf_rotation=90.,
    leaf_font_size=9.,
    show_contracted=True
)
plt.title("Dendrograma Jerárquico Aglomerativo (Método Ward — Top 30 Nodos)", fontweight="bold")
plt.xlabel("Índice de Muestra o Tamaño del Cluster Fusionado")
plt.ylabel("Distancia de Fusión")
plt.axhline(y=50, color="#dc2626", linestyle="--", label="Línea de Corte (h=50 -> ~10 clusters)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
```

---
## Métodos de Enlace (*Linkage Methods*) 📊

<div align="center">
  <img src="images/hac_linkage_methods.PNG" alt="Métodos de Enlace Jerárquico" width="70%"/>
  <p style="color: #64748b; font-size: 0.85em;">Figura 1: Comparación conceptual de los criterios de distancia entre clusters.</p>
</div>

| Criterio | Distancia Inter-Cluster $D(A, B)$ | Características Principales |
|---|---|---|
| **Single (Mínimo)** | $\min \{ d(x, y) : x \in A, y \in B \}$ | Detecta formas complejas no elípticas, pero sufre del efecto de encadenamiento (*chaining*). |
| **Complete (Máximo)** | $\max \{ d(x, y) : x \in A, y \in B \}$ | Genera clusters compactos y diámetros homogéneos. |
| **Average (Promedio)** | $\frac{1}{|A||B|} \sum_{x \in A} \sum_{y \in B} d(x, y)$ | Balance robusto entre Single y Complete. |
| **Ward (Varianza)** | Minimiza el incremento de la varianza intra-cluster | Método por defecto recomendado para variables continuas. |

```python
# Comparativa práctica de los 4 métodos de enlace con Scikit-Learn
from sklearn.cluster import AgglomerativeClustering

metodos = ["single", "average", "complete", "ward"]
fig, axes = plt.subplots(1, 4, figsize=(16, 4))

for ax, m in zip(axes, metodos):
    modelo_agg = AgglomerativeClustering(n_clusters=10, linkage=m)
    etiquetas = modelo_agg.fit_predict(X_std)
    tamanos = [np.sum(etiquetas == j) for j in range(10)]
    ax.bar(range(10), tamanos, color="#4f46e5", edgecolor="k")
    ax.set_title(f"Enlace: {m.capitalize()}", fontweight="bold")
    ax.set_xlabel("ID de Cluster")
    ax.set_ylabel("Frecuencia")
    ax.grid(True, alpha=0.3, axis="y")

plt.suptitle("Distribución de Tamaños de Clusters según el Método de Enlace (k=10)", fontsize=13, fontweight="bold")
plt.tight_layout()
plt.show()
```

---
#### 🛠️ Práctica: Clustering Jerárquico

**Ejercicio 1:**
Ajusta un modelo `AgglomerativeClustering(n_clusters=3, linkage="ward")` sobre un dataset sintético `make_blobs(n_samples=300, centers=3, random_state=42)`. Imprime cuántas observaciones fueron asignadas a cada cluster y visualiza la dispersión espacial coloreada.

```python
# Ejercicio 1 — Escribe tu código aquí
from sklearn.datasets import make_blobs

X_j, _ = make_blobs(n_samples=300, centers=3, random_state=42)

# modelo_j = AgglomerativeClustering(...)
# ...
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
modelo_j = AgglomerativeClustering(n_clusters=3, linkage="ward")
etiquetas_j = modelo_j.fit_predict(X_j)

conteo = pd.Series(etiquetas_j).value_counts().sort_index()
print("Distribución de muestras por cluster:")
print(conteo)

plt.figure(figsize=(7, 4.5))
plt.scatter(X_j[:, 0], X_j[:, 1], c=etiquetas_j, cmap="tab10", s=40, alpha=0.8)
plt.title("Clustering Jerárquico Aglomerativo (Ward Linkage, k=3)", fontweight="bold")
plt.grid(True, alpha=0.3)
plt.show()
```
</details>

---
### Resumen y Preguntas de Autoevaluación 🧠

1. **¿Cuál es la principal ventaja pedagógica y analítica del Dendrograma?**  
   *Respuesta:* Permite visualizar la estructura completa de agrupamiento a todos los niveles de granularidad, facilitando la elección del número de clusters al observar el mayor salto vertical sin fusiones intermedias.

2. **¿En qué consiste el fenómeno de encadenamiento (*chaining effect*) en Single Linkage?**  
   *Respuesta:* Ocurre cuando un par de puntos aislados actúan como puente entre dos clusters grandes, fusionándolos indebidamente en una cadena continua en lugar de dos grupos compactos separados.

3. **¿Cuál es la complejidad temporal y espacial del clustering jerárquico?**  
   *Respuesta:* Su complejidad temporal es $\mathcal{O}(n^2 \log n)$ o $\mathcal{O}(n^3)$ y requiere almacenar la matriz de distancias $\mathcal{O}(n^2)$, lo que limita su aplicación directa en datasets con más de 100,000 registros.

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos</i>
  </p>
</div>
