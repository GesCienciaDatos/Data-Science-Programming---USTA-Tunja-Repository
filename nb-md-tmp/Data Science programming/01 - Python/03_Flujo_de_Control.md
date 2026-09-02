# 03_Flujo_de_Control

<table style="width: 100%; border-collapse: collapse; border: none; background: #f8fafc; border-left: 6px solid #1e3a8a; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #0f172a; font-size: 2.1em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        Flujo de Control: Condicionales y Bucles en Python 🔀
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
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/01%20-%20Python/03_Flujo_de_Control.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

--- 
## Flujo de Control: Dirigiendo la Ejecución 

Por defecto, un script se ejecuta de forma estrictamente **secuencial** (de arriba hacia abajo, línea por línea). Sin embargo, el **flujo de control** es el mecanismo que rompe esta linealidad. Es lo que le otorga "inteligencia" al código, permitiéndole reaccionar a los datos para tomar decisiones, omitir instrucciones o repetir acciones de manera dinámica.

En programación, este control del flujo se gestiona principalmente a través de dos mecanismos:

*   **Estructuras Condicionales (Bifurcaciones):** Permiten que el programa evalúe el estado actual (condiciones booleanas) y elija entre diferentes caminos lógicos. Responden a la lógica de *"Si ocurre A, ejecuta X; de lo contrario, ejecuta Y"* (implementado en Python con `if`, `elif` y `else`).
*   **Estructuras Iterativas (Bucles o Ciclos):** Permiten automatizar la repetición de un bloque de código sin tener que reescribirlo. Esta repetición puede darse un número finito de veces sobre una colección de datos (ciclos `for`) o de forma indefinida mientras una condición siga siendo verdadera (ciclos `while`).

---
### 1. Condicionales (`if`, `elif`, `else`)

Los **condicionales** son estructuras de control de flujo que permiten ejecutar bloques de código específicos únicamente cuando se cumplen ciertas condiciones booleanas (`True` o `False`).

> 🤓 **Regla de Indentación:** Python no utiliza llaves `{}` para delimitar bloques de código. En su lugar, exige una **indentación fija de 4 espacios** debajo de la instrucción condicional.

---

**Desglose de Componentes**

* **Solo uso de `if` (Evaluación Base):** Se evalúa primero. Si la condición es `True`, el bloque indentado se ejecuta; si es `False`, el programa simplemente lo ignora y continúa.
* **Uso de `if` - `else` (Bifurcación Alternativa):** Define una ruta para cuando la condición no se cumple. Si la condición del `if` es `False`, se ejecuta de forma obligatoria el bloque `else`.
* **Uso de `elif` (Condiciones Múltiples):** Abreviatura de *Else If*. Permite encadenar y evaluar condiciones adicionales secuencialmente si la condición del `if` anterior (o del `elif` previo) resultó falsa.
* **Operador Ternario (Sintaxis Compacta):** Permite escribir una estructura condicional simple en una sola línea. Ideal para asignaciones rápidas de variables:
  $$\text{variable} = \text{Valor\_Si\_True } \mathbf{if} \text{ Condición } \mathbf{else} \text{ Valor\_Si\_False}$$

---

**Estructura y Sintaxis**

| Componente | Descripción | Sintaxis Básica |
| :--- | :--- | :--- |
| **`if`** | Condición inicial obligatoria. | `if condicion:` |
| **`if` + `else`** | Alternativa única cuando no se cumple el `if`. | `if condicion:` <br> `else:` |
| **`if` + `elif` + `else`** | Múltiples condiciones excluyentes encadenadas. | `if c1:` <br> `elif c2:` <br> `else:` |
| **Operador Ternario** | Expresión condicional evaluada en una sola línea. | `res = val1 if cond else val2` |

```python
puntuacion = 85

# 🤓 NOTA IMPORTANTE: Python usa indentación (4 espacios) para definir qué hay dentro del condicional.
print(f"Evaluando puntuación: {puntuacion}\n")

# --- 1. SOLO USO DE IF (Evaluación simple) ---
if puntuacion >= 70:
    print("Puntuación por encima del mínimo requerido.")
```

```python
# --- 2. USO DE IF - ELSE (Bifurcación) ---
if puntuacion >= 90:
    print("Nivel: Sobresaliente")
else:
    print("Nivel: Estándar")
```

```python
# --- 3. USO DE IF - ELIF - ELSE (Múltiples condiciones) ---
if puntuacion >= 90:
    print("Calificación: A")
elif puntuacion >= 80:
    print("Calificación: B")
elif puntuacion >= 70:
    print("Calificación: C")
else:
    print("Calificación: Reprobado")
```

```python
# --- 4. OPERADOR TERNARIO (Condicional en una sola línea) ---
# Estructura: [Resultado_Si_True] if [Condicion] else [Resultado_Si_False]
estado = "Aprobado" if puntuacion >= 70 else "Reprobado"
print("\nEstado usando operador ternario:", estado)
```

#### 🛠️ Práctica: Condicionales

**Ejercicio 1:**
Un modelo de Inteligencia Artificial entrenado en la USTA Tunja genera una métrica de precisión (*accuracy*) sobre un conjunto de datos de prueba:

1. Declara la variable `precision_modelo = 0.85` (equivalente al 85%).
2. **Evaluación simple (`if`):** Verifica si `precision_modelo >= 0.80` e imprime `"El modelo cumple el umbral mínimo"`.
3. **Evaluación binaria (`if` - `else`):** Evalúa si `precision_modelo >= 0.90` e imprime `"Pasa a despliegue"`; de lo contrario (`else`), imprime `"Requiere reentrenamiento"`.
4. **Evaluación múltiple (`if` - `elif` - `else`):**
   - Si `precision_modelo >= 0.90`: imprime `"Rendimiento: Excelente"`.
   - Si `precision_modelo >= 0.80`: imprime `"Rendimiento: Bueno"`.
   - Si `precision_modelo >= 0.70`: imprime `"Rendimiento: Aceptable"`.
   - Si no cumple ninguna: imprime `"Rendimiento: Insuficiente"`.
5. **Operador Ternario:** Crea la variable `decision_final` que guarde `"Aprobado"` si la precisión es mayor o igual a `0.85`, de lo contrario `"Rechazado"`, e imprímela.

```python
# Escribe tu código aquí
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
# Ejercicio 1
precision_modelo = 0.85

# Evaluación simple
if precision_modelo >= 0.80:
    print("El modelo cumple el umbral mínimo")

# Evaluación binaria
if precision_modelo >= 0.90:
    print("Pasa a despliegue")
else:
    print("Requiere reentrenamiento")
    
# Evaluación múltiple
if precision_modelo >= 0.90:
    print("Rendimiento: Excelente")
elif precision_modelo >= 0.80:
    print("Rendimiento: Bueno")
elif precision_modelo >= 0.70:
    print("Rendimiento: Aceptable")
else:
    print("Rendimiento: Insuficiente")

# Operador ternario
decision_final = "Aprobado" if precision_modelo >= 0.85 else "Rechazado"
print(f"Decisión final: {decision_final}")

```
</details>

**Ejercicio 2:**
Crea un pequeño script que clasifique un número entero (`numero = -5`).
1. Si el número es mayor que `0`, imprime `"Positivo"`.
2. Si es menor que `0`, imprime `"Negativo"`.
3. Si es exactamente `0`, imprime `"Cero"`.

```python
# Escribe tu código aquí
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
# Ejercicio 1
precision_modelo = 0.85

# Evaluación simple
if precision_modelo >= 0.80:
    print("El modelo cumple el umbral mínimo")

# Evaluación binaria
if precision_modelo >= 0.90:
    print("Pasa a despliegue")
else:
    print("Requiere reentrenamiento")
    
# Evaluación múltiple
if precision_modelo >= 0.90:
    print("Rendimiento: Excelente")
elif precision_modelo >= 0.80:
    print("Rendimiento: Bueno")
elif precision_modelo >= 0.70:
    print("Rendimiento: Aceptable")
else:
    print("Rendimiento: Insuficiente")

# Operador ternario
decision_final = "Aprobado" if precision_modelo >= 0.85 else "Rechazado"
print(f"Decisión final: {decision_final}")

# Ejercicio 2
numero = -5

if numero > 0:
    print("Positivo")
elif numero < 0:
    print("Negativo")
else:
    print("Cero")
```
</details>

---
### 2. Bucle `for` (Ciclo de iteración definida)

El bucle **`for`** es una estructura de control que permite iterar (recorrer) secuencialmente los elementos de cualquier estructura de datos iterable (como listas, tuplas, diccionarios o rangos numéricos).

**Características Principales**
* **Iteración Definida:** El número de repeticiones está determinado de antemano por la cantidad de elementos de la colección o por el rango especificado.
* **Función `range()`:** Genera una secuencia numérica con la sintaxis `range(inicio, fin, paso)`. El valor final **nunca** se incluye en la iteración.
* **Iteración en Diccionarios:** Por defecto itera sobre las *claves*. Para acceder simultáneamente a las claves y a los valores, se utiliza el método `.items()`.
* **Sentencias de Control:**
  * `continue`: Salta la ejecución del código restante en la iteración actual y avanza a la siguiente.
  * `break`: Interrumpe y finaliza el bucle por completo de manera inmediata.

---

**Resumen de Operaciones**

| Operación / Control | Sintaxis | Descripción | Ejemplo |
| :--- | :--- | :--- | :--- |
| **Iterar Lista** | `for x in lista:` | Recorre elemento por elemento la colección. | `for ciudad in ciudades:` |
| **Rango Numérico** | `range(inicio, fin, paso)` | Genera secuencias numéricas personalizadas. | `range(1, 10, 2)` |
| **Iterar Diccionario** | `for k, v in dict.items():` | Recorre simultáneamente parejas de clave y valor. | `for clave, valor in puntajes.items():` |
| **Saltar Iteración** | `continue` | Omite el resto de la iteración actual. | `if i == 3: continue` |
| **Romper Bucle** | `break` | Cancela la ejecución del ciclo inmediatamente. | `if i == 5: break` |

```python
# 1. Iterando sobre una lista
ciudades = ["Bogotá", "Medellín", "Cali"]
print("--- Iterando una lista ---")
for ciudad in ciudades:
    print("Procesando ciudad:", ciudad)
```

```python
# 2. Iterando usando range() 
# range(inicio, fin, paso) -> Genera números. El número 'fin' no se incluye.
print("\n--- Iterando con range(1, 10, 2) ---")
for numero in range(1, 10, 2):  # Del 1 al 9 saltando de 2 en 2
    print("Número:", numero)
```

```python
# 3. Iterando sobre un diccionario 🧗
print("\n--- Iterando un Diccionario ---")
puntajes = {"jugador1": 10, "jugador2": 20}

# Por defecto itera sobre las CLAVES
for clave in puntajes:
    print("Clave base:", clave)

# Iterando sobre pares clave-valor usando .items()
for clave, valor in puntajes.items():
    print(f"El {clave} tiene {valor} puntos.")
```

```python
# 4. Uso de break y continue 🤓
print("\n--- Control de bucle con break y continue ---")
for i in range(1, 6):
    if i == 3:
        print("Encontré un 3, me lo salto (continue)")
        continue # Salta a la siguiente iteración inmediatamente
    if i == 5:
        print("Encontré un 5, detengo el bucle por completo (break)")
        break # Rompe el ciclo por completo
    print("Ejecución normal, i =", i)
```

#### 🛠️ Práctica: Bucles For

**Ejercicio 1:**
El departamento de sistemas de la USTA Tunja requiere procesar el registro de notas e inventario de equipos mediante bucles:

1. Declara la lista `equipos = ["Servidor", "Router", "Switch", "Laptop"]` e itérala con un bucle `for` imprimiendo `"Procesando equipo: [nombre_equipo]"`.
2. Utiliza un bucle `for` con `range()` para generar e imprimir los números pares del `2` al `10` (inclusive).
3. Declara el diccionario `estudiantes = {"Ana": 4.5, "Pedro": 2.8, "Sofia": 3.9}` y recórrelo usando `.items()` para imprimir `"[Nombre] obtuvo una nota de [Nota]"`.
4. Utiliza un bucle `for` sobre la secuencia `range(1, 6)`:
   - Si el número es igual a `2`, muestra un mensaje indicando que se omite y usa `continue`.
   - Si el número es igual a `4`, muestra un mensaje de cancelación y detén el bucle con `break`.
   - En cualquier otro caso, imprime `"Iteración actual: [número]"`.

```python
# Escribe tu código aquí
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
# Ejercicio 1
# 1. Equipos
equipos = ["Servidor", "Router", "Switch", "Laptop"]
for equipo in equipos:
    print(f"Procesando equipo: {equipo}")

# 2. Números pares con range
print("\nNúmeros pares:")
for par in range(2, 11, 2):
    print(par)

# 3. Diccionario estudiantes
print("\nNotas:")
estudiantes = {"Ana": 4.5, "Pedro": 2.8, "Sofia": 3.9}
for nombre, nota in estudiantes.items():
    print(f"{nombre} obtuvo una nota de {nota}")

# 4. Control de flujo (continue, break)
print("\nControl de flujo:")
for num in range(1, 6):
    if num == 2:
        print("Omite el número 2")
        continue
    if num == 4:
        print("Cancelando bucle en el número 4")
        break
    print(f"Iteración actual: {num}")

```
</details>

**Ejercicio 2:**
Tienes una lista de calificaciones: `notas = [4.5, 3.2, 5.0, 2.8, 4.1]`.
1. Inicializa una variable `suma_notas = 0`.
2. Usa un bucle `for` para iterar sobre la lista y sumar cada nota a `suma_notas`.
3. Calcula e imprime el promedio final de la clase dividiendo la suma por la longitud de la lista.

```python
# Escribe tu código aquí
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python

# Ejercicio 2
notas = [4.5, 3.2, 5.0, 2.8, 4.1]
suma_notas = 0

for nota in notas:
    suma_notas += nota

promedio = suma_notas / len(notas)
print(f"\nEl promedio de la clase es: {promedio}")
```
</details>

---
### 3. Bucle `while` (Ciclo de iteración indefinida)

El bucle **`while`** ejecuta repetidamente un bloque de código **mientras** una condición booleana se mantenga como `True`. A diferencia del bucle `for`, se utiliza cuando no se conoce de antemano la cantidad exacta de iteraciones.

**Características Principales**
* **Iteración Indefinida:** Evalúa la condición antes de cada iteración. Si es `False` desde el inicio, el bloque de código nunca se ejecutará.
* **Modificación de Control:** Es imprescindible actualizar la variable de control dentro del cuerpo del bucle para evitar caer en un **bucle infinito**.
* **Cláusula `else`:** Opcional. Se ejecuta **únicamente** cuando la condición del `while` se vuelve `False` de forma natural (no se ejecutará si el bucle finaliza mediante una sentencia `break`).
* **Simulación de `do-while`:** Python **no incluye** la estructura `do-while`. Para simular este comportamiento y garantizar que el bloque se ejecute al menos una vez, se utiliza `while True:` en combinación con un `if ... break` al final del ciclo.

---

**Resumen de Estructuras**

| Estructura | Sintaxis | Descripción |
| :--- | :--- | :--- |
| **Bucle `while` básico** | `while condicion:` | Ejecuta el bloque mientras la condición sea verdadera. |
| **`while` con `else`** | `while cond: ... else:` | Ejecuta el bloque `else` solo cuando la condición pasa a ser `False`. |
| **Simulación `do-while`** | `while True: ... if cond: break` | Asegura al menos una ejecución previa antes de evaluar la salida. |

```python
# 1. BUCLE WHILE BÁSICO (Cuenta regresiva)
contador = 5

print("Iniciando cuenta regresiva...")
while contador > 0:
    print(contador)
    # Es VITAL modificar la variable de control, de lo contrario el bucle será infinito
    contador -= 1 

print("¡Despegue!")
```

```python
# 2. WHILE CON CLÁUSULA 'ELSE'
# Se ejecuta cuando la condición se vuelve False de forma natural
intentos = 0
while intentos < 3:
    intentos += 1
else:
    print("\nSe alcanzó el máximo de intentos permitidos.")
```

```python
# 3. SIMULACIÓN DE DO-WHILE EN PYTHON
# Garantiza que el código se ejecute AL MENOS UNA VEZ
print("\n--- Simulación Do-While ---")
paso = 1
while True:
    print(f"Ejecutando paso {paso} (se ejecuta antes de evaluar)")
    paso += 1
    if paso > 3:  # Condición de salida evaluada al final
        break
```

#### 🛠️ Práctica: Bucles While

**Ejercicio 1:**
El centro de monitoreo de la USTA Tunja requiere controlar la temperatura de un servidor mediante ciclos dinámicos:

1. Declara la variable `temperatura = 40`.
2. Crea un bucle `while` que se ejecute mientras `temperatura > 30`, imprimiendo `"Enfriando... Temperatura actual: [temperatura]°C"` y reduciendo la temperatura en `3` en cada iteración.
3. Agrega una cláusula `else` al bucle `while` que imprima `"Sistema estabilizado a temperatura segura"`.
4. Simula la estructura de un **`do-while`** usando `while True:` para realizar lecturas de control:
   - Declara `lecturas = 0`.
   - Dentro del bucle, incrementa `lecturas` en `1` e imprime `"Realizando lectura técnica #[lecturas]"`.
   - Agrega la condición de salida al final del bucle: si `lecturas >= 3`, interrumpe el ciclo usando `break`.

```python
# Escribe tu código aquí
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
# Ejercicio 1
temperatura = 40

while temperatura > 30:
    print(f"Enfriando... Temperatura actual: {temperatura}°C")
    temperatura -= 3
else:
    print("Sistema estabilizado a temperatura segura\n")

# Do-While simulado
lecturas = 0
while True:
    lecturas += 1
    print(f"Realizando lectura técnica #{lecturas}")
    if lecturas >= 3:
        break

```
</details>

**Ejercicio 2:**
Crea un sistema simple de ahorro.
1. Define `meta_ahorro = 100` y `ahorro_actual = 0`.
2. Usa un bucle `while` que se ejecute mientras `ahorro_actual < meta_ahorro`.
3. En cada iteración, suma `25` al `ahorro_actual` e imprime el saldo.
4. Cuando alcance la meta, el bucle terminará; usa la cláusula `else` del `while` para imprimir `"¡Meta alcanzada!"`.

```python
# Escribe tu código aquí
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python


# Ejercicio 2
print("\nIniciando sistema de ahorro:")
meta_ahorro = 100
ahorro_actual = 0

while ahorro_actual < meta_ahorro:
    ahorro_actual += 25
    print(f"Ahorrado: {ahorro_actual}")
else:
    print("¡Meta alcanzada!")
```
</details>

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos</i>
  </p>
</div>
