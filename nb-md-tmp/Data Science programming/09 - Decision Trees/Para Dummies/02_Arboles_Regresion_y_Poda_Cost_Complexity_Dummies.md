# 02_Arboles_Regresion_y_Poda_Cost_Complexity_Dummies

<table style="width: 100%; border-collapse: collapse; border: none; background: #fffbeb; border-left: 6px solid #f59e0b; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #78350f; font-size: 2em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        💡 Árboles de Regresión y Poda
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
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/09%20-%20Decision%20Trees/Para%20Dummies/02_Arboles_Regresion_y_Poda_Cost_Complexity_Dummies.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## 🌟 La Analogía de la Poda del Bonsái ✂️🌳

Imagina que estás cuidando un árbol bonsái:
* Si dejas que le crezcan **demasiadas ramitas diminutas**, el árbol se vuelve caótico, frágil y pierde su forma hermosa (*Sobreajuste*).
* Si tomas unas tijeras de jardinería y **podas las ramitas innecesarias**, el árbol se vuelve robusto, fuerte y claro (*Generalización*).

---
## 🏠 ¿Cómo predice el precio de una casa un árbol de regresión?
* Divide las casas en grupos (ej. *"Casas de más de 3 cuartos con jardín"*).
* Calcula el **precio promedio** de ese grupito y se lo asigna a cualquier casa parecida.

```python
import pandas as pd
from sklearn.tree import DecisionTreeRegressor

# Pequeña tabla de precios de casas
datos_casas = pd.DataFrame({
    'Habitaciones': [2, 3, 4, 3, 5],
    'Metros_Cuadrados': [65, 90, 140, 110, 200],
    'Precio_Millones': [180, 260, 420, 310, 580]
})

X = datos_casas[['Habitaciones', 'Metros_Cuadrados']]
y = datos_casas['Precio_Millones']

arbol_casas = DecisionTreeRegressor(max_depth=2, random_state=42)
arbol_casas.fit(X, y)

print("🏡 ¡Árbol podado y listo para avaluar casas!")
```

---
##### 🎯 Reto Práctico para Dummies: ¿Cuánto cuesta esta casa?

**Llega una casa nueva:**
* 3 Habitaciones
* 100 Metros cuadrados

¿Cuál es el valor estimado por el árbol?

```python
# =========================================================================
# TU SOLUCIÓN: Reto Dummies 2 - Avalúo Inmobiliario
# =========================================================================

# casa_nueva = [[3, 100]]
# avaluo = arbol_casas.predict(casa_nueva)[0]
# print(...)
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución explicada...</b></summary>

```python
casa_nueva = [[3, 100]]
avaluo = arbol_casas.predict(casa_nueva)[0]

print(f"💰 El precio estimado para la casa es: 👉 ${avaluo:,.0f} Millones de pesos 👈")
```
</details>

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Guía Práctica e Intuitiva</i>
  </p>
</div>
