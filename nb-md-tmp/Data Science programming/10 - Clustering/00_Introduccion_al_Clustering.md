# 00_Introduccion_al_Clustering

<table style="width: 100%; border-collapse: collapse; border: none; background: #f8fafc; border-left: 6px solid #1e3a8a; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #0f172a; font-size: 2.1em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        Introducción al Clustering y Aprendizaje No Supervisado 🌐
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
        Módulo 10 • Cuaderno 00
      </span><br>
      <span style="color: #64748b; font-size: 0.85em;">Docente: Santiago A. Zúñiga M.</span><br>
      <a href="mailto:gestorvirtualcienciadatos@ustatunja.edu.co" style="color: #2563eb; font-size: 0.8em; text-decoration: none; font-weight: 500;">gestorvirtualcienciadatos@ustatunja.edu.co</a>
    </td>
  </tr>
</table>

<div align="center" style="margin-top: 15px; margin-bottom: 15px;">
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/10%20-%20Clustering/00_Introduccion_al_Clustering.ipynb" target="_parent">
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
## Resultados de Aprendizaje y Estructura del Módulo 🔎

En este módulo dominarás las principales metodologías de **Aprendizaje No Supervisado** para descubrir patrones intrínsecos, subgrupos naturales y estructuras latentes en datos sin etiquetas:

* **Cuaderno 00:** ¿Qué es el Clustering? — Fundamentos, aplicaciones reales, agricultura y ecosistema de paquetes.
* **Cuaderno 01:** Métricas de Distancia y Estandarización de Variables para Agrupamiento.
* **Cuaderno 02:** K-Means y Métodos Particionales (Algoritmo de Lloyd y K-Means++).
* **Cuaderno 03:** Clustering Jerárquico Aglomerativo, Matrices de Enlace y Dendrogramas.
* **Cuaderno 04:** DBSCAN y Clustering Basado en Densidad (Detección de ruido y geometrías complejas).
* **Cuaderno 05:** Métricas de Evaluación, Selección del Número Óptimo de Clusters $k$ y Benchmark Comparativo.

#### Recursos y Bibliografía Recomendada 📚
* **Teoría y Fundamentos:**
  * [An Introduction to Statistical Learning (ISLR) — James, Witten, Hastie & Tibshirani](https://www.statlearning.com/)
  * [K-Means Explicado Visualmente — Video de StatQuest en YouTube](https://youtu.be/4b5d3muPQmA?si=ChIcwBpU1M6THIXZ)
  * [Notas de Clase de K-Means — Universidad de Stanford (CS221)](https://stanford.edu/~cpiech/cs221/handouts/kmeans.html)
* **Práctica y Desarrollo:**
  * [Guía de Usuario de Scikit-Learn: Algoritmos de Clustering](https://scikit-learn.org/stable/modules/clustering.html)
  * [Tópicos Avanzados en Ciencia de Datos — Universidad de Harvard (CS109-B)](https://harvard-iacs.github.io/2022-CS109B)
  * [Guía Práctica: 7 Métodos para Seleccionar el Número Óptimo de Clusters en Python](https://towardsdatascience.com/cheat-sheet-to-implementing-7-methods-for-selecting-optimal-number-of-clusters-in-python-898241e1d6ad)

---
## Objetivos de Aprendizaje 🎯

| # | Objetivo |
|:---:|---|
| 1 | Comprender la naturaleza del **Aprendizaje No Supervisado** y en qué se diferencia del Aprendizaje Supervisado. |
| 2 | Identificar casos de uso industriales y agrícolas donde el clustering genera alto impacto operativo. |
| 3 | Configurar el ecosistema completo de librerías en Python necesarias para análisis de clustering. |
| 4 | Diferenciar los conceptos de homogeneidad intra-cluster y separación inter-cluster. |

---
## ¿Qué es el Clustering? 🧩

El **Clustering** (o agrupamiento) es una técnica fundamental del **Aprendizaje Automático No Supervisado** cuyo propósito es organizar un conjunto de observaciones no etiquetadas en subgrupos o *clusters* homogéneos.

El principio rector del clustering es doble:
1. **Maximizar la similitud intra-cluster:** Los puntos asignados al mismo grupo deben compartir características muy cercanas entre sí.
2. **Minimizar la similitud inter-cluster:** Los distintos grupos deben estar lo más separados y diferenciados posible.

A diferencia del aprendizaje supervisado (donde contamos con una variable objetivo $y$ que guía el entrenamiento), en el clustering **no existen respuestas correctas predeterminadas**; el algoritmo explora la geometría espacial del conjunto de datos para revelar su estructura intrínseca.

### Comparativa: Aprendizaje Supervisado vs. Clustering

| Criterio | Aprendizaje Supervisado | Clustering (No Supervisado) |
|---|---|---|
| **Datos de Entrada** | Características $X$ y Etiquetas $y$ | Únicamente Características $X$ |
| **Meta Principal** | Predecir la salida correcta para nuevos datos | Descubrir taxonomías y patrones ocultos |
| **Validación** | Exactitud, Precisión, Recall, MSE, $R^2$ | Coeficiente de Silueta, Inercia, Davies-Bouldin |
| **Ejemplo Típico** | Clasificar correos en Spam o No Spam | Segmentar clientes por hábitos de consumo |

---
## Aplicaciones del Clustering en la Industria y la Tecnología 💼

* **Detección de Anomalías y Fraude:** Al agrupar comportamientos normales recurrentes, los puntos aislados que no pertenecen a ningún cluster consolidado se identifican inmediatamente como posibles fraudes bancarios, fallas mecánicas en turbinas o intrusiones en redes de ciberseguridad.

* **Segmentación de Clientes y Mercado:** Agrupación de usuarios según volumen de compras, frecuencia, edad y preferencias de navegación, permitiendo diseñar campañas publicitarias hiper-personalizadas y programas de fidelización.

* **Compresión y Procesamiento de Imágenes:** Cuantización de paletas de color y reducción del tamaño de archivos al agrupar millones de píxeles en $k$ colores representativos mediante sus centroides.

* **Modelado de Temas y Minería de Textos (NLP):** Agrupamiento semántico de miles de artículos, noticias o documentos legales mediante representaciones vectoriales TF-IDF o embeddings densos.

* **Ingeniería de Características (*Feature Engineering*):** Creación de nuevas variables categóricas que codifican el cluster de pertenencia espacial para alimentar modelos supervisados posteriores.

* **Sistemas de Recomendación:** Agrupamiento de usuarios con perfiles de afinidad compartidos para sugerir contenido personalizado (ejemplo: las listas *Daily Mix* de Spotify o recomendaciones de Netflix).

<div align="center">
  <img src="images/spotify_dailymix.png" width="480" alt="Ejemplo de Clustering en Spotify Daily Mix" style="border-radius: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.1); margin: 12px 0;"/>
  <p style="color: #64748b; font-size: 0.85em;">Figura 1: Las listas personalizadas de Spotify agrupan canciones por similitud acústica y hábitos de reproducción.</p>
</div>

---
## Aplicaciones del Clustering en el Sector Agropecuario 🚜

* **Agricultura de Precisión y Manejo por Zonas:** El clustering permite identificar zonas homogéneas dentro de un lote de cultivo a partir de lecturas de sensores de suelo (pH, conductividad eléctrica, humedad) y características topográficas. Esto habilita la **fertilización y el riego a tasa variable**, ahorrando insumos y agua.

* **Análisis de Imágenes Satelitales y Teledetección:** Agrupamiento de firmas espectrales (como índices NDVI, EVI e infrarrojo cercano) para clasificar tipos de cobertura vegetal, detectar estrés hídrico temprano y monitorear la salud del cultivo.

* **Planificación de Rotación de Cultivos:** Clasificación de variedades agrícolas según sus demandas nutricionales y susceptibilidad a plagas, optimizando cronogramas de siembra para conservar la fertilidad del suelo.

---
## Importación del Ecosistema de Paquetes en Python 📦

A continuación cargamos todas las librerías científicas que utilizaremos a lo largo del módulo:

```python
# Importación de librerías esenciales para Ciencia de Datos y Clustering
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Modelos y utilidades de Scikit-Learn
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.neighbors import NearestNeighbors
from sklearn.metrics import silhouette_score, calinski_harabasz_score, davies_bouldin_score

# Rutinas de clustering jerárquico y cálculo de distancias con SciPy
import scipy.cluster.hierarchy as hac
from scipy.spatial import distance
from scipy.spatial.distance import pdist

%matplotlib inline
print("✅ Librerías fundamentales importadas exitosamente.")
```

```python
# Paquete opcional: gap-stat para el cálculo del Estadístico Gap
# Si no lo tienes instalado, ejecuta en tu terminal o celda: !pip install gap-stat
try:
    from gap_statistic import OptimalK
    print("✅ Paquete gap_statistic listo para evaluación.")
except ImportError:
    print("ℹ️ gap_statistic no está instalado. Si deseas usar OptimalK en el Cuaderno 05 ejecuta: pip install gap-stat")
```

```python
# Paquete opcional: yellowbrick para visualizadores de codo y silueta
# ⚠️ Nota: Yellowbrick modifica algunos estilos globales de Matplotlib.
try:
    from yellowbrick.cluster import silhouette_visualizer, kelbow_visualizer
    print("✅ Paquete yellowbrick listo para diagnósticos visuales.")
except ImportError:
    print("ℹ️ yellowbrick no está instalado. Si deseas usar kelbow_visualizer ejecuta: pip install yellowbrick")
```

---
#### 🛠️ Práctica: Identificación y Formulación de Problemas de Clustering

**Ejercicio 1:**
Analiza los siguientes tres problemas empresariales e indica para cada uno si debe resolverse con **Aprendizaje Supervisado (Clasificación / Regresión)** o con **Clustering (No Supervisado)**, justificando tu respuesta:

1. **Caso A:** Un banco dispone de un histórico de 100,000 préstamos pasados con la columna `Pago_A_Tiempo` (valores: `Sí` / `No`) y desea predecir el riesgo de un nuevo solicitante.
2. **Caso B:** Una plataforma de streaming cuenta con 500,000 usuarios y su registro de horas dedicadas a 20 géneros musicales, buscando crear 5 canales temáticos automáticos.
3. **Caso C:** Un agrónomo recolecta muestras de suelo en una finca de 200 hectáreas con valores de nitrógeno, fósforo y potasio, y desea delimitar 3 zonas de manejo agronómico sin etiquetado previo.

```python
# Ejercicio 1 — Escribe tus respuestas y justificaciones como variables de texto
respuesta_caso_A = """Tu justificación aquí"""
respuesta_caso_B = """Tu justificación aquí"""
respuesta_caso_C = """Tu justificación aquí"""

print("Caso A:", respuesta_caso_A)
print("Caso B:", respuesta_caso_B)
print("Caso C:", respuesta_caso_C)
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada y análisis docente...</b></summary>

```python
# Solución Explicada:
# Caso A -> APRENDIZAJE SUPERVISADO (Clasificación Binaria):
#   Existe una variable objetivo explícita (Pago_A_Tiempo) que el modelo debe predecir.
#
# Caso B -> CLUSTERING (No Supervisado):
#   No existen etiquetas preexistentes; el algoritmo debe descubrir grupos de usuarios
#   con patrones de escucha similares en el espacio de 20 dimensiones de géneros.
#
# Caso C -> CLUSTERING (No Supervisado):
#   Se busca segmentar el terreno en zonas homogéneas a partir de nutrientes sin que nadie
#   haya asignado previamente categorías manuales al suelo.
```
</details>

---
### Resumen y Preguntas de Autoevaluación 🧠

1. **¿Por qué decimos que en Clustering no existe una métrica de "Exactitud" (*Accuracy*) directa?**  
   *Respuesta:* Porque no disponemos de etiquetas verdaderas (*Ground Truth*) contra las cuales contrastar. La calidad se evalúa mediante cohesión interna y separación geométrica entre clusters.

2. **¿En qué consiste el beneficio del clustering para la detección de anomalías?**  
   *Respuesta:* Las observaciones que caen en zonas de bajísima densidad espacial o que quedan muy distantes de cualquier centroide representan comportamientos atípicos o anomalías potenciales.

3. **¿Cómo impacta el clustering en la agricultura moderna?**  
   *Respuesta:* Permite delimitar unidades de manejo agronómico homogéneas para aplicar agua y fertilizantes exactamente donde se necesitan, reduciendo costos operativos y minimizando el impacto ambiental.

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos</i>
  </p>
</div>
