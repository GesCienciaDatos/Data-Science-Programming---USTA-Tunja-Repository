# 01_Estructuras_de_Datos_Pandas

<table style="width: 100%; border-collapse: collapse; border: none; background: #f8fafc; border-left: 6px solid #1e3a8a; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #0f172a; font-size: 2.1em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        Estructuras Fundamentales: Series y DataFrames 📊
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
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/03%20-%20Pandas/01_Estructuras_de_Datos_Pandas.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## Estructuras de Datos de Pandas 

Pandas proporciona dos tipos de clases fundamentales para el manejo de datos:
- **Series:** un arreglo unidimensional etiquetado que contiene datos de cualquier tipo, como enteros, cadenas (strings), objetos de Python, etc.
- **DataFrame:** una estructura de datos bidimensional que almacena datos como un arreglo de dos dimensiones o una tabla con filas y columnas.

---
### 1. Series 🌱

Una **Series** es un arreglo etiquetado unidimensional capaz de contener cualquier tipo de datos (enteros, cadenas, números de punto flotante, objetos de Python, etc.). Al igual que un arreglo de NumPy, una Series de pandas tiene un solo tipo de dato (`dtype`). Las etiquetas de los ejes se conocen colectivamente como el **índice** (`index`). El método básico para crear una Series es:

`s = pd.Series(data, index=index)`

Aquí, `data` puede ser muchas cosas diferentes:
- un diccionario de Python (`dict`)
- un `ndarray` de NumPy
- un iterable (listas, tuplas, cadenas, etc.)
- un valor escalar (como 5)

El parámetro `index` que se pasa es una lista de etiquetas de eje.

```python
# Es buena práctica configurar la salida múltiple en Jupyter
try:
    from IPython.core.interactiveshell import InteractiveShell
    InteractiveShell.ast_node_interactivity = 'all'
except Exception:
    pass
try:
    from IPython.display import display
except Exception:
    pass

import pandas as pd

s = pd.Series([25, 50, 75, 100])
display(s)
print("Tipo:", type(s))
```

Puedes asignar etiquetas a las filas utilizando el parámetro `index`. Una Series es, en esencia, una sola columna de un DataFrame. Sin embargo, una Series no tiene un nombre de columna, solo tiene un nombre general:

```python
s = pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A')
s
```

La `Series` y el `DataFrame` están íntimamente relacionados. Es útil pensar en un DataFrame como un grupo de Series "pegadas".
Las Series de Pandas se pueden dividir en la parte del índice y la parte de los datos usando los atributos `index` y `array`.

```python
display(s.array)
print("Tipo del array:", type(s.array))
```

```python
display(s.index)
print("Tipo del index:", type(s.index))
```

🤓 **Nota:** En el pasado, pandas recomendaba `Series.values` o `DataFrame.values` para extraer los datos de una Series o DataFrame. Aún encontrarás referencias a esto en bases de código antiguas y en línea. La recomendación actual es evitar `.values` y usar `.array` o `.to_numpy()`. `.values` tiene algunos inconvenientes [explicados aquí](https://pandas.pydata.org/docs/user_guide/basics.html#attributes-and-underlying-data).

#### 1.1 Series es similar a un ndarray (ndarray-like)
Una Series actúa de manera muy similar a un `ndarray` y es un argumento válido para la mayoría de las funciones de NumPy. Sin embargo, operaciones como el *slicing* (rebanado) también cortarán el índice.

```python
s[1:3]
```

#### 1.2 Series es similar a un diccionario (dict-like)
Una Series también es como un diccionario (`dict`) de tamaño fijo en el que puedes obtener y establecer valores a través de la etiqueta del índice:

```python
s["2016 Sales"]
```

---
##### 🛠️ Práctica 1: Creando tu primera Series

Crea una Series de Pandas que contenga los precios de tres productos: 150, 200 y 350. Asígnale a las filas (índice) los nombres `'Manzana'`, `'Banana'` y `'Cereza'`, y dale a la Series el nombre `'Precios'`.
Finalmente, imprímela.

```python
# Escribe tu código aquí

# precios_frutas = ...
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
precios_frutas = pd.Series([150, 200, 350], index=['Manzana', 'Banana', 'Cereza'], name='Precios')
print(precios_frutas)
```
</details>

---
### 2. DataFrame 📊

Un **DataFrame** es una estructura de datos etiquetada de 2 dimensiones con columnas de tipos potencialmente diferentes. Puedes pensar en él como una hoja de cálculo, una tabla SQL o un diccionario de objetos Series. En general, es el objeto de pandas más comúnmente utilizado. Al igual que una Series, un DataFrame acepta muchos tipos diferentes de entrada:
- Diccionario (`dict`) de `ndarrays` 1D, listas, diccionarios o Series
- `numpy.ndarray` 2D
- `ndarray` estructurado o de registros
- Una Series
- Otro DataFrame

Junto con los datos, puedes pasar opcionalmente argumentos de `index` (etiquetas de fila) y `columns` (etiquetas de columna). Si pasas un índice y/o columnas, estás garantizando el índice y/o las columnas del DataFrame resultante. Por lo tanto, un diccionario de Series más un índice específico descartará todos los datos que no coincidan con el índice proporcionado.

Si no se pasan etiquetas de eje, se construirán a partir de los datos de entrada según reglas de sentido común.

Vamos a crear un DataFrame simple a partir de un diccionario de listas:

```python
pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})
```

Las entradas del DataFrame no se limitan a números enteros. Por ejemplo, aquí tienes un DataFrame cuyos valores son cadenas (strings):

```python
pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']})
```

El constructor asigna un conteo ascendente desde 0 (0, 1, 2, 3, ...) para las etiquetas de las filas. A veces esto está bien, pero a menudo querremos asignar estas etiquetas nosotros mismos. Por lo tanto, podemos asignar un índice usando el parámetro adecuado:

```python
pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']}, index=['Product A', 'Product B'])
```

También puedes crear un DataFrame usando una lista de listas y especificar las etiquetas de las columnas con el parámetro `columns`:

```python
cities = pd.DataFrame(
    [
        ['California', 39512223, 423967, 'West'],
        ['Washington', 7614893, 184661, 'West'],
        ['New York', 19453561, 141297, 'Est'],
        ['North Carolina', 10488084, 139391, 'Est'],
        ['Florida', 21477737, 170312, 'Est']
    ],
    columns=['name', 'population', 'area', 'position']
)
cities
```

---
##### 🛠️ Práctica 2: Construyendo un DataFrame

Crea un DataFrame a partir de un diccionario que contenga datos de 3 estudiantes.
- Las columnas (llaves del diccionario) deben ser: `'Nombre'`, `'Edad'` y `'Nota'`.
- Usa los nombres y datos numéricos que prefieras.
- Modifica el índice para que sean `'Estudiante 1'`, `'Estudiante 2'` y `'Estudiante 3'`.
- Muestra el DataFrame en pantalla.

```python
# Escribe tu código aquí
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
datos_estudiantes = {
    'Nombre': ['Ana', 'Luis', 'Carlos'],
    'Edad': [22, 23, 21],
    'Nota': [4.5, 3.8, 4.2]
}

df_estudiantes = pd.DataFrame(datos_estudiantes, index=['Estudiante 1', 'Estudiante 2', 'Estudiante 3'])
display(df_estudiantes)
```
</details>

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos</i>
  </p>
</div>
