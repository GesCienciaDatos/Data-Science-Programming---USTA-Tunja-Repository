# 10_Clustering_Hands_On

<table style="width: 100%; border-collapse: collapse; border: none; background: #f8fafc; border-left: 6px solid #1e3a8a; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #0f172a; font-size: 2.1em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        Taller Práctico Evaluativo: Clustering y Aprendizaje No Supervisado (Hands-On Lab)
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
        Taller Práctico • Módulo 10
      </span><br>
      <span style="color: #64748b; font-size: 0.85em;">Docente: Santiago A. Zúñiga M.</span><br>
      <a href="mailto:gestorvirtualcienciadatos@ustatunja.edu.co" style="color: #2563eb; font-size: 0.8em; text-decoration: none; font-weight: 500;">gestorvirtualcienciadatos@ustatunja.edu.co</a>
    </td>
  </tr>
</table>

<div align="center" style="margin-top: 15px; margin-bottom: 15px;">
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/homeworks/10_Clustering_Hands_On.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## 🎯 Objetivo General del Taller

El objetivo de este taller es aplicar de forma rigurosa y autónoma los algoritmos fundamentales de **Aprendizaje No Supervisado (*Clustering*)** sobre un conjunto de datos real de segmentación de clientes (`mall_customers.csv`). 

El estudiante deberá diagnosticar, preprocesar, modelar con **K-Means**, **Clustering Jerárquico (HAC)** y **DBSCAN**, optimizar hiperparámetros y evaluar cuantitativamente la calidad de los agrupamientos mediante métricas de validación interna.

---
## 🛠️ Configuración Inicial del Entorno

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

def load_dataset(filename, module_folder="10 - Clustering"):
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

print("🚀 Entorno configurado exitosamente para el Módulo 10: Clustering.")
```

---
### 📌 Parte 1: Carga, Diagnóstico y Estandarización de Datos

1. Carga el dataset `mall_customers.csv` utilizando la función `load_dataset('mall_customers.csv', '10 - Clustering')`.
2. Muestra las primeras 5 filas y la información de tipos de datos y valores nulos.
3. Extrae la matriz $X$ con las características continuas `Annual_Income_k` y `Spending_Score`.
4. Aplica `StandardScaler` sobre $X$ para obtener $X_{	ext{scaled}}$. Justifica brevemente por qué es indispensable este paso.

```python
### TU CÓDIGO AQUÍ ###
```

---
### 📌 Parte 2: Segmentación con K-Means y Selección del $k$ Óptimo

1. Ejecuta un ciclo iterativo para evaluar `KMeans` con $k \in [2, 10]$ utilizando `init='k-means++'` y `random_state=42`.
2. Almacena la inercia (WCSS) y el `silhouette_score` para cada $k$.
3. Grafica en dos subplots: la curva del **Método del Codo** y la curva del **Coeficiente de Silueta**.
4. Determina el $k$ óptimo e imprime las coordenadas des-escaladas de los centroides finales.

```python
### TU CÓDIGO AQUÍ ###
```

---
### 📌 Parte 3: Clustering Jerárquico Aglomerativo (HAC) y Dendrograma

1. Calcula la matriz de enlace con `scipy.cluster.hierarchy.linkage` utilizando el método `'ward'` y métrica `'euclidean'`.
2. Grafica el **Dendrograma Jerárquico** y dibuja una línea horizontal de corte que genere el mismo número de clusters óptimo seleccionado en la Parte 2.
3. Ajusta la clase `AgglomerativeClustering` de Scikit-Learn con el $k$ óptimo y compara la asignación de clusters con la de K-Means mediante una tabla de contingencia o gráfico de dispersión.

```python
### TU CÓDIGO AQUÍ ###
```

---
### 📌 Parte 4: Detección de Patrones No Convexos y Anomalías con DBSCAN

1. Construye el **gráfico de $k$-distancias** utilizando `NearestNeighbors(n_neighbors=5)` para estimar el valor óptimo de $arepsilon$ (`eps`).
2. Ajusta un modelo `DBSCAN(min_samples=5)` utilizando el $arepsilon$ identificado.
3. Reporta el número de clusters encontrados y el número de clientes clasificados como ruido (`-1`).
4. Genera un gráfico de dispersión destacando los clientes clasificados como anomalías.

```python
### TU CÓDIGO AQUÍ ###
```

---
### 📌 Parte 5: Benchmark Cuantitativo y Conclusiones de Negocio

1. Construye un DataFrame resumen comparando **K-Means**, **HAC (Ward)** y **DBSCAN** (excluyendo ruido para DBSCAN) en las siguientes métricas:
   * **Silhouette Score** (mayor es mejor)
   * **Davies-Bouldin Index** (menor es mejor)
   * **Calinski-Harabasz Index** (mayor es mejor)
2. Redacta una conclusión ejecutiva interpretando los perfiles de los segmentos descubiertos y formulando una recomendación estratégica para el equipo de mercadeo.

```python
### TU CÓDIGO AQUÍ ###
# Conclusión del Estudiante:
```

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Taller Práctico Evaluativo</i>
  </p>
</div>
