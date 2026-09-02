# 01_Regresion_Logistica_Simple_y_Multiple_Dummies

<table style="width: 100%; border-collapse: collapse; border: none; background: #fffbeb; border-left: 6px solid #f59e0b; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #78350f; font-size: 2em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        💡 Regresión Logística [Edición Dummies] 🎯
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
        💡 Para Dummies • Módulo 08
      </span><br>
      <span style="color: #78350f; font-size: 0.85em;">Docente: Santiago A. Zúñiga M.</span><br>
      <a href="mailto:gestorvirtualcienciadatos@ustatunja.edu.co" style="color: #b45309; font-size: 0.8em; text-decoration: none; font-weight: 500;">gestorvirtualcienciadatos@ustatunja.edu.co</a>
    </td>
  </tr>
</table>

<div align="center" style="margin-top: 15px; margin-bottom: 15px;">
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/08%20-%20Classification/Para%20Dummies/01_Regresion_Logistica_Simple_y_Multiple_Dummies.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## 🌟 La Analogía de la Balanza de Decisiones ⚖️

¿Cómo decide la Regresión Logística?
* Funciona como una balanza: suma puntos positivos o negativos según las características del paciente (edad, presión arterial, frecuencia cardiaca).
* Luego, pasa ese puntaje total por un convertidor que te dice: *"Hay un 82% de probabilidad de que ocurra el evento"*.
* Si el porcentaje supera el **50%**, el modelo dictamina: **"SÍ"**; si no, dice **"NO"**.

```python
import pandas as pd
from sklearn.linear_model import LogisticRegression

url = "https://raw.githubusercontent.com/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/main/Data%20Science%20programming/08%20-%20Classification/data/heart_disease.csv"
df = pd.read_csv(url)

X = df[['age', 'trestbps', 'thalach']]
y = df['target']

modelo = LogisticRegression()
modelo.fit(X, y)

print("✅ Modelo entrenado y listo para evaluar nuevos pacientes.")
```

## 🩺 Consultando a un Paciente Nuevo
* **Edad:** 58 años
* **Presión:** 140 mm Hg
* **Frecuencia cardiaca:** 115 lpm

```python
nuevo_paciente = [[58, 140, 115]]
prob = modelo.predict_proba(nuevo_paciente)[0][1] * 100
veredicto = "🚨 Riesgo Detectado" if modelo.predict(nuevo_paciente)[0] == 1 else "✅ Saludable"

print(f"Probabilidad calculada: {prob:.1f}%")
print(f"Veredicto final: {veredicto}")
```

---
##### 🎯 Reto Práctico para Dummies: ¿Quién tiene mayor riesgo?

**Situación:** Tenemos dos pacientes:
* **Paciente A (Joven y activo):** Edad = 32, Presión = 120, Frecuencia = 165
* **Paciente B (Mayor y sedentario):** Edad = 68, Presión = 155, Frecuencia = 105

¿A cuál de los dos pacientes le asigna el modelo mayor probabilidad de afección?

```python
# =========================================================================
# TU SOLUCIÓN: Reto Dummies 1 - Comparación de Pacientes
# =========================================================================

# 1. Definir pacientes
# pac_A = [[32, 120, 165]]
# pac_B = [[68, 155, 105]]

# 2. Calcular probabilidades con modelo.predict_proba()
# prob_A = ...
# prob_B = ...
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución explicada...</b></summary>

```python
pac_A = [[32, 120, 165]]
pac_B = [[68, 155, 105]]

prob_A = modelo.predict_proba(pac_A)[0][1] * 100
prob_B = modelo.predict_proba(pac_B)[0][1] * 100

print(f"👤 Paciente A: {prob_A:.1f}% de riesgo (Saludable ✅)")
print(f"👤 Paciente B: {prob_B:.1f}% de riesgo (¡Riesgo Alto 🚨!)")
```
</details>

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Guía Práctica e Intuitiva</i>
  </p>
</div>
