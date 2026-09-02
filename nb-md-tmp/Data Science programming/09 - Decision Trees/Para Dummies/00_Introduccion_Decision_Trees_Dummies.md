# 00_Introduccion_Decision_Trees_Dummies

<table style="width: 100%; border-collapse: collapse; border: none; background: #fffbeb; border-left: 6px solid #f59e0b; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #78350f; font-size: 2em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        💡 Introducción a los Árboles de Decisión
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
        💡 Para Dummies • Módulo 09
      </span><br>
      <span style="color: #78350f; font-size: 0.85em;">Docente: Santiago A. Zúñiga M.</span><br>
      <a href="mailto:gestorvirtualcienciadatos@ustatunja.edu.co" style="color: #b45309; font-size: 0.8em; text-decoration: none; font-weight: 500;">gestorvirtualcienciadatos@ustatunja.edu.co</a>
    </td>
  </tr>
</table>

<div align="center" style="margin-top: 15px; margin-bottom: 15px;">
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/09%20-%20Decision%20Trees/Para%20Dummies/00_Introduccion_Decision_Trees_Dummies.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## 🌟 La Analogía del Juego de las 20 Preguntas ❓

¿Alguna vez has jugado a adivinar un personaje haciendo preguntas de *Sí* o *No*?
* *"¿Es una persona real?"* $\to$ Sí.
* *"¿Es deportista?"* $\to$ No.
* *"¿Es cantante?"* $\to$ Sí.

Un **Árbol de Decisión** funciona exactamente igual:
En lugar de usar fórmulas matemáticas complicadas, le hace preguntas a los datos paso a paso para clasificar una situación.

<div align="center">
  <img src="images/flowchart.png" width="550" alt="Diagrama de Flujo Cotidiano" style="border-radius:8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); margin:10px 0;"/>
</div>

---
## 🌲 Las Partes del Árbol en Palabras Sencillas:
1. **La Raíz:** La primera pregunta que divide al grupo.
2. **Las Ramas:** Los caminos del *SÍ* o del *NO*.
3. **Las Hojas:** La respuesta final (ej. *"El cliente comprará el producto"* o *"El correo es Spam"*).

```python
import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

# Pequeño ejemplo de decisión cotidiana: ¿Salimos a jugar al parque?
datos_parque = pd.DataFrame({
    'Lluvia': [0, 0, 1, 1, 0, 1],         # 0: Soleado, 1: Lloviendo
    'Temperatura': [25, 28, 14, 18, 15, 12],# Grados centígrados
    'Viento_Fuerte': [0, 1, 1, 0, 0, 1],   # 0: Brisa suave, 1: Viento fuerte
    'Jugar': ['Sí', 'Sí', 'No', 'No', 'Sí', 'No']
})

X = datos_parque[['Lluvia', 'Temperatura', 'Viento_Fuerte']]
y = datos_parque['Jugar']

arbol_juego = DecisionTreeClassifier(max_depth=2, random_state=42)
arbol_juego.fit(X, y)

print("🌳 ¡Árbol de decisiones entrenado exitosamente!")
```

```python
# Visualizar el mapa de decisiones
plt.figure(figsize=(9, 4.5), dpi=110)
plot_tree(
    arbol_juego,
    feature_names=['¿Lluvia?', 'Temperatura', '¿Viento Fuerte?'],
    class_names=['No Jugar', 'Sí Jugar'],
    filled=True,
    rounded=True
)
plt.title("💡 El Árbol para Decidir si Salimos al Parque", fontweight='bold')
plt.show()
```

---
##### 🎯 Reto Práctico para Dummies: ¿Salimos hoy a jugar?

**Situación del día de hoy:**
* No está lloviendo (`Lluvia = 0`)
* Hace calor (`Temperatura = 24 °C`)
* No hay viento fuerte (`Viento_Fuerte = 0`)

¿Cuál es la decisión del árbol?

```python
# =========================================================================
# TU SOLUCIÓN: Reto Dummies 0 - Prediciendo la salida al parque
# =========================================================================

# dia_hoy = [[0, 24, 0]]
# veredicto = arbol_juego.predict(dia_hoy)[0]
# print(...)
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución explicada...</b></summary>

```python
dia_hoy = [[0, 24, 0]]
veredicto = arbol_juego.predict(dia_hoy)[0]

print(f"☀️ Para el día de hoy, el veredicto es: 👉 ¡{veredicto.upper()} SALIMOS A JUGAR! 👈")
```
</details>

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Guía Práctica e Intuitiva</i>
  </p>
</div>
