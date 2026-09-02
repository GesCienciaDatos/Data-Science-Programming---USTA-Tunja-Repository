# 01_Metricas_de_Distancia_y_Estandarizacion

<table style="width: 100%; border-collapse: collapse; border: none; background: #f8fafc; border-left: 6px solid #1e3a8a; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #0f172a; font-size: 2.1em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        Métricas de Distancia y Estandarización para Clustering 📏
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
        Módulo 10 • Cuaderno 01
      </span><br>
      <span style="color: #64748b; font-size: 0.85em;">Docente: Santiago A. Zúñiga M.</span><br>
      <a href="mailto:gestorvirtualcienciadatos@ustatunja.edu.co" style="color: #2563eb; font-size: 0.8em; text-decoration: none; font-weight: 500;">gestorvirtualcienciadatos@ustatunja.edu.co</a>
    </td>
  </tr>
</table>

<div align="center" style="margin-top: 15px; margin-bottom: 15px;">
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/10%20-%20Clustering/01_Metricas_de_Distancia_y_Estandarizacion.ipynb" target="_parent">
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
| 1 | Definir matemática y computacionalmente las métricas Euclidiana, Manhattan, Coseno y Hamming. |
| 2 | Evaluar experimentalmente cómo la elección de la métrica transforma los clusters formados. |
| 3 | Comprender por qué la estandarización de escala con `StandardScaler` es obligatoria en clustering. |
| 4 | Visualizar datos multidimensionales con PCA antes de calcular matrices de distancias. |

---
## Métricas de Distancia en Espacios Multidimensionales 📏

El concepto de **similitud** en clustering se formaliza a través de funciones matemáticas de distancia. Dadas dos observaciones $p = (p_1, p_2, \dots, p_d)$ y $q = (q_1, q_2, \dots, q_d)$ en $\mathbb{R}^d$:

### 1. Distancia Euclidiana (Norma $\ell_2$)
Mide la longitud geométrica en línea recta entre dos puntos:
$$d_{\text{Eucl}}(p, q) = \|p - q\|_2 = \sqrt{\sum_{i=1}^d (p_i - q_i)^2}$$

### 2. Distancia Manhattan / Cityblock (Norma $\ell_1$)
Mide la distancia recorrida a lo largo de ejes perpendiculares (como las manzanas de una cuadrícula urbana):
$$d_{\text{Manh}}(p, q) = \|p - q\|_1 = \sum_{i=1}^d |p_i - q_i|$$

<div align="center">
  <img src="images/manhattan_distance.svg" width="280" alt="Distancia Euclidiana vs Manhattan" style="margin: 10px 0;"/>
  <p style="color: #64748b; font-size: 0.85em;">Figura 1: La línea verde representa la distancia Euclidiana; las líneas roja, azul y amarilla representan trayectorias Manhattan equivalentes.</p>
</div>

### 3. Similitud y Distancia del Coseno
Cuantifica el ángulo entre dos vectores, siendo independiente de su magnitud o norma. Es la métrica estándar para minería de textos, procesamiento de lenguaje natural y embeddings:
$$\text{Sim}_{\cos}(u, v) = \frac{u \cdot v}{\|u\|_2 \|v\|_2} = \frac{\sum_{i=1}^d u_i v_i}{\sqrt{\sum u_i^2}\sqrt{\sum v_i^2}}, \quad d_{\cos}(u, v) = 1 - \text{Sim}_{\cos}(u, v)$$

### 4. Distancia de Hamming
Para vectores categóricos o binarios, mide la proporción de componentes en las que ambos vectores difieren:
$$d_H(u, v) = \frac{1}{d} \sum_{i=1}^d \mathbb{I}(u_i \neq v_i)$$

```python
# Demostración del impacto de la métrica de distancia en la formación de clusters
# Adaptado del ejemplo clásico de Gael Varoquaux en Scikit-Learn
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering

np.random.seed(0)
X_demo = np.random.randn(24, 2)

metricas = ["euclidean", "cityblock", "cosine"]
fig, axes = plt.subplots(1, 3, figsize=(15, 4.2))

for ax, metrica in zip(axes, metricas):
    enlace = "average" if metrica == "cosine" else "complete"
    modelo = AgglomerativeClustering(n_clusters=3, metric=metrica, linkage=enlace)
    etiquetas = modelo.fit_predict(X_demo)
    ax.scatter(X_demo[:, 0], X_demo[:, 1], c=etiquetas, cmap="tab10", s=70, edgecolors="k")
    ax.set_title(f"Métrica: {metrica.capitalize()}\n(Enlace: {enlace})", fontweight="bold")
    ax.grid(True, alpha=0.3)

plt.suptitle("Impacto Crítico de la Métrica de Distancia en la Agrupación Espacial", fontsize=13, fontweight="bold")
plt.tight_layout()
plt.show()
```

---
## La Importancia Crítica de la Estandarización de Escalas ⚖️

> [!WARNING]
> Los algoritmos de clustering calculan distancias numéricas en $\mathbb{R}^d$. Si una variable se expresa en millones (ej. Salario: $2,000,000$) y otra en decenas (ej. Edad: $25$), la variable de mayor magnitud **dominará completamente** el cálculo de distancias, haciendo que la edad tenga influencia nula en la formación de clusters.

Para corregir este sesgo, aplicamos `StandardScaler`:
$$z = \frac{x - \mu}{\sigma} \quad \implies \quad \mu_z = 0, \; \sigma_z = 1$$

```python
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import euclidean_distances

# Demostración con 3 perfiles de clientes: [Edad (años), Salario Anual (COP)]
clientes = np.array([
    [25,  20_000_000],  # Joven, ingreso bajo
    [27,  21_000_000],  # Joven, ingreso muy similar al cliente 1
    [65,  20_000_000],  # Adulto mayor, exactamente el mismo ingreso del cliente 1
])

scaler = StandardScaler()
clientes_std = scaler.fit_transform(clientes)

# Cálculo de distancias sin escalar
d_sin_1_2 = euclidean_distances([clientes[0]], [clientes[1]])[0, 0]
d_sin_1_3 = euclidean_distances([clientes[0]], [clientes[2]])[0, 0]

# Cálculo de distancias con estandarización
d_con_1_2 = euclidean_distances([clientes_std[0]], [clientes_std[1]])[0, 0]
d_con_1_3 = euclidean_distances([clientes_std[0]], [clientes_std[2]])[0, 0]

print("=== RESULTADOS DEL ESCALADO ===")
print(f"Distancia SIN Escalar (Cliente 1 vs 2): {d_sin_1_2:,.2f}")
print(f"Distancia SIN Escalar (Cliente 1 vs 3): {d_sin_1_3:,.2f}")
print(f"\nDistancia CON StandardScaler (Cliente 1 vs 2): {d_con_1_2:.4f}")
print(f"Distancia CON StandardScaler (Cliente 1 vs 3): {d_con_1_3:.4f}")
print("\n💡 Conclusión: Sin estandarizar, la diferencia de salario eclipsó la edad por un factor de 100,000x.")
```

```python
# Visualización de la distribución antes y después de estandarizar
from sklearn.datasets import load_digits
digits = load_digits()
X_dig = digits.data
X_dig_std = StandardScaler().fit_transform(X_dig)

fig, axes = plt.subplots(1, 2, figsize=(12, 4.2))
axes[0].hist(X_dig.ravel(), bins=40, color="#3b82f6", alpha=0.8, edgecolor="none")
axes[0].set_title("Distribución Original de Intensidades (0 a 16)", fontweight="bold")
axes[0].set_xlabel("Valor de Píxel")
axes[0].set_ylabel("Frecuencia")
axes[0].grid(True, alpha=0.3)

axes[1].hist(X_dig_std.ravel(), bins=40, color="#10b981", alpha=0.8, edgecolor="none")
axes[1].set_title(r"Distribución Estandarizada ($\mu=0, \sigma=1$)", fontweight="bold")
axes[1].set_xlabel("Puntuación z")
axes[1].set_ylabel("Frecuencia")
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

---
#### 🛠️ Práctica: Métricas y Estandarización

**Ejercicio 1:**
Dispones de cuatro clientes con las variables `[Edad, Ingreso_Mensual, Horas_Conexion_Semanal]`. Calcula la matriz de distancias Euclidianas $4 \times 4$ antes y después de aplicar `StandardScaler`. Determina qué par de clientes es el más similar en cada escenario.

```python
# Ejercicio 1 — Escribe tu código aquí
matriz_clientes = np.array([
    [21, 1_200_000, 35],
    [23, 1_300_000, 38],
    [55, 1_250_000, 8],
    [58, 9_500_000, 5]
])

# D_original = ...
# D_escalada = ...
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import euclidean_distances
import pandas as pd

# 1. Matriz de distancias sin estandarizar
D_sin = euclidean_distances(matriz_clientes)
print("Matriz de Distancias SIN Estandarizar:")
print(pd.DataFrame(D_sin, index=["C1","C2","C3","C4"], columns=["C1","C2","C3","C4"]).round(1))

# 2. Matriz con StandardScaler
clientes_escalados = StandardScaler().fit_transform(matriz_clientes)
D_con = euclidean_distances(clientes_escalados)
print("\nMatriz de Distancias CON StandardScaler:")
print(pd.DataFrame(D_con, index=["C1","C2","C3","C4"], columns=["C1","C2","C3","C4"]).round(4))
# Observación: Tras estandarizar, los clientes más cercanos son C1 y C2 (jóvenes con alta conexión).```
</details>

---
### Resumen y Preguntas de Autoevaluación 🧠

1. **¿Por qué la distancia de Coseno es insensible a la longitud de un documento de texto?**  
   *Respuesta:* Porque normaliza los vectores dividiéndolos por sus normas euclidianas, evaluando únicamente la dirección angular del vector de frecuencias.

2. **¿Cuándo es preferible utilizar la distancia Manhattan sobre la Euclidiana?**  
   *Respuesta:* En espacios de alta dimensionalidad (donde la distancia Euclidiana sufre por la maldición de la dimensionalidad) o cuando existen valores atípicos (*outliers*) moderados que inflarían el cuadrado de las diferencias.

3. **¿Qué consecuencias matemáticas tiene omitir la estandarización antes de aplicar K-Means?**  
   *Respuesta:* Las isolíneas de distancia se convierten en elipses extremadamente alargadas en lugar de esferas, provocando que el algoritmo solo agrupe según las características de mayor varianza absoluta.

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos</i>
  </p>
</div>
