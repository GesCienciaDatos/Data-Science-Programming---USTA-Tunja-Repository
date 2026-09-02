# 04_EDA_Hands_On

<table style="width: 100%; border-collapse: collapse; border: none; background: #f8fafc; border-left: 6px solid #1e3a8a; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #0f172a; font-size: 2.1em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        Ejercicios Prácticos de EDA
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
        Taller Práctico • Módulo 04
      </span><br>
      <span style="color: #64748b; font-size: 0.85em;">Docente: Santiago A. Zúñiga M.</span><br>
      <a href="mailto:gestorvirtualcienciadatos@ustatunja.edu.co" style="color: #2563eb; font-size: 0.8em; text-decoration: none; font-weight: 500;">gestorvirtualcienciadatos@ustatunja.edu.co</a>
    </td>
  </tr>
</table>

<div align="center" style="margin-top: 15px; margin-bottom: 15px;">
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/homeworks/04_EDA_Hands_On.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

## Exploratory Data Analysis (EDA)
En este notebook aplicaremos los conceptos de estadística descriptiva y visualización de datos usando el clásico dataset del Titanic.

**1. Importa las librerías necesarias**

Importa `pandas` como `pd`, `matplotlib.pyplot` como `plt` y `seaborn` como `sns`.

```python
### TU CÓDIGO AQUÍ ###
```

**2. Carga del Dataset**

Usa la función `sns.load_dataset('titanic')` para cargar los datos y guárdalos en un DataFrame llamado `df`. Luego, muestra las primeras 5 filas.

```python
### TU CÓDIGO AQUÍ ###
```

**3. Exploración Preliminar**

Utiliza el método `info()` para observar la cantidad de registros, los tipos de datos de cada columna y la presencia de valores nulos.

```python
### TU CÓDIGO AQUÍ ###
```

**4. Estadística Descriptiva**

Obtén las estadísticas descriptivas (media, desviación estándar, mínimos y máximos) de las variables numéricas del DataFrame.

```python
### TU CÓDIGO AQUÍ ###
```

**5. Distribución de Edades (Histograma)**

Crea un histograma usando Seaborn (`sns.histplot()`) para visualizar la distribución de la columna `age`. Añade un título apropiado al gráfico.

```python
### TU CÓDIGO AQUÍ ###
```

**6. Sobrevivientes vs No Sobrevivientes (Gráfico de Barras)**

Utiliza un `countplot` de Seaborn para mostrar cuántos pasajeros sobrevivieron (`survived`) y cuántos no.

```python
### TU CÓDIGO AQUÍ ###
```

**7. Edad según Clase del Pasajero (Diagrama de Caja)**

Crea un *boxplot* (`sns.boxplot()`) que compare la edad (`age`) en el eje Y respecto a la clase en la que viajaban (`pclass`) en el eje X.

```python
### TU CÓDIGO AQUÍ ###
```

**8. Correlación entre Variables Numéricas (Heatmap)**

Calcula la matriz de correlación para las variables numéricas del dataset y visualízala usando un mapa de calor (`sns.heatmap()`). 

*Pista:* Asegúrate de filtrar el DataFrame para seleccionar solo las columnas numéricas (`select_dtypes(include='number')`) antes de calcular la correlación (`.corr()`).

```python
### TU CÓDIGO AQUÍ ###
```
