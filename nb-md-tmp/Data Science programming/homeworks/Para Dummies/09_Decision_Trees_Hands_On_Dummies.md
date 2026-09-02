# 09_Decision_Trees_Hands_On_Dummies

<table style="width: 100%; border-collapse: collapse; border: none; background: #fffbeb; border-left: 6px solid #f59e0b; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #78350f; font-size: 2em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        💡 Árboles y Bosques de Decisión (Taller Guiado)
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
        💡 Taller Dummies • Módulo 09
      </span><br>
      <span style="color: #78350f; font-size: 0.85em;">Docente: Santiago A. Zúñiga M.</span><br>
      <a href="mailto:gestorvirtualcienciadatos@ustatunja.edu.co" style="color: #b45309; font-size: 0.8em; text-decoration: none; font-weight: 500;">gestorvirtualcienciadatos@ustatunja.edu.co</a>
    </td>
  </tr>
</table>

<div align="center" style="margin-top: 15px; margin-bottom: 15px;">
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/homeworks/Para%20Dummies/09_Decision_Trees_Hands_On_Dummies.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## 🎯 Tu Misión de Hoy: Entrenar a un Asistente Inteligente 🤖

Hoy vas a construir un sistema inteligente para predecir si un paciente tiene riesgo cardiaco usando:
1. **Paso 1:** Un **Árbol de Decisión Simple** (fácil de entender y dibujar).
2. **Paso 2:** Un **Bosque Aleatorio (Random Forest)** (una junta de 50 médicos que votan juntos).
3. **Paso 3:** Ver qué variables son las más importantes para tomar la decisión.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os, urllib.request
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.ensemble import RandomForestClassifier

def load_dataset(filename, module_folder="09 - Decision Trees"):
    local_path = os.path.join(os.getcwd(), "data", filename)
    if os.path.exists(local_path):
        return local_path
    
    parent_path = os.path.join(os.getcwd(), "..", module_folder, "data", filename)
    if os.path.exists(parent_path):
        return parent_path

    raw_url = f"https://raw.githubusercontent.com/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/main/Data%20Science%20programming/{module_folder.replace(' ', '%20')}/data/{filename}"
    os.makedirs("data", exist_ok=True)
    target_path = os.path.join("data", filename)
    if not os.path.exists(target_path):
        urllib.request.urlretrieve(raw_url, target_path)
    return target_path

print("🚀 ¡Entorno listo para el Taller de Dummies 09!")
```

---
### 📌 Paso 1: Carga los datos de pacientes cardiacos

```python
file_heart = load_dataset('heart_disease.csv', '08 - Classification')
df = pd.read_csv(file_heart)

# Elegimos 3 variables muy claras:
# 1. 'age': Edad del paciente
# 2. 'chol': Nivel de colesterol
# 3. 'thalach': Ritmo cardiaco máximo
X = df[['age', 'chol', 'thalach']]
y = df['target'] # 0: Sano, 1: Riesgo Cardiaco

display(X.head())
```

---
### 📌 Paso 2: Entrena un Árbol Simple y Dibújalo

```python
# =========================================================================
# TU SOLUCIÓN: Paso 2 - Árbol Simple de 2 Niveles
# =========================================================================

# 1. Crear el árbol
# arbol_simple = DecisionTreeClassifier(max_depth=2, random_state=42)
# arbol_simple.fit(X, y)

# 2. Dibujarlo
# plt.figure(figsize=(10, 5))
# plot_tree(arbol_simple, feature_names=['Edad', 'Colesterol', 'Ritmo_Maximo'], class_names=['Sano', 'Riesgo'], filled=True)
# plt.show()
```

---
### 📌 Paso 3: Entrena una Junta de Médicos (Random Forest)

```python
# =========================================================================
# TU SOLUCIÓN: Paso 3 - Junta de 50 Médicos
# =========================================================================

# bosque_medico = RandomForestClassifier(n_estimators=50, random_state=42)
# bosque_medico.fit(X, y)

# print(f"Exactitud del Bosque: {bosque_medico.score(X, y)*100:.2f}%")
```

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Guía Práctica e Intuitiva</i>
  </p>
</div>
