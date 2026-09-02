# 05_Asignacion_de_Datos_Pandas

<table style="width: 100%; border-collapse: collapse; border: none; background: #f8fafc; border-left: 6px solid #1e3a8a; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #0f172a; font-size: 2.1em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        Asignación, Modificación y Creación de Columnas ✏️
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
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/03%20-%20Pandas/05_Asignacion_de_Datos_Pandas.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## Asignación de Datos 

Asignar datos a un DataFrame es una operación sencilla y directa. Podemos sobrescribir columnas existentes o crear nuevas asignando valores de diferentes maneras.

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

### 1. Asignar un valor constante
Puedes asignar un único valor a toda una columna. Si la columna no existe, se creará automáticamente.

```python
wine_reviews['critic'] = 'everyone'
wine_reviews['critic'].head()
```

### 2. Asignar un iterable de valores
También puedes asignar una lista, un rango o cualquier iterable, siempre y cuando **su longitud coincida exactamente** con la cantidad de filas del DataFrame.

```python
# Creamos un índice invertido contando hacia atrás desde el total de filas hasta 1
wine_reviews['index_reversed'] = range(len(wine_reviews), 0, -1)
wine_reviews['index_reversed'].head()
```

### 3. Asignar valores con filtros condicionales (Indexación Booleana)
A menudo queremos modificar solo **algunos** valores específicos que cumplen cierta condición. Para esto, usamos nuestro confiable método `loc`.

⚠️ *Tip: Si quieres modificar una columna basado en una condición, asegúrate de usar `loc[condición, 'nombre_columna'] = nuevo_valor`. Hacerlo directamente con corchetes puede sobrescribir toda la fila o generar errores de copia en memoria.*

```python
print("Puntaje mínimo original:", wine_reviews['points'].min())

# Todos los vinos con menos de 85 puntos, ahora tendrán 85 puntos.
wine_reviews.loc[wine_reviews['points'] < 85, 'points'] = 85

print("Puntaje mínimo después de la asignación:", wine_reviews['points'].min())
```

---
##### 🛠️ Práctica: Promoción de Vinos
Vamos a hacer una oferta. Para todos los vinos que sean de Italia (`country == 'Italy'`), cambia su precio a `10.0` usando `loc`.

```python
# Escribe tu código aquí
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
wine_reviews.loc[wine_reviews['country'] == 'Italy', 'price'] = 10.0
```
</details>

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos</i>
  </p>
</div>
