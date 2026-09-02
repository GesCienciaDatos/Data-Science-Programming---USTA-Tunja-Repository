# 01_Sintaxis_Variables_y_Tipos_de_Datos_Dummies

<table style="width: 100%; border-collapse: collapse; border: none; background: #fffbeb; border-left: 6px solid #f59e0b; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #78350f; font-size: 2em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        💡 01. Sintaxis, Variables y Tipos de Datos
      </h1>
      <p style="margin: 6px 0 0 0; color: #b45309; font-size: 1.15em; font-weight: 600; font-family: system-ui, -apple-system, sans-serif;">
        Especialización en Ciencia de Datos | Programación para Ciencia de Datos
      </p>
      <p style="margin: 4px 0 0 0; color: #92400e; font-size: 0.95em; font-family: system-ui, -apple-system, sans-serif;">
        Universidad Santo Tomás — Seccional Tunja
      </p>
    </td>
    <td style="text-align: right; vertical-align: middle; border: none; padding: 15px 20px; width: 30%;">
      <span style="background: #f59e0b; color: #ffffff; padding: 6px 14px; border-radius: 20px; font-size: 0.85em; font-weight: 700; display: inline-block; margin-bottom: 8px;">
        💡 Para Dummies • Módulo 01
      </span><br>
      <span style="color: #78350f; font-size: 0.85em;">Docente: Santiago A. Zúñiga M.</span><br>
      <a href="mailto:gestorvirtualcienciadatos@ustatunja.edu.co" style="color: #b45309; font-size: 0.8em; text-decoration: none; font-weight: 500;">gestorvirtualcienciadatos@ustatunja.edu.co</a>
    </td>
  </tr>
</table>

<div align="center" style="margin-top: 15px; margin-bottom: 15px;">
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/01%20-%20Python/Para%20Dummies/01_Sintaxis_Variables_y_Tipos_de_Datos_Dummies.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## 1. ¿Qué es una Variable? 📦

### 💡 La Analogía de las Cajas con Etiquetas
Imagina que te estás mudando de casa y tienes varias cajas de cartón. Para no volverte loco buscando tus cosas, le pegas una **etiqueta adhesiva** a cada caja:
- A una caja le pegas la etiqueta `"edad"` y metes el número `28`.
- A otra le pegas `"nombre"` y metes el texto `"Carlos"`.
- A otra le pegas `"precio_cafe"` y metes `3.50`.

En Python, una **variable es exactamente esa etiqueta**. El nombre de la variable te permite guardar, consultar y cambiar cualquier dato en cualquier momento.

```python
# Creando nuestras primeras cajas (variables):
nombre_cliente = "Laura Gómez"   # Texto (String)
edad_cliente = 34                # Número entero (Integer)
saldo_cuenta = 1520.75           # Número con decimales (Float)
es_cliente_activo = True         # Verdadero o Falso (Booleano)

print("Nombre:", nombre_cliente)
print("Edad:", edad_cliente, "años")
print("Saldo disponible: $", saldo_cuenta)
print("¿Está activo?:", es_cliente_activo)
```

---
## 2. Los 4 Tipos de Datos Primitivos en Python 🧱

Python tiene 4 tipos de datos básicos que son como los 4 materiales fundamentales de construcción:

| Tipo de Dato | Nombre en Python | 💡 ¿Qué representa? | Ejemplos cotidianos |
|---|---|---|---|
| **Enteros** | `int` | Números completos sin decimales. | Número de hijos (`2`), año (`2026`), stock de productos (`150`). |
| **Decimales / Flotantes** | `float` | Números con punto decimal. | Estatura en metros (`1.75`), temperatura (`36.6`), precio (`9.99`). |
| **Texto / Cadenas** | `str` | Palabras, frases o símbolos entre comillas. | `"Bogotá"`, `"usuario@correo.com"`, `"Factura #104"`. |
| **Booleanos** | `bool` | Solo dos valores: `True` (Verdadero) o `False` (Falso). | `tiene_descuento = True`, `esta_lloviendo = False`. |

> ⚠️ **Ojo:** En Python los decimales se escriben con **punto** (`3.14`), NO con coma (`3,14`). Si usas coma, Python pensará que son dos cosas distintas.

```python
# Usamos la función type() para preguntarle a Python qué tipo de dato hay en cada caja:
print(type(edad_cliente))       # <class 'int'>
print(type(saldo_cuenta))       # <class 'float'>
print(type(nombre_cliente))     # <class 'str'>
print(type(es_cliente_activo))  # <class 'bool'>
```

---
## 3. Operaciones Matemáticas Básicas ➕➖✖️➗

Python funciona como una calculadora superpotente:

| Operación | Símbolo en Python | Ejemplo en la vida real |
|---|---|---|
| Suma | `+` | `total = subtotal + iva` |
| Resta | `-` | `ganancia = ingresos - costos` |
| Multiplicación | `*` | `total_horas = dias * 24` |
| División | `/` | `promedio = suma_notas / cantidad` |
| División Entera | `//` | Repartir 10 galletas entre 3 niños: `10 // 3` da `3` galletas a cada uno. |
| Residuo / Módulo | `%` | Lo que sobra de la repartición: `10 % 3` da `1` (la galleta sobrante). |
| Potencia (Exponente) | `**` | $2^3$ se escribe `2 ** 3` (resultado: 8). |

```python
# Calculando el costo de un viaje en taxi:
tarifa_base = 5000       # Pesos
costo_por_km = 1200      # Pesos por cada km
distancia_recorrida = 8.5 # Kilómetros

total_viaje = tarifa_base + (costo_por_km * distancia_recorrida)
print(f"🚕 El total a pagar por el viaje es: ${total_viaje:,.2f}")
```

---
## 4. Conversión de Tipos (Casting) 🔄

### 💡 La Analogía del Número Escrito en un Papel
Si alguien escribe el número `"50"` en un pedazo de papel, para la computadora eso es **texto**, no un número con el que pueda hacer sumas.
Para poder hacer matemáticas, debemos decirle a Python: *"Por favor, convierte este texto a un número real"*.

* `int("25")` $ightarrow$ Convierte el texto `"25"` al número entero `25`.
* `float("19.99")` $ightarrow$ Convierte a decimal `19.99`.
* `str(100)` $ightarrow$ Convierte el número `100` al texto `"100"`.

```python
# Supongamos que recibimos la cantidad de un formulario web (siempre entra como texto):
cantidad_str = "15"
precio_unitario = 2000

# Si intentamos multiplicar sin convertir: ¡Python repetiría el texto 15 veces!
# Convertimos primero con int():
cantidad_num = int(cantidad_str)
total = cantidad_num * precio_unitario

print(f"Total de {cantidad_num} unidades a ${precio_unitario} = ${total}")
```

---
## 🛠️ Práctica: Calculadora de Presupuesto Personal

**Problema:**
Estás creando un pequeño programa para un negocio familiar de venta de café:
- Tienen 3 sacos de café tipo Exportación a \\$350,000 cada uno.
- Tienen 5 sacos de café tipo Tradicional a \\$220,000 cada uno.
- Hay un costo de envío fijo de \\$50,000.
- El cliente tiene un cupón de descuento del 10% sobre el valor del café (antes del envío).

Calcula el valor total a cobrar e imprímelo en pantalla de forma bonita.

```python
# 1. Escribe tus variables y cálculos aquí:
sacos_exportacion = 3
precio_exportacion = 350000

sacos_tradicional = 5
precio_tradicional = 220000

costo_envio = 50000
porcentaje_descuento = 0.10

# Tu cálculo:
subtotal_cafe = (sacos_exportacion * precio_exportacion) + (sacos_tradicional * precio_tradicional)
descuento = subtotal_cafe * porcentaje_descuento
total_con_descuento_y_envio = (subtotal_cafe - descuento) + costo_envio

print(f"Subtotal Café: ${subtotal_cafe:,.2f}")
print(f"Descuento (10%): -${descuento:,.2f}")
print(f"Envío: ${costo_envio:,.2f}")
print(f"👉 Total Final: ${total_con_descuento_y_envio:,.2f}")
```

<details>
<summary>💡 Haz clic aquí para ver la explicación detallada de la solución</summary>

1. Multiplicamos la cantidad de cada saco por su precio unitario y los sumamos para obtener el `subtotal_cafe`.
2. Calculamos el `descuento` multiplicando por `0.10`.
3. Restamos el descuento al subtotal y finalmente sumamos el `costo_envio`.
4. El formato `f"${total:,.2f}"` formatea el número automáticamente con comas para los miles y 2 cifras decimales.
</details>

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos (Edición Para No Ingenieros)</i>
  </p>
</div>
