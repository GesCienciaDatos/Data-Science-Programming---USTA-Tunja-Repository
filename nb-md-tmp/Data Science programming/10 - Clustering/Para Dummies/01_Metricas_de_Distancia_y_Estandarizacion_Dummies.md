# 01_Metricas_de_Distancia_y_Estandarizacion_Dummies

<table style="width: 100%; border-collapse: collapse; border: none; background: #fffbeb; border-left: 6px solid #f59e0b; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #78350f; font-size: 2em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        💡 01. Métricas de Distancia y Estandarización Para Dummies: La Balanza Justa 💡
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
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/10%20-%20Clustering/Para%20Dummies/01_Metricas_de_Distancia_y_Estandarizacion_Dummies.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Abrir en Google Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## ¿Cómo Sabe la Computadora Qué Tan Cerca Están Dos Cosas? 📏

Imagina dos ciudades en un mapa:
* **Distancia Euclidiana (En línea recta como un pájaro):** Mides con una regla directa entre los dos puntos.
* **Distancia Manhattan (En taxi por las calles):** Tienes que avanzar por cuadras horizontales y verticales obligatorias.
* **Distancia de Coseno (El ángulo de la brújula):** No le importa si un viaje fue de 1 km o de 100 km; solo mira si fuiste en la misma dirección.

---
## La Analogía de la Balanza Justa: ¿Por Qué Hay que Estandarizar? ⚖️

Imagina que comparas a dos personas usando dos medidas:
1. Su estatura en metros: $1.70$ m vs $1.75$ m (diferencia de **$0.05$**).
2. Su salario en pesos: $\$2,000,000$ vs $\$2,500,000$ (diferencia de **$\$500,000$**).

Si sumas esas diferencias directamente, el salario aplastará a la estatura por completo. **`StandardScaler` es una balanza justa:** convierte todas las columnas a la misma escala de puntuación ($z$) para que todas tengan voz y voto en la agrupación.

```python
from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd

datos_ejemplo = np.array([
    [1.70, 2_000_000],
    [1.75, 2_100_000],
    [1.90, 8_000_000]
])

scaler = StandardScaler()
datos_en_balanza_justa = scaler.fit_transform(datos_ejemplo)

print("Datos originales (Estatura en m, Salario en COP):\n", datos_ejemplo)
print("\nDatos tras pasar por la Balanza Justa (StandardScaler):\n", datos_en_balanza_justa.round(2))
```

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos (Edición Conceptual Para Dummies)</i>
  </p>
</div>
