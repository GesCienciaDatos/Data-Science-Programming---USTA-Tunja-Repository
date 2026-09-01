# Módulo 10: Clustering y Aprendizaje No Supervisado (Clustering & Unsupervised Learning) 🔮🧩

> **Especialización en Ciencia de Datos**  
> **Universidad Santo Tomás — Seccional Tunja**  
> **Docente:** Santiago A. Zúñiga M.  
> **Contacto:** [gestorvirtualcienciadatos@ustatunja.edu.co](mailto:gestorvirtualcienciadatos@ustatunja.edu.co)

---

## 📌 Descripción del Módulo

Este módulo cubre de manera exhaustiva y matemática el **Aprendizaje No Supervisado (*Unsupervised Learning*)** y los **Métodos de Agrupamiento (*Clustering*)**, esenciales para la minería de datos, segmentación de clientes, sistemas de recomendación y descubrimiento de patrones latentes sin etiquetas previas:
* **Fundamentos y Espacios Métricos:** Naturaleza del aprendizaje no supervisado, formulación de funciones de distancia métrica (**Euclidiana $L_2$**, **Manhattan $L_1$**, **Coseno**, **Minkowski**) y efecto crítico de la estandarización (`StandardScaler`, `MinMaxScaler`).
* **Métodos Particionales (K-Means):** Algoritmo de Lloyd (pasos de asignación y actualización), partición del espacio en teselaciones de Voronoi, inicialización inteligente **K-Means++**, función de pérdida de inercia (**WCSS**) y optimización para grandes volúmenes con **MiniBatchKMeans**.
* **Clustering Jerárquico Aglomerativo (HAC):** Paradigma ascendente (*Bottom-Up*), criterios de enlace (**Single**, **Complete**, **Average**, **Ward's Minimum Variance**), matrices de enlace SciPy y construcción, interpretación y corte de **Dendrogramas**.
* **Clustering Basado en Densidad (DBSCAN):** Conceptos de $\varepsilon$-vecindad y `min_samples`, clasificación de puntos (**Núcleo**, **Borde**, **Ruido / Outliers**), gráfico de $k$-distancias para estimación de $\varepsilon$ y agrupamiento robusto en geometrías no convexas (semilunas, anillos concéntricos).
* **Validación Cuantitativa y Selección de $k$:** Métricas de validación interna (**Coeficiente de Silueta**, **Índice de Davies-Bouldin**, **Índice de Calinski-Harabasz**), método del codo (*Elbow Method*), *Gap Statistic* y benchmark comparativo global.

---

## 📓 Cuadernos de Clase (Notebooks)

El módulo se compone de **5 cuadernos interactivos estándar** y **5 guías complementarias *Para Dummies***:

| Cuaderno Estándar | Guía Para Dummies | Temáticas Principales |
|---|---|---|
| [**00_Introduccion_Clustering_y_Metricas_Distancia.ipynb**](00_Introduccion_Clustering_y_Metricas_Distancia.ipynb) | [**00_Introduccion_Clustering_y_Metricas_Distancia_Dummies.ipynb**](Para%20Dummies/00_Introduccion_Clustering_y_Metricas_Distancia_Dummies.ipynb) | Fundamentos de clustering, aplicaciones industriales (Spotify Daily Mix), distancias métricas (Euclidiana, Manhattan, Coseno) e impacto del escalado. |
| [**01_KMeans_y_Metodos_Particionales.ipynb**](01_KMeans_y_Metodos_Particionales.ipynb) | [**01_KMeans_y_Metodos_Particionales_Dummies.ipynb**](Para%20Dummies/01_KMeans_y_Metodos_Particionales_Dummies.ipynb) | Algoritmo de Lloyd, convergencia de centroides, inicialización K-Means++, inercia WCSS, fronteras de Voronoi y MiniBatchKMeans. |
| [**02_Clustering_Jerarquico_Aglomerativo_y_Dendrogramas.ipynb**](02_Clustering_Jerarquico_Aglomerativo_y_Dendrogramas.ipynb) | [**02_Clustering_Jerarquico_Aglomerativo_y_Dendrogramas_Dummies.ipynb**](Para%20Dummies/02_Clustering_Jerarquico_Aglomerativo_y_Dendrogramas_Dummies.ipynb) | Paradigma HAC (Bottom-Up), métodos de enlace (Ward, Complete, Single, Average), matriz de enlace SciPy y dendrogramas jerárquicos. |
| [**03_DBSCAN_y_Clustering_Basado_en_Densidad.ipynb**](03_DBSCAN_y_Clustering_Basado_en_Densidad.ipynb) | [**03_DBSCAN_y_Clustering_Basado_en_Densidad_Dummies.ipynb**](Para%20Dummies/03_DBSCAN_y_Clustering_Basado_en_Densidad_Dummies.ipynb) | Densidad espacial, puntos núcleo, borde y ruido (-1), gráfico de $k$-distancias para ajuste de $\varepsilon$ y agrupamiento no convexo. |
| [**04_Validacion_Seleccion_K_y_Benchmark_Comparativo.ipynb**](04_Validacion_Seleccion_K_y_Benchmark_Comparativo.ipynb) | [**04_Validacion_Seleccion_K_y_Benchmark_Comparativo_Dummies.ipynb**](Para%20Dummies/04_Validacion_Seleccion_K_y_Benchmark_Comparativo_Dummies.ipynb) | Coeficiente de Silueta, Davies-Bouldin, Calinski-Harabasz, método del codo, Gap Statistic y gran benchmark comparativo. |

---

## 📂 Conjuntos de Datos (*Datasets*)

* **`data/mall_customers.csv`:** Conjunto de datos de segmentación de clientes en centro comercial (200 registros con ID, Género, Edad, Ingreso Anual en miles de USD y Puntuación de Gasto).

---

## 🛠️ Utilidades y Funciones del Módulo

* **`functions/clustering_metrics.py`:** Cálculo de matrices de incidencia, correlación y sumas cuadráticas dentro (WSS) y entre (BSS) clusters.
* **`functions/dendrogram_util.py`:** Utilidad para graficar dendrogramas jerárquicos con cortes dinámicos y visualización de hojas.

---

## 📝 Talleres Prácticos Evaluativos (*Homeworks*)

* [**10_Clustering_Hands_On.ipynb**](../homeworks/10_Clustering_Hands_On.ipynb) — Taller evaluativo de 5 partes (Preprocesamiento, K-Means con análisis de inercia y codo, Dendrograma HAC con corte de umbral, DBSCAN con detección de anomalías y benchmark cuantitativo).
* [**10_Clustering_Hands_On_Dummies.ipynb**](../homeworks/Para%20Dummies/10_Clustering_Hands_On_Dummies.ipynb) — Taller guiado paso a paso con la analogía del gerente de tienda departamental.

---

<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Plataforma de Laboratorios Virtuales</i>
  </p>
</div>
