# 08_Modulos_y_Paquetes_Dummies

<table style="width: 100%; border-collapse: collapse; border: none; background: #fffbeb; border-left: 6px solid #f59e0b; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #78350f; font-size: 2em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        💡 08. Módulos y Paquetes
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
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/01%20-%20Python/Para%20Dummies/08_Modulos_y_Paquetes_Dummies.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## 1. ¿Qué es un Módulo y un Paquete? 🧰

### 💡 La Analogía de la Ferretería
No tienes que inventar el martillo, el taladro ni los clavos cada vez que quieras colgar un cuadro en la pared. Vas a la ferretería y pides la herramienta que necesitas.

- **Un Módulo:** Es un archivo de Python (`.py`) que contiene funciones ya escritas listas para usar (ej. `math`, `random`, `datetime`).
- **Un Paquete / Librería:** Es una caja completa con varios módulos organizados (ej. `NumPy`, `Pandas`, `Matplotlib`).

---
## 2. Formas de Importar en Python 📦

```python
# 1. Importar el módulo completo:
import math

print("El valor exacto de Pi es:", math.pi)
print("La raíz cuadrada de 144 es:", math.sqrt(144))
```

```python
# 2. Importar solo una herramienta específica y renombrarla con un apodo (alias):
import datetime as dt

fecha_hora_actual = dt.datetime.now()
print(f"📅 Fecha y hora de hoy: {fecha_hora_actual.strftime('%d/%m/%Y %H:%M:%S')}")
```

```python
# 3. Importar utilidades aleatorias:
import random

estudiantes = ["Carolina", "Diego", "Esteban", "Gabriela", "Hernán"]
ganador_sorteo = random.choice(estudiantes)
numero_aleatorio = random.randint(1, 100)

print(f"🎉 El ganador seleccionado al azar es: {ganador_sorteo}")
print(f"🎲 Número de la suerte generado: {numero_aleatorio}")
```

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos (Edición Para No Ingenieros)</i>
  </p>
</div>
