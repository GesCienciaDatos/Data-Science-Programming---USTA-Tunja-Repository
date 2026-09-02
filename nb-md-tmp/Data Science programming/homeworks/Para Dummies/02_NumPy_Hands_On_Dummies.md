# 02_NumPy_Hands_On_Dummies

<table style="width: 100%; border-collapse: collapse; border: none; background: #fffbeb; border-left: 6px solid #f59e0b; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #78350f; font-size: 2em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        💡 Taller Práctico 02: NumPy para No Ingenieros
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
        💡 Taller Dummies • Módulo 02
      </span><br>
      <span style="color: #78350f; font-size: 0.85em;">Docente: Santiago A. Zúñiga M.</span><br>
      <a href="mailto:gestorvirtualcienciadatos@ustatunja.edu.co" style="color: #b45309; font-size: 0.8em; text-decoration: none; font-weight: 500;">gestorvirtualcienciadatos@ustatunja.edu.co</a>
    </td>
  </tr>
</table>

<div align="center" style="margin-top: 15px; margin-bottom: 15px;">
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/homeworks/Para%20Dummies/02_NumPy_Hands_On_Dummies.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## Taller 02: Cálculos Masivos con NumPy 🚀

Practicaremos la creación de matrices, operaciones vectorizadas y filtrado de datos sin usar bucles.

---
### Ejercicio 1: Conversión de Temperatura de Sensores 🌡️
**Situación:** Un sensor industrial registró 5 temperaturas en grados Celsius: `[20.5, 24.0, 18.2, 31.5, 27.8]`.
Convierte todas las temperaturas a Fahrenheit usando la fórmula $F = (C \times rac{9}{5}) + 32$ de un solo golpe con NumPy.

```python
import numpy as np

celsius = np.array([20.5, 24.0, 18.2, 31.5, 27.8])

# Operación vectorizada directa:
fahrenheit = (celsius * (9/5)) + 32

print("Temperaturas en Celsius:   ", celsius)
print("Temperaturas en Fahrenheit:", np.round(fahrenheit, 2))
```

---
### Ejercicio 2: Filtrando Ventas Extraordinarias 💰
**Situación:** Tienes un array de ventas diarias: `[150, 320, 890, 450, 1200, 210, 670]`.
Filtra y muestra únicamente los días donde las ventas superaron los `\\$500` USD.

```python
ventas = np.array([150, 320, 890, 450, 1200, 210, 670])

# Filtro booleano:
ventas_altas = ventas[ventas > 500]

print("Todas las ventas:", ventas)
print("Ventas mayores a $500 USD:", ventas_altas)
print("Promedio de ventas en días altos: $", ventas_altas.mean())
```

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos (Edición Para No Ingenieros)</i>
  </p>
</div>
