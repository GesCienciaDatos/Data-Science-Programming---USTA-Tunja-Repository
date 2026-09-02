# 05_Evaluacion_Seleccion_K_y_Benchmark

<table style="width: 100%; border-collapse: collapse; border: none; background: #f8fafc; border-left: 6px solid #1e3a8a; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #0f172a; font-size: 2.1em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        Métricas de Evaluación, Selección de K y Benchmark Comparativo 🏆
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
        Módulo 10 • Cuaderno 05
      </span><br>
      <span style="color: #64748b; font-size: 0.85em;">Docente: Santiago A. Zúñiga M.</span><br>
      <a href="mailto:gestorvirtualcienciadatos@ustatunja.edu.co" style="color: #2563eb; font-size: 0.8em; text-decoration: none; font-weight: 500;">gestorvirtualcienciadatos@ustatunja.edu.co</a>
    </td>
  </tr>
</table>

<div align="center" style="margin-top: 15px; margin-bottom: 15px;">
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/10%20-%20Clustering/05_Evaluacion_Seleccion_K_y_Benchmark.ipynb" target="_parent">
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
| 1 | Calcular e interpretar las métricas cuantitativas: Inercia, Coeficiente de Silueta, Davies-Bouldin y Calinski-Harabasz. |
| 2 | Aplicar el Método del Codo (*Elbow Method*) para determinar el número óptimo de clusters $k$. |
| 3 | Comprender el fundamento estadístico del Estadístico Gap (*Gap Statistic*). |
| 4 | Ejecutar un benchmark comparativo de múltiples algoritmos sobre datasets sintéticos complejos. |

---
## Métricas Cuantitativas de Evaluación Interna 📊

Al carecer de etiquetas verdaderas, la calidad del clustering se mide mediante índices que evalúan la **cohesión intra-cluster** y la **separación inter-cluster**:

### 1. Inercia (Suma de Cuadrados Intra-Cluster / WCSS)
$$\text{Inercia} = \sum_{j=1}^k \sum_{x_i \in S_j} \|x_i - \mu_j\|^2$$
* **Interpretación:** Menor valor indica clusters más compactos. Siempre decrece con $k$ (con $k=n$, Inercia $=0$).

### 2. Coeficiente de Silueta (*Silhouette Score*)
$$s(i) = \frac{b(i) - a(i)}{\max(a(i), b(i))}, \quad s(i) \in [-1, 1]$$

<div align="center">
  <img src="images/silhouette_eq.png" alt="Ecuación del Coeficiente de Silueta" width="45%"/>
</div>

* $a(i)$: Distancia promedio de la muestra $i$ a los demás puntos de su **mismo** cluster (cohesión).
* $b(i)$: Distancia promedio de la muestra $i$ a los puntos del cluster **vecino más cercano** (separación).
* $s \to +1$: Puntos fuertemente agrupados y bien separados | $s \to 0$: Solapamiento | $s < 0$: Muestra mal asignada.

### 3. Índice Davies-Bouldin (DB Index)
Evalúa la similitud promedio entre cada cluster y su cluster más parecido. **Menor valor es mejor ($\downarrow$).**

### 4. Índice Calinski-Harabasz (Criterio del Ratio de Varianzas)
$$CH = \frac{\text{tr}(B_k) / (k - 1)}{\text{tr}(W_k) / (n - k)}$$
Mide la dispersión inter-cluster ($B_k$) dividida por la dispersión intra-cluster ($W_k$). **Mayor valor es mejor ($\uparrow$).**

```python
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.metrics import silhouette_score, davies_bouldin_score, calinski_harabasz_score
from sklearn.datasets import load_digits
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

digits = load_digits()
X, y = digits.data, digits.target
X_std = StandardScaler().fit_transform(X)

# Ajuste de modelos con k=10
km = KMeans(n_clusters=10, init="k-means++", n_init="auto", random_state=109).fit(X_std)
agg = AgglomerativeClustering(n_clusters=10, linkage="ward").fit(X_std)

# Tabla comparativa de métricas
metricas_resumen = pd.DataFrame({
    "Algoritmo": ["K-Means", "Clustering Jerárquico (Ward)"],
    "Inercia (WCSS)": [round(km.inertia_, 2), "N/A"],
    "Silhouette Score (↑)": [round(silhouette_score(X_std, km.labels_), 4), round(silhouette_score(X_std, agg.labels_), 4)],
    "Davies-Bouldin (↓)": [round(davies_bouldin_score(X_std, km.labels_), 4), round(davies_bouldin_score(X_std, agg.labels_), 4)],
    "Calinski-Harabasz (↑)": [round(calinski_harabasz_score(X_std, km.labels_), 2), round(calinski_harabasz_score(X_std, agg.labels_), 2)]
}).set_index("Algoritmo")

print("=== EVALUACIÓN COMPARATIVA EN SMALL MNIST ===")
print(metricas_resumen)
```

---
## Selección del Número Óptimo de Clusters $k$ 🔢

### 1. Método del Codo (*Elbow Method*)
Graficamos la Inercia y el Coeficiente de Silueta para un rango de $k \in [2, 12]$. Buscamos el punto de inflexión donde incrementos posteriores en $k$ ofrecen rendimientos marginales decrecientes.

```python
rango_k = range(2, 13)
inercias = []
silhouettes = []

for k in rango_k:
    modelo_k = KMeans(n_clusters=k, init="k-means++", n_init="auto", random_state=42).fit(X_std)
    inercias.append(modelo_k.inertia_)
    silhouettes.append(silhouette_score(X_std, modelo_k.labels_))

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 4.2))

# Gráfico de Inercia
ax1.plot(list(rango_k), inercias, "bo-", lw=2, markersize=6)
ax1.axvline(x=10, color="#dc2626", linestyle="--", label="k=10 (Codo Sugerido)")
ax1.set_title("Método del Codo: Inercia (WCSS)", fontweight="bold")
ax1.set_xlabel("Número de Clusters (k)")
ax1.set_ylabel("Inercia Total")
ax1.legend()
ax1.grid(True, alpha=0.3)

# Gráfico de Silhouette Score
ax2.plot(list(rango_k), silhouettes, "rs--", lw=2, markersize=6)
ax2.axvline(x=10, color="#dc2626", linestyle="--", label="k=10")
ax2.set_title("Coeficiente de Silueta por Valor de k", fontweight="bold")
ax2.set_xlabel("Número de Clusters (k)")
ax2.set_ylabel("Silhouette Score Promedio")
ax2.legend()
ax2.grid(True, alpha=0.3)

plt.suptitle("Diagnóstico Conjunto para la Selección del Número Óptimo de Clusters", fontsize=13, fontweight="bold")
plt.tight_layout()
plt.show()
```

---
### 2. Estadístico Gap (*Gap Statistic*)

El Estadístico Gap compara formalmente el logaritmo de la inercia observada $\log W_k$ con el valor esperado bajo una distribución de referencia espacial nula y uniforme:

$$\text{Gap}(k) = \mathbb{E}^\ast[\log W_k] - \log W_k$$

<div align="center">
  <img src="images/gapstat.jpg" alt="Estadístico Gap" width="60%"/>
  <p style="color: #64748b; font-size: 0.85em;">Figura 1: El valor óptimo de $k$ maximiza la brecha entre la inercia real y la distribución uniforme nula.</p>
</div>

---
## Benchmark Comparativo Masivo en Datasets Sintéticos 🔬

Evaluamos K-Means y DBSCAN sobre 3 geometrías sintéticas clásicas para observar sus fronteras de decisión y comportamiento espacial:

```python
import time
from sklearn.datasets import make_circles, make_moons, make_blobs

n_muestras = 300
datasets_benchmark = [
    ("Blobs Esféricos", *make_blobs(n_samples=n_muestras, centers=3, random_state=42)),
    ("Lunas No Lineales", *make_moons(n_samples=n_muestras, noise=0.07, random_state=42)),
    ("Anillos Concéntricos", *make_circles(n_samples=n_muestras, factor=0.5, noise=0.05, random_state=42)),
]

algoritmos = [
    ("K-Means (k=3)", KMeans(n_clusters=3, random_state=42)),
    ("K-Means (k=2)", KMeans(n_clusters=2, random_state=42)),
    ("DBSCAN",        DBSCAN(eps=0.3, min_samples=5)),
]

fig, axes = plt.subplots(len(datasets_benchmark), len(algoritmos), figsize=(14, 10))

for fila, (nombre_ds, X_ds, _) in enumerate(datasets_benchmark):
    X_s = StandardScaler().fit_transform(X_ds)
    for col, (nombre_alg, alg) in enumerate(algoritmos):
        t0 = time.time()
        pred = alg.fit_predict(X_s)
        t_ejecucion = (time.time() - t0) * 1000
        ax = axes[fila, col]
        mascara = pred != -1
        ax.scatter(X_s[mascara, 0], X_s[mascara, 1], c=pred[mascara], cmap="tab10", s=22, alpha=0.8)
        if (-1 in pred):
            ax.scatter(X_s[~mascara, 0], X_s[~mascara, 1], c="black", marker="x", s=40, label="Ruido")
        if fila == 0:
            ax.set_title(nombre_alg, fontweight="bold", fontsize=11)
        if col == 0:
            ax.set_ylabel(nombre_ds, fontweight="bold", fontsize=10)
        ax.set_xticks([])
        ax.set_yticks([])
        ax.grid(True, alpha=0.2)

plt.suptitle("Benchmark de Algoritmos de Clustering en Geometrías Complejas", fontsize=13, fontweight="bold", y=0.99)
plt.tight_layout()
plt.show()
```

---
#### 🛠️ Práctica: Evaluación Multicriterio

**Ejercicio 1:**
Para un dataset sintético con 4 clusters reales (`make_blobs(n_samples=400, centers=4, random_state=42)`), calcula en un bucle el `silhouette_score`, `davies_bouldin_score` y `calinski_harabasz_score` para $k \in [2, 3, 4, 5, 6]$. Crea un DataFrame resumen y verifica si las 3 métricas coinciden en señalar $k=4$ como el óptimo.

```python
# Ejercicio 1 — Escribe tu código aquí
from sklearn.datasets import make_blobs

X_eval, _ = make_blobs(n_samples=400, centers=4, random_state=42)
X_eval_std = StandardScaler().fit_transform(X_eval)

# resultados = []
# for k in [2, 3, 4, 5, 6]:
#     ...
# df_eval = pd.DataFrame(resultados).set_index("k")
# print(df_eval)
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
resultados = []
for k in [2, 3, 4, 5, 6]:
    km_test = KMeans(n_clusters=k, n_init="auto", random_state=42).fit(X_eval_std)
    resultados.append({
        "k": k,
        "Inercia (↓)": round(km_test.inertia_, 2),
        "Silhouette (↑)": round(silhouette_score(X_eval_std, km_test.labels_), 4),
        "Davies-Bouldin (↓)": round(davies_bouldin_score(X_eval_std, km_test.labels_), 4),
        "Calinski-Harabasz (↑)": round(calinski_harabasz_score(X_eval_std, km_test.labels_), 1)
    })

df_resumen = pd.DataFrame(resultados).set_index("k")
print(df_resumen)
# Observación: k=4 alcanza el máximo Silhouette, el mínimo Davies-Bouldin y el máximo Calinski-Harabasz.```
</details>

---
### Resumen y Preguntas de Autoevaluación 🧠

1. **¿Por qué la Inercia por sí sola no permite elegir $k$?**  
   *Respuesta:* Porque la inercia decrece monotónicamente conforme $k$ aumenta. Alcanza cero cuando $k=n$, pero un modelo donde cada observación es su propio cluster carece de valor analítico.

2. **¿Qué indica un valor del Coeficiente de Silueta cercano a -1 para una muestra?**  
   *Respuesta:* Indica que la muestra está en promedio mucho más cerca de los miembros de un cluster vecino que de los miembros de su propio cluster asignado, señalando una mala partición.

3. **¿Cuál es la ventaja analítica del Estadístico Gap sobre el método visual del codo?**  
   *Respuesta:* Proporciona una prueba formal cuantitativa al comparar la varianza observada contra una distribución nula aleatoria, eliminando la ambigüedad y subjetividad del juicio visual humano.

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos</i>
  </p>
</div>
