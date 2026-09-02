# 04_Indexacion_y_Seleccion_Pandas

<table style="width: 100%; border-collapse: collapse; border: none; background: #f8fafc; border-left: 6px solid #1e3a8a; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #0f172a; font-size: 2.1em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        Indexación, Selección y Filtrado con loc e iloc 🎯
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
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/03%20-%20Pandas/04_Indexacion_y_Seleccion_Pandas.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## Indexación y Selección de Datos 

Seleccionar columnas o filas específicas de un DataFrame es una de las tareas más comunes e importantes en la manipulación de datos. Pandas nos ofrece múltiples formas de extraer exactamente la porción de datos que necesitamos.

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
### 1. Acceso a Columnas (Atributos vs Corchetes)

#### 1.1 Acceso como Atributo (Punto)
Puedes acceder a una columna de un DataFrame directamente como si fuera un atributo utilizando el punto (`.`). Por ejemplo, para acceder a la propiedad `country` de nuestro DataFrame:

```python
wine_reviews.country
```

⚠️ **¡Advertencia importante!**
Solo puedes utilizar este tipo de acceso si el nombre de la columna es un identificador de Python **válido**. Por ejemplo:
- No puedes usar números (`wine_reviews.1` no es válido).
- No puedes usar nombres con espacios (`wine_reviews.taster name`).
- No funcionará si el nombre de la columna entra en conflicto con un método existente de Pandas (por ejemplo, si tienes una columna llamada `min`, `wine_reviews.min` ejecutará la función mínima, no te devolverá la columna).

#### 1.2 Acceso con Corchetes `[]` (Getitem)
La forma estándar, más segura y común de indexar columnas es utilizando corchetes (`[]`). Si pasas un solo nombre, te devolverá una `Series`.

```python
display(wine_reviews['country'])
print("Tipo:", type(wine_reviews['country']))
```

Para extraer un valor único, usamos el operador de indexación dos veces (primero la columna, luego la fila):

```python
wine_reviews['country'][0]
```

También puedes pasar una **lista de columnas** dentro de los corchetes `[['col1', 'col2']]` para seleccionar múltiples columnas al mismo tiempo. En este caso, Pandas devolverá un `DataFrame`, no una Series:

```python
display(wine_reviews[['country', 'price']])
print("Tipo:", type(wine_reviews[['country', 'price']]))
```

---
### 2. Rangos de corte (Slicing `[:]`) ✂️

Con las **Series**, la sintaxis del rebanado (*slicing*) funciona exactamente igual que con una lista de Python o un arreglo de NumPy, devolviendo un corte de los valores y sus etiquetas correspondientes.

```python
# Haciendo slicing a una Series (columna country)
wine_reviews['country'][3:9]
```

Con un **DataFrame**, al hacer slicing directamente dentro de los corchetes `[]`, Pandas corta las **filas**. Esto se diseñó así por simple conveniencia, ya que es una operación muy común.

```python
# Haciendo slicing directamente al DataFrame entero (corta filas)
wine_reviews[3:9]
```

---
### 3. Selección experta con `loc` e `iloc` 🗺️

¿Cómo hacemos para seleccionar **filas Y columnas específicas** al mismo tiempo? Usar solo los corchetes `[]` no es suficiente para cortes precisos de dos dimensiones. Para esto, existen los operadores `loc` e `iloc`.

La sintaxis siempre es: `dataframe.iloc[filas_que_quieres, columnas_que_quieres]`

#### 3.1 Selección por Posición (`iloc`)
`iloc` viene de *Integer Location*. Permite hacer selecciones basadas puramente en los **índices numéricos de las posiciones**, ignorando el nombre de las columnas. Sigue la regla tradicional de Python (el límite inferior se incluye, el superior no).

```python
# Extraer la primera fila entera (posición 0)
wine_reviews.iloc[0]
```

```python
# Extraer TODAS las filas (:), pero solo de la primera columna (posición 0)
wine_reviews.iloc[:, 0]
```

```python
# Seleccionar las tres primeras filas, de la primera columna
wine_reviews.iloc[:3, 0]
```

```python
# También podemos pasarle listas arbitrarias
wine_reviews.iloc[[0, 1, 10, 100], 0]
```

#### 3.2 Selección por Etiqueta (`loc`)
`loc` viene de *Location*. Permite hacer selecciones puramente basadas en el **nombre (etiqueta)** de las filas y las columnas.

⚠️ **Cuidado con `loc`**: Contrario al corte habitual de Python, en `loc` el límite final **SÍ se incluye**.

```python
# Para obtener la primera entrada (etiquetada como '0') de la columna con etiqueta 'country'
wine_reviews.loc[0, 'country']
```

```python
# Extraer todas las filas de una lista específica de nombres de columnas
wine_reviews.loc[:, ['taster_name', 'taster_twitter_handle', 'points']]
```

**Transición entre loc e iloc (Combinación):**
¿Qué pasa si deseas obtener los elementos 0 y 2 del índice pero utilizando la etiqueta de columna 'country'?
Puedes apoyarte en la función `get_loc` de las columnas, o usar los índices directamente sobre `loc`.

```python
display(wine_reviews.loc[wine_reviews.index[[0, 2]], 'country'])

# O combinando con iloc pidiendo que busque la posición de la palabra 'country'
posicion_country = wine_reviews.columns.get_loc('country')
display(wine_reviews.iloc[[0, 2], posicion_country])
```

---
##### 🛠️ Práctica 1: Jugando con loc e iloc

Utiliza la herramienta adecuada (`loc` o `iloc`) para:
1. Seleccionar las filas de la posición 10 a la posición 15.
2. Seleccionar, para esas mismas filas, **solo** las columnas `title` y `price`.
Guarda el resultado en una variable llamada `subset_vinos` e imprímelo.

```python
# Escribe tu código aquí
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
subset_vinos = wine_reviews.loc[10:15, ['title', 'price']]
display(subset_vinos)
```
</details>

---
### 4. Indexación Booleana (Condicional) 🎭

Hasta ahora hemos extraído fragmentos utilizando propiedades estructurales del DataFrame. Sin embargo, para hacer cosas interesantes con los datos, solemos necesitar **hacer preguntas basadas en condiciones** (filtros).

Por ejemplo, supongamos que estamos interesados ​​específicamente en los vinos producidos en Italia.
Podemos comenzar preguntándole al DataFrame: ¿Eres de Italia o no?

```python
# Esto devuelve una "Máscara Booleana" (una serie llena de True / False)
wine_reviews['country'] == 'Italy'
```

Ahora, simplemente inyectamos esa Máscara Booleana dentro de nuestro poderoso `loc` para que filtre y traiga solo las filas que son `True`:

```python
wine_reviews.loc[wine_reviews['country'] == 'Italy']
```

**Múltiples condiciones (AND `&` y OR `|`)**

Queríamos saber cuáles vinos italianos son mejores que el promedio. Sabiendo que los vinos se puntúan en una escala hasta 100, queremos vinos que tengan al menos 90 puntos.

Podemos utilizar el *ampersand* (`&`) para indicar que se deben cumplir **ambas** condiciones a la vez (AND). **Nota vital:** Siempre debes colocar paréntesis `()` alrededor de cada condición independiente.

```python
# Vinos de Italia que TAMBIÉN tienen 90 o más puntos
wine_reviews.loc[(wine_reviews['country'] == 'Italy') & (wine_reviews['points'] >= 90)]
```

Supongamos que en cambio compraremos cualquier vino que se haga en Italia **O** que tenga más de 90 puntos sin importar el país. Para el condicional OR usamos la barra vertical (`|`):

```python
# Vinos de Italia O que tengan 90 o más puntos
wine_reviews.loc[(wine_reviews['country'] == 'Italy') | (wine_reviews['points'] >= 90)]
```

---
### 5. Métodos `isin()` y `notnull()`

Pandas incluye funciones diseñadas para ahorrarnos escribir filtros booleanos interminables.

- **`isin(lista)`**: Retorna `True` si el valor de la fila coincide con **cualquiera** de los elementos de la lista que le pases. Muy útil para buscar múltiples categorías sin llenar todo de condiciones `|`.

```python
# Filtrar vinos que sean de Italia o de Francia
wine_reviews.loc[wine_reviews['country'].isin(['Italy', 'France'])]
```

- **`notnull()`** y su reverso **`isnull()`**: Te permiten resaltar valores que están (o no están) vacíos/Nulos (NaN). Por ejemplo, si quisiéramos filtrar todos los vinos que no tengan una etiqueta de precio (`price` no nulo):

```python
wine_reviews.loc[wine_reviews['price'].notnull()]
```

---
##### 🛠️ Práctica 2: Filtros Booleanos Avanzados

Utiliza Máscaras Booleanas dentro de `loc` para resolver este desafío:
- Queremos filtrar todos los vinos cuyo **país** sea España (`'Spain'`) y que su **precio** sea estrictamente menor a 15 (`< 15`).
- Asigna los resultados a una variable llamada `ofertas_españolas` e imprime las primeras 5 filas con `head()`.

```python
# Escribe tu código aquí
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
ofertas_españolas = wine_reviews.loc[(wine_reviews['country'] == 'Spain') & (wine_reviews['price'] < 15)]
display(ofertas_españolas.head())
```
</details>

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos</i>
  </p>
</div>
