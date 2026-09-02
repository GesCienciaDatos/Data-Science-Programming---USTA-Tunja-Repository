# 01_Criterios_Division_y_Arboles_Clasificacion_Dummies

<table style="width: 100%; border-collapse: collapse; border: none; background: #fffbeb; border-left: 6px solid #f59e0b; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #78350f; font-size: 2em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        💡 Criterios de División
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
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/09%20-%20Decision%20Trees/Para%20Dummies/01_Criterios_Division_y_Arboles_Clasificacion_Dummies.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## 🌟 La Analogía de Separar Frutas Mezcladas 🍎🍊

Imagina que tienes una canasta con manzanas rojas y naranjas:
* Si la canasta tiene **mitad manzanas y mitad naranjas**, la canasta está muy "mezclada" (*Alta Impureza / Alta Entropía*).
* Si logras separarlas en dos cajas y una caja queda **100% de manzanas** y la otra **100% de naranjas**, las cajas están "puras" (*Impureza = 0*).

---
## 🎯 ¿Cómo decide el árbol qué pregunta hacer primero?
El árbol prueba muchas preguntas (ej. *"¿El correo contiene la palabra 'GRATIS'?"*) y elige la pregunta que logre **separar mejor las manzanas de las naranjas**.

```python
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Pequeño clasificador de Spam
datos_correo = pd.DataFrame({
    'Tiene_Palabra_Gratis': [1, 1, 0, 0, 1, 0],
    'Tiene_Simbolo_Dolar': [1, 0, 0, 0, 1, 0],
    'Es_Spam': [1, 1, 0, 0, 1, 0]
})

X = datos_correo[['Tiene_Palabra_Gratis', 'Tiene_Simbolo_Dolar']]
y = datos_correo['Es_Spam']

arbol_spam = DecisionTreeClassifier(criterion='gini', max_depth=2)
arbol_spam.fit(X, y)

print("📧 ¡Filtro de correo no deseado listo!")
```

---
##### 🎯 Reto Práctico para Dummies: El Detective de Correos

**Llega un correo nuevo:**
* Tiene la palabra 'Gratis' = 1
* Tiene el símbolo de dólar '\$' = 1

¿Es Spam o es correo legítimo?

```python
# =========================================================================
# TU SOLUCIÓN: Reto Dummies 1 - Filtro de Spam
# =========================================================================

# correo_nuevo = [[1, 1]]
# prediccion = arbol_spam.predict(correo_nuevo)[0]
# print(...)
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución explicada...</b></summary>

```python
correo_nuevo = [[1, 1]]
prediccion = arbol_spam.predict(correo_nuevo)[0]

veredicto = "🚨 ¡CORREO BASURA (SPAM)!" if prediccion == 1 else "✅ Correo Seguro"
print(f"El veredicto del árbol es: 👉 {veredicto} 👈")
```
</details>

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Guía Práctica e Intuitiva</i>
  </p>
</div>
