# 02_KMeans_Clustering_Dummies

<table style="width: 100%; border-collapse: collapse; border: none; background: #fffbeb; border-left: 6px solid #f59e0b; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #78350f; font-size: 2em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        💡 02. K-Means Para Dummies: Los Capitanes de Equipo en el Recreo 💡
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
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/10%20-%20Clustering/Para%20Dummies/02_KMeans_Clustering_Dummies.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Abrir en Google Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## La Analogía de los Capitanes de Equipo en el Recreo ⚽

Imagina que 30 estudiantes quieren jugar fútbol y necesitamos formar 3 equipos ($k=3$):

1. **Elegir 3 Capitanes (Centroides Iniciales):** El profesor escoge a 3 estudiantes y los ubica en distintos puntos del campo.
2. **Cada uno corre a su Capitán (Paso de Asignación):** Cada estudiante camina hacia el capitán que le queda más cerca.
3. **Los Capitanes se mueven al centro (Paso de Actualización):** Cada capitán se mueve al centro exacto de su nuevo grupo.
4. **Repetir hasta que nadie cambie de equipo:** ¡Equipos listos y perfectamente equilibrados!

**¿Qué es K-Means++?** Una regla inteligente para que los capitanes iniciales no arranquen pegados unos a otros.

```python
from sklearn.cluster import KMeans
import numpy as np
import pandas as pd

# Posición (X, Y) de 9 personas en un parque
personas_parque = np.array([
    [10, 10], [12, 11], [11, 13],  # Grupo de amigos 1
    [50, 50], [52, 51], [51, 53],  # Grupo de amigos 2
    [90, 90], [92, 91], [91, 93]   # Grupo de amigos 3
])

# Ajustamos K-Means pidiendo 3 capitanes
modelo_partido = KMeans(n_clusters=3, random_state=42)
equipos = modelo_partido.fit_predict(personas_parque)

print("Equipo asignado a cada persona:", equipos)
print("Ubicación final de los 3 capitanes (centroides):\n", modelo_partido.cluster_centers_)
```

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos (Edición Conceptual Para Dummies)</i>
  </p>
</div>
