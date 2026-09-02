# 03b_Pandas_Hands_On_Kaggle

<table style="width: 100%; border-collapse: collapse; border: none; background: #f8fafc; border-left: 6px solid #1e3a8a; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #0f172a; font-size: 2.1em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        Ejercicios Prácticos de Pandas
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
        Taller Práctico • Módulo 03
      </span><br>
      <span style="color: #64748b; font-size: 0.85em;">Docente: Santiago A. Zúñiga M.</span><br>
      <a href="mailto:gestorvirtualcienciadatos@ustatunja.edu.co" style="color: #2563eb; font-size: 0.8em; text-decoration: none; font-weight: 500;">gestorvirtualcienciadatos@ustatunja.edu.co</a>
    </td>
  </tr>
</table>

<div align="center" style="margin-top: 15px; margin-bottom: 15px;">
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/homeworks/03b_Pandas_Hands_On_Kaggle.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

## Parte 2: Importación de un Dataset desde Kaggle
Para estos ejercicios, utilizaremos el dataset **Pandas Practice Dataset** disponible en Kaggle.

Usaremos la librería `kagglehub` para descargarlo automáticamente.

```python
import kagglehub

# Descarga la última versión del dataset
path = kagglehub.dataset_download("themrityunjaypathak/pandas-practice-dataset")

print("Ruta de los archivos del dataset:", path)
```

**1. Importa la librería pandas como `pd`**

```python
### TU CÓDIGO AQUÍ ###
```

**2. Lee el archivo CSV descargado y guárdalo en un DataFrame llamado `df`**

*Nota:* Combina la ruta generada por `path` con el nombre del archivo CSV (puedes listar los archivos del directorio usando `os.listdir(path)` si no sabes el nombre exacto).

```python
### TU CÓDIGO AQUÍ ###
```

**3. Muestra las primeras 5 y las últimas 5 filas del DataFrame**

*Nota:* Puedes usar `head()` y `tail()`.

```python
### TU CÓDIGO AQUÍ ###
```

**4. Muestra información general del DataFrame (tipos de datos, columnas, memoria usada)**

*Nota:* Utiliza el método `info()`.

```python
### TU CÓDIGO AQUÍ ###
```

**5. Obtén un resumen estadístico de las columnas numéricas usando `describe()`**

```python
### TU CÓDIGO AQUÍ ###
```

**6. Verifica si existen valores nulos en cada columna**

*Pista:* Combina los métodos `isnull()` y `sum()`.

```python
### TU CÓDIGO AQUÍ ###
```

**7. Manejo de valores faltantes (si existen)**

Elimina las filas que contengan valores nulos (usando `dropna()`) o rellénalas con el valor adecuado (usando `fillna()`). Si el dataset no tiene nulos, puedes saltar este paso.

```python
### TU CÓDIGO AQUÍ ###
```

**8. Realiza una agrupación de los datos (`groupby`)**

Agrupa los datos por una columna categórica de tu elección y calcula el promedio (`mean`) de una columna numérica.

*Nota:* Ajusta los nombres de las columnas según lo que observaste en los pasos anteriores.

```python
### TU CÓDIGO AQUÍ ###
```

**9. Ordena el DataFrame**

Ordena los datos en base a una columna numérica de forma descendente usando el método `sort_values()`.

```python
### TU CÓDIGO AQUÍ ###
```

**10. Guarda el DataFrame final en un nuevo archivo CSV**

Llámalo `dataset_analizado.csv` y asegúrate de no exportar el índice (`index=False`).

```python
### TU CÓDIGO AQUÍ ###
```
