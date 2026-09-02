# 02a_Estructuras_Listas_Tuplas_Conjuntos

<table style="width: 100%; border-collapse: collapse; border: none; background: #f8fafc; border-left: 6px solid #1e3a8a; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #0f172a; font-size: 2.1em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        Colecciones en Python: Listas, Tuplas y Conjuntos 📋
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
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/01%20-%20Python/02a_Estructuras_Listas_Tuplas_Conjuntos.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---

## Estructuras de Datos Nativas
Manejar múltiples datos es el pan de cada día en Ciencia de Datos. En este notebook dominaremos las tres colecciones (estructuras de datos) más importantes que complementan a los diccionarios: **Listas, Tuplas y Conjuntos (Sets)**, desde lo más básico hasta trucos de rendimiento y comprensión.


Las **estructuras de datos nativas** son contenedores integrados en Python que permiten almacenar, organizar y manipular colecciones de elementos. 

Para seleccionar la estructura correcta en un flujo de Ciencia de Datos, se deben evaluar tres propiedades fundamentales:

* **Mutabilidad:** Determina si los elementos de la estructura pueden modificarse, añadirse o eliminarse después de su creación (**Mutable**) o si permanecen fijos (**Inmutable**).
* **Orden / Indexación:** Indica si la estructura preserva una secuencia de posiciones indexables $(0, 1, 2, \dots)$, lo que permite acceder a elementos específicos mediante su índice.
* **Duplicación:** Define si la colección admite valores repetidos o si exige que cada elemento sea único.

---
### 1. Las Listas (`list`) 🌱

Las **listas** son estructuras de datos secuenciales, dinámicas y **mutables**. Son fundamentales en Python para gestionar colecciones de elementos que cambian a lo largo del tiempo.

**Características Principales**
* **Mutables:** Se pueden modificar, añadir o eliminar elementos después de su creación.
* **Ordenadas:** Cada elemento conserva una posición con un índice basado en `0`.
* **Heterogéneas:** Pueden almacenar distintos tipos de datos simultáneamente (enteros, cadenas, booleanos o incluso otras listas).
* **Admiten Duplicados:** Un mismo valor puede aparecer múltiples veces en diferentes posiciones.

---

**Métodos Clave para la Manipulación de Listas**

| Categoría | Método / Operación | Descripción | Ejemplo |
| :--- | :--- | :--- | :--- |
| **Agregar** | `.append(x)` | Agrega el elemento `x` al **final** de la lista. | `lista.append(60)` |
| | `.insert(i, x)` | Inserta el elemento `x` en la posición del índice `i`. | `lista.insert(0, 5)` |
| | `.extend(coleccion)` | Concatena los elementos de otra colección al final. | `lista.extend([70, 80])` |
| **Eliminar** | `.remove(x)` | Busca y elimina la **primera ocurrencia** del valor `x`. | `lista.remove(20)` |
| | `.pop(i)` | Elimina y **retorna** el elemento en el índice `i` (por defecto el último). | `lista.pop()` |
| **Orden y Uso** | `.sort()` | Ordena la lista original (*ascendente* por defecto o *descendente* con `reverse=True`). | `lista.sort(reverse=True)` |
| | `.count(x)` | Cuenta cuántas veces se repite el elemento `x`. | `lista.count(3)` |
| | `len(lista)` | Función *built-in* que retorna el número total de elementos. | `len(lista)` |

```python
# Creación de listas (uso de corchetes [])
lista_numeros = [10, 20, 30, 40, 50]
lista_mixta = ["Python", 3.10, True, [1, 2, 3]] # Una lista puede contener otra lista

# Acceso por índice
print("Primera lista:", lista_numeros[0])
print("Última lista:", lista_numeros[-1])

print("\nLista inicial:", lista_numeros)
```

```python
# --- MÉTODOS PARA AGREGAR ELEMENTOS ---
print("\n--- Agregando elementos ---")
lista_numeros.append(60) # Agrega un elemento AL FINAL
print("append(60):", lista_numeros)

lista_numeros.insert(0, 5) # Inserta el valor '5' en el índice '0' (al inicio)
print("insert(0, 5):", lista_numeros)

lista_numeros.extend([70, 80]) # Concatena otra colección de elementos al final
print("extend([70, 80]):", lista_numeros)
```

```python
# --- MÉTODOS PARA ELIMINAR ELEMENTOS ---
print("\n--- Eliminando elementos ---")
lista_numeros.remove(20) # Busca el primer '20' en la lista y lo elimina
print("remove(20):", lista_numeros)

elemento_borrado = lista_numeros.pop() # Elimina y RETORNA el ÚLTIMO elemento (por defecto)
print("pop(): Eliminó el", elemento_borrado, "| Lista resultante:", lista_numeros)

elemento_indice_2 = lista_numeros.pop(2) # Elimina y RETORNA el elemento en el índice 2
print("pop(2): Eliminó el", elemento_indice_2, "| Lista resultante:", lista_numeros)
```

```python
# --- OTROS MÉTODOS Y OPERACIONES UTILES ---
print("\n--- Otras operaciones ---")
lista_desordenada = [8, 3, 15, 1, 10]

lista_desordenada.sort() # Ordena la lista de menor a mayor (Modifica la lista original)
print("sort() - Orden ascendente:", lista_desordenada)

lista_desordenada.sort(reverse=True) # Ordena de mayor a menor
print("sort(reverse=True) - Orden descendente:", lista_desordenada)

print("Cantidad de veces que aparece el '3':", lista_desordenada.count(3))
print("Longitud de la lista (cuántos elementos tiene):", len(lista_desordenada))

# Operadores entre listas
lista_a = [1, 2]
lista_b = [3, 4]
print("\nConcatenación de listas (lista_a + lista_b):", lista_a + lista_b)
print("Repetición de listas (lista_a * 3):", lista_a * 3)
```

#### 🛠️ Práctica: Listas

**Ejercicio 1:**
Un docente de la USTA Tunja requiere registrar y actualizar las notas parciales de un estudiante en la asignatura de Programación para Ciencia de Datos:

1. Declara la lista `notas = [3.8, 2.5, 4.2, 3.0]`.
2. Añade la nota `4.5` al final de la lista utilizando `.append()`.
3. Inserta una nota perfecta `5.0` en la primera posición (índice `0`) usando `.insert()`.
4. Elimina la nota corregida `2.5` de la lista mediante `.remove()`.
5. Ordena la lista de mayor a menor utilizando `.sort(reverse=True)`.
6. Imprime en pantalla la lista final de notas organizada y el número total de evaluaciones registradas con `len()`.

```python
# Tu solución aquí
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
# Ejercicio 1
notas = [3.8, 2.5, 4.2, 3.0]
notas.append(4.5)
notas.insert(0, 5.0)
notas.remove(2.5)
notas.sort(reverse=True)
print("Notas finales:", notas)
print("Total de evaluaciones:", len(notas))

```
</details>

**Ejercicio 2:**
Crea una lista llamada `numeros` con los valores `[10, 20, 30, 40]`.
1. Añade el número `50` al final.
2. Cambia el primer elemento (el `10`) por un `5`.
3. Usa `.pop()` para eliminar el número `30` pasándole su índice correspondiente. Imprime la lista final.

```python
# Tu solución aquí
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
# Ejercicio 2
numeros = [10, 20, 30, 40]
numeros.append(50)
numeros[0] = 5
numeros.pop(2) # El 30 está en el índice 2
print("Lista de numeros final:", numeros)
```
</details>

---

### 2. Las Tuplas (`tuple`) y el Desempaquetado 🛠️

Las **tuplas** son colecciones de datos ordenadas e **inmutables**. A diferencia de las listas, una vez que una tupla es creada, sus elementos no pueden modificarse, añadirse ni eliminarse. Son especialmente eficientes en el uso de memoria y garantizan la integridad de datos que deben permanecer constantes. Pueden usarse como claves en diccionarios.

**Características Principales**
* **Inmutables:** No admiten operaciones de modificación como `.append()`, `.remove()` o asignación directa de elementos.
* **Ordenadas:** Cada elemento conserva una posición indexable basada en `0`.
* **Eficiencia:** Ocupan menos espacio en memoria y ejecutan búsquedas más rápidas que las listas.
* **Empaquetado y Desempaquetado (*Unpacking*):** Permiten asignar sus valores directamente a múltiples variables de forma simultánea.

> 🤓 **Sintaxis para elemento único:** Para definir una tupla con un solo elemento, es obligatorio incluir una coma al final: `mi_tupla = (10,)`. De lo contrario, Python la interpretará como un tipo de dato entero o paréntesis de agrupación.

---

**Métodos Disponibles en Tuplas**

Debido a su naturaleza inmutable, las tuplas cuentan únicamente con dos métodos de búsqueda:

| Método | Descripción | Ejemplo |
| :--- | :--- | :--- |
| `.count(x)` | Cuenta el número de apariciones del valor `x` en la tupla. | `tupla.count(2)` |
| `.index(x)` | Retorna el primer índice donde se encuentra el valor `x`. | `tupla.index("Jueves")` |

```python
# Creación de tuplas (uso de paréntesis ())
dias_semana = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes")

# 🤓 Nota: Para crear una tupla de un solo elemento, DEBES poner una coma al final.
tupla_un_elemento = (10,)

# También se pueden crear sin paréntesis si hay comas
punto_3d = 10, 20, 30

print("Tupla completa:", dias_semana)
print("Acceso por índice (dias_semana[1]):", dias_semana[1])

# Intentar modificar arroja error (TypeError):
# dias_semana[0] = "Domingo"
```

```python
# --- MÉTODOS (Solo tiene 2 métodos porque no puede ser modificada) ---
tupla_numeros = (1, 2, 3, 2, 4, 2)
print("\ncount(2) - ¿Cuántos números '2' hay?:", tupla_numeros.count(2))
print("index('Jueves') - ¿En qué índice está 'Jueves'?:", dias_semana.index("Jueves"))
```

```python
# --- 🧗 DESEMPAQUETADO (Unpacking) ---
# Puedes asignar los elementos de una tupla directamente a variables
coordenada_gps = (4.5, -74.0)
latitud, longitud = coordenada_gps

print("\nDesempaquetado Básico:")
print("Latitud extraída:", latitud)
print("Longitud extraída:", longitud)

# Desempaquetado avanzado usando *
primero, *medio, ultimo = (1, 2, 3, 4, 5)
print("\nDesempaquetado Avanzado:")
print("Primero:", primero)
print("Medio (se vuelve lista):", medio)
print("Último:", ultimo)
```

#### 🛠️ Práctica: Tuplas

**Ejercicio 1:**
Una estación meteorológica instalada en la USTA Tunja registra la ubicación de un sensor y una serie de temperaturas fijas tomadas durante un ciclo de prueba:

1. Declara la tupla `ubicacion_sensor = (5.5353, -73.3678, 2820)` que contiene la latitud, la longitud y la altitud en metros.
2. Realiza el **desempaquetado** de la tupla `ubicacion_sensor` en tres variables: `lat`, `lon` y `altitud`.
3. Declara una tupla con las lecturas de temperatura: `temperaturas = (14.5, 12.0, 14.5, 16.2, 14.5, 11.8)`.
4. Utiliza `.count()` para determinar cuántas veces se registró exactamente la temperatura de `14.5`.
5. Obtén el índice de la lectura `16.2` utilizando el método `.index()`.
6. Imprime en pantalla las coordenadas desempaquetadas, la cantidad de repeticiones de `14.5` y el índice hallado.

```python
# Tu solución aquí
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
# Ejercicio 1
ubicacion_sensor = (5.5353, -73.3678, 2820)
lat, lon, altitud = ubicacion_sensor

temperaturas = (14.5, 12.0, 14.5, 16.2, 14.5, 11.8)
conteo_14_5 = temperaturas.count(14.5)
indice_16_2 = temperaturas.index(16.2)

print(f"Coordenadas - Lat: {lat}, Lon: {lon}, Alt: {altitud}m")
print(f"Temperatura 14.5 registrada {conteo_14_5} veces.")
print(f"El índice de la lectura 16.2 es: {indice_16_2}")

```
</details>

**Ejercicio 2:**
Tienes una tupla con información de una persona: `persona = ("Ana", 28, "Ingeniera", "Madrid", "España")`.
Usa el **desempaquetado avanzado** con `*` para guardar el nombre en una variable, la edad en otra, y meter todo el resto (profesión, ciudad, país) en una variable lista llamada `detalles`.

```python
# Tu solución aquí
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
# Ejercicio 2
persona = ("Ana", 28, "Ingeniera", "Madrid", "España")
nombre, edad, *detalles = persona

print("\nNombre:", nombre)
print("Edad:", edad)
print("Detalles Extras:", detalles)
```
</details>

---

### 3. Los Conjuntos (`set`) y Valores Únicos 🧠

Los **conjuntos** son colecciones no ordenadas de elementos **únicos** y **mutables**. Son ampliamente utilizados en Ciencia de Datos para la depuración de datos (eliminación de duplicados) y para realizar operaciones algebraicas de teoría de conjuntos.

**Características Principales**
* **Únicos:** No permiten elementos duplicados. Si se ingresan valores repetidos, Python los descarta automáticamente.
* **Desordenados:** Los elementos no conservan una posición ni índice fijo, por lo que no es posible acceder a ellos mediante sintaxis de corchetes (`set[0]`).
* **Mutables:** Permiten agregar y quitar elementos.

---

**Operaciones y Métodos Principales**

| Operación / Método | Sintaxis | Descripción | Ejemplo |
| :--- | :---: | :--- | :--- |
| **Agregar** | `.add(x)` | Añade el elemento `x` al conjunto. | `conjunto.add(105)` |
| **Eliminar seguro** | `.discard(x)` | Elimina `x`. No genera error si el valor no existe (a diferencia de `.remove()`). | `conjunto.discard(102)` |
| **Unión** | `A \| B` | Retorna todos los elementos presentes en ambos conjuntos (sin repetir). | `grupo_A \| grupo_B` |
| **Intersección** | `A & B` | Retorna solo los elementos presentes en ambos conjuntos simultáneamente. | `grupo_A & grupo_B` |
| **Diferencia** | `A - B` | Retorna los elementos presentes en `A` pero que no están en `B`. | `grupo_A - grupo_B` |
| **Diferencia Simétrica** | `A ^ B` | Retorna los elementos que están en uno u otro conjunto, pero no en ambos. | `grupo_A ^ grupo_B` |

> 💡 **Tip de Limpieza de Datos:** Puedes eliminar todos los duplicados de una lista convirtiéndola a conjunto con `set()` y volviéndola a transformar a lista con `list()`: `lista_limpia = list(set(lista_duplicados))`.

```python
# Creación de conjuntos (uso de llaves {} PERO sin formato clave:valor como los diccionarios)
ids_usuarios = {101, 102, 103, 101, 104, 102} # Notar que hay duplicados

# Python automáticamente elimina los duplicados
print("Conjunto original (duplicados eliminados):", ids_usuarios)

# Convertir lista a conjunto (Truco para eliminar duplicados)
lista_con_duplicados = [1, 1, 2, 2, 3, 3]
lista_sin_duplicados = list(set(lista_con_duplicados))
print("Truco para limpiar duplicados de una lista:", lista_sin_duplicados)
```

```python
# --- AGREGAR Y ELIMINAR ---
ids_usuarios.add(105) # Agrega un elemento
print("Después de add(105):", ids_usuarios)

ids_usuarios.discard(102) # Elimina el elemento. Si no existe, NO arroja error (remove() sí arrojaría error)
print("Después de discard(102):", ids_usuarios)
```

```python
# --- OPERACIONES MATEMÁTICAS ENTRE CONJUNTOS (Teoría de conjuntos) 🧗 ---
grupo_A = {"Ana", "Juan", "Pedro", "Maria"}
grupo_B = {"Pedro", "Maria", "Luis", "Carlos"}

print("\n--- Operaciones de Conjuntos ---")
print("Unión (A | B) - Todos los miembros únicos:", grupo_A | grupo_B)
print("Intersección (A & B) - Miembros en común:", grupo_A & grupo_B)
print("Diferencia (A - B) - En A pero no en B:", grupo_A - grupo_B)
print("Diferencia Simétrica (A ^ B) - En uno o en otro, pero no en ambos:", grupo_A ^ grupo_B)

# Eficiencia de Búsqueda (Se recomienda usar Sets si vas a hacer muchos 'in')
print("\n¿Está Carlos en el Grupo A?", "Carlos" in grupo_A)
```

#### 🛠️ Práctica: Conjuntos

**Ejercicio 1:**
El departamento de admisiones de la USTA Tunja registra las listas de asistencia a dos talleres de actualización técnica:
`taller_python = ["Ana", "Juan", "Pedro", "Ana", "Carlos"]`
`taller_sql = ["Pedro", "Maria", "Luis", "Carlos"]`

1. Convierte la lista `taller_python` a un conjunto (`set`) para eliminar automáticamente el duplicado de `"Ana"`.
2. Convierte la lista `taller_sql` a un conjunto (`set`).
3. Agrega la estudiante `"Sofia"` al conjunto de Python mediante `.add()`.
4. Utiliza el operador de **unión** (`|`) para obtener la lista total de estudiantes únicos en ambos talleres.
5. Utiliza el operador de **intersección** (`&`) para identificar qué estudiantes asistieron a ambos talleres.
6. Utiliza el operador de **diferencia** (`-`) para encontrar qué estudiantes asistieron exclusivamente al taller de Python.

```python
# Tu solución aquí
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
# Ejercicio 1
taller_python = ["Ana", "Juan", "Pedro", "Ana", "Carlos"]
taller_sql = ["Pedro", "Maria", "Luis", "Carlos"]

set_python = set(taller_python)
set_sql = set(taller_sql)

set_python.add("Sofia")

print("Unión (todos únicos):", set_python | set_sql)
print("Intersección (ambos talleres):", set_python & set_sql)
print("Diferencia (Solo Python):", set_python - set_sql)

```
</details>

**Ejercicio 2:**
Tienes la lista `correos = ["a@a.com", "b@b.com", "a@a.com", "c@c.com"]`. Transforma la lista en un conjunto para quedarte solo con correos únicos, añade el correo `"d@d.com"`, e imprime la cantidad final de correos únicos (usando `len()`).

```python
# Tu solución aquí
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python

# Ejercicio 2
correos = ["a@a.com", "b@b.com", "a@a.com", "c@c.com"]
correos_unicos = set(correos)
correos_unicos.add("d@d.com")
print("\nCorreos únicos:", correos_unicos)
print("Cantidad total:", len(correos_unicos))

```
</details>

**Ejercicio 3:**
Tienes a los alumnos de `matematicas = {"A", "B", "C"}` y los de `fisica = {"B", "C", "D"}`.
Imprime a los alumnos que estudian **ambas** materias, y luego imprime a los alumnos que estudian **solo matemáticas** (que no están en física).

```python
# Tu solución aquí
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python

# Ejercicio 3
matematicas = {"A", "B", "C"}
fisica = {"B", "C", "D"}

print("\nEstudian ambas (Intersección):", matematicas & fisica)
print("Solo Matemáticas (Diferencia):", matematicas - fisica)
```
</details>

---

### 4. List Comprehensions, `zip` y `enumerate` 🏆

Escribir código *Pythónico* implica abandonar patrones heredados de otros lenguajes (como C o Java) y aprovechar al máximo las estructuras nativas de Python. Esto incluye usar **List Comprehensions** en lugar de largos bucles `for`, e iterar eficientemente con las funciones nativas `zip()` y `enumerate()`. 

El objetivo principal de estas tres herramientas es la **expresividad**: permitir que el código comunique la intención del programador de forma directa, reduciendo el "ruido" visual de la lógica de control.

#### 4.1 List Comprehensions (Comprensiones de Listas)
Inspiradas en la notación de construcción de conjuntos en matemáticas (ej. $S = \{x^2 \mid x \in \mathbb{N}, x < 10\}$), las comprensiones proporcionan una sintaxis concisa para crear nuevas listas a partir de iterables existentes.

**Teoría y rendimiento:**
Conceptualmente, una comprensión colapsa la lógica de inicialización, iteración, evaluación condicional y anexión (append) en una sola expresión. A nivel de rendimiento, las *List Comprehensions* son significativamente más rápidas que un bucle `for` equivalente. Esto se debe a que la comprensión se ejecuta a nivel del intérprete en C, evitando la sobrecarga (overhead) de buscar y llamar al método `.append()` en cada iteración.

**Sintaxis general:**
`[expresión for elemento in iterable if condición]`

*   **`expresión`**: Lo que conformará cada elemento de la nueva lista (puede ser el elemento mismo o una mutación de este).
*   **`for elemento in iterable`**: El ciclo que extrae los datos de la estructura original.
*   **`if condición` (Opcional)**: Un filtro que determina si el elemento debe incluirse.

```python
# Enfoque tradicional (Bucle FOR clásico)
cuadrados_tradicional = []
for x in range(1, 11):
    if x % 2 == 0:
        cuadrados_tradicional.append(x**2)
print("Tradicional:", cuadrados_tradicional)

# Enfoque Pythónico (List Comprehension)
# Sintaxis: [expresión for elemento in iterable if condición]
cuadrados_comprehension = [x**2 for x in range(1, 11) if x % 2 == 0]
print("Comprehension:", cuadrados_comprehension)

# Otro ejemplo: Transformar cadenas a mayúsculas
frutas = ["manzana", "banana", "cereza"]
frutas_mayus = [fruta.upper() for fruta in frutas]
print("\nFrutas en mayúscula:", frutas_mayus)
```

#### 4.2 Iteración con estado: `enumerate()`
En la teoría de la programación, es común el "patrón de recorrido con índice", donde se necesita tanto el valor actual como su posición espacial dentro de la estructura de datos. Python resuelve esto mediante la función incorporada `enumerate()`.

**Teoría:**
`enumerate(iterable, start=0)` toma una colección y la envuelve en un objeto iterador especial. En lugar de devolver un solo elemento por ciclo, devuelve una **tupla** que contiene un contador (que por defecto inicia en 0) y el valor extraído del iterable original. 

Esto elimina la necesidad de gestionar manualmente variables de estado (como inicializar un `contador = 0` y sumarle 1 en cada ciclo) y erradica el antipatrón `for i in range(len(lista))`, el cual rompe la abstracción de iterar directamente sobre los elementos.

```python
modelos = ["Regresión Lineal", "Árbol de Decisión", "Red Neuronal"]

# Antipatrón (Heredado de C/Java):
# for i in range(len(modelos)):
#     print(f"Modelo {i}: {modelos[i]}")

# Enfoque Pythónico con enumerate()
# Devuelve la tupla (índice, valor) en cada iteración
print("--- Iteración con Enumerate ---")
for indice, modelo in enumerate(modelos, start=1):
    print(f"Modelo {indice}: {modelo}")
```

#### 4.3 Iteración paralela: `zip()`
En el procesamiento de datos, frecuentemente nos encontramos con información relacional distribuida en diferentes colecciones (vectores paralelos). `zip()` es la respuesta teórica de Python para unificar múltiples ejes de datos.

**Teoría:**
El nombre proviene de "zipper" (cremallera). La función `zip(*iterables)` toma un número arbitrario de iterables y los evalúa de forma perezosa (lazy evaluation), devolviendo un iterador de tuplas. En cada paso, extrae el elemento *i-ésimo* de cada colección y los agrupa en una única tupla relacional.

Un aspecto crucial de la teoría de conjuntos implementada en `zip()` es su comportamiento en las fronteras: la iteración se detiene estrictamente cuando el iterable **más corto** se agota. Esto previene automáticamente las excepciones de "índice fuera de rango" (IndexError) sin necesidad de escribir aserciones condicionales que comparen las longitudes previas de las listas.

```python
nombres = ["Ana", "Juan", "Luis"]
edades = [28, 30, 25]
ciudades = ["Madrid", "Bogotá", "Lima"]

# Unificando 3 listas paralelas
print("--- Iteración Paralela con Zip ---")
for nombre, edad, ciudad in zip(nombres, edades, ciudades):
    print(f"{nombre} tiene {edad} años y vive en {ciudad}")

# Truco de Data Science: Convertir dos listas en un diccionario en O(N)
# Ideal para mapeos rápidos
columnas = ["id", "nombre", "edad"]
valores = [101, "Carlos", 35]
registro = dict(zip(columnas, valores))
print("\nDiccionario creado con zip():", registro)
```

#### 🛠️ Práctica: List Comprehensions, `zip` y `enumerate`

**Problema:**
Tienes las listas `productos = ["Teclado", "Mouse", "Monitor"]` y `precios = [50, 20, 200]`.
1. Usa una **List Comprehension** sobre `precios` para crear una lista `precios_con_iva` que contenga el precio multiplicado por `1.21`.
2. Usa un bucle `for` junto con `zip()` para iterar e imprimir en cada línea: `"El <producto> cuesta $<precio_con_iva>"`.

```python
productos = ["Teclado", "Mouse", "Monitor"]
precios = [50, 20, 200]

# Tu solución aquí
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
productos = ["Teclado", "Mouse", "Monitor"]
precios = [50, 20, 200]

precios_con_iva = [p * 1.21 for p in precios]

for prod, precio_iva in zip(productos, precios_con_iva):
    print(f"El {prod} cuesta ${precio_iva:.2f}")
```

</details>

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos</i>
  </p>
</div>
