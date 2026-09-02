# 03_Exploracion_de_Datos_Pandas

<table style="width: 100%; border-collapse: collapse; border: none; background: #f8fafc; border-left: 6px solid #1e3a8a; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #0f172a; font-size: 2.1em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        Exploración y Diagnóstico Inicial de Datos 🔎
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
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/03%20-%20Pandas/03_Exploracion_de_Datos_Pandas.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## Exploración de Datos 

Una vez que importamos nuestro dataset, el siguiente paso natural es explorarlo para entender qué información contiene, cómo está estructurada y si hay datos faltantes. 

Pandas ofrece numerosos atributos y funciones para obtener rápidamente una vista panorámica (metadata) de nuestros DataFrames.

```python
import os
import urllib.parse
import urllib.request
import pandas as pd

# 🚀 Función de utilidad para cargar datasets de forma segura (Local o Google Colab)
def load_dataset(filename, module_name="03 - Pandas"):
    candidates = [
        f"data/{filename}",
        f"{module_name}/data/{filename}",
        filename
    ]
    for path in candidates:
        if os.path.exists(path):
            return path
            
    os.makedirs("data", exist_ok=True)
    target_path = f"data/{filename}"
    encoded_module = urllib.parse.quote(module_name)
    encoded_file = urllib.parse.quote(filename)
    url_main = f"https://raw.githubusercontent.com/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/main/{encoded_module}/data/{encoded_file}"
    url_master = f"https://raw.githubusercontent.com/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/master/{encoded_module}/data/{encoded_file}"
    
    print(f"📥 Descargando dataset '{filename}' desde el repositorio oficial...")
    try:
        urllib.request.urlretrieve(url_main, target_path)
    except Exception:
        urllib.request.urlretrieve(url_master, target_path)
    print(f"✅ Dataset '{filename}' cargado exitosamente.")
    return target_path

# Carga del dataset desde ruta local o descarga automática desde GitHub
file_path = load_dataset('winemag-data-130k-v2.csv', '03 - Pandas')
reviews = pd.read_csv(file_path, index_col=0)
reviews.head(3)
```

---
### 1. Atributos y metadatos base 🏷️

Los objetos de pandas tienen varios atributos (variables internas que no llevan paréntesis al final) que nos permiten acceder a su información estructural:

- `shape`: devuelve una tupla con las dimensiones del objeto (filas, columnas), de manera idéntica a los *ndarrays* de NumPy.
- Etiquetas de los ejes:
  - **Series:** `index` (es su único eje)
  - **DataFrame:** `index` (para las filas) y `columns` (para las columnas)
  
🤓 *Nota: ¡Estos atributos pueden ser asignados/modificados de forma segura!*

```python
print("Dimensiones (filas, columnas):", wine_reviews.shape)

display(wine_reviews.index)
display(wine_reviews.columns)
```

Por ejemplo, podemos aprovechar que las columnas son modificables para reescribir todos los nombres en mayúsculas usando una comprensión de listas (*List Comprehension*) de Python:

```python
# Reescribimos los nombres de las columnas en mayúsculas
wine_reviews.columns = [x.upper() for x in wine_reviews.columns]
display(wine_reviews.columns)
```

---
##### 🛠️ Práctica 1: Normalización de columnas

Escribir columnas en mayúsculas puede ser un poco agresivo a la vista. 
Cambia el atributo `columns` del DataFrame `wine_reviews` nuevamente, esta vez para que todos los nombres estén en minúsculas (puedes usar el método `.lower()` de los strings de Python).

```python
# Escribe tu código aquí
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
wine_reviews.columns = [x.lower() for x in wine_reviews.columns]
display(wine_reviews.columns)
```
</details>

---
### 2. Visualizando los datos (Head, Tail, Info) 👀

Para visualizar una pequeña muestra de un objeto Series o DataFrame y no colapsar la pantalla, usamos los métodos `head()` y `tail()`. El número predeterminado de elementos a mostrar es cinco, pero puedes pasarle un número personalizado.

```python
# Primeras 5 filas (por defecto)
wine_reviews.head()
```

```python
# Últimas 2 filas
wine_reviews.tail(2)
```

El método `info()` nos brinda toda la información técnica clave sobre el DataFrame de un solo vistazo: cantidad de registros, conteo de valores nulos, y el tipo de dato subyacente en memoria de cada columna.

```python
wine_reviews.info()
```

---
### 3. Resumen estadístico (`describe`) 📊

El método `describe()` muestra un resumen estadístico rápido de tus datos. Es "inteligente" respecto al tipo de dato (`type-aware`), lo que significa que su salida cambia según si los datos son numéricos o categóricos.

```python
# Si no le pasamos argumentos, por defecto describe SÓLO las columnas numéricas
wine_reviews.describe()
```

Para datos tipo `object` (como textos o strings), el resumen incluirá el conteo (`count`), los valores únicos (`unique`), el valor más común (`top`) y la frecuencia de ese valor más común (`freq`).

Podemos forzarlo a describir TODAS las columnas:

```python
# Describe todas las columnas (las numéricas tendrán valores nulos en top/freq)
wine_reviews.describe(include='all')
```

También puedes apuntar `describe()` a una columna específica (una Series) para ver su resumen individual:

```python
# Aseguramos columnas en minúsculas para consistencia
wine_reviews.columns = wine_reviews.columns.str.lower()
wine_reviews["taster_name"].describe()
```

---
### 4. Funciones estadísticas particulares 🧮

Si deseas obtener algún estadístico resumido particular, normalmente hay una función específica de Pandas que lo hace directamente.

Por ejemplo, para ver el **promedio** de los puntos otorgados, usamos `mean()`:

```python
wine_reviews["points"].mean()
```

Para ver una lista de **valores únicos** (sin repeticiones) de una categoría, usamos `unique()`:

```python
wine_reviews["taster_name"].unique()
```

Para ver una lista de los valores únicos y **cuántas veces ocurren** en el dataset, usamos el maravilloso método `value_counts()`:

```python
wine_reviews["taster_name"].value_counts()
```

---
##### 🛠️ Práctica 2: Extracción de información estadística

Responde con código a las siguientes preguntas analíticas:
1. ¿Cuál es el precio **máximo** registrado en este conjunto de reseñas? *(Pista: hay una función `max()`)*
2. ¿Cuántos **países** diferentes hay en la base de datos y cuáles son? *(Pista: fíjate en la columna `'country'` y en la función `unique()` o `nunique()`)*
3. Haz un **conteo** de vinos reseñados por provincia (`'province'`).

```python
# Escribe tu código aquí
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
# 1. Precio Máximo
precio_max = wine_reviews["price"].max()
print("Precio máximo registrado:", precio_max)

# 2. Países únicos
paises = wine_reviews["country"].unique()
print("\nPaíses diferentes:", len(paises)) # o wine_reviews['country'].nunique()
print(paises)

# 3. Conteo por provincia
display(wine_reviews["province"].value_counts())
```
</details>

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos</i>
  </p>
</div>
