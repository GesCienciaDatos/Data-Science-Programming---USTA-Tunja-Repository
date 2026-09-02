# 03_Metodos_Ensamble_Bagging_y_Random_Forests_Dummies

<table style="width: 100%; border-collapse: collapse; border: none; background: #fffbeb; border-left: 6px solid #f59e0b; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #78350f; font-size: 2em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        💡 Bagging y Bosques Aleatorios
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
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/09%20-%20Decision%20Trees/Para%20Dummies/03_Metodos_Ensamble_Bagging_y_Random_Forests_Dummies.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## 🌟 La Analogía de la Junta de Médicos 🩺👥

* Si consultas a **un solo médico**, su diagnóstico puede ser brillante pero también puede tener un mal día o equivocarse (*Árbol individual*).
* Si reúnes a una **junta de 100 médicos especialistas**, cada uno analiza el caso desde su perspectiva y al final **votan democráticamente**, el diagnóstico final será inmensamente más confiable y seguro (*Bosque Aleatorio / Random Forest*).

<div align="center">
  <img src="images/trees.png" width="450" alt="Bosque de Arboles" style="border-radius:8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); margin:10px 0;"/>
</div>

---
## 🌲 ¿Qué hace "Aleatorio" al Bosque?
1. Cada árbol estudia una **muestra diferente de pacientes** (con reemplazo).
2. En cada pregunta, el médico solo puede mirar un **grupo aleatorio de síntomas** para no copiarse siempre del mismo síntoma dominante.

```python
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Datos de pacientes cardiacos simplificados
datos = pd.DataFrame({
    'Edad': [65, 45, 58, 70, 38, 52],
    'Presion': [150, 120, 140, 160, 115, 130],
    'Colesterol': [280, 190, 240, 310, 180, 220],
    'Cardiopatia': [1, 0, 1, 1, 0, 0]
})

X = datos[['Edad', 'Presion', 'Colesterol']]
y = datos['Cardiopatia']

# Bosque de 50 árboles
bosque = RandomForestClassifier(n_estimators=50, random_state=42)
bosque.fit(X, y)

print("🌳🌲 ¡Junta médica de 50 árboles lista para diagnosticar!")
```

---
##### 🎯 Reto Práctico para Dummies: La Votación de la Junta Médica

**Nuevo paciente:**
* Edad: 62 años
* Presión: 145
* Colesterol: 260

¿Qué opina la junta de 50 árboles?

```python
# =========================================================================
# TU SOLUCIÓN: Reto Dummies 3 - Diagnóstico por Bosque Aleatorio
# =========================================================================

# paciente = [[62, 145, 260]]
# veredicto = bosque.predict(paciente)[0]
# probabilidades = bosque.predict_proba(paciente)[0]
# print(...)
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución explicada...</b></summary>

```python
paciente = [[62, 145, 260]]
veredicto = bosque.predict(paciente)[0]
probabilidades = bosque.predict_proba(paciente)[0]

print("=" * 60)
print(f"• Veredicto de la Junta Médica: 👉 {'RIESGO ALTO (1)' if veredicto == 1 else 'SANO (0)'} 👈")
print(f"• Votos a favor de Cardiopatía: {probabilidades[1]*100:.1f}% de los 50 médicos")
print("=" * 60)
```
</details>

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Guía Práctica e Intuitiva</i>
  </p>
</div>
