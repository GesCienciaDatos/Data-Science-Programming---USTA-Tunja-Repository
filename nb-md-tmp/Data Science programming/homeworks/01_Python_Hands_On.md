# 01_Python_Hands_On

<table style="width: 100%; border-collapse: collapse; border: none; background: #f8fafc; border-left: 6px solid #1e3a8a; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #0f172a; font-size: 2.1em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        Ejercicios Prácticos de Python
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
        Taller Práctico • Módulo 01
      </span><br>
      <span style="color: #64748b; font-size: 0.85em;">Docente: Santiago A. Zúñiga M.</span><br>
      <a href="mailto:gestorvirtualcienciadatos@ustatunja.edu.co" style="color: #2563eb; font-size: 0.8em; text-decoration: none; font-weight: 500;">gestorvirtualcienciadatos@ustatunja.edu.co</a>
    </td>
  </tr>
</table>

<div align="center" style="margin-top: 15px; margin-bottom: 15px;">
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/homeworks/01_Python_Hands_On.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

```python
# Ejecuta este código para hacer que Jupyter imprima cada 
# declaración imprimible y no solo la última 
from IPython.core.interactiveshell import InteractiveShell 
InteractiveShell.ast_node_interactivity = "all"
```

**1. Escribe un programa en Python que acepte el radio de un círculo proporcionado por el usuario y calcule su área**

*Nota 1*: usa la función `input()` para obtener datos del usuario.

*Nota 2*: el área de un círculo es $\pi * r^2$.

```python
### TU CÓDIGO AQUÍ ###
```

**2. Genera una lista y una tupla a partir de números separados por comas**

*Nota 1*: la función `input()` retorna una cadena de texto (string).

*Nota 2*: busca en la documentación oficial de Python la función `split()` ([enlace](https://docs.python.org/3.10/library/stdtypes.html#str.split)).

```python
### TU CÓDIGO AQUÍ ###
```

**3. Escribe un programa en Python para mostrar el horario de exámenes (extrae la fecha de `exam_st_date`)**

Para formatear cadenas de texto:
A la izquierda del operador `%`, proporciona una cadena de formato que contenga uno o más objetivos de conversión, cada uno de los cuales comienza con un `%` (ej., `%d`).
A la derecha del operador `%`, proporciona el objeto (u objetos, dentro de una tupla) que deseas que Python inserte en la cadena de formato en lugar de los objetivos de conversión.

Algunos códigos comunes de formato de texto:
- `%s` - cadena de texto (string)
- `%d` - decimal
- `%i` - entero (integer)
- `%f` - decimal de punto flotante (floating-point)

Por ejemplo, en el siguiente caso, el entero 1 reemplaza a `%d` y la cadena 'muerto' reemplaza a `%s`:
```python
# Ejemplo de formato 
'¡Ese es %d pájaro %s!' % (1, 'muerto')
```
> '¡Ese es 1 pájaro muerto!'

```python
exam_st_date = (11,12,2014)

### TU CÓDIGO AQUÍ ###
```

**4. Escribe una función en Python para calcular la suma de tres números dados; si los valores son iguales, entonces devuelve el triple de su suma**

```python
def sum_thrice(x, y, z): 
    ### TU CÓDIGO AQUÍ ###
    pass

print(sum_thrice(1, 2, 3)) 
print(sum_thrice(3, 3, 3))
```

**5. Escribe una función en Python para verificar si un valor específico `n` está contenido en un grupo de valores `group_data`**

```python
def is_group_member(group_data, n): 
    ### TU CÓDIGO AQUÍ ###
    pass

print(is_group_member([1, 5, 8, 3], 3)) 
print(is_group_member([5, 8, 3], -1))
```

**6. Escribe una función en Python para contar el número de caracteres (frecuencia de caracteres) en una cadena de texto**

*Nota 1*: usa un diccionario.

*Nota 2*: usa el método `keys()` para obtener las llaves del diccionario.

```python
def char_frequency(str1): 
    ### TU CÓDIGO AQUÍ ###
    pass

print(char_frequency('google.com'))
```

**7. Escribe una función en Python para contar el número de números pares e impares de una tupla dada**

```python
def count_even_odd(numbers): 
    ### TU CÓDIGO AQUÍ ###
    pass

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) # Declarando la tupla 
count_even, count_odd = count_even_odd(numbers) 
print("Número de números pares :", count_even) 
print("Número de números impares :", count_odd)
```

**8. Escribe un programa en Python que acepte una palabra del usuario y la invierta**

*Nota*: es posible que necesites especificar el parámetro `end` de la función incorporada `print()` ([enlace](https://docs.python.org/3/library/functions.html#print)).

```python
word = input("Ingresa una palabra para invertir: ")

### TU CÓDIGO AQUÍ ###
```

**9. Escribe un programa en Python para probar si todos los números de una lista son mayores que un cierto número `n`**

*Nota*: puedes usar la función incorporada `all()`. La función `all()` retorna `True` si todos los elementos en un iterable (como una lista) son verdaderos, de lo contrario retorna `False`.

```python
num = [2, 3, 4, 5] 
n = 1

### TU CÓDIGO AQUÍ ###
```

**10. Escribe un programa en Python para imprimir todos los números pares de una lista dada en el mismo orden y detener la impresión de cualquier número que venga después del 237 en la secuencia**

*Nota*: la declaración `break` en Python termina el bucle actual y reanuda la ejecución en la siguiente declaración.

```python
numbers = [ 
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 
    597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 
    918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 
    687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 
    553, 81, 379, 843, 831, 445, 742, 717, 958, 743, 527 
]

### TU CÓDIGO AQUÍ ###
```
