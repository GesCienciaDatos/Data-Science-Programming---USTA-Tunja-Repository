# 07_Agrupacion_y_Ordenamiento_Pandas

<table style="width: 100%; border-collapse: collapse; border: none; background: #f8fafc; border-left: 6px solid #1e3a8a; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #0f172a; font-size: 2.1em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        Agrupación, Agregación y Ordenamiento con GroupBy 📈
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
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/03%20-%20Pandas/07_Agrupacion_y_Ordenamiento_Pandas.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## Agrupación de Datos (`groupby`) 

A menudo queremos agrupar nuestros datos por categorías y luego hacer algo específico para cada grupo (como calcular promedios, contar elementos, encontrar máximos, etc.).

Para esto utilizamos el poderoso método `groupby()`.

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

Una función que ya hemos visto antes es `value_counts()`, que cuenta cuántas veces aparece un valor. Podemos replicar exactamente lo que hace esa función utilizando `groupby()` de la siguiente manera:

```python
wine_reviews.groupby('points')['points'].count()
```

`groupby()` creó un "grupo" virtual de reseñas que le asignaron la misma cantidad de puntos a los vinos. Luego, para cada uno de estos grupos, tomamos la columna `points` y le aplicamos la función `count()` para contar cuántas veces apareció. `value_counts()` es simplemente un atajo de conveniencia para esta operación.

Podemos usar **cualquiera de las funciones de resumen estadístico** con esta agrupación. Por ejemplo, para obtener **el vino más barato** dentro de cada categoría de puntaje:

```python
wine_reviews.groupby('points')['price'].min()
```

Para un control aún más detallado, también puedes agrupar por **más de una columna** pasándole una lista. 

A continuación, calculamos el **promedio de puntos** para cada país y su respectiva provincia (esto generará un MultiIndex):

```python
wine_reviews.groupby(['country', 'province'])['points'].mean()
```

---
## Ordenamiento de Datos (`sort_values`) 🔀

A menudo, el resultado de una agrupación no viene en el orden que nos gustaría leerlo. Para ordenarlo, podemos concatenar la función `sort_values()`.

```python
# ¿Qué país tiene el vino más caro? Agrupamos por país, buscamos el precio máximo y ordenamos descendentemente
wine_reviews.groupby('country')['price'].max().sort_values(ascending=False).head(10)
```

---
##### 🛠️ Práctica: Análisis Agrupado
Utiliza `groupby` para descubrir cuál es el precio promedio (`mean`) de los vinos **para cada variedad (`variety`)**.
Luego, utiliza `sort_values` para ordenar ese resultado de mayor a menor y muestra las 5 variedades más caras en promedio.

```python
# Escribe tu código aquí
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
precio_por_variedad = wine_reviews.groupby('variety')['price'].mean()
top_caros = precio_por_variedad.sort_values(ascending=False).head(5)
display(top_caros)
```
</details>

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos</i>
  </p>
</div>
