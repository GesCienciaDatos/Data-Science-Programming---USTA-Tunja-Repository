# 00_Introduccion_Data_Preparation

<table style="width: 100%; border-collapse: collapse; border: none; background: #f8fafc; border-left: 6px solid #1e3a8a; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #0f172a; font-size: 2.1em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        Introducción a la Preparación y Limpieza de Datos 🧹
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
        Módulo 05
      </span><br>
      <span style="color: #64748b; font-size: 0.85em;">Docente: Santiago A. Zúñiga M.</span><br>
      <a href="mailto:gestorvirtualcienciadatos@ustatunja.edu.co" style="color: #2563eb; font-size: 0.8em; text-decoration: none; font-weight: 500;">gestorvirtualcienciadatos@ustatunja.edu.co</a>
    </td>
  </tr>
</table>

<div align="center" style="margin-top: 15px; margin-bottom: 15px;">
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/05%20-%20Data%20Preparation/00_Introduccion_Data_Preparation.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## Objetivos de Aprendizaje 🔎

En este quinto módulo abordaremos una de las tareas más críticas, exigentes y determinantes para cualquier Científico de Datos: la **Preparación y Limpieza de Datos (*Data Cleaning / Data Wrangling*)**. El material está organizado progresivamente en los siguientes cuadernos interactivos:

1. **[Introducción a la Preparación de Datos](00_Introduccion_Data_Preparation.ipynb)** *(Este cuaderno)*: Fundamentos, ciclo de saneamiento de datos y el impacto del ruido en los modelos analíticos.
2. **[Valores Faltantes (Missing Values)](01_Valores_Faltantes_Data_Preparation.ipynb)**: Mecanismos de ausencia (MCAR, MAR, MNAR), diagnóstico de nulos, eliminación justificada e imputación con Pandas y Scikit-Learn (`SimpleImputer`, `KNNImputer`).
3. **[Escalado de Características (Feature Scaling)](02_Escalado_Caracteristicas_Data_Preparation.ipynb)**: Normalización (*Min-Max Scaling*), Estandarización (*StandardScaler*), transformaciones robustas (*RobustScaler*) y sensibilidad algorítmica.
4. **[Fechas y Datos Inconsistentes](03_Fechas_y_Datos_Inconsistentes_Data_Preparation.ipynb)**: Parseo y validación de fechas (`pd.to_datetime`), extracción de componentes temporales y corrección de entradas de texto irregulares con *Fuzzy Matching* (`fuzzywuzzy`).

> 🧗 **Nota:** Los temas con mayor nivel de complejidad teórica y técnica están identificados con el ícono de escalador.

---
## Recursos Recomendados 📚

### 📖 Libros de Referencia:
- [Data Preparation for Machine Learning](https://machinelearningmastery.com/data-preparation-for-machine-learning/) — *Jason Brownlee*
- [Python for Data Analysis](https://wesmckinney.com/book/) — *Wes McKinney*
- [Feature Engineering and Selection](http://www.feat.engineering/) — *Max Kuhn & Kjell Johnson*

### 🌐 Enlaces y Documentación Oficial:
- [Curso de Kaggle: Data Cleaning](https://www.kaggle.com/learn/data-cleaning)
- [Guía de Usuario de Scikit-Learn: Preprocessing data](https://scikit-learn.org/stable/modules/preprocessing.html)
- [Guía de Usuario de Scikit-Learn: Imputation of missing values](https://scikit-learn.org/stable/modules/impute.html)
- [Normalization vs Standardization — Quantitative analysis](https://towardsdatascience.com/normalization-vs-standardization-quantitative-analysis-a91e8a79cebf)

*Basado en: Practical Data Science Lessons (Riccardo Bertoglio, Politecnico di Milano)*

---
## 1. ¿Por qué es Crítica la Preparación de Datos? 🧹

En los proyectos reales de Ciencia de Datos e Inteligencia Artificial, los datos casi nunca se presentan en formatos perfectamente limpios y tabulados. Suelen contener errores tipográficos, registros incompletos, fechas en formatos inconsistentes, escalas dispares y valores faltantes.

### La Regla del 80/20 en Ciencia de Datos:
Estudios empíricos (como la encuesta anual de Kaggle y KDnuggets) revelan consistentemente que los Científicos de Datos dedican **entre el 70% y el 80% de su tiempo** a la adquisición, diagnóstico, limpieza y transformación de datos, dejando el 20% restante al entrenamiento de modelos.

```
  ┌─────────────────────────────────────────────────────────────┐
  │  75% - 80%: Preparación, Limpieza e Ingeniería de Datos    │
  └──────────────────────────────────────────────┬──────────────┘
                                                 │
  ┌──────────────────────────────────────────────▼──────────────┐
  │  20% - 25%: Modelado, Ajuste de Hiperparámetros y Despliegue│
  └─────────────────────────────────────────────────────────────┘
```

> 📌 **El Principio GIGO (*Garbage In, Garbage Out*):**  
> Ningún algoritmo de Machine Learning, por sofisticado que sea (Redes Neuronales Profundas, XGBoost o Transformers), puede extraer patrones de valor si se alimenta con datos corruptos, mal escalados o con fugas de información (*Data Leakage*).

---
## 2. Taxonomía de los Problemas de Datos 🛠️

| Categoría | Problemas Frecuentes | Impacto en el Modelo | Cuaderno del Módulo |
|---|---|---|:---:|
| **Valores Faltantes (*Missing Values*)** | `NaN`, `None`, registros en blanco, códigos nulos (`-999`, `?`). | Errores de ejecución en algoritmos, sesgo en la estimación de parámetros. | `01_Valores_Faltantes` |
| **Escalas Heterogéneas** | Variables en rangos de 0 a 1 vs otras en rangos de 0 a 1,000,000. | Dominancia artificial en algoritmos basados en distancia (KNN, SVM, K-Means, PCA). | `02_Escalado_Caracteristicas` |
| **Fechas y Componentes Temporales** | Fechas almacenadas como texto (`object`), formatos mezclados (`DD/MM/YY` vs `MM/DD/YYYY`). | Imposibilidad de extraer estacionalidad, tendencias o realizar ordenamientos cronológicos. | `03_Fechas_y_Datos_Inconsistentes` |
| **Inconsistencias Textuales (*Typos*)** | Variaciones tipográficas (`'Colombia'`, `'colombia '`, `'colomiba'`). | Fragmentación artificial de categorías y explosión de cardinalidad. | `03_Fechas_y_Datos_Inconsistentes` |

---
## Configuración del Entorno y Verificación 🛠️

Importemos las librerías fundamentales requeridas para la preparación y limpieza de datos:

```python
# Configuración de interacción en Jupyter Notebooks
try:
    from IPython.core.interactiveshell import InteractiveShell
    InteractiveShell.ast_node_interactivity = 'all'
except Exception:
    pass
try:
    from IPython.display import display
except Exception:
    pass

# Librerías base
import pandas as pd
import numpy as np
import datetime

# Preprocesamiento con Scikit-Learn
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler
from sklearn.impute import SimpleImputer, KNNImputer

# Visualización estadística
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración de estilo visual
sns.set_theme(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 5)

import warnings
warnings.filterwarnings("ignore")

print("✅ Entorno preparado para Preparación y Limpieza de Datos.")
print(f"📦 Versiones cargadas: Pandas {pd.__version__} | NumPy {np.__version__}")
```

---
### Demostración Rápida: Diagnóstico de Datos Faltantes

Carguemos un dataset de demostración con datos faltantes e inspeccionemos su impacto porcentual:

```python
# Dataset de prueba con valores nulos integrados (Titanic)
df_titanic = sns.load_dataset('titanic')

# Diagnóstico rápido de valores faltantes por columna
nulos_por_columna = df_titanic.isnull().sum()
porcentaje_nulos = (nulos_por_columna / len(df_titanic)) * 100

resumen_nulos = pd.DataFrame({
    'Valores_Faltantes': nulos_por_columna,
    'Porcentaje (%)': porcentaje_nulos
})

# Mostramos las columnas con al menos un valor nulo
resumen_nulos[resumen_nulos['Valores_Faltantes'] > 0].sort_values(by='Porcentaje (%)', ascending=False)
```

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos</i>
  </p>
</div>
