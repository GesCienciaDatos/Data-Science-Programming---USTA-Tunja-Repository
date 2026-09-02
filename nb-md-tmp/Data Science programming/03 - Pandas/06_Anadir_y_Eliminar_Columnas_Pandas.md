# 06_Anadir_y_Eliminar_Columnas_Pandas

<table style="width: 100%; border-collapse: collapse; border: none; background: #f8fafc; border-left: 6px solid #1e3a8a; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #0f172a; font-size: 2.1em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        Adición, Eliminación y Renombrado de Columnas ✂️
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
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/03%20-%20Pandas/06_Anadir_y_Eliminar_Columnas_Pandas.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## Añadir y Eliminar Columnas 

Conceptualmente, puedes tratar un DataFrame como si fuera un diccionario (`dict`) de objetos Series que comparten el mismo índice. 

Por lo tanto, obtener, asignar y eliminar columnas funciona con una sintaxis prácticamente idéntica a las operaciones de diccionarios en Python nativo.

Para explorar esto, construiremos un pequeño DataFrame de ciudades:

```python
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
display(cities)
```

---
### 1. Añadir Columnas

La forma más básica de añadir una columna es asignarle valores a una nueva llave del DataFrame. De forma predeterminada, **las nuevas columnas se insertan al final (a la derecha).**

```python
# Convertimos la población a millones
cities['population (M)'] = cities['population'] / 1000000
display(cities)
```

También podemos crear columnas lógicas booleanas directamente evaluando condiciones (creará valores `True` o `False`):

```python
cities['high-density'] = (cities['population'] / cities['area']) > 100.0
display(cities)
```

#### Insertar en una posición específica (`insert`)
Si no quieres que la columna vaya al final, el método `insert()` te permite colocarla exactamente donde quieres (usando el índice numérico de la posición de la columna).

```python
pop_density = cities['population'] / cities['area']

# Insertamos en la posición 3 (es decir, como la 4ta columna)
cities.insert(3, "population density", pop_density)
display(cities)
```

---
### 2. Eliminar Columnas (`drop`)

Para eliminar usamos la función `drop()`. Es de suma importancia especificar el argumento `axis=1`, lo que le indica a Pandas que estamos buscando en las columnas, no en las filas (`axis=0`).

```python
cities.drop('population (M)', axis=1)
```

⚠️ **¡Cuidado! El DataFrame original no ha sido modificado aún.**
Casi todas las funciones destructivas en Pandas devuelven una *copia* visual del DataFrame con el cambio aplicado, pero dejan el original intacto por seguridad.

```python
display(cities)
```

Si de verdad queremos hacer el borrado permanente, tenemos dos opciones válidas:

**Solución 1) Reasignar la variable:** Sobrescribimos el DataFrame.

```python
cities = cities.drop('population (M)', axis=1)
display(cities)
```

**Solución 2) Usar el parámetro `inplace=True`:** Esto fuerza a Pandas a mutar el DataFrame original sin devolver copias. Es un poco más rápido y gasta menos memoria RAM.

```python
cities.drop('population density', axis=1, inplace=True)
display(cities)
```

---
##### 🛠️ Práctica: Limpieza de Columnas
Elimina la columna `position` del DataFrame `cities` de manera permanente utilizando el parámetro `inplace=True`.

```python
# Escribe tu código aquí
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
cities.drop('position', axis=1, inplace=True)
display(cities)
```
</details>

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos</i>
  </p>
</div>
