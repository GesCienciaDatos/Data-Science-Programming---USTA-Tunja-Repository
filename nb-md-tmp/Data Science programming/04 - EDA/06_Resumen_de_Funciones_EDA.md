# 06_Resumen_de_Funciones_EDA

<table style="width: 100%; border-collapse: collapse; border: none; background: #f8fafc; border-left: 6px solid #1e3a8a; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #0f172a; font-size: 2.1em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        Resumen de Funciones y Hoja de Trucos para EDA 🚀
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
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/04%20-%20EDA/06_Resumen_de_Funciones_EDA.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## Guía Definitiva de Funciones para EDA 📖

A lo largo de este módulo hemos explorado una gran cantidad de herramientas para manipular, describir y visualizar datos. Este cuaderno sirve como tu **diccionario o guía de referencia rápida** (Cheatsheet) para recordar qué hace cada función y, lo más importante, **cuándo usarla**.

Guarda este notebook como tu referencia personal para futuros proyectos de Machine Learning.

---
## 1. Pandas: Manipulación y Exploración

| Función | ¿Qué hace? | ¿Cuándo usarla en EDA? |
| :--- | :--- | :--- |
| `pd.read_csv()` | Carga un archivo CSV como un DataFrame. | **Siempre.** Es el punto de partida (junto con `read_excel`, `read_json`, etc.). |
| `pd.concat()` | Concatena múltiples DataFrames juntos (vertical u horizontalmente). | Cuando tus datos vienen en múltiples archivos (ej. ventas por mes) y necesitas unirlos para analizarlos juntos. |
| `pd.get_dummies()` | Convierte variables categóricas en columnas indicadoras (0 o 1). | Cuando necesitas calcular correlaciones o entrenar modelos con variables de texto (ej. género o nacionalidad). |
| `df.info()` | Muestra un resumen del dataset: columnas, tipos de datos, uso de memoria y conteo de no nulos. | **Primer paso exploratorio.** Para identificar rápidamente si hay valores faltantes o si una columna numérica fue cargada como texto. |
| `df.head()` / `df.tail()` | Retorna las primeras/últimas 5 filas del DataFrame. | Para darle un vistazo rápido a la estructura visual y formato de los datos reales. |
| `df.sample()` | Retorna filas aleatorias. | Mejor que `head()` si los datos están ordenados cronológicamente y quieres ver la diversidad real de registros. |
| `df.describe()` | Genera estadísticas descriptivas (media, min, max, cuartiles). | Para entender la dispersión de los datos y detectar outliers obvios (ej. un valor negativo en edad). |
| `df.unique()` | Retorna todos los valores únicos de una columna (categorías). | Para entender cuántas opciones diferentes existen en una variable categórica (ej. tipos de membresía). |
| `df['col'].str` | Habilita funciones de manipulación de texto vectorizadas (ej. `.str.lower()`, `.str[-1]`). | Cuando necesitas limpiar o extraer partes específicas de un texto en toda una columna masivamente. |
| `df.groupby()` | Agrupa el dataset según los valores de una o más columnas categóricas. | Para comparar métricas entre grupos (ej. calcular el salario promedio agrupado por departamento). |
| `df.sort_values()` | Ordena el DataFrame por los valores de una columna específica. | Crítico antes de dibujar gráficos de líneas (Lineplots) o para encontrar el Top 10 de mejores registros. |
| `df.corr()` | Calcula la matriz de correlación por pares de todas las columnas. | Para encontrar qué variables numéricas tienen relación lineal entre sí. |
| `df.corrwith()` | Calcula la correlación de todas las columnas frente a una Serie específica. | Cuando quieres saber exclusivamente qué variables afectan a tu variable objetivo (Target variable). |
| `df.groupby().size()` | Devuelve el tamaño (número de filas) de cada grupo tras un `groupby`. | Para comprobar si tus clases están desbalanceadas (ej. 90% sanos, 10% enfermos). |

---
## 2. Pandas: Visualización Integrada
Pandas utiliza Matplotlib por debajo para generar gráficos rápidos. Úsalos para **exploración personal**, no para presentaciones.

| Función | ¿Qué hace? | ¿Cuándo usarla en EDA? |
| :--- | :--- | :--- |
| `df.boxplot()` | Diagrama de caja rápido de columnas numéricas. | Para detectar rápidamente valores atípicos masivos de una variable sin importar la estética. |
| `df.hist()` | Genera histogramas de todas las columnas numéricas de golpe. | ¡El mejor atajo de Pandas! Con un solo comando ves la distribución de todo tu dataset numérico en una cuadrícula. |
| `df.plot()` | Dibuja líneas por defecto. | Cuando tus datos están ordenados en el tiempo y solo quieres ver la tendencia. |
| `df.plot.kde()` | Gráfico de densidad de Kernel. | Para observar la curva suavizada de distribución de los datos en lugar de barras cuadradas. |
| `df.plot.pie()` | Dibuja un gráfico circular. | Cuando necesitas graficar la proporción de 2 o 3 categorías (Seaborn no tiene pie plots). |
| `df.plot.scatter()` | Diagrama de dispersión de X vs Y. | Para verificar visualmente la correlación entre dos variables sin importar Seaborn. |

---
## 3. Matplotlib (`plt`)
Es el motor base. Se usa principalmente para **configurar el lienzo y la estructura geométrica** sobre la cual dibujará Seaborn.

| Función | ¿Qué hace? | ¿Cuándo usarla en EDA? |
| :--- | :--- | :--- |
| `plt.subplots()` | Crea una figura (lienzo) y un conjunto de ejes (subplots). | Cuando quieres crear una cuadrícula manual (ej. 2x2) y decidir en qué eje dibujar gráficos diferentes. |
| `plt.figure()` | Crea un lienzo con dimensiones específicas (ej. `figsize=(10,5)`). | Siempre que los gráficos se vean aplastados o muy pequeños. |
| `plt.subplot()` | Selecciona un eje específico de la cuadrícula. | Para iterar manualmente y apuntar a diferentes cuadrantes mientras iteras sobre un DataFrame. |
| `plt.title()` | Establece el título principal de los ejes actuales. | Para darle contexto específico a cada subgráfico individual. |
| `plt.suptitle()` | Establece el gran título centrado para toda la figura completa. | Para ponerle título a toda la ventana gráfica cuando hay múltiples subgráficos. |
| `plt.subplots_adjust()`| Ajusta el espacio entre los subgráficos. | Cuando los títulos y etiquetas de los ejes de los subgráficos se traslapan entre sí (`hspace`, `wspace`). |
| `plt.plot()` | Dibuja líneas o marcadores en Matplotlib crudo. | Para dibujar funciones matemáticas complejas o líneas base personalizadas. |
| `plt.ylabel()` / `xlabel()`| Cambia las etiquetas de los ejes. | Cuando el nombre de la columna del dataframe no es un nombre muy bonito para la presentación final. |
| `plt.legend()` | Muestra los identificadores (cajas de color) de los datos en pantalla. | Cuando estás superponiendo gráficas manuales de Matplotlib y necesitas diferenciar qué es qué. |

---
## 4. Seaborn (`sns`): Estética y Análisis Avanzado
La librería definitiva para presentaciones formales, paneles de control (dashboards) y análisis estadístico multivariado complejo.

| Función | ¿Qué hace? | ¿Cuándo usarla en EDA? |
| :--- | :--- | :--- |
| `sns.boxplot()` | Diagrama de caja estadístico con excelente paleta. | Para presentar formalmente las medianas, IQR y anomalías al cliente. |
| `sns.boxenplot()` | Letter-value plot (diagrama de cajas multinivel). | Cuando tu boxplot clásico se vuelve inútil porque tienes millones de datos y quieres ver mejor el grosor y distribución de los extremos (colas). |
| `sns.violinplot()`| Mezcla de Boxplot y KDE simétrico. | Cuando necesitas mostrar en un solo gráfico la mediana (caja) y la forma multimodal (curva) de los datos a través de diferentes categorías. |
| `sns.histplot()` | Histograma estadístico altamente configurable. | Cuando necesitas hacer un histograma superpuesto por categorías (`hue`) o activar el suavizado (`kde=True`). |
| `sns.barplot()` | Gráfico de barras de estimación central. | Muy útil para plotear proporciones agregadas (promedios) que requieran intervalo de confianza, calculando métricas a partir del dataset. |
| `sns.countplot()` | Gráfico de recuento de frecuencia. | Simplemente para contar cuántas filas hay de cada categoría en lugar de usar `value_counts().plot.bar()`. |
| `sns.scatterplot()`| Diagrama de dispersión premium. | Para trazar interacciones entre X y Y agregando dimensiones extra fácilmente por color (`hue`) o tamaño (`size`). |
| `sns.lineplot()` | Diagrama de líneas con intervalo de confianza. | Cuando trazas datos a lo largo del tiempo o secuencias y quieres que Seaborn calcule automáticamente el margen de error probabilístico. |
| `sns.pairplot()` | Matriz completa de scatterplots y distribuciones de todo el dataset. | **El comando exploratorio más poderoso.** Se ejecuta al inicio para visualizar las relaciones cruzadas de todas las columnas numéricas simultáneamente. |
| `sns.heatmap()` | Mapa topográfico de calor (colores). | Para graficar la **Matriz de Correlación** con números por encima (`annot=True`) y encontrar rápidamente multicolinealidad. |
| `sns.kdeplot()` | Gráfico topográfico KDE independiente. | Para dibujar curvas de densidad suavizadas de una o múltiples variables superpuestas. |
| `sns.FacetGrid()` | Objeto cuadrícula mapeable por condiciones (columnas/filas). | Cuando necesitas generar docenas de subgráficos automáticamente separando por categorías (ej. una gráfica por país y por género) sin usar bucles. |
| `sns.PairGrid()` | Objeto cuadrícula para relaciones por pares personalizable. | Cuando `pairplot()` no es suficiente y quieres dibujar cosas distintas en la diagonal, la parte superior e inferior de la matriz cruzada. |

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos</i>
  </p>
</div>
