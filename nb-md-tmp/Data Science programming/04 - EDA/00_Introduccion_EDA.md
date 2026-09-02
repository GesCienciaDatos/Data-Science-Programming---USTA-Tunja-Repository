# 00_Introduccion_EDA

<table style="width: 100%; border-collapse: collapse; border: none; background: #f8fafc; border-left: 6px solid #1e3a8a; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #0f172a; font-size: 2.1em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        Introducción al Análisis Exploratorio de Datos (EDA) 🔍
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
        Módulo 04
      </span><br>
      <span style="color: #64748b; font-size: 0.85em;">Docente: Santiago A. Zúñiga M.</span><br>
      <a href="mailto:gestorvirtualcienciadatos@ustatunja.edu.co" style="color: #2563eb; font-size: 0.8em; text-decoration: none; font-weight: 500;">gestorvirtualcienciadatos@ustatunja.edu.co</a>
    </td>
  </tr>
</table>

<div align="center" style="margin-top: 15px; margin-bottom: 15px;">
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/04%20-%20EDA/00_Introduccion_EDA.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## Objetivos de Aprendizaje 🔎

En este cuarto módulo aprenderemos a aplicar el **Análisis Exploratorio de Datos (*Exploratory Data Analysis - EDA*)**, la fase más crítica para descubrir la estructura íntima, los patrones, las anomalías y las hipótesis ocultas en un conjunto de datos antes de construir cualquier modelo. El material está organizado progresivamente en los siguientes cuadernos interactivos:

1. **[Introducción al EDA](00_Introduccion_EDA.ipynb)** *(Este cuaderno)*: Filosofía, objetivos e importancia del EDA en el flujo de trabajo de Ciencia de Datos.
2. **[Exploración Preliminar](01_Exploracion_Preliminar_EDA.ipynb)**: Primer contacto con los datos: dimensiones, tipos de datos, inspección de valores nulos y muestreo inicial.
3. **[Estadística Descriptiva](02_Estadistica_Descriptiva_EDA.ipynb)**: Resumen cuantitativo: medidas de tendencia central (media, mediana), dispersión (desviación estándar, IQR) y forma (asimetría, curtosis).
4. **[Visualización de Datos](03_Visualizacion_de_Datos_EDA.ipynb)**: Análisis visual univariado, bivariado y multivariado (histogramas, diagramas de caja, gráficos de dispersión y mapas de calor).
5. **[Librerías de Visualización: Pandas, Seaborn y Matplotlib](04_Librerias_de_Visualizacion_EDA.ipynb)**: Selección de la herramienta gráfica adecuada según la complejidad y el objetivo comunicativo.
6. **[Comparación Práctica de Librerías](05_Comparacion_Librerias_Visualizacion.ipynb)**: Comparativa de sintaxis y capacidades visuales entre Matplotlib y Seaborn.
7. **[Resumen de Funciones y Cheat Sheet](06_Resumen_de_Funciones_EDA.ipynb)**: Guía rápida de consulta con las funciones y métodos fundamentales para auditoría exploratoria.

> 🧗 **Nota:** Los temas con mayor nivel de complejidad están identificados con el ícono de escalador.

---
## Recursos Recomendados 📚

### 📖 Libros de Referencia:
- [Exploratory Data Analysis](https://www.pearson.com/en-us/subject-catalog/p/exploratory-data-analysis/P200000003504) — *John W. Tukey (pionero del concepto)*
- [Storytelling with Data: A Data Visualization Guide for Business Professionals](https://www.storytellingwithdata.com/book) — *Cole Nussbaumer Knaflic*
- [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/) — *Jake VanderPlas*

### 🌐 Enlaces y Documentación Oficial:
- [Harvard CS109A: Introduction to Data Science](https://harvard-iacs.github.io/2021-CS109A/)
- [Galería y Tutoriales Oficiales de Seaborn](https://seaborn.pydata.org/tutorial.html)
- [Guía de Usuario Oficial de Matplotlib](https://matplotlib.org/stable/tutorials/index.html)

*Basado en: Practical Data Science Lessons (Riccardo Bertoglio, Politecnico di Milano)*

---
## 1. ¿Qué es el Análisis Exploratorio de Datos (EDA)? 🔍

El **Análisis Exploratorio de Datos (EDA - *Exploratory Data Analysis*)** es el enfoque analítico y filosófico introducido formalmente por el matemático y estadístico **John Tukey** en 1977. Consiste en interrogar y examinar críticamente un conjunto de datos antes de aplicar cualquier modelo formal de inferencia o Machine Learning.

### ¿Por qué es el paso más importante en Ciencia de Datos?
1. **Comprender la estructura subyacente:** Dimensiones, tipos de variables, distribuciones y escalas.
2. **Diagnosticar la calidad del dato:** Detección de valores atípicos (*outliers*), datos faltantes (*missing values*), duplicados y registros anómalos.
3. **Validar o refutar hipótesis iniciales:** Comprobación de supuestos estadísticos (normalidad, homocedasticidad, linealidad).
4. **Descubrir patrones ocultos y correlaciones:** Identificar relaciones no lineales, agrupaciones naturales y variables predictoras clave.

> 📌 **Frase Célebre de John Tukey:**  
> *"El análisis exploratorio de datos es una actitud, un estado de flexibilidad mental y una búsqueda abierta de lo que los datos pueden decirnos, más que una confirmación de lo que creemos saber."*

---
## 2. Los Cuatro Pilares del EDA Moderno 🏛️

```
                    ┌───────────────────────────────┐
                    │    Pilares del Análisis EDA   │
                    └───────────────┬───────────────┘
                                    │
    ┌────────────────┬──────────────┴───────────────┬────────────────┐
    ▼                ▼                              ▼                ▼
┌──────────────┐ ┌──────────────┐             ┌──────────────┐ ┌──────────────┐
│  Inspección  │ │  Estadística │             │ Visualización│ │  Ingeniería  │
│  Preliminar  │ │ Descriptiva  │             │  Estratégica │ │de Features   │
└──────────────┘ └──────────────┘             └──────────────┘ └──────────────┘
  • Shape          • Centralidad (Media/Mediana) • Univariada    • Dummies
  • Tipos/Dtypes   • Dispersión (IQR/Std)        • Bivariada     • Agrupaciones
  • Nulos          • Forma (Skewness/Kurtosis)   • Multivariada  • Ratios/Flags
```

---
## 3. La Advertencia del Cuarteto de Anscombe ⚠️

En 1973, el estadístico Francis Anscombe construyó cuatro conjuntos de datos sintéticos que demuestran por qué **la estadística numérica aislada es insuficiente** sin visualización gráfica:

* Los cuatro datasets tienen **exactamente la misma media** ($\mu_x = 9.0$, $\mu_y = 7.5$).
* Tienen **exactamente la misma varianza** ($\sigma_x^2 = 11.0$, $\sigma_y^2 = 4.12$).
* Tienen **la misma correlación lineal** ($r = 0.816$) y la misma recta de regresión ($y = 3.0 + 0.5x$).
* Sin embargo, al graficarlos, uno es una relación lineal estándar, otro es una curva cuadrática perfecta, otro tiene un outlier vertical y otro tiene un punto de apalancamiento extremo.

> 💡 **Lección Fundamental:** *Nunca confíes ciegamente en resúmenes numéricos sin graficar tus datos.*

```python
# Configuración de interactividad en Jupyter Notebooks
try:
    from IPython.core.interactiveshell import InteractiveShell
    InteractiveShell.ast_node_interactivity = 'all'
except Exception:
    pass
try:
    from IPython.display import display
except Exception:
    pass

# Librerías base para manipulación y computación
import pandas as pd
import numpy as np

# Librerías base para visualización de datos
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración de estilo visual uniforme
sns.set_theme(style="whitegrid", palette="muted")
plt.rcParams["figure.figsize"] = (10, 5)
plt.rcParams["font.size"] = 11

import warnings
warnings.filterwarnings("ignore")

print("✅ Entorno configurado para Análisis Exploratorio de Datos (EDA).")
print(f"📦 Versiones cargadas: Pandas {pd.__version__} | Seaborn {sns.__version__} | Matplotlib {plt.matplotlib.__version__}")
```

---
### Demostración Rápida de Exploración Visual

Carguemos un dataset clásico integrado en Seaborn (`tips`) para una inspección visual inmediata:

```python
# Carga rápida de un dataset de prueba
df_tips = sns.load_dataset('tips')

# Resumen visual univariado y bivariado en una sola gráfica
fig, axes = plt.subplots(1, 2, figsize=(12, 4))

# Histograma con KDE de la cuenta total
sns.histplot(data=df_tips, x='total_bill', kde=True, ax=axes[0], color='#1e3a8a')
axes[0].set_title("Distribución de la Cuenta Total (total_bill)")

# Boxplot de propina según el día
sns.boxplot(data=df_tips, x='day', y='tip', palette='Blues', ax=axes[1])
axes[1].set_title("Propinas por Día de la Semana")

plt.tight_layout()
plt.show()
```

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos</i>
  </p>
</div>
