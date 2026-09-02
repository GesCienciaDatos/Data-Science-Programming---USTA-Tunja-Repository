# 00_Introduccion_Pandas

<table style="width: 100%; border-collapse: collapse; border: none; background: #f8fafc; border-left: 6px solid #1e3a8a; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #0f172a; font-size: 2.1em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        Introducción a Pandas y Análisis de Datos Tabulares 🐼
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
        Módulo 03
      </span><br>
      <span style="color: #64748b; font-size: 0.85em;">Docente: Santiago A. Zúñiga M.</span><br>
      <a href="mailto:gestorvirtualcienciadatos@ustatunja.edu.co" style="color: #2563eb; font-size: 0.8em; text-decoration: none; font-weight: 500;">gestorvirtualcienciadatos@ustatunja.edu.co</a>
    </td>
  </tr>
</table>

<div align="center" style="margin-top: 15px; margin-bottom: 15px;">
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/03%20-%20Pandas/00_Introduccion_Pandas.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## Objetivos de Aprendizaje 🔎

En este tercer módulo dominaremos **Pandas**, la herramienta estándar en la industria para la ingesta, limpieza, exploración, manipulación y transformación de datos tabulares y series temporales. El material está organizado progresivamente en los siguientes cuadernos interactivos:

1. **[Introducción a Pandas](00_Introduccion_Pandas.ipynb)** *(Este cuaderno)*: ¿Qué es Pandas, cómo se relaciona con NumPy y por qué es la navaja suiza del analista de datos?
2. **[Estructuras de Datos de Pandas](01_Estructuras_de_Datos_Pandas.ipynb)**: Los dos pilares fundamentales: `Series` unidimensionales y `DataFrames` tabulares bidimensionales.
3. **[Importación y Exportación de Datos](02_Importacion_y_Exportacion_Pandas.ipynb)**: Lectura y escritura en diversos formatos estructurados (`read_csv`, `read_excel`, `read_json`, `to_csv`, `to_parquet`).
4. **[Exploración de Datos](03_Exploracion_de_Datos_Pandas.ipynb)**: Diagnóstico rápido de datasets mediante atributos (`shape`, `dtypes`) y métodos clave (`head`, `info`, `describe`, `value_counts`).
5. **[Indexación y Selección de Datos](04_Indexacion_y_Seleccion_Pandas.ipynb)**: Extracción precisa de subconjuntos mediante posición (`iloc`), etiquetas (`loc`) y filtrado con máscaras booleanas.
6. **[Asignación y Modificación de Datos](05_Asignacion_de_Datos_Pandas.ipynb)**: Mutación de celdas, operaciones condicionales y prevención de advertencias `SettingWithCopyWarning`.
7. **[Añadir y Eliminar Columnas](06_Añadir_y_Eliminar_Columnas_Pandas.ipynb)**: Creación de variables derivadas, método `insert`, eliminación segura con `drop` y asignación funcional.
8. **[Agrupación y Ordenamiento](07_Agrupacion_y_Ordenamiento_Pandas.ipynb)**: El paradigma *Split-Apply-Combine* con `groupby`, funciones de agregación múltiple (`agg`) y ordenamiento (`sort_values`).
9. **[Fusión y Combinación de Datos (Merge, Join, Concat)](08_Fusion_de_Datos_Pandas.ipynb)** 🧗: Cruces relacionales estilo SQL (Inner, Left, Right y Outer Joins) y concatenación de tablas con `concat`.

> 🧗 **Nota:** Los temas con mayor nivel de abstracción y complejidad están identificados con el ícono de escalador.

---
## Recursos Recomendados 📚

### 📖 Libros de Referencia:
- [Python for Data Analysis: Data Wrangling with pandas, NumPy & Jupyter (3rd Edition)](https://wesmckinney.com/book/) — *Wes McKinney (creador de Pandas)*
- [Pandas in Action](https://www.manning.com/books/pandas-in-action) — *Boris Paskhaver*
- [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/) — *Jake VanderPlas*

### 🌐 Enlaces y Documentación Oficial:
- [Guía de Usuario Oficial de Pandas](https://pandas.pydata.org/docs/user_guide/index.html)
- [10 Minutes to pandas (Guía Rápida Oficial)](https://pandas.pydata.org/docs/user_guide/10min.html)
- [Pandas Cookbook (Recetario con soluciones a problemas comunes)](https://pandas.pydata.org/pandas-docs/stable/user_guide/cookbook.html)

*Basado en: Practical Data Science Lessons (Riccardo Bertoglio, Politecnico di Milano)*

---
## 1. ¿Qué es Pandas y por qué es el Estándar en Ciencia de Datos? 🐼

**Pandas** es la biblioteca de código abierto más popular y potente para la manipulación, estructuración, análisis y limpieza de **datos tabulares** en Python. Fue desarrollada originalmente en 2008 por **Wes McKinney** en el sector financiero cuantitativo (AQR Capital Management) ante la necesidad de contar con una herramienta flexible, expresiva y de alto rendimiento para el análisis de series temporales y tablas relacionales.

### Los Dos Pilares Estructurales de Pandas:
1. **`Series` (1D):** Arreglos unidimensionales etiquetados homogéneos (equivalentes a una columna en Excel o una variable estadística).
2. **`DataFrame` (2D):** Estructuras tabulares bidimensionales con filas y columnas etiquetadas (equivalentes a una tabla SQL o una hoja de cálculo).

> 📌 **Concepto Clave:** Pandas está construido directamente sobre **NumPy**. Esto significa que combina la velocidad computacional de los arrays en C con la flexibilidad de indexación por etiquetas de texto y manejo nativo de datos faltantes (`NaN`).

---
## 2. Ventajas Competitivas de Pandas 🚀

* 📊 **Alineación Automática por Índices:** Realiza operaciones entre tablas y series alineando automáticamente las etiquetas de filas y columnas, evitando desajustes de datos.
* 🧹 **Tratamiento Robusto de Valores Faltantes:** Identificación, imputación y eliminación sistemática de datos nulos (`NaN`, `None`).
* 🔀 **Operaciones Relacionales Tipo SQL:** `merge()`, `join()`, `concat()` y agregaciones complejas con `groupby()`.
* 📁 **Conectividad Universal de E/S:** Lectura y escritura optimizada para CSV, Excel (`.xlsx`), JSON, SQL, Parquet, Feather y HDF5.
* ⏱️ **Manipulación Avanzada de Series Temporales:** Conversión de zonas horarias, remuestreo (*resampling*), ventanas móviles (*rolling windows*) y desfases (*lagging*).

---
## 3. Arquitectura del Flujo de Trabajo en Ciencia de Datos 🔄

```
  ┌───────────────────────┐
  │  Ingesta de Datos     │ ──► pd.read_csv(), pd.read_parquet(), pd.read_sql()
  └───────────┬───────────┘
              │
  ┌───────────▼───────────┐
  │  Exploración y Perfil │ ──► df.info(), df.describe(), df.shape, df.head()
  └───────────┬───────────┘
              │
  ┌───────────▼───────────┐
  │  Limpieza y Selección │ ──► df.loc[], df.dropna(), df.drop_duplicates()
  └───────────┬───────────┘
              │
  ┌───────────▼───────────┐
  │  Transformación / FE  │ ──► df.groupby(), df.merge(), df.apply()
  └───────────┬───────────┘
              │
  ┌───────────▼───────────┐
  │  Modelado / ML        │ ──► Scikit-Learn, PyTorch, XGBoost
  └───────────────────────┘
```

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

# Importación estándar de Pandas y NumPy
import pandas as pd
import numpy as np

# Configuración de visualización de DataFrames
pd.set_option('display.max_columns', 15)
pd.set_option('display.precision', 2)

print("✅ Entorno preparado para manipulación de datos con Pandas.")
print(f"📦 Versión de Pandas: {pd.__version__}")
```

---
### Demostración Rápida de un DataFrame

Creemos un `DataFrame` a partir de un diccionario de Python y visualicemos su estructura:

```python
# Creación de un DataFrame de ejemplo
datos = {
    'Ciudad': ['Bogotá', 'Medellín', 'Tunja', 'Cali', 'Bucaramanga'],
    'Poblacion_k': [7900, 2600, 180, 2200, 580],
    'Altitud_msnm': [2640, 1495, 2775, 1018, 959],
    'Sede_USTA': [True, True, True, False, True]
}

df_ejemplo = pd.DataFrame(datos)
df_ejemplo
```

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos</i>
  </p>
</div>
