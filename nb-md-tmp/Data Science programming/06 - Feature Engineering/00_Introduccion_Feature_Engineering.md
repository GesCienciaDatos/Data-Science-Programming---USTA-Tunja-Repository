# 00_Introduccion_Feature_Engineering

<table style="width: 100%; border-collapse: collapse; border: none; background: #f8fafc; border-left: 6px solid #1e3a8a; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #0f172a; font-size: 2.1em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        Introducción a la Ingeniería de Características (Feature Engineering) ⚙️
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
        Módulo 06
      </span><br>
      <span style="color: #64748b; font-size: 0.85em;">Docente: Santiago A. Zúñiga M.</span><br>
      <a href="mailto:gestorvirtualcienciadatos@ustatunja.edu.co" style="color: #2563eb; font-size: 0.8em; text-decoration: none; font-weight: 500;">gestorvirtualcienciadatos@ustatunja.edu.co</a>
    </td>
  </tr>
</table>

<div align="center" style="margin-top: 15px; margin-bottom: 15px;">
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/06%20-%20Feature%20Engineering/00_Introduccion_Feature_Engineering.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## Objetivos de Aprendizaje 🔎

En este sexto módulo exploraremos la **Ingeniería de Características (*Feature Engineering*)**, una de las disciplinas más determinantes y creativas dentro de la Ciencia de Datos y el Machine Learning.

El contenido se estructura progresivamente a través de los siguientes temas:

1. **[Introducción a Feature Engineering](00_Introduccion_Feature_Engineering.ipynb)** *(Este cuaderno)*: Fundamentos, ciclo de vida e impacto en modelos predictivos.
2. **[Manejo de Variables Categóricas](01_Variables_Categoricas_Feature_Engineering.ipynb)**: Codificación ordinal, One-Hot Encoding, Mean Target Encoding y buenas prácticas.
3. **[Target Encoding y Suavizado (Smoothing)](02_Target_Encoding_y_Suavizado_Feature_Engineering.ipynb)** 🧗: Regularización bayesiana, $m$-estimate, manejo de alta cardinalidad y caso práctico MovieLens 1M.
4. **[Creación de Características (Creating Features)](03_Creacion_de_Caracteristicas_Feature_Engineering.ipynb)**: Transformaciones matemáticas, cocientes, transformaciones logarítmicas, conteos booleanos, descomposición de cadenas y transformaciones agrupadas (*group transforms*).
5. **[Análisis de Componentes Principales (PCA)](05_PCA_Feature_Engineering.ipynb)** 🧗: Reducción de dimensionalidad lineal, ejes de variación, proyecciones ortogonales y descubrimiento de relaciones.
6. **[Selección de Características e Información Mutua](06_Seleccion_Caracteristicas_y_Mutual_Information.ipynb)** 🧗: Métodos de filtro, wrapper y embebidos, entropía, Información Mutua (*Mutual Information*) y detección de interacciones no lineales.

> 🧗 **Nota:** Los temas con mayor nivel de abstracción matemática y complejidad algorítmica están identificados con el ícono de escalador.

---
## Recursos Recomendados 📚

### 📖 Libros de Referencia:
- [An Introduction to Statistical Learning (ISLR)](https://www.statlearning.com/) — *Gareth James, Daniela Witten, Trevor Hastie, Robert Tibshirani*
- [The Kaggle Book: Data analysis and machine learning for competitive data science](https://www.packtpub.com/en-it/product/the-kaggle-book-9781801817479) — *Konrad Banachewicz & Luca Massaron*
- [Feature Engineering and Selection: A Practical Approach for Predictive Models](http://www.feat.engineering/) — *Max Kuhn & Kjell Johnson*

### 🌐 Enlaces y Documentación Oficial:
- [Curso de Kaggle: Feature Engineering](https://www.kaggle.com/learn/feature-engineering)
- [Guía de Usuario de Scikit-Learn: Preprocessing Data](https://scikit-learn.org/stable/modules/preprocessing.html)
- [Guía de Usuario de Scikit-Learn: Feature Selection](https://scikit-learn.org/stable/modules/feature_selection.html)
- [Encoding Categorical Variables: A Deep Dive into Target Encoding](https://towardsdatascience.com/encoding-categorical-variables-a-deep-dive-into-target-encoding-2862217c2753)

---
## 1. ¿Qué es Feature Engineering y por qué es el Factor Determinante? ⚙️

**Feature Engineering (Ingeniería de Características)** es el arte, la ciencia y la disciplina de transformar datos crudos en variables numéricas estructuradas que maximicen el poder predictivo de los algoritmos de Machine Learning.

> 📌 **Frase Clave de Andrew Ng (Stanford / DeepLearning.AI):**  
> *"Aplicar Machine Learning es esencialmente hacer Feature Engineering. Es la parte más difícil, más creativa y la que realmente marca la diferencia entre un modelo mediocre y uno ganador."*

### Los 5 Grandes Pilares del Feature Engineering:
1. **Codificación Categórica Avanzada:** Transformación de variables cualitativas sin sesgo ni explosión dimensional (Ordinal, One-Hot, Target Encoding).
2. **Creación de Ratios y Relaciones Físicas:** Fusión matemática de variables basada en el conocimiento del dominio (e.g. $\text{Densidad} = \frac{\text{Población}}{\text{Área}}$).
3. **Descomposición de Estructuras Complejas:** Extracción de partes informativas en fechas, coordenadas geográficas y campos textuales.
4. **Transformaciones Agrupadas (*Group Transforms*):** Agregaciones estadísticas contextuales (`mean`, `median`, `std`) por segmento de negocio.
5. **Reducción Dimensional y Selección de Variables:** Compresión informativa con PCA y ranking de utilidad con **Información Mutua ($MI$)**.

---
## 2. Mapa Estratégico del Módulo 🗺️

```
┌────────────────────────────────────────────────────────────────────────┐
│               Pipeline Integral de Feature Engineering                 │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
    ┌───────────────────────────────┼───────────────────────────────┐
    ▼                               ▼                               ▼
┌────────────────────────┐      ┌────────────────────────┐      ┌────────────────────────┐
│  01. Variables         │      │  02. Target Encoding   │      │  03. Creación de       │
│      Categóricas       │ ───► │      y Suavizado       │ ───► │      Features          │
│ • Ordinal Encoding     │      │ • Media de la Variable │      │ • Ratios y Fórmulas    │
│ • One-Hot Encoding     │      │ • Suavizado m-estimate │      │ • Logaritmos / Bins    │
│ • Alta Cardinalidad    │      │ • Prevención Overfit   │      │ • Group Transforms     │
└────────────────────────┘      └────────────────────────┘      └───────────┬────────────┘
                                                                            │
    ┌───────────────────────────────────────────────────────────────────────┘
    ▼
┌────────────────────────┐      ┌────────────────────────┐
│  04. PCA               │      │  05. Selección y       │
│      Dimensional       │ ───► │      Mutual Info       │
│ • Rotación de Ejes     │      │ • Información Mutua    │
│ • Cargas / Loadings    │      │ • Métodos Filtro       │
│ • Varianza Explicada   │      │ • Wrappers y Embebidos │
└────────────────────────┘      └────────────────────────┘
```

---
## Configuración del Entorno 🛠️

Para desarrollar las prácticas de este módulo utilizaremos las librerías estándar del ecosistema científico de Python (`pandas`, `numpy`, `scikit-learn`, `matplotlib` y `seaborn`).

```python
try:
    from IPython.core.interactiveshell import InteractiveShell
    InteractiveShell.ast_node_interactivity = 'all'
except Exception:
    pass
try:
    from IPython.display import display
except Exception:
    pass

# Módulos base de computación y manipulación de datos
import pandas as pd
import numpy as np

# Visualización de datos
import matplotlib.pyplot as plt
import seaborn as sns

# Preprocesamiento y Feature Engineering con Scikit-Learn
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder, StandardScaler
from sklearn.decomposition import PCA
from sklearn.feature_selection import mutual_info_regression, mutual_info_classif, SelectKBest

# Configuración de estilo gráfico
sns.set_theme(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 5)

import warnings
warnings.filterwarnings("ignore")

print("✅ Entorno preparado para Ingeniería de Características.")
print(f"📦 Versiones cargadas:\n - Pandas: {pd.__version__}\n - NumPy: {np.__version__}")
```

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos</i>
  </p>
</div>
