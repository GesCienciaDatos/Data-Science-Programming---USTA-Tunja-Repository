# 04_DBSCAN_Clustering

<table style="width: 100%; border-collapse: collapse; border: none; background: #f8fafc; border-left: 6px solid #1e3a8a; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #0f172a; font-size: 2.1em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        DBSCAN y Clustering Basado en Densidad 🔬
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
        Módulo 10 • Cuaderno 04
      </span><br>
      <span style="color: #64748b; font-size: 0.85em;">Docente: Santiago A. Zúñiga M.</span><br>
      <a href="mailto:gestorvirtualcienciadatos@ustatunja.edu.co" style="color: #2563eb; font-size: 0.8em; text-decoration: none; font-weight: 500;">gestorvirtualcienciadatos@ustatunja.edu.co</a>
    </td>
  </tr>
</table>

<div align="center" style="margin-top: 15px; margin-bottom: 15px;">
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/10%20-%20Clustering/04_DBSCAN_Clustering.ipynb" target="_parent">
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
| 1 | Comprender el paradigma de clustering espacial basado en densidad topológica. |
| 2 | Diferenciar y clasificar puntos Núcleo (*Core*), Borde (*Border*) y Ruido (*Noise* / `-1`). |
| 3 | Calibrar óptimamente el radio $\varepsilon$ mediante el gráfico de $k$-distancias con `NearestNeighbors`. |
| 4 | Aplicar DBSCAN para descubrir clusters de geometrías no convexas y no lineales. |

---
## Fundamentos del Algoritmo DBSCAN 🔬

**DBSCAN** (*Density-Based Spatial Clustering of Applications with Noise*) agrupa observaciones en función de la densidad espacial de puntos, superando las limitaciones geométricas de K-Means.

<div align="center">
  <img src="images/dbscan.png" alt="Conceptos de Densidad en DBSCAN" width="75%"/>
  <p style="color: #64748b; font-size: 0.85em;">Figura 1: Clasificación de puntos en DBSCAN según el radio $\varepsilon$ y el parámetro min_samples.</p>
</div>

### Conceptos Clave de Densidad:
* **Vecindad $\varepsilon$:** El entorno circular o esférico de radio $\varepsilon$ alrededor del punto $p$:
  $$\mathcal{N}_\varepsilon(p) = \{ q \in D : \text{dist}(p, q) \le \varepsilon \}$$
* **Punto Núcleo (*Core Point*):** Contiene al menos `min_samples` observaciones dentro de su radio $\varepsilon$ ($|\mathcal{N}_\varepsilon(p)| \ge \text{min\_samples}$).
* **Punto Borde (*Border Point*):** No alcanza la densidad mínima requerida pero pertenece a la vecindad de un Punto Núcleo.
* **Punto de Ruido (*Noise / Outlier*):** No es núcleo ni borde; se le asigna la etiqueta **`-1`**.

```python
from sklearn.cluster import DBSCAN, KMeans
from sklearn.datasets import make_moons
from sklearn.preprocessing import StandardScaler
import numpy as np
import matplotlib.pyplot as plt

# Generación de dataset de dos lunas entrelazadas con ruido añadido
X_lunas, _ = make_moons(n_samples=500, noise=0.08, random_state=42)
X_lunas_std = StandardScaler().fit_transform(X_lunas)

# Ajuste de DBSCAN
dbscan = DBSCAN(eps=0.28, min_samples=5)
etiquetas_db = dbscan.fit_predict(X_lunas_std)

n_clusters_ = len(set(etiquetas_db)) - (1 if -1 in etiquetas_db else 0)
n_ruido_ = list(etiquetas_db).count(-1)

print(f"Clusters autónomos descubiertos: {n_clusters_}")
print(f"Puntos de ruido atípico detectados (-1): {n_ruido_}")

# Comparativa lado a lado: DBSCAN vs K-Means
fig, axes = plt.subplots(1, 2, figsize=(13, 4.5))

# Gráfico DBSCAN
mascara_validos = etiquetas_db != -1
axes[0].scatter(X_lunas_std[mascara_validos, 0], X_lunas_std[mascara_validos, 1],
                c=etiquetas_db[mascara_validos], cmap="tab10", s=30)
axes[0].scatter(X_lunas_std[~mascara_validos, 0], X_lunas_std[~mascara_validos, 1],
                c="black", marker="x", s=55, label="Ruido (-1)")
axes[0].set_title("DBSCAN: Detección Perfecta de Geometrías Complejas", fontweight="bold")
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# Gráfico K-Means
etiquetas_km = KMeans(n_clusters=2, random_state=42).fit_predict(X_lunas_std)
axes[1].scatter(X_lunas_std[:, 0], X_lunas_std[:, 1], c=etiquetas_km, cmap="tab10", s=30)
axes[1].set_title("K-Means (k=2): Fracasa ante Formas No Lineales", fontweight="bold")
axes[1].grid(True, alpha=0.3)

plt.suptitle("Comparativa: DBSCAN vs K-Means en Datasets No Lineales", fontsize=13, fontweight="bold")
plt.tight_layout()
plt.show()
```

---
## Calibración del Radio $\varepsilon$ mediante Gráfico de $k$-Distancias 📈

La técnica estándar para encontrar el valor idóneo de $\varepsilon$ consiste en calcular la distancia de cada observación a su $k$-ésimo vecino más cercano, ordenar estas distancias en forma ascendente y ubicar el **punto de máxima curvatura o codo**.

```python
from sklearn.neighbors import NearestNeighbors

k_vecinos = 5
nn = NearestNeighbors(n_neighbors=k_vecinos)
nn.fit(X_lunas_std)
distancias, _ = nn.kneighbors(X_lunas_std)

# Distancia al 5to vecino más cercano, ordenada ascendentemente
k_dist = np.sort(distancias[:, k_vecinos - 1])

plt.figure(figsize=(9, 4.2))
plt.plot(k_dist, color="#0284c7", lw=2)
plt.axhline(y=0.28, color="#dc2626", linestyle="--", label=r"$\epsilon$ seleccionado = 0.28 (Punto de Codo)")
plt.title(f"Gráfico de {k_vecinos}-Distancias para Calibrar el Radio Epsilon", fontweight="bold")
plt.xlabel("Observaciones Ordenadas por Distancia Ascendente")
plt.ylabel(f"Distancia al {k_vecinos}-ésimo Vecino Más Cercano")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
```

---
#### 🛠️ Práctica: DBSCAN en Anillos Concéntricos

**Ejercicio 1:**
Aplica DBSCAN al dataset `make_circles(n_samples=500, factor=0.5, noise=0.06, random_state=42)`. Ajusta los parámetros $\varepsilon$ y `min_samples` para que el modelo distinga con precisión los 2 anillos concéntricos sin clasificar puntos legítimos como ruido.

```python
# Ejercicio 1 — Escribe tu código aquí
from sklearn.datasets import make_circles

X_circ, _ = make_circles(n_samples=500, factor=0.5, noise=0.06, random_state=42)
X_circ_std = StandardScaler().fit_transform(X_circ)

# db_circ = DBSCAN(eps=..., min_samples=...)
# ...
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
db_circ = DBSCAN(eps=0.22, min_samples=5)
etiquetas_circ = db_circ.fit_predict(X_circ_std)

n_c = len(set(etiquetas_circ)) - (1 if -1 in etiquetas_circ else 0)
n_r = list(etiquetas_circ).count(-1)
print(f"Clusters identificados: {n_c} | Puntos de ruido: {n_r}")

plt.figure(figsize=(6.5, 5))
plt.scatter(X_circ_std[etiquetas_circ != -1, 0], X_circ_std[etiquetas_circ != -1, 1],
            c=etiquetas_circ[etiquetas_circ != -1], cmap="tab10", s=30)
plt.scatter(X_circ_std[etiquetas_circ == -1, 0], X_circ_std[etiquetas_circ == -1, 1],
            c="black", marker="x", s=50, label="Ruido (-1)")
plt.title("DBSCAN — Segmentación de Anillos Concéntricos", fontweight="bold")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
```
</details>

---
### Resumen y Preguntas de Autoevaluación 🧠

1. **¿Por qué DBSCAN no requiere que el usuario defina el número de clusters $k$ previamente?**  
   *Respuesta:* Porque el número de clusters emerge dinámicamente según la conectividad de componentes densas en el espacio de características.

2. **¿Qué sucede si el radio $\varepsilon$ se configura con un valor excesivamente grande?**  
   *Respuesta:* La vecindad abarcará casi todo el espacio, fusionando clusters distintos en un único supercluster masivo y eliminando la capacidad de detectar ruido.

3. **¿Cuál es la principal desventaja de DBSCAN estándar?**  
   *Respuesta:* Tiene dificultades para segmentar datasets que contienen clusters con densidades espaciales marcadamente diferentes, ya que un único radio global $\varepsilon$ no se adapta a densidades variables (para esto se usa HDBSCAN u OPTICS).

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos</i>
  </p>
</div>
