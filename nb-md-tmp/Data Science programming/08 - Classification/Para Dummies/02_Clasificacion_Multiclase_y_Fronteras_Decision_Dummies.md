# 02_Clasificacion_Multiclase_y_Fronteras_Decision_Dummies

<table style="width: 100%; border-collapse: collapse; border: none; background: #fffbeb; border-left: 6px solid #f59e0b; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #78350f; font-size: 2em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        💡 Clasificación Multiclase y Fronteras [Edición Dummies] 🎯
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
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/08%20-%20Classification/Para%20Dummies/02_Clasificacion_Multiclase_y_Fronteras_Decision_Dummies.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## 🌟 La Analogía de las Cercas y Parcelas de Flores 🌸

Imagina que tienes un mapa con 3 tipos de flores (Setosa, Versicolor, Virginica):

<div align="center">
  <img src="images/iris_yong_cui_towarddatascience.png" width="600" alt="Especies de Iris" style="border-radius:8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); margin:10px 0;"/>
</div>

* El modelo actúa como un **agrimensor** que dibuja cercas en el mapa dividiendo los terrenos.
* Cuando encuentras una flor nueva, simplemente miras en qué parcela del mapa cayó para saber qué especie es.

```python
import pandas as pd
from sklearn.linear_model import LogisticRegression

url = "https://raw.githubusercontent.com/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/main/Data%20Science%20programming/08%20-%20Classification/data/iris.csv"
df = pd.read_csv(url)

X = df[['petal_length', 'petal_width']]
y = df['species']

modelo = LogisticRegression(multi_class='multinomial')
modelo.fit(X, y)

print("🌸 ¡Modelo multiclase entrenado para clasificar las 3 flores!")
```

## 🌼 ¿Qué flor encontramos en el jardín?

```python
flor_nueva = [[4.8, 1.6]]  # Pétalo de 4.8 cm de largo y 1.6 cm de ancho
prediccion = modelo.predict(flor_nueva)[0]
print(f"Veredicto del modelo: 👉 {prediccion.upper()} 👈")
```

---
##### 🎯 Reto Práctico para Dummies: El Botánico en el Invernadero

**Situación:** Encuentras una flor muy pequeña:
* Longitud del pétalo = 1.4 cm
* Ancho del pétalo = 0.2 cm

¿A cuál de las 3 parcelas de flores pertenece?

```python
# =========================================================================
# TU SOLUCIÓN: Reto Dummies 2 - Clasificando la flor pequeña
# =========================================================================

# flor_pequena = [[1.4, 0.2]]
# resultado = modelo.predict(flor_pequena)[0]
# print(...)
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución explicada...</b></summary>

```python
flor_pequena = [[1.4, 0.2]]
resultado = modelo.predict(flor_pequena)[0]
probs = modelo.predict_proba(flor_pequena)[0]

print(f"🌺 La flor pequeña pertenece a la especie: 👉 {resultado.upper()} 👈")
for esp, p in zip(modelo.classes_, probs):
    print(f" - Seguridad {esp}: {p*100:.1f}%")
```
</details>

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Guía Práctica e Intuitiva</i>
  </p>
</div>
