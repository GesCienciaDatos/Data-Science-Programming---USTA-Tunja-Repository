# 05_Evaluacion_Seleccion_K_y_Benchmark_Dummies

<table style="width: 100%; border-collapse: collapse; border: none; background: #fffbeb; border-left: 6px solid #f59e0b; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #78350f; font-size: 2em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        💡 05. Evaluación y Selección de K Para Dummies: El Codo y la Felicidad 💡
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
        💡 Para Dummies • Módulo 10
      </span><br>
      <span style="color: #78350f; font-size: 0.85em;">Docente: Santiago A. Zúñiga M.</span><br>
      <a href="mailto:gestorvirtualcienciadatos@ustatunja.edu.co" style="color: #b45309; font-size: 0.8em; text-decoration: none; font-weight: 500;">gestorvirtualcienciadatos@ustatunja.edu.co</a>
    </td>
  </tr>
</table>

<div align="center" style="margin-top: 15px; margin-bottom: 15px;">
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/10%20-%20Clustering/Para%20Dummies/05_Evaluacion_Seleccion_K_y_Benchmark_Dummies.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Abrir en Google Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## ¿Cómo Saber Cuántos Grupos Armar? El Método del Codo 🦾

Imagina que tienes el brazo completamente estirado y lo vas doblando lentamente:

* Probar con 1 solo grupo es muy malo (inercia gigante, esfuerzo máximo).
* Con 2 y 3 grupos la mejora es gigantesca.
* Después de 4 grupos, agregar más grupos casi no aporta nada nuevo (el brazo ya dobló en el codo).
* **El número perfecto es exactamente la punta del codo.**

---
## El Coeficiente de Silueta: El Termómetro de Felicidad Escolar 😊

El coeficiente de silueta mide qué tan contenta está cada persona en su grupo:
* **Cercano a $+1.0$:** ¡Felicidad total! La persona está muy cerca de sus amigos de equipo y lejana de los otros equipos.
* **Cercano a $0.0$:** Indiferencia (está en la frontera entre dos equipos).
* **Negativo ($-1.0$):** Incomodidad (quedó en el equipo equivocado y está más cerca del equipo rival).

```python
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import numpy as np

datos_ejemplo = np.array([
    [1, 1], [1, 2], [2, 1],  # Montón 1
    [8, 8], [8, 9], [9, 8]   # Montón 2
])

for k in [2, 3]:
    km = KMeans(n_clusters=k, random_state=42).fit(datos_ejemplo)
    puntaje_felicidad = silhouette_score(datos_ejemplo, km.labels_)
    print(f"Puntaje de Silueta con k={k} grupos: {puntaje_felicidad:.4f} (Más cercano a +1 es mejor)")
```

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos (Edición Conceptual Para Dummies)</i>
  </p>
</div>
