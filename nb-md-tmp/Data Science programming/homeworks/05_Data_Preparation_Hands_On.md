# 05_Data_Preparation_Hands_On

<table style="width: 100%; border-collapse: collapse; border: none; background: #f8fafc; border-left: 6px solid #1e3a8a; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #0f172a; font-size: 2.1em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        Ejercicios Prácticos de Data Preparation
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
        Taller Práctico • Módulo 05
      </span><br>
      <span style="color: #64748b; font-size: 0.85em;">Docente: Santiago A. Zúñiga M.</span><br>
      <a href="mailto:gestorvirtualcienciadatos@ustatunja.edu.co" style="color: #2563eb; font-size: 0.8em; text-decoration: none; font-weight: 500;">gestorvirtualcienciadatos@ustatunja.edu.co</a>
    </td>
  </tr>
</table>

<div align="center" style="margin-top: 15px; margin-bottom: 15px;">
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/homeworks/05_Data_Preparation_Hands_On.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

## Preparación de Datos (Data Preparation)
En este notebook aplicaremos técnicas de limpieza y preparación de datos basadas estrictamente en los temas vistos en clase: manejo de valores nulos, escalado de características, análisis de fechas y datos inconsistentes.

**1. Importa las librerías necesarias**

Importa `pandas` como `pd`, `numpy` como `np`, `seaborn` como `sns`, `MinMaxScaler` de `sklearn.preprocessing`, y `fuzzywuzzy`.

```python
### TU CÓDIGO AQUÍ ###
```

### Parte 1: Valores Faltantes y Escalado
**2. Carga del Dataset**

Usa la función `sns.load_dataset('titanic')` para cargar los datos y guárdalos en un DataFrame llamado `df`. Luego, muestra las primeras 5 filas para inspeccionar el contenido.

```python
### TU CÓDIGO AQUÍ ###
```

**3. Identificación de Valores Faltantes**

Calcula cuántos valores nulos (NaN) existen en cada columna del DataFrame.

```python
### TU CÓDIGO AQUÍ ###
```

**4. Manejo de Valores Faltantes (Imputación)**

La columna `age` tiene bastantes valores faltantes. Rellena (imputa) estos valores con la **mediana** de las edades y verifica que ya no haya nulos en esa columna.

```python
### TU CÓDIGO AQUÍ ###
```

**5. Manejo de Valores Faltantes (Eliminación)**

La columna `deck` tiene demasiados valores nulos. Elimina esta columna por completo del DataFrame.

```python
### TU CÓDIGO AQUÍ ###
```

**6. Escalado de Características (Min-Max Scaling)**

La columna `fare` (tarifa) tiene rangos muy variados. Utiliza `MinMaxScaler` para escalar los valores de esta columna entre 0 y 1. Guarda el resultado en una nueva columna llamada `fare_scaled`.

```python
### TU CÓDIGO AQUÍ ###
```

### Parte 2: Fechas y Datos Inconsistentes
**7. Análisis de Fechas (Parsing Dates)**

A continuación, crearemos un DataFrame de ejemplo con fechas en formato de texto (string). Tu tarea es convertir esta columna a tipo `datetime64` usando `pd.to_datetime` y extraer el **año** en una nueva columna llamada `year`.

```python
# DataFrame de ejemplo
df_dates = pd.DataFrame({'date_string': ['03/02/2007', '04/15/2009', '12/01/2015', '07/22/2020']})

### TU CÓDIGO AQUÍ ###
```

**8. Datos Inconsistentes (Inconsistent Data Entry)**

Tenemos un DataFrame con nombres de ciudades que han sido ingresados de manera inconsistente (con espacios extra o diferencias en mayúsculas/minúsculas). Estandariza la columna `city` convirtiendo todo a minúsculas y eliminando los espacios en blanco al inicio y al final usando `.str.lower()` y `.str.strip()`.

```python
# DataFrame de ejemplo
df_cities = pd.DataFrame({'city': [' Bogota', 'BOGOTA', 'bogota ', 'Medellin', ' medellin']})

### TU CÓDIGO AQUÍ ###
```
