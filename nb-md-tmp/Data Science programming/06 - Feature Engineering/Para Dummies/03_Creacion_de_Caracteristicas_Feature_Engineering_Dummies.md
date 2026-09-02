# 03_Creacion_de_Caracteristicas_Feature_Engineering_Dummies

<table style="width: 100%; border-collapse: collapse; border: none; background: #fffbeb; border-left: 6px solid #f59e0b; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #78350f; font-size: 2em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        💡 03. Creación de Características Derivadas
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
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/06%20-%20Feature%20Engineering/Para%20Dummies/03_Creacion_de_Caracteristicas_Feature_Engineering_Dummies.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## ¿Cómo inventar variables que hagan brillar a tu modelo? ✨

### 💡 Las 3 Recetas Más Usadas:
1. **Ratios (Divisiones de Sentido Común):**
   - $\text{Densidad Poblacional} = rac{\text{Habitantes}}{\text{Área en } km^2}$
   - $\text{Carga Financiera} = rac{\text{Cuota Mensual de Deuda}}{\text{Ingreso Total}}$
2. **Interacciones (Multiplicaciones):**
   - $\text{Volumen} = \text{Largo} \times \text{Ancho} \times \text{Alto}$
3. **Transformación Logarítmica (`np.log1p`):**
   - Si los salarios van desde `\\$1M` hasta `\\$5,000M` (distribución súper sesgada con cola larga), el logaritmo comprime la escala y hace que los datos parezcan una campana bonita y balanceada.

```python
import pandas as pd
import numpy as np

df_creditos = pd.DataFrame({
    "Solicitante": ["Andrés", "Beatriz", "Camilo"],
    "Ingreso_Mensual": [3000000, 8000000, 2500000],
    "Deuda_Actual": [1200000, 1600000, 2000000]
})

# 1. Creamos el ratio de endeudamiento (DTI - Debt to Income):
df_creditos["Ratio_Endeudamiento"] = df_creditos["Deuda_Actual"] / df_creditos["Ingreso_Mensual"]

# 2. Transformación logarítmica del ingreso:
df_creditos["Log_Ingreso"] = np.log(df_creditos["Ingreso_Mensual"]).round(2)

display(df_creditos)
```

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos (Edición Para No Ingenieros)</i>
  </p>
</div>
