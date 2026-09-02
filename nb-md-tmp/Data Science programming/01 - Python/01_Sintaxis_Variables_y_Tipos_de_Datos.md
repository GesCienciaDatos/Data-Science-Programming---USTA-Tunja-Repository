# 01_Sintaxis_Variables_y_Tipos_de_Datos

<table style="width: 100%; border-collapse: collapse; border: none; background: #f8fafc; border-left: 6px solid #1e3a8a; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #0f172a; font-size: 2.1em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        Sintaxis, Variables y Tipos de Datos en Python 🔢
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
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/01%20-%20Python/01_Sintaxis_Variables_y_Tipos_de_Datos.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## Tipos de Datos y Sintaxis Básica 🧱

En este cuaderno aprenderás a declarar variables, realizar operaciones numéricas, manipular valores lógicos y trabajar con cadenas de texto:

* **1. Números:** Enteros (`int`), flotantes (`float`), type casting y operadores aritméticos.
* **2. Booleanos:** Operadores relacionales de comparación, conectores lógicos (`and`, `or`, `not`) y evaluación de cortocircuito.
* **3. Cadenas de Texto:** Inmutabilidad, indexación, *slicing*, métodos de limpieza y formateo avanzado con `f-strings`.

> 💡 **Buenas Prácticas PEP 8:** En Python, los nombres de variables deben seguir la convención **`snake_case`** (minúsculas unidas por guiones bajos: `salario_promedio`, `total_ventas`). Los nombres deben ser descriptivos y evitar caracteres especiales o abreviaciones confusas.

---
### 1. Números: Enteros (`int`) y Flotantes (`float`)

Python gestiona automáticamente la precisión numérica:
* **`int`:** Números enteros con precisión ilimitada (la memoria se expande según el tamaño del número).
* **`float`:** Números reales con decimales implementados bajo el estándar internacional IEEE 754 de 64 bits de doble precisión.

| Operador | Nombre | Ejemplo | Resultado |
|:---:|---|:---:|:---:|
| `+` | Suma | `15 + 4` | `19` |
| `-` | Resta | `15 - 4` | `11` |
| `*` | Multiplicación | `15 * 4` | `60` |
| `/` | División Real (siempre devuelve `float`) | `15 / 4` | `3.75` |
| `//` | División Entera (cociente) | `15 // 4` | `3` |
| `%` | Módulo (residuo) | `15 % 4` | `3` |
| `**` | Potencia / Exponente | `2 ** 4` | `16` |

> 📌 **Nota sobre Type Casting:** Las funciones `int()`, `float()` y `str()` permiten transformar explícitamente valores entre diferentes tipos de datos compatibles.

```python
# --- DECLARACIÓN DE VARIABLES NUMÉRICAS ---
entero = 150
flotante = 3.14159

# En Python, puedes usar guiones bajos para leer mejor números grandes (no afecta el valor)
millon = 1_000_000 

print("Valor del entero:", entero, "| Tipo:", type(entero))
print("Valor del flotante:", flotante, "| Tipo:", type(flotante))
print("Un millón numérico:", millon)
```

```python
# --- CONVERSIÓN (CASTING) 🧗 ---
# Podemos convertir de entero a flotante y viceversa
entero_a_float = float(entero)
float_a_entero = int(flotante) # Trunca (corta) los decimales, NO redondea

print("\nEntero convertido a float:", entero_a_float)
print("Float truncado a entero:", float_a_entero)
```

```python
# --- OPERACIONES MATEMÁTICAS FUNDAMENTALES ---
a = 15
b = 4

print("\n--- Operaciones con", a, "y", b, "---")
print("Suma (a + b):", a + b)
print("Resta (a - b):", a - b)
print("Multiplicación (a * b):", a * b)
print("División estándar (a / b):", a / b)  # Siempre retorna un float (3.75)
print("División entera (a // b):", a // b)  # Retorna el cociente entero (3)
print("Módulo / Residuo (a % b):", a % b)   # Lo que sobra de la división entera (3)
print("Potencia (a ** b):", a ** b)         # 15 elevado a la 4
```

```python
# --- OPERACIONES MATEMÁTICAS FUNDAMENTALES ---
a = 15
b = 4

print("\n--- Operaciones con", a, "y", b, "---")
print("Suma (a + b):", a + b)
print("Resta (a - b):", a - b)
print("Multiplicación (a * b):", a * b)
print("División estándar (a / b):", a / b)  # Siempre retorna un float (3.75)
print("División entera (a // b):", a // b)  # Retorna el cociente entero (3)
print("Módulo / Residuo (a % b):", a % b)   # Lo que sobra de la división entera (3)
print("Potencia (a ** b):", a ** b)         # 15 elevado a la 4

# --- FUNCIONES INTEGRADAS PARA NÚMEROS ---
print("\n--- Funciones Integradas (Built-in) ---")
print("Valor absoluto de -10:", abs(-10))   
print("Redondeo de 3.567 a 2 decimales:", round(3.567, 2))
print("Máximo entre 10, 50 y 30:", max(10, 50, 30))
print("Mínimo entre 10, 50 y 30:", min(10, 50, 30))
```

#### 🛠️ Práctica: Números

**Ejercicio 1:**
Dado un presupuesto de **1_500_000 COP** para la compra de sensores de monitoreo en un laboratorio:

1. Declara la variable `presupuesto = 1_500_000` (tipo `int`) y `precio_sensor = 320500.75` (tipo `float`).
2. Convierte `precio_sensor` a número entero usando `int()` para truncar los decimales.
3. Calcula cuántos sensores completos se pueden comprar usando la **división entera (`//`)** y obtén el dinero sobrante mediante el **módulo (`%`)**.
4. Usa la función `round()` para calcular el valor del sensor redondeado a 1 decimal.
5. Imprime en pantalla los resultados indicando: precio redondeado, cantidad de sensores a comprar y dinero sobrante.

```python
#Ejercicio 1
# Escribe tu código aquí
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
# Ejercicio 1
presupuesto = 1_500_000
precio_sensor = 320500.75

precio_entero = int(precio_sensor)
cantidad_sensores = presupuesto // precio_entero
sobrante = presupuesto % precio_entero
precio_redondeado = round(precio_sensor, 1)

print(f"Precio redondeado: {precio_redondeado}")
print(f"Se pueden comprar {cantidad_sensores} sensores y sobran {sobrante} COP")

print(f"El IMC del paciente es: {imc}")
```
</details>

**Ejercicio 2:**
Calcula el Índice de Masa Corporal (IMC) de un paciente. 
1. Declara la variable `peso_kg = 75.5` y `altura_m = 1.75`. 
2. Utiliza el operador de potencia (`**`) para calcular el IMC ($IMC = \frac{peso}{altura^2}$) y redondéalo a 2 decimales usando `round()`.
3. Imprime el resultado.

```python
# Escribe tu código aquí
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python

# Ejercicio 2
peso_kg = 75.5
altura_m = 1.75
imc = round(peso_kg / (altura_m ** 2), 2)

print(f"El IMC del paciente es: {imc}")
```
</details>

---
### 2. Booleanos (`bool`) y Operadores Lógicos

Representan dos estados lógicos: `True` (Verdadero) y `False` (Falso). Son la base de la toma de decisiones y el control de flujo en la programación.

**Operadores de Comparación**

Comparan dos valores y retornan un resultado booleano (`True` o `False`).

| Operador | Significado | Ejemplo | Resultado |
| :---: | :--- | :--- | :--- |
| `==` | Igual a | `10 == 20` | `False` |
| `!=` | Diferente de | `10 != 20` | `True` |
| `>` | Mayor que | `10 > 20` | `False` |
| `<` | Menor que | `10 < 20` | `True` |
| `>=` | Mayor o igual que | `10 >= 10` | `True` |
| `<=` | Menor o igual que | `10 <= 20` | `True` |

> **Atención con la sintaxis:** No confundas el operador de asignación (`=`) con el operador de igualdad (`==`). El primero asigna un valor a una variable; el segundo compara si dos valores son iguales.

**Operadores Lógicos**

Permiten combinar múltiples expresiones booleanas para evaluar condiciones compuestas:

* **`and` (Y lógico):** Retorna `True` únicamente si **todas** las condiciones son verdaderas.
* **`or` (O lógico):** Retorna `True` si **al menos una** de las condiciones es verdadera.
* **`not` (Negación):** Invierte el valor lógico (transforma `True` en `False` y viceversa).

```python
# Declaración (Siempre con primera letra en mayúscula)
es_verdadero = True
es_falso = False
print("Tipo de es_verdadero:", type(es_verdadero))
```

```python
# --- OPERADORES DE COMPARACIÓN (Retornan booleanos) ---
x = 10
y = 20
print("\n--- Comparaciones ---")
print(f"¿{x} es igual a {y}? (x == y):", x == y)
print(f"¿{x} es diferente de {y}? (x != y):", x != y)
print(f"¿{x} es mayor que {y}? (x > y):", x > y)
print(f"¿{x} es menor o igual que {y}? (x <= y):", x <= y)
```

```python
# --- OPERADORES LÓGICOS (and, or, not) ---
# Permiten combinar múltiples expresiones booleanas
print("\n--- Lógica Compuesta ---")
print("True and False:", True and False) # Ambas deben ser True para retornar True
print("True or False:", True or False)   # Al menos una debe ser True para retornar True
print("not True:", not True)             # Invierte el valor (Negación)
```

```python
# Ejemplo real:
edad = 25
tiene_licencia = True
puede_conducir = (edad >= 18) and tiene_licencia
print("\n¿Puede conducir?:", puede_conducir)
```

#### 🛠️ Práctica: Booleanos y Lógica

**Ejercicio 1:**
Para autorizar la entrada de un estudiante al Laboratorio de Ciencia de Datos de la USTA Tunja, se evalúan las siguientes condiciones de acceso:

1. Declara las variables: `edad = 20` (tipo `int`), `es_matriculado = True` (tipo `bool`) y `sanciones_activas = False` (tipo `bool`).
2. Comprueba si la edad es mayor o igual a 18 mediante un operador de comparación (`>=`).
3. Evalúa si el estudiante **no** tiene sanciones utilizando el operador lógico `not`.
4. Determina la autorización en la variable `acceso_permitido` combinando las condiciones: la edad debe ser mayor o igual a 18 **`and`** estar matriculado **`and`** **`not`** tener sanciones activas.
5. Imprime en pantalla el tipo de dato de `es_matriculado` y el resultado final del permiso de acceso (`acceso_permitido`).

```python
#Ejercicio 1
# Escribe tu código aquí
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
# Ejercicio 1
edad = 20
es_matriculado = True
sanciones_activas = False

acceso_permitido = (edad >= 18) and es_matriculado and (not sanciones_activas)

print("Tipo de es_matriculado:", type(es_matriculado))
print("¿Acceso permitido?:", acceso_permitido)

```
</details>

**Ejercicio 2:**
Una plataforma de cursos online otorga un certificado si el estudiante cumple al menos UNA de dos condiciones: 1) Tiene un promedio (`promedio`) mayor o igual a `4.0`, O (`or`) 2) Ha completado el proyecto final (`proyecto_completado = True`). 
Escribe el código para evaluar si un estudiante con `promedio = 3.5` y `proyecto_completado = True` recibe el certificado (`recibe_certificado`) e imprímelo.

```python
#Ejercicio 2
#  Escribe tu código aquí
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python

# Ejercicio 2
promedio = 3.5
proyecto_completado = True

recibe_certificado = (promedio >= 4.0) or proyecto_completado
print("¿Recibe certificado?:", recibe_certificado)
```
</details>

---
### 3. Cadenas de Texto (`str`) y sus Métodos

Las cadenas de texto (**`str`**) representan secuencias de caracteres. En Ciencia de Datos, la limpieza y manipulación de datos textuales (Data Cleaning) es una de las tareas más comunes e importantes.

**Declaración, Concatenación y Repetición**

Se pueden definir con comillas simples (`'...'`), dobles (`"..."`) o triples (`"""..."""`) para textos multilínea.
* **Concatenación (`+`):** Une dos o más cadenas de texto.
* **Repetición (`*`):** Duplica un texto el número de veces especificado.

**Indexación y Segmentación (Slicing)**

En Python, el primer carácter tiene el índice `0` y los índices negativos cuentan desde el final (`-1` es el último carácter). La estructura general del *slicing* es: `[inicio : fin : paso]` (donde el índice `fin` **no** se incluye).

| Operación | Sintaxis | Descripción |
| :--- | :---: | :--- |
| **Primer carácter** | `texto[0]` | Accede al elemento inicial. |
| **Último carácter** | `texto[-1]` | Accede al elemento final. |
| **Rango / Rbanzo** | `texto[0:3]` | Extrae desde el índice `0` hasta el `2`. |
| **Inversión** | `texto[::-1]` | Invierte la cadena por completo. |

**Métodos Frecuentes para Manipulación de Texto**

| Método | Descripción | Ejemplo (`"  Hola  "`) | Resultado |
| :--- | :--- | :--- | :--- |
| `.strip()` | Elimina espacios en blanco al inicio y final | `"  Hola  ".strip()` | `"Hola"` |
| `.lower()` | Convierte todo a minúsculas | `"Hola".lower()` | `"hola"` |
| `.upper()` | Convierte todo a mayúsculas | `"Hola".upper()` | `"HOLA"` |
| `.title()` | Primera letra de cada palabra en mayúscula | `"usta tunja".title()` | `"Usta Tunja"` |
| `.replace(a, b)` | Reemplaza la subcadena `a` por `b` | `"Datos".replace("a", "o")` | `"Dotos"` |
| `.split(sep)` | Divide el texto en una lista según el separador | `"a,b,c".split(",")` | `['a', 'b', 'c']` |
| `.join(lista)` | Une una lista de cadenas con un conector | `" \| ".join(['a', 'b'])` | `"a \| b"` |

**Formateo con f-strings**

Permiten inyectar variables e impresiones con formato (por ejemplo, limitar decimales) directamente en una cadena usando la sintaxis `f"{variable:.2f}"`.

```python
# --- DECLARACIÓN ---
texto_simple = 'Uso comillas simples'
texto_doble = "Uso comillas dobles"
texto_multilinea = """
    Con tres comillas, puedo 
    escribir textos que ocupen 
    múltiples líneas.
"""
```

```python
# --- OPERACIONES CON STRINGS ---
saludo = "Hola"
nombre = "Mundo"

print("--- Concatenación y Repetición ---")
print("Concatenación (+):", saludo + " " + nombre)
print("Repetición (*):", saludo * 3)

# 🤓 INDEXACIÓN Y SLICING (Corte)
# En Python, el primer carácter tiene índice 0.
# Los índices negativos empiezan desde el final (-1 es el último carácter).
palabra = "Python"
print("\n--- Indexación y Slicing de la palabra 'Python' ---")
print("Primer carácter (palabra[0]):", palabra[0])
print("Último carácter (palabra[-1]):", palabra[-1])

# 🧗 Slicing sigue la estructura: [inicio : fin : paso]
# NOTA: El índice 'fin' NO se incluye en el resultado.
print("Primeras 3 letras (palabra[0:3]):", palabra[0:3])
print("Desde el índice 2 hasta el final (palabra[2:]):", palabra[2:])
print("Toda la palabra, pero saltando de 2 en 2 (palabra[::2]):", palabra[::2])
print("Palabra invertida (palabra[::-1]):", palabra[::-1])
```

```python
# --- MÉTODOS DE STRINGS ---
print("\n--- Métodos para manipulación de Strings ---")
texto_sucio = "   PYTHON para Datos   "

# Limpieza
print(f"Original: '{texto_sucio}'")
print(f"strip() - Quita espacios a los extremos: '{texto_sucio.strip()}'")

# Mayúsculas / Minúsculas
texto_limpio = texto_sucio.strip()
print("lower() - Todo a minúsculas:", texto_limpio.lower())
print("upper() - Todo a mayúsculas:", texto_limpio.upper())
print("title() - Primera letra de cada palabra en mayúscula:", texto_limpio.title())

# Búsqueda y Reemplazo
print("replace() - Cambiar 'Datos' por 'Data Science':", texto_limpio.replace("Datos", "Data Science"))
print("count() - ¿Cuántas letras 'O' hay?:", texto_limpio.count("O"))
print("find() - Índice donde empieza la palabra 'para':", texto_limpio.find("para"))

# 🧗 Separación y Unión (esenciales para procesar archivos como CSV)
csv_ejemplo = "nombre,edad,ciudad"
lista_columnas = csv_ejemplo.split(",")  # Divide la cadena en una lista, usando la coma como separador
print("\nsplit() - Texto a Lista:", lista_columnas)

texto_unido = " | ".join(lista_columnas) # Une los elementos de una lista usando ' | ' como conector
print("join() - Lista a Texto:", texto_unido)
```

```python
# --- FORMATEO (f-strings) ---
usuario = "Ana"
score = 98.765
# Podemos inyectar variables directamente e incluso darles formato (ej: 2 decimales)
print(f"\nF-string: La usuaria {usuario} obtuvo un score de {score:.2f} puntos.")
```

#### 🛠️ Práctica: Cadenas de Texto

**Ejercicio 1:**
Un dataset importado de la USTA Tunja contiene un registro de texto con errores de formato y espacios innecesarios:
`registro_raw = "   codigo:2026_01, materia:PROGRAMACION DE DATOS - usta tunja   "`

1. Limpia los espacios en los extremos del texto utilizando `.strip()`.
2. Convierte todo el texto resultante a formato título mediante `.title()`.
3. Reemplaza la palabra `"Datos"` por `"Ciencia De Datos"` usando `.replace()`.
4. Divide la cadena en una lista de dos elementos (código y materia) con `.split(",")`.
5. Imprime en pantalla el código y la materia por separado utilizando un **f-string**.

```python
# Escribe tu código aquí
```

```python
# Escribe tu código aquí
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
# Ejercicio 1
registro_raw = "   codigo:2026_01, materia:PROGRAMACION DE DATOS - usta tunja   "

limpio = registro_raw.strip()
titulo = limpio.title()
reemplazado = titulo.replace("Datos", "Ciencia De Datos")
lista_datos = reemplazado.split(",")

codigo = lista_datos[0]
materia = lista_datos[1]

print(f"El código es: {codigo}")
print(f"La materia es: {materia}")

```
</details>

**Ejercicio 2:**
Se tiene el siguiente código de producto: `codigo_producto = "PROD-2024-X"`.
Usando *Slicing* e Indexación:
1. Extrae los primeros 4 caracteres para obtener el prefijo (`"PROD"`).
2. Extrae el año (caracteres desde el índice 5 hasta el 9 sin incluirlo, es decir `"2024"`).
3. Extrae la categoría (la última letra `"X"`) utilizando un índice negativo.

```python
# Escribe tu código aquí
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
# Ejercicio 2
codigo_producto = "PROD-2024-X"

prefijo = codigo_producto[0:4]
anio = codigo_producto[5:9]
categoria = codigo_producto[-1]

print(f"Prefijo: {prefijo} | Año: {anio} | Categoría: {categoria}")
```
</details>

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos</i>
  </p>
</div>
