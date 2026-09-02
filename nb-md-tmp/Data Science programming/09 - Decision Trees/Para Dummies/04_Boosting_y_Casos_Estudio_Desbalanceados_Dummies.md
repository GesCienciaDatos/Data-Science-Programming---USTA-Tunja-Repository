# 04_Boosting_y_Casos_Estudio_Desbalanceados_Dummies

<table style="width: 100%; border-collapse: collapse; border: none; background: #fffbeb; border-left: 6px solid #f59e0b; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #78350f; font-size: 2em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        💡 Boosting y Aprendizaje Continuo
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
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/09%20-%20Decision%20Trees/Para%20Dummies/04_Boosting_y_Casos_Estudio_Desbalanceados_Dummies.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## 🌟 La Analogía de Estudiar para un Examen Difícil 📝🧠

Imagina que estás resolviendo cuestionarios para preparar un examen:
* En el primer intento, respondes 10 preguntas y fallas en 3.
* En el segundo intento, **te enfocas con especial atención en las 3 preguntas que fallaste** hasta dominarlas.
* En el tercer intento, repasas los detalles mínimos donde todavía dudas.

Eso es **Boosting**:
Cada nuevo árbol se enfoca en corregir los errores cometidos por los árboles anteriores.

<div align="center">
  <img src="images/boosting.png" width="450" alt="Boosting Intuitivo" style="border-radius:8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); margin:10px 0;"/>
</div>

```python
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier

# Datos de spam simplificados
datos = pd.DataFrame({
    'Palabra_Gratis': [1, 0, 1, 0, 1, 0],
    'Simbolo_Dolar': [1, 0, 0, 0, 1, 0],
    'Letras_Mayusculas': [15, 2, 4, 1, 25, 0],
    'Es_Spam': [1, 0, 1, 0, 1, 0]
})

X = datos[['Palabra_Gratis', 'Simbolo_Dolar', 'Letras_Mayusculas']]
y = datos['Es_Spam']

# Entrenar un Gradient Boosting
modelo_boosting = GradientBoostingClassifier(n_estimators=30, learning_rate=0.1, random_state=42)
modelo_boosting.fit(X, y)

print("🚀 ¡Modelo Boosting entrenado y afinado paso a paso!")
```

---
##### 🎯 Reto Práctico para Dummies: Detección con Boosting

**Llega un correo sospechoso:**
* Palabra 'Gratis': 1
* Símbolo '\$': 1
* Letras Mayúsculas: 20

¿Qué dice el modelo Boosting?

```python
# =========================================================================
# TU SOLUCIÓN: Reto Dummies 4 - Predicción con Boosting
# =========================================================================

# correo = [[1, 1, 20]]
# prediccion = modelo_boosting.predict(correo)[0]
# print(...)
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución explicada...</b></summary>

```python
correo = [[1, 1, 20]]
prediccion = modelo_boosting.predict(correo)[0]

veredicto = "🚨 ¡SPAM CONFIRMADO!" if prediccion == 1 else "✅ Correo Seguro"
print(f"El modelo Boosting concluye: 👉 {veredicto} 👈")
```
</details>

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Guía Práctica e Intuitiva</i>
  </p>
</div>
