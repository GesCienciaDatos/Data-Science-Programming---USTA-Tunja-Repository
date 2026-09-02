# 08_Fusion_de_Datos_Pandas

<table style="width: 100%; border-collapse: collapse; border: none; background: #f8fafc; border-left: 6px solid #1e3a8a; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #0f172a; font-size: 2.1em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        Fusión y Combinación de Datos: Merge, Join y Concat 🔗
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
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/03%20-%20Pandas/08_Fusion_de_Datos_Pandas.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## Fusión de Datos 

En Pandas, `merge`, `join` y `concat` son tres métodos diferentes que se utilizan para combinar datos de múltiples tablas, pero tienen casos de uso y comportamientos distintos. En resumen:

- **Merge**: Úsalo cuando desees realizar una operación compleja, como combinar DataFrames basándote en columnas o índices comunes (muy similar a los JOINs de SQL).
- **Join**: Úsalo cuando quieras combinar DataFrames basándote directamente en sus **índices**.
- **Concat**: Úsalo cuando quieras pegar o concatenar DataFrames apilándolos a lo largo de un eje específico (uno encima del otro, o uno al lado del otro).


### Importando Nuevos Datos
Para explorar esto, dejaremos los vinos un momento y utilizaremos dos conjuntos de datos climáticos de la [NOAA](https://www.ncdc.noaa.gov/cdo-web/).

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

# Carga de datasets de clima
temp_path = load_dataset('climate_temp.csv', '03 - Pandas')
precip_path = load_dataset('climate_precip.csv', '03 - Pandas')
climate_temp = pd.read_csv(temp_path)
climate_precip = pd.read_csv(precip_path)
print('Dimensiones Temp:', climate_temp.shape)
print('Dimensiones Precip:', climate_precip.shape)
climate_temp.head(2)
```

---
### 1. Merge (Fusión por Columnas Comunes)

`merge()` te permite especificar las columnas clave por las cuales se debe realizar la fusión, al igual que los joins de SQL (`inner`, `outer`, `left`, `right`).

![image.png](attachment:image.png)

```python
# Aislaremos las precipitaciones de UNA SOLA estación para ver más claros los ejemplos
precip_one_station = climate_precip.query("STATION == 'GHCND:USC00045721'")
precip_one_station.shape
```

#### Inner Join (Por defecto)
Fusión estricta: solo mantiene las filas que **existen y coinciden en AMBOS** DataFrames.

```python
# Si no especificas 'how' ni 'on', pandas busca columnas con el mismo nombre y hace un inner join
inner_merged = pd.merge(precip_one_station, climate_temp)
display(inner_merged.head())
print("Shape del inner_merged:", inner_merged.shape)
```

Obtienes 365 filas porque cualquier fila del dataset grande de temperaturas que no coincidió con nuestra pequeña estación de 365 días fue descartada.

¿Qué pasa si quieres fusionar los dos conjuntos de datos completos, especificando explícitamente en qué columnas deben buscar coincidencias? Usas el parámetro `on`:

```python
inner_merged_total = pd.merge(
    climate_temp, 
    climate_precip, 
    on=["STATION", "DATE"] # Lista de columnas clave a cruzar
)
print("Shape total:", inner_merged_total.shape)
```

#### Outer Join
Fusión inclusiva: mantiene TODAS las filas de ambos DataFrames. Si no hay coincidencia, rellena los huecos con `NaN`.

```python
outer_merged = pd.merge(
    precip_one_station, 
    climate_temp, 
    how="outer", 
    on=["STATION", "DATE"]
)
print("Shape outer_merged:", outer_merged.shape)
```

Con un `outer join`, puedes esperar tener la misma cantidad de filas que el DataFrame más grande (127020), ya que no se pierde ninguna.

#### Left y Right Join
Mantienen **todas** las filas de la tabla de la izquierda (el primer argumento) o de la derecha (el segundo argumento), respectivamente. Los faltantes se rellenan con `NaN`.

```python
# Left Join (Mantiene todas las filas de climate_temp)
left_merged = pd.merge(climate_temp, precip_one_station, how="left", on=["STATION", "DATE"])
print("Shape left_merged:", left_merged.shape)

# Right Join (Mantiene todas las filas de climate_temp, que es el de la derecha ahora)
right_merged = pd.merge(precip_one_station, climate_temp, how="right", on=["STATION", "DATE"])
print("Shape right_merged:", right_merged.shape)
```

---
##### 🛠️ Práctica 1: Merge
Haz un `inner join` entre `precip_one_station` y `climate_temp`, pero esta vez cruza los datos **SOLO por la columna `"DATE"`**.
Imprime el `.shape` del resultado. ¿Notaste cómo la cantidad de filas se dispara al no cruzar también por la estación?

```python
# Escribe tu código aquí
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
merge_date_only = pd.merge(precip_one_station, climate_temp, on=["DATE"], how="inner")
print("Shape:", merge_date_only.shape)
```
</details>

---
### 2. Join (Fusión por Índices)

`join()` utiliza `merge()` por debajo, pero proporciona una interfaz mucho más simplificada y, por defecto, combina los DataFrames basándose en sus **Índices** en lugar de sus columnas.

Para manejar los nombres de columnas superpuestos, usamos `lsuffix` (sufijo izquierdo) y `rsuffix` (sufijo derecho).

```python
joined_df = precip_one_station.join(climate_temp, lsuffix="_left", rsuffix="_right")
display(joined_df.head())
print("Shape:", joined_df.shape)
```

Si de verdad necesitas usar `join()` comparando por el valor de columnas (como STATION y DATE), primero debes convertir esas columnas en los índices temporales del DataFrame usando `.set_index()`:

```python
inner_joined_total = climate_temp.join(
    climate_precip.set_index(["STATION", "DATE"]), 
    on=["STATION", "DATE"], 
    how="inner", 
    lsuffix="_x", 
    rsuffix="_y"
)
print("Shape inner joined:", inner_joined_total.shape)
```

---
##### 🛠️ Práctica 2: Join
Para no complicarnos con el dataset de clima, utilicemos dos DataFrames de juguete que ya tienen la columna `id` configurada como índice.

```python
df_a = pd.DataFrame({'id': [1, 2, 3], 'nombre': ['Ana', 'Beto', 'Cata']}).set_index('id')
df_b = pd.DataFrame({'id': [1, 2, 4], 'edad': [25, 30, 22]}).set_index('id')
display(df_a, df_b)
```

Aplica un `.join()` directo de `df_a` con `df_b` e imprime el resultado. Nota cómo al ser un Left Join por defecto, el id '3' se queda, pero el id '4' se descarta.

```python
# Escribe tu código aquí
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
resultado_join = df_a.join(df_b)
display(resultado_join)
```
</details>

---
### 3. Concat (Apilado de Datos)

`concat` no realiza fusiones buscando coincidencias de valores como tal; simplemente agarra los DataFrames y los **apila** o **pega** a lo largo de un eje (filas o columnas).

#### Concatenación Vertical (Por Filas - Axis 0)

```python
# Apilamos el DataFrame de 365 filas consigo mismo (uno encima del otro)
double_precip = pd.concat([precip_one_station, precip_one_station])
print("Shape duplicado:", double_precip.shape)

# ⚠️ Los índices se duplican. Para forzar un índice limpio del 0 en adelante usamos ignore_index
reindexed = pd.concat([precip_one_station, precip_one_station], ignore_index=True)
display(reindexed.head())
```

Si apilamos verticalmente dos DataFrames que **tienen columnas diferentes**, Pandas conservará todas las columnas (comportamiento Outer) y rellenará con `NaN` los vacíos:

```python
outer_joined = pd.concat([climate_precip, climate_temp])
print("Shape:", outer_joined.shape)
```

Podemos forzarlo a que, al apilar verticalmente, **solo conserve las columnas que ambos tienen en común** (`join="inner"`):

```python
inner_joined = pd.concat([climate_temp, climate_precip], join="inner")
display(inner_joined.head())
```

#### Concatenación Horizontal (Por Columnas - Axis 1)
Pega los DataFrames de lado a lado en lugar de uno encima de otro.

```python
inner_joined_cols = pd.concat([climate_temp, climate_precip], axis="columns", join="inner")
print("Shape concatenación de columnas:", inner_joined_cols.shape)
```

---
##### 🛠️ Práctica 3: Concat
Utiliza la función `pd.concat` para apilar verticalmente el DataFrame `df_a` (de la práctica anterior) consigo mismo. 
Asegúrate de pasar el parámetro necesario para **resetear el índice** y que cuente de forma continua en vez de repetir el 1, 2, 3.

```python
# Escribe tu código aquí
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
resultado_concat = pd.concat([df_a, df_a], ignore_index=True)
display(resultado_concat)
```
</details>

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos</i>
  </p>
</div>
