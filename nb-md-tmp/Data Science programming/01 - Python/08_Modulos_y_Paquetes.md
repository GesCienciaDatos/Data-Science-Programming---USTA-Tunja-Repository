# 08_Modulos_y_Paquetes

<table style="width: 100%; border-collapse: collapse; border: none; background: #f8fafc; border-left: 6px solid #1e3a8a; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #0f172a; font-size: 2.1em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        Módulos, Paquetes y Entornos en Python 📦
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
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/01%20-%20Python/08_Modulos_y_Paquetes.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---

## Módulos y Paquetes en Python

### 1. Fundamentos de Módulos y Paquetes 🌱

#### 1.1 ¿Qué es un Módulo y un Paquete?
A medida que tus programas crecen, escribir todo el código en un solo archivo se vuelve insostenible. Aquí es donde entran en juego los **Modules** y **Packages**, los pilares de la arquitectura y organización en Python. Además, son la puerta de acceso a la "Librería Estándar" de Python y a miles de herramientas creadas por la comunidad.

*   **Module (Módulo):** En su forma más simple, un módulo es solo un archivo de Python (con extensión `.py`) que contiene definiciones de variables, funciones y clases. Piensa en él como un "caja de herramientas" específica. 
*   **Package (Paquete):** Es una carpeta que contiene múltiples módulos (varios archivos `.py`). Para que Python reconozca esa carpeta oficialmente como un paquete, tradicionalmente debe contener un archivo especial (usualmente vacío) llamado `__init__.py`.

> 🤓 **La conexión con los Namespaces:** Cuando importas un módulo, lo que Python hace internamente es ejecutar ese archivo y cargar todas sus variables y funciones en tu **Namespace** actual. Entender los Namespaces (Sección 7) es clave aquí, porque al importar evitas que las herramientas del módulo colisionen con las variables que tú mismo has creado.

---

#### 1.2 Formas de Importar

Python te ofrece mucha flexibilidad sobre *cómo* quieres traer esas herramientas a tu archivo principal. 

*   **Importación absoluta (`import modulo`):** Trae todo el archivo. Es la forma más segura porque mantiene el Namespace del módulo separado del tuyo. Para usar una función, debes escribir `modulo.funcion()`.
*   **Importación específica (`from modulo import herramienta`):** Trae solo una función, clase o variable específica directamente a tu Namespace local. Te ahorra escribir el nombre del módulo cada vez, pero debes tener cuidado de no tener una variable local con ese mismo nombre.
*   **Alias (`import modulo as apodo`):** Permite renombrar el módulo dentro de tu archivo. Es extremadamente común en el análisis de datos (ej. `import pandas as pd`).
*   **Importación con comodín (`from modulo import *`):** Trae *absolutamente todo* del módulo a tu Namespace local. **No se recomienda** en proyectos serios porque inunda tu espacio de nombres y puede sobrescribir tus propias variables sin que te des cuenta.

---

#### 1.3 Estructura y Sintaxis

| Tipo de Importación | Cuándo usarlo | Sintaxis de Ejemplo |
| :--- | :--- | :--- |
| **Básica completa** | Quieres usar muchas cosas del módulo y mantener el orden. | `import math` <br> `math.sqrt(9)` |
| **Específica** | Solo necesitas una o dos herramientas del módulo. | `from math import sqrt, pi` <br> `sqrt(9)` |
| **Con Alias (`as`)** | El nombre del módulo es muy largo o hay un estándar. | `import matplotlib.pyplot as plt` <br> `plt.plot()` |
| **El archivo `__init__.py`**| Se coloca dentro de una carpeta para volverla un Package. | `mi_paquete/` <br> `├── __init__.py` <br> `└── modulo.py` |

---
### 2. Importaciones y la Librería Estándar 🛠️

#### 2.1 Usando la Librería Estándar (Módulos integrados)
Python viene con "pilas incluidas". No necesitas instalar nada extra para usar módulos como `math`, `random` o `datetime`.

```python
# Importamos el módulo 'random' completo
import random

# Como usamos la importación básica, debemos usar la notación de punto: modulo.funcion()
numero_azar = random.randint(1, 100)
print(f"Tu número de la suerte es: {numero_azar}")
```

#### 2.2 Importaciones específicas y Alias
A veces solo quieres una herramienta muy concreta para no escribir tanto.

```python
# Importamos solo 'datetime' (la clase) del módulo 'datetime' (el archivo)
from datetime import datetime

# Importamos el módulo 'math' pero le ponemos un apodo corto
import math as m

# Ya no escribimos 'datetime.datetime.now()', solo lo siguiente:
hora_actual = datetime.now()
print(f"El proceso inició a las: {hora_actual}")

# Usamos el alias 'm' en lugar de 'math'
radio = 5
area_circulo = m.pi * m.pow(radio, 2)
print(f"El área del círculo es {area_circulo:.2f}")
```

--- 
### 3. Construyendo tus propios módulos 🧠
Si estuvieras construyendo un proyecto real, tendrías dos archivos en la misma carpeta:

Archivo 1: `operaciones.py` (Tu módulo)

```python
%%writefile operaciones.py
# Contenido de operaciones.py
def sumar(a, b):
    return a + b
```

Archivo 2: `main.py` (Tu archivo principal)

```python
# Contenido de main.py
import operaciones

resultado = operaciones.sumar(10, 5)
print(resultado) # Salida: 15
```

### 🛠️ Práctica: Módulos y Paquetes

Imagina que estás escribiendo un programa para simular un sorteo de lotería y necesitas calcular las probabilidades.

Tu tarea es arreglar la sección de importaciones en la parte superior del script. Necesitas importar el módulo `random` con el alias `rd`, y extraer específicamente la función `factorial` del módulo `math`.

```python
# 1. Tu código va aquí:
# Importa el módulo 'random' y asígnale el alias 'rd'


# 2. Tu código va aquí:
# Importa ESPECÍFICAMENTE la función 'factorial' del módulo 'math'


# --- Código de prueba (No modificar) ---

def simular_sorteo():
    # Usamos el alias 'rd' para generar una lista de 3 números ganadores del 1 al 50
    ganadores = [rd.randint(1, 50) for _ in range(3)]
    
    # Usamos la función específica 'factorial' (sin notación de punto porque fue importada directamente)
    # Calculamos cuántas combinaciones posibles hay de 50 números tomados de 3 en 3
    combinaciones = factorial(50) // (factorial(3) * factorial(50 - 3))
    
    print(f"Los números ganadores son: {ganadores}")
    print(f"Probabilidad de ganar: 1 en {combinaciones}")

# Ejecutar simulación
simular_sorteo()
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
# 1. Tu código va aquí:
import random as rd

# 2. Tu código va aquí:
from math import factorial

def simular_sorteo():
    ganadores = [rd.randint(1, 50) for _ in range(3)]
    combinaciones = factorial(50) // (factorial(3) * factorial(50 - 3))
    
    print(f"Los números ganadores son: {ganadores}")
    print(f"Probabilidad de ganar: 1 en {combinaciones}")

simular_sorteo()
```
</details>

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos</i>
  </p>
</div>
