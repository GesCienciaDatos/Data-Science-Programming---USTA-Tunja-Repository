# 01_Exploracion_Preliminar_EDA

<table style="width: 100%; border-collapse: collapse; border: none; background: #f8fafc; border-left: 6px solid #1e3a8a; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #0f172a; font-size: 2.1em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        Exploración Preliminar y Calidad del Dato 📋
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
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/04%20-%20EDA/01_Exploracion_Preliminar_EDA.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## Carga de Datos y Exploración Inicial 🕵️‍♂️

Para explorar el valor real del Análisis Exploratorio de Datos, utilizaremos un archivo llamado `quartets.csv`. Este archivo contiene 4 conjuntos de datos diminutos que nos ayudarán a entender rápidamente el inmenso valor de graficar y explorar nuestra información.

```python
import os
import urllib.parse
import urllib.request
import pandas as pd

# 🚀 Función de utilidad para cargar datasets de forma segura (Local o Google Colab)
def load_dataset(filename, module_name="04 - EDA"):
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

# Carga del Cuarteto de Anscombe
file_path = load_dataset('quartets.csv', '04 - EDA')
df = pd.read_csv(file_path, index_col=0)
df.head()
```

### Exploración Preliminar
Lo primero que siempre debemos hacer al cargar un nuevo dataset es mirar su información técnica básica usando `.info()`.

```python
quartets.info()
```

Vemos que hay **44 entradas (filas)**, dos columnas numéricas (`x` e `y`) y una columna de tipo objeto (texto) llamada `quartet` que potencialmente identifica a cada uno de los 4 conjuntos de datos.

¿Cómo se ve físicamente este DataFrame? Utilicemos `.head()` para ver las primeras filas y `.sample()` para tomar una muestra aleatoria.

```python
# Primeras 5 filas
quartets.head()
```

```python
# 5 filas aleatorias (muy útil para no sesgarnos solo con el inicio de la tabla)
quartets.sample(5)
```

¿Cuáles son exactamente los nombres únicos de esos 4 conjuntos de datos que están en la columna `quartet`?

```python
quartets['quartet'].unique().tolist()
```

Para hacernos una mejor idea, podemos combinar `.groupby()` con funciones de exploración para ver fragmentos de cada uno de los 4 grupos al mismo tiempo:

```python
# Mostrar las primeras 3 muestras de CADA grupo (cuarteto)
quartets.groupby('quartet').head(3)
```

```python
# Mostrar 2 muestras ALEATORIAS de CADA grupo
quartets.groupby('quartet').sample(2)
```

Finalmente, verifiquemos si los 4 conjuntos de datos están balanceados (tienen la misma cantidad de filas):

```python
quartets.groupby('quartet').size()
```

---
##### 🛠️ Práctica: Explorando tus propios recortes
Imprime las **últimas 2 filas** de **cada grupo** utilizando la misma lógica de encadenamiento que vimos arriba.

```python
# Escribe tu código aquí
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
quartets.groupby('quartet').tail(2)
```
</details>

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos</i>
  </p>
</div>
