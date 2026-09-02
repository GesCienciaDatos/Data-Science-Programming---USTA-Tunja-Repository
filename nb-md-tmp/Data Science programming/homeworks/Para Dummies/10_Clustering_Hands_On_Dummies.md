# 10_Clustering_Hands_On_Dummies

<table style="width: 100%; border-collapse: collapse; border: none; background: #fffbeb; border-left: 6px solid #f59e0b; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #78350f; font-size: 2.1em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        💡 Taller Práctico para Dummies: Agrupando Clientes como un Experto
      </h1>
      <p style="margin: 6px 0 0 0; color: #1e3a8a; font-size: 1.15em; font-weight: 600; font-family: system-ui, -apple-system, sans-serif;">
        Especialización en Ciencia de Datos | Programación para Ciencia de Datos
      </p>
      <p style="margin: 4px 0 0 0; color: #64748b; font-size: 0.95em; font-family: system-ui, -apple-system, sans-serif;">
        Universidad Santo Tomás — Seccional Tunja
      </p>
    </td>
    <td style="text-align: right; vertical-align: middle; border: none; padding: 15px 20px; width: 30%;">
      <span style="background: #f59e0b; color: #ffffff; padding: 6px 14px; border-radius: 20px; font-size: 0.85em; font-weight: 700; display: inline-block; margin-bottom: 8px;">
        💡 Taller Dummies • Módulo 10
      </span><br>
      <span style="color: #64748b; font-size: 0.85em;">Docente: Santiago A. Zúñiga M.</span><br>
      <a href="mailto:gestorvirtualcienciadatos@ustatunja.edu.co" style="color: #2563eb; font-size: 0.8em; text-decoration: none; font-weight: 500;">gestorvirtualcienciadatos@ustatunja.edu.co</a>
    </td>
  </tr>
</table>

<div align="center" style="margin-top: 15px; margin-bottom: 15px;">
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/homeworks/Para%20Dummies/10_Clustering_Hands_On_Dummies.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## 🎯 Reto del Taller: Organizar a los Clientes de una Tienda de Ropa 🛍️

¡Bienvenido al taller práctico de clustering! Tu misión como analista de datos junior es ayudar al gerente de una tienda departamental a descubrir los diferentes tipos de clientes que visitan su local, para enviarles promociones que realmente les interesen.

---
## 🛠️ Configuración Inicial

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
### 📌 Paso 1: Conocer a los Clientes

1. Carga los datos de `mall_customers.csv`.
2. Muestra los primeros 5 clientes para ver qué información tenemos de ellos.

```python
### TU CÓDIGO AQUÍ ###
```

---
### 📌 Paso 2: Escalar y Agrupar con K-Means

1. Selecciona `Annual_Income_k` (Ingreso) y `Spending_Score` (Gasto).
2. Escala las variables con `StandardScaler`.
3. Aplica `KMeans` con $k = 5$ grupos y guarda las etiquetas en el DataFrame.

```python
### TU CÓDIGO AQUÍ ###
```

---
### 📌 Paso 3: Dibujar el Mapa de Clientes

1. Haz un gráfico de dispersión coloreando cada uno de los 5 grupos con un color distinto.
2. Coloca los centroides (las "estaciones de bomberos") en color negro con una 'X'.

```python
### TU CÓDIGO AQUÍ ###
```

---
### 📌 Paso 4: Calificar la Calidad de los Grupos con Silueta

1. Calcula el `silhouette_score` de tu modelo de 5 grupos.
2. Si la silueta es mayor a 0.5, ¡significa que tus grupos están muy bien definidos!

```python
### TU CÓDIGO AQUÍ ###
```

---
### 📌 Paso 5: Veredicto y Recomendación para el Gerente

Describe con tus propias palabras qué tipo de cliente pertenece a cada uno de los 5 grupos (ej. *Ahorradores, Derrochadores, Promedio, VIP, Sensatos*) y qué campaña de mercadeo le recomendarías a cada uno.

```python
# Escribe aquí tu informe final para el gerente:
# Grupo 0: ...
# Grupo 1: ...
# Grupo 2: ...
# Grupo 3: ...
# Grupo 4: ...
```

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Taller Práctico Evaluativo</i>
  </p>
</div>
