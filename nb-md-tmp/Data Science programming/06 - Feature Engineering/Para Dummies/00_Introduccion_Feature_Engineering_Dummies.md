# 00_Introduccion_Feature_Engineering_Dummies

<table style="width: 100%; border-collapse: collapse; border: none; background: #fffbeb; border-left: 6px solid #f59e0b; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #78350f; font-size: 2em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        💡 00. Introducción a la Ingeniería de Características
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
        💡 Para Dummies • Módulo 06
      </span><br>
      <span style="color: #78350f; font-size: 0.85em;">Docente: Santiago A. Zúñiga M.</span><br>
      <a href="mailto:gestorvirtualcienciadatos@ustatunja.edu.co" style="color: #b45309; font-size: 0.8em; text-decoration: none; font-weight: 500;">gestorvirtualcienciadatos@ustatunja.edu.co</a>
    </td>
  </tr>
</table>

<div align="center" style="margin-top: 15px; margin-bottom: 15px;">
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/06%20-%20Feature%20Engineering/Para%20Dummies/00_Introduccion_Feature_Engineering_Dummies.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## ¿Qué es la Ingeniería de Características (*Feature Engineering*)? 🛠️

Los algoritmos de Machine Learning no son adivinos mágicos: son simples calculadoras estadísticas que buscan patrones matemáticos. Si les entregas datos crudos sin preparar, tendrán muchas dificultades para aprender.

### 💡 La Analogía del Chef y los Ingredientes:
Si quieres preparar el mejor café del mundo:
- **Datos Crudos:** Entregarle al cliente un saco de granos verdes recién cosechados y una taza de agua fría.
- **Feature Engineering:** Tostar el grano en el punto exacto, molerlo con la finura adecuada, extraer la esencia a la temperatura correcta y servirlo con una pizca de canela.

---
### Los 5 Grandes Trucos de Feature Engineering:
1. **Convertir Texto/Categorías a Números:** One-Hot Encoding, Ordinal Encoding y Target Encoding.
2. **Crear Nuevos Indicadores (Ratios e Interacciones):** Por ejemplo, en lugar de darle al modelo solo el `precio` y los `metros_cuadrados`, crearle la variable `precio_por_metro_cuadrado`.
3. **Transformaciones Matemáticas:** Aplicar logaritmos para calmar datos extremadamente disparados.
4. **PCA (Reducción de Dimensiones):** Comprimir 20 variables correlacionadas en 3 súper-variables principales.
5. **Información Mutua (Mutual Information):** Medir matemáticamente qué variables aportan luz y cuáles son puro ruido inútil.

```python
import pandas as pd
import numpy as np
import sklearn

print("✅ Entorno de Feature Engineering listo.")
```

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos (Edición Para No Ingenieros)</i>
  </p>
</div>
