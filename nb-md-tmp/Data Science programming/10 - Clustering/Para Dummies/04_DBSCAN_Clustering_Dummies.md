# 04_DBSCAN_Clustering_Dummies

<table style="width: 100%; border-collapse: collapse; border: none; background: #fffbeb; border-left: 6px solid #f59e0b; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #78350f; font-size: 2em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        💡 04. DBSCAN Para Dummies: La Fiesta y los Grupos de Amigos 💡
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
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/10%20-%20Clustering/Para%20Dummies/04_DBSCAN_Clustering_Dummies.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Abrir en Google Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## La Analogía de la Fiesta de Cumpleaños 🎉

En una fiesta grande, los invitados no forman círculos perfectos:

* **Los Líderes de Grupo (*Core Points*):** Están bailando en la pista rodeados de al menos 4 o 5 amigos muy cerca.
* **Los Amigos de la Orilla (*Border Points*):** Están conversando en el borde del grupo pero pertenecen a la conversación.
* **Los Lobos Solitarios (*Ruido / Outliers con etiqueta `-1`*):** Están parados solos junto a la puerta sin hablar con nadie.

**DBSCAN** descubre grupos por densidad de personas sin importar la forma que tengan (filas, círculos, herraduras) y detecta automáticamente a los solitarios.

```python
from sklearn.cluster import DBSCAN
import numpy as np

# Invitados a la fiesta: Grupo apretado + 1 persona solitaria en la coordenada [100, 100]
invitados = np.array([
    [10, 10], [11, 10], [10, 11], [11, 11],  # Grupo bailando en la pista
    [100, 100]                               # Persona solitaria en la entrada
])

detector_fiesta = DBSCAN(eps=3.0, min_samples=3)
etiquetas_fiesta = detector_fiesta.fit_predict(invitados)

print("Etiquetas de la fiesta:", etiquetas_fiesta)
print("💡 El número -1 identifica a la persona solitaria (ruido).")
```

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos (Edición Conceptual Para Dummies)</i>
  </p>
</div>
