# 02b_Estructuras_Diccionarios

<table style="width: 100%; border-collapse: collapse; border: none; background: #f8fafc; border-left: 6px solid #1e3a8a; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #0f172a; font-size: 2.1em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        Diccionarios y Estructuras Clave-Valor en Python 🔑
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
        Módulo 01
      </span><br>
      <span style="color: #64748b; font-size: 0.85em;">Docente: Santiago A. Zúñiga M.</span><br>
      <a href="mailto:gestorvirtualcienciadatos@ustatunja.edu.co" style="color: #2563eb; font-size: 0.8em; text-decoration: none; font-weight: 500;">gestorvirtualcienciadatos@ustatunja.edu.co</a>
    </td>
  </tr>
</table>

<div align="center" style="margin-top: 15px; margin-bottom: 15px;">
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/01%20-%20Python/02b_Estructuras_Diccionarios.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## Los Diccionarios (`dict`) 

Los diccionarios son estructuras de datos mutables y altamente eficientes que almacenan información organizada en pares **clave-valor** (`key: value`). A diferencia de las listas o tuplas, los elementos no se consultan mediante un índice numérico, sino a través de una clave única.

**Características Principales**

* **Pares Clave-Valor:** Cada dato almacenado (valor) se encuentra asociado a una etiqueta identificadora (clave).
* **Claves Únicas e Inmutables:** No pueden existir claves duplicadas. Las claves deben ser tipos de datos inmutables (como cadenas o números).
* **Mutables:** Permiten modificar valores existentes, añadir nuevos pares o eliminar claves.
* **Preservación de Orden:** Desde Python 3.7+, los diccionarios mantienen el orden de inserción de sus elementos.

**Métodos y Operaciones Fundamentales**

| Categoría | Método / Sintaxis | Descripción | Ejemplo |
| :--- | :--- | :--- | :--- |
| **Acceso** | `dict[clave]` | Acceso directo. Lanza `KeyError` si la clave no existe. | `vehiculo["marca"]` |
| | `.get(clave, def)` | Acceso seguro. Retorna `None` o un valor por defecto si la clave no existe. | `vehiculo.get("color", "N/A")` |
| **Modificación** | `dict[clave] = val` | Asigna o actualiza el valor asociado a la clave. | `vehiculo["precio"] = 14500` |
| | `.update(dict)` | Agrega o actualiza múltiples pares clave-valor a la vez. | `vehiculo.update({"color": "Rojo"})` |
| **Eliminación** | `.pop(clave)` | Elimina la clave especificada y retorna su valor. | `vehiculo.pop("precio")` |
| **Exploración** | `.keys()` | Retorna una vista con todas las claves del diccionario. | `list(vehiculo.keys())` |
| | `.values()` | Retorna una vista con todos los valores almacenados. | `list(vehiculo.values())` |
| | `.items()` | Retorna una vista con los pares `(clave, valor)` en tuplas. | `list(vehiculo.items())` |

```python
# Creación de un diccionario (uso de llaves {}, pares clave:valor)
vehiculo = {
    "marca": "Toyota",
    "modelo": "Corolla",
    "año": 2020,
    "precio": 15000.50
}

print("Diccionario completo:", vehiculo)
```

```python
# --- ACCESO A DATOS ---
# Acceso directo por clave (Si la clave no existe, arroja un error 'KeyError')
print("\nAcceso a la marca:", vehiculo["marca"])

# Acceso usando el método get() -> Es más seguro, porque si la clave no existe retorna 'None' o un valor por defecto.
print("Uso de get() para 'año':", vehiculo.get("año"))
print("Uso de get() para clave inexistente:", vehiculo.get("color", "Color no registrado"))
```

```python
# --- MODIFICAR Y AGREGAR DATOS ---
vehiculo["precio"] = 14500.00   # Modifica un valor existente
vehiculo["kilometraje"] = 35000 # Si la clave no existe, la crea
print("\nDespués de modificar y agregar:", vehiculo)

# update() permite agregar/modificar múltiples pares a la vez
vehiculo.update({"color": "Rojo", "puertas": 4})
```

```python
# --- ELIMINAR DATOS ---
precio_borrado = vehiculo.pop("precio") # Elimina la clave y retorna su valor
print("\nSe eliminó el precio que era:", precio_borrado)
```

```python
# --- EXPLORACIÓN DE DICCIONARIOS (Métodos fundamentales) 🧗 ---
print("\n--- Explorando el diccionario ---")
print("Solo las Claves (keys):", list(vehiculo.keys()))
print("Solo los Valores (values):", list(vehiculo.values()))
print("Pares Clave-Valor (items):", list(vehiculo.items()))
```

#### 🛠️ Práctica: Diccionarios Básicos

**Ejercicio 1:**
El centro de investigación de la USTA Tunja requiere registrar y actualizar la información técnica de un servidor de procesamiento de datos:

1. Declara el diccionario `servidor = {"ip": "192.168.1.50", "so": "Ubuntu", "ram_gb": 32, "estado": "activo"}`.
2. Accede al sistema operativo utilizando el método seguro `.get("so")` e imprímelo en pantalla.
3. Intenta obtener la clave `"almacenamiento_tb"` con `.get()`, asignándole como valor por defecto `"1TB"`.
4. Actualiza la memoria RAM a `64` asignando directamente el nuevo valor a la clave `ram_gb`.
5. Agrega las claves `"puerto"` con valor `8080` y `"mantenimiento"` con valor `False` usando el método `.update()`.
6. Elimina la clave `"estado"` usando el método `.pop()`.

```python
# Escribe tu código aquí
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
# Ejercicio 1
servidor = {"ip": "192.168.1.50", "so": "Ubuntu", "ram_gb": 32, "estado": "activo"}

print(f"Sistema Operativo: {servidor.get('so')}")
print(f"Almacenamiento: {servidor.get('almacenamiento_tb', '1TB')}")

servidor['ram_gb'] = 64
servidor.update({"puerto": 8080, "mantenimiento": False})
servidor.pop("estado")

print("\nEstado final del servidor:")
print(servidor)

```
</details>

**Ejercicio 2:**
1. Crea un diccionario llamado `libro` con las claves: `'titulo'` (string), `'autor'` (string) y `'año'` (int).
2. Añade una nueva clave `'genero'` con el valor `'Ficción'`.
3. Incrementa el valor de `'año'` en 5.
4. Intenta imprimir la clave `'editorial'` usando `.get()` con un mensaje por defecto de `'Editorial desconocida'`.

```python
# Escribe tu código aquí
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
# Ejercicio 2
libro = {'titulo': '1984', 'autor': 'George Orwell', 'año': 1949}
libro['genero'] = 'Ficción'
libro['año'] += 5

print(f"\nEditorial: {libro.get('editorial', 'Editorial desconocida')}")
```
</details>

--- 
### 1. Iteración y Vistas

Los diccionarios tienen 3 métodos útiles para ver sus elementos: `.keys()`, `.values()` y `.items()`.

```python
inventario = {'manzanas': 50, 'naranjas': 30, 'peras': 15}

print("--- Iterar sobre claves (por defecto) ---")
for fruta in inventario:  # Equivalente a inventario.keys()
    print(fruta)

print("\n--- Iterar sobre valores ---")
for cantidad in inventario.values():
    print(cantidad)

print("\n--- Iterar sobre pares clave-valor ---")
for fruta, cantidad in inventario.items():
    print(f"{fruta.capitalize()}: {cantidad} unidades")
```

#### 🛠️ Práctica: Iteración

**Problema:**
Dado el diccionario `calificaciones = {'Ana': 8.5, 'Luis': 9.0, 'Pedro': 7.0, 'Maria': 9.5}`.
1. Itera sobre los pares clave-valor.
2. Imprime **solo** los nombres de los estudiantes que tienen una calificación mayor o igual a `9.0`.

```python
calificaciones = {'Ana': 8.5, 'Luis': 9.0, 'Pedro': 7.0, 'Maria': 9.5}

# Tu solución aquí
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
calificaciones = {'Ana': 8.5, 'Luis': 9.0, 'Pedro': 7.0, 'Maria': 9.5}
for nombre, nota in calificaciones.items():
    if nota >= 9.0:
        print(nombre)
```

</details>

--- 
### 2. Dictionary Comprehensions y Actualizaciones

Las *Dictionary Comprehensions* nos permiten crear diccionarios de forma muy elegante y concisa en una sola línea.

```python
# Crear un diccionario de números y sus cuadrados
cuadrados = {x: x**2 for x in range(1, 6)}
print("Comprensión (cuadrados):", cuadrados)

# Filtrar un diccionario (ej. solo los que tienen cuadrado par)
pares = {k: v for k, v in cuadrados.items() if v % 2 == 0}
print("Comprensión (solo pares):", pares)
```

```python
# Invertir un diccionario (Intercambiar claves y valores)
codigos = {'a': 1, 'b': 2, 'c': 3}
codigos_invertidos = {v: k for k, v in codigos.items()}
print("Invertido:", codigos_invertidos)
```

```python
# Actualización masiva con .update()
config = {'host': 'localhost', 'port': 8080}
nuevos_ajustes = {'port': 9000, 'debug': True}

config.update(nuevos_ajustes)
print("Configuración actualizada:", config)
```

#### 🛠️ Práctica: Comprehensions

**Problema:**
A partir de la lista de palabras `palabras = ['sol', 'luna', 'estrella', 'cielo']`:
1. Usa una **dictionary comprehension** para crear un diccionario donde la clave sea la palabra y el valor sea la longitud de esa palabra (usando `len()`).
2. Llama al diccionario resultante `longitud_palabras` e imprímelo.

```python
palabras = ['sol', 'luna', 'estrella', 'cielo']

# Tu solución aquí
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
palabras = ['sol', 'luna', 'estrella', 'cielo']
longitud_palabras = {p: len(p) for p in palabras}
print(longitud_palabras)
```

</details>

--- 
### 3. Operadores modernos y trucos 💎

Python 3.9+ introdujo operadores nativos para diccionarios. Además, métodos como `.setdefault()` son el secreto de los profesionales.

```python
# Fusión de diccionarios (Merge)
default_config = {'tema': 'oscuro', 'fuente': 'Arial', 'tamaño': 12}
user_config = {'tema': 'claro', 'tamaño': 14}

# Método Clásico (Python 3.5+): Unpacking
config_final_1 = {**default_config, **user_config}
print("Merge con **:", config_final_1)

# Método Moderno (Python 3.9+): Operador | (Pipe)
# Este es el más recomendado hoy en día.
config_final_2 = default_config | user_config
print("Merge con | :", config_final_2)
```

```python
# Truco Pro: .setdefault()
# Obtiene un valor, pero si no existe, lo inserta primero.
conteo_palabras = {}
texto = "hola mundo hola python hola"

for palabra in texto.split():
    # En lugar de hacer if palabra in conteo_palabras:
    conteo_palabras[palabra] = conteo_palabras.setdefault(palabra, 0) + 1

print("Frecuencia de palabras:", conteo_palabras)
```

#### 🛠️ Práctica: Operadores modernos

**Problema:**
Tienes dos diccionarios de ventas parciales:
`v_q1 = {'enero': 100, 'febrero': 200}` y `v_q2 = {'marzo': 150, 'abril': 300}`.
1. Fusiónalos en un nuevo diccionario `ventas_totales` usando el operador moderno `|`.
2. Usa el método `.setdefault()` para asegurarte de que exista la clave `'mayo'`, asignándole el valor `0` (si ya existe no debe sobreescribirlo, aunque aquí no existirá).

```python
v_q1 = {'enero': 100, 'febrero': 200}
v_q2 = {'marzo': 150, 'abril': 300}

# Tu solución aquí
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
v_q1 = {'enero': 100, 'febrero': 200}
v_q2 = {'marzo': 150, 'abril': 300}

ventas_totales = v_q1 | v_q2
ventas_totales.setdefault('mayo', 0)

print(ventas_totales)
```

</details>

--- 
### 4. Diccionarios Anidados y Copias 🏆

Los diccionarios pueden contener otros diccionarios (anidados). Aquí es vital entender cómo se copian los datos en memoria.

```python
# Diccionario Anidado
empresa = {
    'desarrollo': {
        'empleados': ['Juan', 'Ana'],
        'lenguaje': 'Python'
    },
    'ventas': {
        'empleados': ['Luis'],
        'objetivo': 10000
    }
}

print("Lenguaje de Desarrollo:", empresa['desarrollo']['lenguaje'])
```

```python
# ⚠️ El peligro de la Copia Superficial (Shallow Copy)
empresa_copia = empresa.copy()

# Si modificamos un elemento interno en la copia...
empresa_copia['desarrollo']['lenguaje'] = 'Rust'

# ...¡También se modifica en el original!
print("Lenguaje original:", empresa['desarrollo']['lenguaje'])
print("Lenguaje copia:   ", empresa_copia['desarrollo']['lenguaje'])

print("\n¿Por qué? Porque .copy() solo copia el primer nivel. Los niveles internos siguen compartiendo referencia.")
```

```python
# Solución: Copia Profunda (Deep Copy) usando el módulo estándar 'copy'
import copy

# Restauramos para el ejemplo
empresa['desarrollo']['lenguaje'] = 'Python'

empresa_deep = copy.deepcopy(empresa)
empresa_deep['desarrollo']['lenguaje'] = 'Go'

print("Lenguaje original después del deepcopy:", empresa['desarrollo']['lenguaje'])
print("Lenguaje deepcopy:                     ", empresa_deep['desarrollo']['lenguaje'])
```

#### 🛠️ Práctica: Anidados y Copias

**Problema:**
Dada la estructura anidada de la `biblioteca`:
1. Usa el módulo `copy` para hacer una **copia profunda (deep copy)** del diccionario `biblioteca` a una variable `biblioteca_backup`.
2. En la `biblioteca_backup`, añade un nuevo elemento `'Dune'` a la lista de libros de la categoría `'Ciencia Ficción'`.
3. Imprime la lista de libros de Ciencia Ficción de **ambos** diccionarios para comprobar que la adición afectó al backup pero no a la biblioteca original.

```python
import copy

biblioteca = {
    'Ciencia Ficción': ['1984', 'Fahrenheit 451'],
    'Fantasía': ['El Señor de los Anillos', 'El Hobbit']
}

# Tu solución aquí
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
import copy

biblioteca = {
    'Ciencia Ficción': ['1984', 'Fahrenheit 451'],
    'Fantasía': ['El Señor de los Anillos', 'El Hobbit']
}

biblioteca_backup = copy.deepcopy(biblioteca)
biblioteca_backup['Ciencia Ficción'].append('Dune')

print("Original:", biblioteca['Ciencia Ficción'])
print("Backup:  ", biblioteca_backup['Ciencia Ficción'])
```

</details>

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos</i>
  </p>
</div>
