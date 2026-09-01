# Módulo 03: Análisis y Manipulación de Datos con Pandas 🐼

> **Especialización en Ciencia de Datos**  
> **Universidad Santo Tomás — Seccional Tunja**  
> **Docente:** Santiago A. Zúñiga M.  
> **Contacto:** [gestorvirtualcienciadatos@ustatunja.edu.co](mailto:gestorvirtualcienciadatos@ustatunja.edu.co)

---

## 📌 Descripción General

**Pandas** es la biblioteca por excelencia para la manipulación, limpieza, transformación y análisis estructurado de datos tabulares y series temporales en Python.

A lo largo de este módulo dominarás las estructuras de datos fundamentales (`Series` y `DataFrames`), la lectura y escritura eficiente de múltiples formatos de archivos (CSV, Excel, JSON, Parquet), técnicas avanzadas de filtrado e indexación con `loc` e `iloc`, transformaciones y agregaciones grupales (*Group By*), y cruces relacionales estilo base de datos SQL (*Merge, Join, Concat*).

---

## 🗺️ Estructura del Módulo

| # | Cuaderno Interactivo | Temas Principales | Dificultad |
|:---:|---|---|:---:|
| **00** | [**Introducción a Pandas**](00_Introduccion_Pandas.ipynb) | Filosofía de diseño, ventajas sobre NumPy en datos heterogéneos y conceptos de estructuras tabulares. | 🟢 Básico |
| **01** | [**Estructuras de Datos: Series y DataFrames**](01_Estructuras_de_Datos_Pandas.ipynb) | Anatomía de una `Series` (índice y valores) y de un `DataFrame` (columnas, filas e índices explícitos). | 🟢 Básico |
| **02** | [**Importación y Exportación de Datos**](02_Importacion_y_Exportacion_Pandas.ipynb) | Lectura y almacenamiento en formatos CSV (`read_csv`), Excel (`read_excel`), JSON y Parquet, con gestión de codificación y delimitadores. | 🟢 Básico |
| **03** | [**Exploración y Diagnóstico de Datos**](03_Exploracion_de_Datos_Pandas.ipynb) | Inspección preliminar con `.info()`, `.describe()`, `.head()`, `.tail()`, `.shape`, `.dtypes` y `.value_counts()`. | 🟢 Básico |
| **04** | [**Indexación, Selección y Filtrado**](04_Indexacion_y_Seleccion_Pandas.ipynb) | Selección por etiqueta (`loc`), selección posicional (`iloc`), filtros condicionales booleanos y operadores lógicos (`&`, `|`, `~`). | 🟡 Intermedio |
| **05** | [**Asignación y Modificación de Datos**](05_Asignacion_de_Datos_Pandas.ipynb) | Modificación de valores, operaciones condicionales con `.apply()`, `np.where()`, reemplazo de datos y advertencias de `SettingWithCopyWarning`. | 🟡 Intermedio |
| **06** | [**Añadir y Eliminar Columnas**](06_Anadir_y_Eliminar_Columnas_Pandas.ipynb) | Creación de columnas calculadas, inserción posicional con `.insert()`, renombrado con `.rename()` y eliminación con `.drop()`. | 🟢 Básico |
| **07** | [**Agrupación y Ordenamiento (Group By)**](07_Agrupacion_y_Ordenamiento_Pandas.ipynb) | El patrón *Split-Apply-Combine* con `.groupby()`, agregaciones múltiples con `.agg()`, filtros con `.filter()` y ordenamiento con `.sort_values()`. | 🟡 Intermedio |
| **08** | [**Fusión Relacional de Datos (Merge, Join, Concat)**](08_Fusion_de_Datos_Pandas.ipynb) | Cruces relacionales de tipo SQL (*Inner, Left, Right, Outer Joins*) con `pd.merge()`, unión por índices con `.join()` y concatenación con `pd.concat()`. | 🧗 Avanzado |

---

## 💡 Guías "Para Dummies" (Explicaciones Intuitivas Sin Jerga Compleja)

* [**00. Introducción a Pandas (Dummies)**](Para%20Dummies/00_Introduccion_Pandas_Dummies.ipynb): La hoja de cálculo supercargada con esteroides.
* [**01. Series y DataFrames (Dummies)**](Para%20Dummies/01_Estructuras_de_Datos_Pandas_Dummies.ipynb): Columnas de recibos y tablas completas de datos.
* [**02. Importar y Exportar (Dummies)**](Para%20Dummies/02_Importacion_y_Exportacion_Pandas_Dummies.ipynb): Abrir y guardar archivos CSV y Excel en un parpadeo.
* [**03. Diagnóstico de Datos (Dummies)**](Para%20Dummies/03_Exploracion_de_Datos_Pandas_Dummies.ipynb): La radiografía médica de la tabla con .info() y .describe().
* [**04. Indexación y Filtros (Dummies)**](Para%20Dummies/04_Indexacion_y_Seleccion_Pandas_Dummies.ipynb): Buscar clientes por su nombre (loc) o por su número de fila (iloc).
* [**05. Modificar Datos (Dummies)**](Para%20Dummies/05_Asignacion_de_Datos_Pandas_Dummies.ipynb): Corregir errores y aplicar descuentos automáticos con apply().
* [**06. Añadir y Borrar Columnas (Dummies)**](Para%20Dummies/06_Anadir_y_Eliminar_Columnas_Pandas_Dummies.ipynb): Agregar nuevas columnas y desechar las que no sirven.
* [**07. Agrupaciones GroupBy (Dummies)**](Para%20Dummies/07_Agrupacion_y_Ordenamiento_Pandas_Dummies.ipynb): Separar por ciudades, calcular totales y juntar el reporte.
* [**08. Fusión de Tablas Merge (Dummies)**](Para%20Dummies/08_Fusion_de_Datos_Pandas_Dummies.ipynb): Cruzar la lista de clientes con la lista de facturas.

---

## 📂 Conjuntos de Datos (*Datasets*)

En este módulo se emplean los siguientes datasets ubicados en la carpeta `data/`:
- `winemag-data-130k-v2.csv`: Reseñas y calificaciones de más de 130,000 vinos a nivel internacional.
- `climate_precip.csv`: Mediciones de precipitaciones por estación meteorológica y fecha.
- `climate_temp.csv`: Registros de temperaturas mínimas y máximas por estación meteorológica y fecha.

---

## 📝 Talleres Prácticos Evaluativos (*Hands-On Homeworks*)

* 📝 [**03a_Pandas_Hands_On_Local.ipynb**](../homeworks/03a_Pandas_Hands_On_Local.ipynb): Taller práctico diseñado para ejecutarse localmente.
* 📝 [**03b_Pandas_Hands_On_Kaggle.ipynb**](../homeworks/03b_Pandas_Hands_On_Kaggle.ipynb): Taller práctico estructurado para Kaggle Datasets.
* 💡 [**03a_Pandas_Hands_On_Local_Dummies.ipynb**](../homeworks/Para%20Dummies/03a_Pandas_Hands_On_Local_Dummies.ipynb): Taller guiado paso a paso para no ingenieros.

---

<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos</i>
  </p>
</div>
