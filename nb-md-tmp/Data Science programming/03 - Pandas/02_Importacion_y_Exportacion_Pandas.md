# 02_Importacion_y_Exportacion_Pandas

<table style="width: 100%; border-collapse: collapse; border: none; background: #f8fafc; border-left: 6px solid #1e3a8a; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #0f172a; font-size: 2.1em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        Importación y Exportación de Datos en Pandas 💾
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
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/03%20-%20Pandas/02_Importacion_y_Exportacion_Pandas.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## Importación y Exportación de Datos 

Ser capaz de crear un DataFrame o una Series a mano es útil. Pero, la mayoría de las veces, no estaremos creando nuestros propios datos manualmente. En su lugar, trabajaremos con datos que ya existen.

Los datos pueden almacenarse en una variedad de formas y formatos. Con diferencia, el más básico de estos es el humilde archivo CSV. Cuando abres un archivo CSV, obtienes algo parecido a esto:

```csv
Product A,Product B,Product C
30,21,9
35,34,1
41,11,11
```

Por lo tanto, un archivo CSV es simplemente una tabla de valores separados por comas. De ahí su nombre: **"Valores Separados por Comas"** (Comma-Separated Values, o CSV).

---
### 1. Leyendo un archivo CSV 📖

Dejemos a un lado nuestros pequeños conjuntos de datos de prueba y veamos cómo luce un conjunto de datos real cuando lo leemos en un DataFrame. Usaremos la función `pd.read_csv()` para leer datos de reseñas de vinos en un DataFrame.

El conjunto de datos *Wine Reviews* contiene reseñas extraídas de la web con información sobre variedad, ubicación, bodega, precio y descripción de sumilleres.

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
### 2. Exportando un DataFrame a CSV 📤

¡No es solo CSV! Pandas puede leer y escribir desde Excel, SQL, JSON, HTML y más.
[Fuente de la imagen](https://pandas.pydata.org/docs/getting_started/intro_tutorials/02_read_write.html)

Después de realizar alguna manipulación de datos, es muy común que queramos guardar los datos resultantes en un nuevo archivo CSV. Para esto, podemos usar la función `DataFrame.to_csv()`:

```python
# Guardamos el DataFrame en un nuevo archivo CSV en la carpeta actual
wine_reviews.to_csv("exported_wine_reviews.csv")
```

---
### 3. Ajustando los parámetros de lectura ⚙️

La función `pd.read_csv()` tiene **más de 30 parámetros opcionales** que puedes especificar. 

Por ejemplo, puedes notar en el conjunto de datos anterior que el archivo CSV ya tenía un índice incorporado en la primera columna (`Unnamed: 0`), pero pandas no lo detectó automáticamente y creó un índice numérico nuevo (0, 1, 2...).

Para hacer que pandas use esa columna existente como el índice del DataFrame (en lugar de crear uno nuevo desde cero), podemos especificar el parámetro `index_col`:

```python
# Leemos el archivo indicando que la columna 0 debe ser el índice
wine_reviews = pd.read_csv("data/winemag-data-130k-v2.csv", index_col=0)
wine_reviews.head()
```

---
##### 🛠️ Práctica: Explorando `pd.read_csv`

Intenta leer de nuevo el archivo `"data/winemag-data-130k-v2.csv"`, pero esta vez usa el parámetro opcional `nrows=10` para cargar solamente las **primeras 10 filas** del archivo. 

Asigna el resultado a una variable llamada `wine_reviews_small` y usa la función nativa `len()` para comprobar su longitud.

*(Tip: Puedes consultar la [documentación oficial](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html) para ver la lista completa de parámetros de lectura).*

```python
# Escribe tu código aquí

# wine_reviews_small = ...
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
wine_reviews_small = pd.read_csv("data/winemag-data-130k-v2.csv", nrows=10)
print("Total de filas cargadas:", len(wine_reviews_small))
display(wine_reviews_small.head())
```
</details>

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos</i>
  </p>
</div>
