# 08_Classification_Hands_On_Dummies

<table style="width: 100%; border-collapse: collapse; border: none; background: #fffbeb; border-left: 6px solid #f59e0b; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #78350f; font-size: 2em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        💡 Taller Práctico 08: Clasificación para No Ingenieros
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
        💡 Taller Dummies • Módulo 08
      </span><br>
      <span style="color: #78350f; font-size: 0.85em;">Docente: Santiago A. Zúñiga M.</span><br>
      <a href="mailto:gestorvirtualcienciadatos@ustatunja.edu.co" style="color: #b45309; font-size: 0.8em; text-decoration: none; font-weight: 500;">gestorvirtualcienciadatos@ustatunja.edu.co</a>
    </td>
  </tr>
</table>

<div align="center" style="margin-top: 15px; margin-bottom: 15px;">
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/homeworks/Para%20Dummies/08_Classification_Hands_On_Dummies.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## 🎯 Taller Integrador: ¡Prediciendo Decisiones como un Científico de Datos! 🚀

En este taller resolverás paso a paso un problema real de clasificación médica para predecir si una persona tiene riesgo cardiaco.

---
### 1. Carga de Datos y Primer Vistazo 👀

```python
import pandas as pd
import numpy as np

# Cargar dataset de pacientes
url = "https://raw.githubusercontent.com/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/main/Data%20Science%20programming/08%20-%20Classification/data/heart_disease.csv"
df_pacientes = pd.read_csv(url)

print("Primeras 5 filas de pacientes:")
display(df_pacientes.head())
```

---
### 2. Entrenando la Balanza de Decisiones (Regresión Logística) ⚖️

**Paso 1:** Selecciona las variables de salud: `age` (edad), `trestbps` (presión arterial), `thalach` (frecuencia cardiaca) y la variable objetivo `target` (0 = Sano, 1 = Riesgo).

```python
### TU CÓDIGO AQUÍ: Define X e y, y ajusta un modelo LogisticRegression() ###
```

---
### 3. Consultando al Modelo para 3 Pacientes Nuevos 🩺

**Paso 2:** Prueba el modelo con estos 3 pacientes y calcula su probabilidad de riesgo (%):
1. **Paciente 1:** Edad 35, Presión 118, Frecuencia 170
2. **Paciente 2:** Edad 55, Presión 138, Frecuencia 130
3. **Paciente 3:** Edad 70, Presión 160, Frecuencia 100

```python
### TU CÓDIGO AQUÍ: Calcula las probabilidades de los 3 pacientes con modelo.predict_proba() ###
```

---
### 4. Evaluando los Aciertos y Falsas Alarmas (Matriz de Confusión) 📊

**Paso 3:** Con los datos de prueba, calcula la matriz de confusión e indica cuántos pacientes enfermos logró detectar el modelo a tiempo.

```python
### TU CÓDIGO AQUÍ: Divide en train_test_split, predice y muestra confusion_matrix ###
```

---
### 5. Consultando a los Vecinos Más Parecidos ($k$-NN) 👥

**Paso 4:** Entrena un modelo `KNeighborsClassifier(n_neighbors=5)` usando `StandardScaler` y compara su veredicto para el Paciente 3 frente a la Regresión Logística.

```python
### TU CÓDIGO AQUÍ: Crea un make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=5)) y predice el Paciente 3 ###
```

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos (Edición Para No Ingenieros)</i>
  </p>
</div>
