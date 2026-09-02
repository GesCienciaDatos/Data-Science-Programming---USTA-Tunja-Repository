# 04_Funciones

<table style="width: 100%; border-collapse: collapse; border: none; background: #f8fafc; border-left: 6px solid #1e3a8a; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #0f172a; font-size: 2.1em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        Funciones y Modularización en Python ⚙️
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
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/01%20-%20Python/04_Funciones.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## Funciones: Definición, Parámetros y Retorno 

**¿Qué son las Funciones?**
Las funciones son bloques de código reutilizables diseñados para realizar una tarea específica, permitiendo organizar y evitar la repetición de instrucciones en el desarrollo.

Una función se define con la palabra reservada `def`. Puede recibir parámetros (inputs) en su declaración y devolver resultados (outputs) a quien la invoca mediante la sentencia `return`.
Si no se especifica `return`, la función devuelve implícitamente `None`.

### 1. Características de una Función Básica
1. **Definición:** Uso de `def nombre_funcion():`.
2. **Argumentos:** Variables pasadas a la función entre paréntesis.
3. **Llamada:** Ejecución de la función usando su nombre seguido de paréntesis `nombre_funcion()`.

```python
# 1. Definición básica de una función sin parámetros
def mi_funcion():
    print("¡Hola desde mi función!")

# Llamada a la función
mi_funcion()
```

```python
# 2. Función con parámetros (argumentos)
def mi_funcion_con_argumentos(usuario, saludo):
    print(f"Hola, {usuario}. ¡{saludo}!")

# Llamada a la función pasándole valores
mi_funcion_con_argumentos("Santiago", "Bienvenido al curso")
```

```python
# 3. Función que retorna un valor
def sumar_dos_numeros(a, b):
    return a + b

# Guardamos el resultado de la función en una variable
resultado = sumar_dos_numeros(10, 5)
print("El resultado de la suma es:", resultado)
```

```python
# 4. Parámetros opcionales (valores por defecto)
# Un parámetro es opcional si se le asigna un valor por defecto en la definición
def presentar_estudiante(nombre, universidad="USTA Tunja"):
    print(f"Estudiante: {nombre}, Universidad: {universidad}")

presentar_estudiante("Carlos") # Usa el valor por defecto
presentar_estudiante("Laura", "Nacional") # Sobreescribe el valor por defecto
```

#### 🛠️ Práctica: Funciones Básicas

**Ejercicio 1:**
Crea una función llamada `calcular_area_rectangulo` que reciba dos parámetros: `base` y `altura`. La función debe calcular el área (`base * altura`) y **retornar** el resultado. Luego, llámala pasándole los valores `10` y `5` e imprime el resultado.

```python
# Escribe tu código aquí
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
# Ejercicio 1
def calcular_area_rectangulo(base, altura):
    return base * altura

area = calcular_area_rectangulo(10, 5)
print("El área del rectángulo es:", area)

print("\n" + "-"*30 + "\n")

```
</details>

**Ejercicio 2:**
En este ejercicio crearás un pequeño programa funcional usando funciones encadenadas.

1. Agrega una función llamada `listar_beneficios()` que no reciba argumentos y retorne la siguiente lista de strings: 
   `["Código más organizado", "Código más legible", "Mayor facilidad para reutilizar código", "Permite compartir y conectar código"]`.
2. Agrega una función llamada `construir_oracion(beneficio)` que reciba un solo argumento de tipo string y retorne una oración que comience con el string dado y termine con `" es un beneficio de las funciones!"`.
3. Crea una función principal `nombrar_los_beneficios()` que obtenga la lista usando `listar_beneficios()`, itere sobre ella y por cada beneficio imprima el resultado de `construir_oracion(beneficio)`.
4. ¡Ejecuta `nombrar_los_beneficios()` para ver la magia!

```python
# Escribe tu código aquí
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python

# Ejercicio 2
def listar_beneficios():
    return [
        "Código más organizado", 
        "Código más legible", 
        "Mayor facilidad para reutilizar código", 
        "Permite compartir y conectar código"
    ]

def construir_oracion(beneficio):
    return f"{beneficio} es un beneficio de las funciones!"

def nombrar_los_beneficios():
    lista_de_beneficios = listar_beneficios()
    for beneficio in lista_de_beneficios:
        print(construir_oracion(beneficio))

# Ejecución
nombrar_los_beneficios()
```
</details>

--- 
### 2. Argumentos y Retorno Múltiple 🛠️

Python permite definir valores por defecto para los argumentos, pasar argumentos por su nombre (keywords) y devolver múltiples valores simultáneamente (en forma de tupla).

```python
# Argumentos por defecto
def crear_perfil(nombre, rol="Usuario"):
    print(f"Perfil creado: {nombre}, Rol: {rol}")

crear_perfil("Ana")                # Usa el valor por defecto
crear_perfil("Luis", "Admin")      # Sobreescribe el valor por defecto

# Argumentos nombrados (Keyword Arguments)
crear_perfil(rol="Invitado", nombre="Maria") # El orden no importa si se nombran
```

```python
# Retorno Múltiple (Retorna una tupla implícitamente)
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    return suma, resta # Retorna múltiples valores

# Desempaquetado (Unpacking) del resultado
resultado_suma, resultado_resta = operaciones_basicas(10, 4)
print(f"Suma: {resultado_suma}, Resta: {resultado_resta}")
```

#### 🛠️ Práctica: Retorno Múltiple

**Problema:**
Crea una función llamada `analizar_numeros` que reciba una lista de números. La función debe retornar dos cosas: el número máximo y el número mínimo de esa lista (puedes usar las funciones integradas `max()` y `min()`). Luego, llama a la función con `[15, 2, 8, 99, -5]` y desempaqueta los resultados en dos variables para imprimirlas.

```python
numeros = [15, 2, 8, 99, -5]

# Tu solución aquí
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
def analizar_numeros(lista):
    return max(lista), min(lista)

numeros = [15, 2, 8, 99, -5]
maximo, minimo = analizar_numeros(numeros)

print(f"El máximo es {maximo} y el mínimo es {minimo}")
```

</details>

--- 
### 3. *args y **kwargs 🧠

A veces no sabemos cuántos argumentos recibirá nuestra función. `*args` permite recibir un número indefinido de **argumentos posicionales** (como una tupla), y `**kwargs` un número indefinido de **argumentos nombrados** (como un diccionario).

```python
# *args (Argumentos Posicionales Múltiples)
def sumar_todos(*args):
    print("args es de tipo:", type(args)) # Es una tupla
    total = sum(args)
    return total

print("Suma de 3 números:", sumar_todos(1, 2, 3))
print("Suma de 6 números:", sumar_todos(10, 20, 30, 40, 50, 60))
```

```python
# **kwargs (Keyword Arguments Múltiples)
def mostrar_informacion(**kwargs):
    print("kwargs es de tipo:", type(kwargs)) # Es un diccionario
    for clave, valor in kwargs.items():
        print(f"{clave.capitalize()}: {valor}")

mostrar_informacion(nombre="Pedro", edad=25, pais="México", activo=True)
```

#### 🛠️ Práctica: Argumentos variables

**Problema:**
Crea una función `crear_ticket_compra` que reciba un argumento requerido llamado `cliente`, seguido de cualquier cantidad de argumentos nombrados (`**kwargs`) que representen los productos comprados y su precio.
La función debe imprimir el nombre del cliente, luego iterar sobre los productos mostrando "Producto: Precio" y finalmente imprimir el total gastado.

```python
# Tu solución aquí
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
def crear_ticket_compra(cliente, **productos):
    print(f"--- Ticket de {cliente} ---")
    total = 0
    for producto, precio in productos.items():
        print(f"{producto}: ${precio}")
        total += precio
    print(f"Total a pagar: ${total}")

crear_ticket_compra("Ana Lopez", zapatos=50.5, camisa=20.0, pantalon=35.0)
```

</details>

--- 
### 4. Funciones Lambda y Orden Superior 💎

Las funciones **lambda** son funciones anónimas de una sola línea. Son muy útiles combinadas con funciones de orden superior (funciones que reciben otras funciones como argumento) como `map()` o `filter()`.

```python
# Función Lambda equivalente a def elevar_cuadrado(x): return x**2
elevar_cuadrado = lambda x: x**2
print("Cuadrado de 5:", elevar_cuadrado(5))

numeros = [1, 2, 3, 4, 5, 6]

# Uso de map() con lambda (Aplica la función a cada elemento)
# Nota: map devuelve un iterador, lo convertimos a lista para verlo.
cuadrados = list(map(lambda x: x**2, numeros))
print("Map (Cuadrados):", cuadrados)

# Uso de filter() con lambda (Filtra elementos donde la función da True)
pares = list(filter(lambda x: x % 2 == 0, numeros))
print("Filter (Pares):", pares)
```

#### 🛠️ Práctica: Funciones Lambda

**Problema:**
Dada una lista de temperaturas en grados Celsius `celsius = [0, 10, 20, 30, 40]`, usa la función `map()` junto con una función `lambda` para convertir todas las temperaturas a Fahrenheit y guárdalas en una lista llamada `fahrenheit`.
*(Fórmula: F = (C * 9/5) + 32)*

```python
celsius = [0, 10, 20, 30, 40]

# Tu solución aquí
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
celsius = [0, 10, 20, 30, 40]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
print("Temperaturas en Fahrenheit:", fahrenheit)
```

</details>

--- 
### 5. Scope y Decoradores 🏆

El nivel más alto de dominio implica entender el **Scope** (ámbito global vs local) y cómo modificar el comportamiento de funciones de forma dinámica creando **Decoradores**.

```python
# Scope (Ámbito)
variable_global = "Soy global"

def prueba_scope():
    # variable_global = "Intento modificarla" # Esto crearía una variable LOCAL nueva
    global variable_global # Así le decimos a Python que queremos la global
    variable_global = "Fui modificada dentro de la función"
    variable_local = "Soy local"
    print("Local: ", variable_local)

prueba_scope()
print("Global después: ", variable_global) # Cambio persistió
```

```python
# Decoradores
# Un decorador es una función que recibe una función, le añade comportamiento y la devuelve.

def mi_decorador(funcion_original):
    def funcion_envoltura(*args, **kwargs):
        print("--- Antes de ejecutar la función ---")
        resultado = funcion_original(*args, **kwargs)
        print("--- Después de ejecutar la función ---")
        return resultado
    return funcion_envoltura

# Usamos la sintaxis @ para "decorar" nuestra función
@mi_decorador
def decir_hola(nombre):
    print(f"¡Hola {nombre}!")

decir_hola("Mundo")
```

#### 🛠️ Práctica: Decoradores

**Problema:**
Crea un decorador llamado `@medir_tiempo` (nota: para esto deberás importar la librería estándar `time` solo para usar `time.time()`).
El decorador debe:
1. Tomar el tiempo justo antes de ejecutar la función original (`inicio = time.time()`).
2. Ejecutar la función original.
3. Tomar el tiempo justo después (`fin = time.time()`).
4. Imprimir `"La función tardó X segundos"` (donde X es `fin - inicio`).
Luego, decora una función simulada que incluya un `time.sleep(1)` para probarlo.

```python
import time

# Tu solución aquí
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
import time

def medir_tiempo(funcion_original):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = funcion_original(*args, **kwargs)
        fin = time.time()
        print(f"[Tiempo] La función tardó {fin - inicio:.4f} segundos")
        return resultado
    return wrapper

@medir_tiempo
def proceso_lento():
    print("Iniciando proceso...")
    time.sleep(1.5) # Simula un proceso que tarda 1.5 seg
    print("Proceso terminado.")

proceso_lento()
```

</details>

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos</i>
  </p>
</div>
