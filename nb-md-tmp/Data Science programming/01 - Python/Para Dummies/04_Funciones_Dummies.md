# 04_Funciones_Dummies

<table style="width: 100%; border-collapse: collapse; border: none; background: #fffbeb; border-left: 6px solid #f59e0b; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #78350f; font-size: 2em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        💡 04. Funciones: Creando Tus Propias Herramientas
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
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/01%20-%20Python/Para%20Dummies/04_Funciones_Dummies.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## 1. ¿Qué es una Función? 🍳

### 💡 La Analogía de la Cafetera Automática
En lugar de levantarte todos los días a calentar agua, moler granos, poner el filtro y medir el café manualmente, compras una **cafetera automática**. Tú solo presionas un botón (o le pasas cuántas tazas quieres), y la máquina ejecuta toda la receta internamente y te entrega el café listo.

Una **Función** es exactamente eso: un bloque de código con un nombre que hace una tarea específica cada vez que lo llamas con `def nombre_funcion():`.

```python
# 1. Definimos nuestra primera función con 'def':
def saludar_estudiante(nombre, curso="Ciencia de Datos"):
    '''Saluda a un estudiante de forma personalizada.'''
    mensaje = f"¡Hola {nombre}! Bienvenido a tu clase de {curso} 🚀"
    return mensaje

# 2. Llamamos la función con diferentes personas:
print(saludar_estudiante("Sofía"))
print(saludar_estudiante("Mateo", curso="Machine Learning"))
print(saludar_estudiante("Camila"))
```

---
## 2. Parámetros vs Retorno (`return`) 📬

* **Parámetros (Entradas):** Los ingredientes que le entregas a la receta.
* **Cuerpo:** Los pasos que realiza la receta.
* **`return` (Salida):** El platillo terminado que la función te devuelve para que lo guardes o uses en otro cálculo.

> ⚠️ **Diferencia entre `print()` y `return`:** `print()` solo muestra algo en la pantalla para que tus ojos lo lean. `return` entrega el dato a Python para que otra variable pueda guardarlo y seguir calculando.

```python
# Calculadora de Índice de Masa Corporal (IMC):
def calcular_imc(peso_kg, estatura_metros):
    imc = peso_kg / (estatura_metros ** 2)
    return imc

# Usamos el valor retornado en otra variable:
mi_imc = calcular_imc(72, 1.75)
print(f"Tu IMC es: {mi_imc:.2f}")

if mi_imc < 25:
    print("Estado: Peso Saludable ✅")
else:
    print("Estado: Sobrepeso o superior ⚠️")
```

---
## 3. Argumentos Flexibles: `*args` y `**kwargs` 🎒

### 💡 La Analogía de la Maleta de Viaje
- **`*args`:** Una mochila donde puedes meter **cualquier cantidad de objetos sueltos** (ej. calcular el promedio de 3, 5 o 20 números sin saber cuántos vendrán).
- **`**kwargs`:** Una maleta con bolsillos etiquetados donde metes pares de datos opcionales (`color="azul"`, `talla="M"`).

```python
# Función que suma cualquier cantidad de números usando *args:
def sumar_todos(*numeros):
    total = sum(numeros)
    return total

print("Suma de 3 números:", sumar_todos(10, 20, 30))
print("Suma de 6 números:", sumar_todos(5, 15, 25, 35, 45, 55))
```

---
## 4. Funciones Lambda: Las funciones exprés en una sola línea ⚡

Son pequeñas funciones anónimas que se usan para transformaciones rápidas sin necesidad de escribir un `def` completo.

```python
# Queremos convertir precios de dólares a pesos colombianos (TRM aproximada: $4,000)
convertir_a_cop = lambda dolares: dolares * 4000

print("$5 USD en pesos colombianos son:", convertir_a_cop(5), "COP")
print("$50 USD en pesos colombianos son:", convertir_a_cop(50), "COP")
```

---
## 🛠️ Práctica: Calculador de Descuentos Comerciales

**Problema:**
Crea una función llamada `aplicar_descuento(precio_original, porcentaje_descuento)` que:
1. Calcule el monto ahorrado.
2. Calcule el precio final a pagar.
3. Retorne ambos valores.
4. Pruébala con un artículo de \\$150,000 con el 20% de descuento.

```python
# Solución guiada:
def aplicar_descuento(precio_original, porcentaje_descuento):
    ahorro = precio_original * (porcentaje_descuento / 100)
    precio_final = precio_original - ahorro
    return ahorro, precio_final

ahorro, final = aplicar_descuento(150000, 20)
print(f"Precio Original: $150,000")
print(f"Te ahorraste: ${ahorro:,.2f}")
print(f"Precio final a pagar: ${final:,.2f}")
```

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos (Edición Para No Ingenieros)</i>
  </p>
</div>
