# 02_KMeans_Clustering

<table style="width: 100%; border-collapse: collapse; border: none; background: #f8fafc; border-left: 6px solid #1e3a8a; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #0f172a; font-size: 2.1em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        K-Means y Métodos Particionales 🔄
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
        Módulo 10 • Cuaderno 02
      </span><br>
      <span style="color: #64748b; font-size: 0.85em;">Docente: Santiago A. Zúñiga M.</span><br>
      <a href="mailto:gestorvirtualcienciadatos@ustatunja.edu.co" style="color: #2563eb; font-size: 0.8em; text-decoration: none; font-weight: 500;">gestorvirtualcienciadatos@ustatunja.edu.co</a>
    </td>
  </tr>
</table>

<div align="center" style="margin-top: 15px; margin-bottom: 15px;">
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/10%20-%20Clustering/02_KMeans_Clustering.ipynb" target="_parent">
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
| 1 | Comprender la formulación matemática de la función objetivo de K-Means (Inercia / WCSS). |
| 2 | Dominar el ciclo iterativo de Expectation-Maximization (Algoritmo de Lloyd). |
| 3 | Entender la inicialización probabilística K-Means++ y su convergencia. |
| 4 | Implementar y ajustar modelos con Scikit-Learn e inspeccionar centroides aprendidos. |

---
## El Algoritmo K-Means (Algoritmo de Lloyd) 🔄

Dado un número fijo de clusters $k$, K-Means particiona $n$ observaciones en $k$ conjuntos $S = \{S_1, S_2, \dots, S_k\}$ minimizando la **Suma de Cuadrados Intra-Cluster (WCSS o Inercia)**:

$$\arg\min_S \sum_{j=1}^k \sum_{x_i \in S_j} \|x_i - \mu_j\|^2$$

donde $\mu_j$ es el **centroide** (media vectorial) de los puntos asignados al cluster $S_j$.

### Fases Iterativas del Algoritmo:
1. **Inicialización:** Se seleccionan $k$ centroides iniciales $\mu_1^{(0)}, \dots, \mu_k^{(0)}$.
2. **Paso de Asignación (Paso E):** Cada punto se asigna al centroide más cercano según distancia euclidiana:
   $$S_j^{(t)} = \left\{ x_i : \|x_i - \mu_j^{(t)}\|^2 \le \|x_i - \mu_l^{(t)}\|^2 \quad \forall l \in \{1, \dots, k\} \right\}$$
3. **Paso de Actualización (Paso M):** Se recalculan los centroides como el promedio aritmético de sus miembros:
   $$\mu_j^{(t+1)} = \frac{1}{|S_j^{(t)}|} \sum_{x_i \in S_j^{(t)}} x_i$$
4. **Criterio de Convergencia:** El proceso se repite hasta que ningún centroide cambie de posición o se alcance `max_iter`.

```python
from sklearn.cluster import KMeans
from sklearn.datasets import load_digits
from sklearn.preprocessing import StandardScaler
import numpy as np
import matplotlib.pyplot as plt

# Carga del dataset Small MNIST (1797 imágenes de dígitos de 8x8 píxeles)
digits = load_digits()
X, y = digits.data, digits.target
X_std = StandardScaler().fit_transform(X)

# Ajuste de K-Means con k=10 clusters e inicialización K-Means++
modelo_kmeans = KMeans(
    n_clusters=10,
    init="k-means++",
    n_init="auto",
    random_state=109
)
etiquetas_clusters = modelo_kmeans.fit_predict(X_std)

print(f"Inercia final del modelo (WCSS): {modelo_kmeans.inertia_:.2f}")
print(f"Forma de la matriz de centroides: {modelo_kmeans.cluster_centers_.shape} (10 clusters x 64 características)")
print(f"Número de iteraciones hasta converger: {modelo_kmeans.n_iter_}")
```

```python
# Visualización de los 10 centroides aprendidos como imágenes reconstruidas de 8x8
scaler = StandardScaler().fit(X)
fig, axes = plt.subplots(2, 5, figsize=(12, 5), subplot_kw={"xticks": [], "yticks": []})

for i, ax in enumerate(axes.flat):
    centroide_original = scaler.inverse_transform(modelo_kmeans.cluster_centers_[i].reshape(1, -1))
    ax.imshow(centroide_original.reshape(8, 8), cmap="binary", interpolation="nearest")
    ax.set_title(f"Centroide Cluster {i}", fontweight="bold", fontsize=9)

plt.suptitle("Imágenes Promedio (Centroides) Aprendidas por K-Means para los Dígitos", fontsize=12, fontweight="bold")
plt.tight_layout()
plt.show()
```

---
## Inicialización Inteligente: K-Means++ 🚀

La inicialización puramente aleatoria puede provocar que múltiples centroides comiencen en el mismo cluster real, atrapando el algoritmo en un mínimo local subóptimo.

**K-Means++** resuelve esto seleccionando el primer centroide al azar y los siguientes con una probabilidad proporcional al cuadrado de la distancia al centroide más cercano ya existente:

$$P(x_i) = \frac{\min_j \|x_i - \mu_j\|^2}{\sum_m \min_j \|x_m - \mu_j\|^2}$$

### Puntos Clave y Propiedades 🔑

* **Complejidad Temporal:** $\mathcal{O}(n \cdot k \cdot I \cdot d)$ — es muy eficiente y escala linealmente con el número de muestras $n$.
* **Supuestos Geométricos:** Asume clusters esféricos, convexos y con varianza similar.
* **Hiperparámetro `n_init`:** Controla cuántas veces se reinicia el algoritmo con diferentes semillas para retornar la solución con menor inercia.

---
#### 🛠️ Práctica: K-Means en Datos Sintéticos

**Ejercicio 1:**
Genera un conjunto de datos con `make_blobs(n_samples=400, centers=4, random_state=42)` y ajusta un modelo `KMeans(n_clusters=4)`. Grafica los puntos coloreados por cluster y marca los centroides finales con estrellas rojas de gran tamaño.

```python
# Ejercicio 1 — Escribe tu código aquí
from sklearn.datasets import make_blobs

X_blobs, _ = make_blobs(n_samples=400, centers=4, random_state=42)

# modelo_blobs = KMeans(...)
# ...
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
km_blobs = KMeans(n_clusters=4, init="k-means++", random_state=42)
pred_blobs = km_blobs.fit_predict(X_blobs)

plt.figure(figsize=(8, 5))
plt.scatter(X_blobs[:, 0], X_blobs[:, 1], c=pred_blobs, cmap="tab10", s=35, alpha=0.8)
plt.scatter(km_blobs.cluster_centers_[:, 0], km_blobs.cluster_centers_[:, 1],
            c="red", marker="*", s=300, edgecolor="black", label="Centroides Aprendidos", zorder=5)
plt.title("Agrupamiento K-Means con k=4 y sus Centroides", fontweight="bold")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
print(f"Inercia WCSS obtenida: {km_blobs.inertia_:.2f}")
```
</details>

---
### Resumen y Preguntas de Autoevaluación 🧠

1. **¿Por qué K-Means converge siempre pero no garantiza el óptimo global?**  
   *Respuesta:* Porque en cada paso la inercia WCSS decrece estrictamente, pero la función objetivo no es convexa y presenta múltiples mínimos locales según la inicialización.

2. **¿Qué papel cumple el atributo `inertia_` en Scikit-Learn?**  
   *Respuesta:* Almacena la suma total de distancias cuadradas de cada muestra a su centroide asignado. Es la métrica interna base para el método del codo.

3. **¿Cómo se comporta K-Means ante datos con forma de anillos concéntricos o medialunas?**  
   *Respuesta:* Falla drásticamente porque sus fronteras de decisión son hiperplanos lineales (teselación de Voronoi), dividiendo los anillos en sectores en lugar de reconocer su topología continua.

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos</i>
  </p>
</div>
