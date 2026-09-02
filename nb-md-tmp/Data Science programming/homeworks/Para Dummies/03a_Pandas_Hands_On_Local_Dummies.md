# 03a_Pandas_Hands_On_Local_Dummies

<table style="width: 100%; border-collapse: collapse; border: none; background: #fffbeb; border-left: 6px solid #f59e0b; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #78350f; font-size: 2em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        💡 Taller Práctico 03a: Pandas Local para No Ingenieros
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
        💡 Taller Dummies • Módulo 03
      </span><br>
      <span style="color: #78350f; font-size: 0.85em;">Docente: Santiago A. Zúñiga M.</span><br>
      <a href="mailto:gestorvirtualcienciadatos@ustatunja.edu.co" style="color: #b45309; font-size: 0.8em; text-decoration: none; font-weight: 500;">gestorvirtualcienciadatos@ustatunja.edu.co</a>
    </td>
  </tr>
</table>

<div align="center" style="margin-top: 15px; margin-bottom: 15px;">
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/homeworks/Para%20Dummies/03a_Pandas_Hands_On_Local_Dummies.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## Taller 03a: Dominando DataFrames en Local 📊

Aprenderás a crear un DataFrame, consultar información y generar métricas ejecutivas de ventas.

```python
import pandas as pd

# Creación del DataFrame de un restaurante:
df_menu = pd.DataFrame({
    "Plato": ["Ajiaco Santafereño", "Bandeja Paisa", "Mote de Queso", "Sancocho Trifásico"],
    "Categoria": ["Sopas", "Platos Fuertes", "Sopas", "Sopas"],
    "Precio_COP": [28000, 35000, 22000, 30000],
    "Porciones_Vendidas": [45, 60, 25, 50]
})

# 1. Calculamos los ingresos generados por cada plato:
df_menu["Ingreso_Total_COP"] = df_menu["Precio_COP"] * df_menu["Porciones_Vendidas"]

display(df_menu)
print(f"\n💵 Ingreso Total del Día: ${df_menu['Ingreso_Total_COP'].sum():,.2f} COP")
```

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos (Edición Para No Ingenieros)</i>
  </p>
</div>
