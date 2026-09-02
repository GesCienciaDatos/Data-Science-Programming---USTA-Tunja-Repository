# 03_Evaluacion_de_Modelos_y_Metricas_Clasificacion_Dummies

<table style="width: 100%; border-collapse: collapse; border: none; background: #fffbeb; border-left: 6px solid #f59e0b; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #78350f; font-size: 2em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        💡 Evaluación de Modelos [Edición Dummies] 🎯
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
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/08%20-%20Classification/Para%20Dummies/03_Evaluacion_de_Modelos_y_Metricas_Clasificacion_Dummies.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## 🌟 La Analogía de la Alarma de Incendios y la Prueba Médica 🚨

¿Cómo sabemos si un detector es bueno?
1. **Verdadero Positivo:** Había fuego y la alarma sonó.
2. **Verdadero Negativo:** No había fuego y la alarma estuvo en silencio.
3. **Falso Positivo (Falsa Alarma):** Se quemó una arepa y sonó la alarma para todo el edificio.
4. **Falso Negativo (Peligro):** ¡Había fuego y la alarma no sonó!

---
## 🔍 Las 3 Métricas en Palabras Sencillas:
* **Exactitud (*Accuracy*):** ¿Qué porcentaje total de casos acertó el modelo?
* **Precisión:** Cuando el modelo dice *"¡Peligro!"*, ¿qué tan seguro es que sea verdad?
* **Sensibilidad (*Recall*):** De todos los peligros reales, ¿cuántos logró detectar a tiempo?

```python
import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

url = "https://raw.githubusercontent.com/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/main/Data%20Science%20programming/08%20-%20Classification/data/heart_disease.csv"
df = pd.read_csv(url)

X = df[['age', 'trestbps', 'thalach', 'oldpeak']]
y = df['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

modelo = LogisticRegression()
modelo.fit(X_train, y_train)

y_pred = modelo.predict(X_test)
cm = confusion_matrix(y_test, y_pred)

print(f"✅ Pacientes sanos detectados correctamente: {cm[0,0]}")
print(f"⚠️ Falsas alarmas (sanos asustados):         {cm[0,1]}")
print(f"🚨 Enfermos no detectados (Peligro):         {cm[1,0]}")
print(f"🎯 Enfermos detectados a tiempo:             {cm[1,1]}")
```

---
##### 🎯 Reto Práctico para Dummies: Calculando la Puntuación del Modelo

**Pregunta:** Con los 4 números de la matriz de arriba:
* Total de aciertos = Pacientes sanos bien detectados + Enfermos detectados a tiempo.
* Total de pacientes evaluados = Suma de los 4 cuadrantes.
* ¿Cuál es el porcentaje de exactitud (*Accuracy*) del modelo?

```python
# =========================================================================
# TU SOLUCIÓN: Reto Dummies 3 - Calculando la Exactitud
# =========================================================================

# aciertos = cm[0,0] + cm[1,1]
# total = cm.sum()
# exactitud_porcentaje = (aciertos / total) * 100
# print(...)
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución explicada...</b></summary>

```python
aciertos = cm[0,0] + cm[1,1]
total = cm.sum()
exactitud = (aciertos / total) * 100

print(f"🎉 Total de aciertos: {aciertos} de {total} pacientes")
print(f"📈 Exactitud global del modelo: {exactitud:.2f}%")
```
</details>

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Guía Práctica e Intuitiva</i>
  </p>
</div>
