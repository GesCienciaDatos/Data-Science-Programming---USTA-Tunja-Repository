# 02_Importacion_y_Exportacion_Pandas_Dummies

<table style="width: 100%; border-collapse: collapse; border: none; background: #fffbeb; border-left: 6px solid #f59e0b; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #78350f; font-size: 2em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        💡 02. Importación y Exportación de Datos
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
        💡 Para Dummies • Módulo 03
      </span><br>
      <span style="color: #78350f; font-size: 0.85em;">Docente: Santiago A. Zúñiga M.</span><br>
      <a href="mailto:gestorvirtualcienciadatos@ustatunja.edu.co" style="color: #b45309; font-size: 0.8em; text-decoration: none; font-weight: 500;">gestorvirtualcienciadatos@ustatunja.edu.co</a>
    </td>
  </tr>
</table>

<div align="center" style="margin-top: 15px; margin-bottom: 15px;">
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/03%20-%20Pandas/Para%20Dummies/02_Importacion_y_Exportacion_Pandas_Dummies.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## ¿Cómo traer datos a Pandas? 📂

En el 99% de los proyectos de Ciencia de Datos no creas los datos a mano; los lees desde un archivo CSV o Excel que descargaste de una base de datos o sistema empresarial:
- **Leer CSV:** `pd.read_csv("ruta/archivo.csv")`
- **Guardar CSV:** `df.to_csv("ruta/archivo_limpio.csv", index=False)`
- **Leer Excel:** `pd.read_excel("ruta/archivo.xlsx")`

```python
import pandas as pd
import os

# Creamos un archivo CSV de demostración temporal:
os.makedirs("data", exist_ok=True)
df_ejemplo = pd.DataFrame({
    "ID": [101, 102, 103],
    "Nombre": ["Ana", "Bernardo", "Clara"],
    "Sueldo": [3200000, 4100000, 2900000]
})

# Guardamos a disco:
df_ejemplo.to_csv("data/empleados_demo.csv", index=False)
print("✅ Archivo CSV guardado en 'data/empleados_demo.csv'")

# Lo leemos de regreso con read_csv:
df_leido = pd.read_csv("data/empleados_demo.csv")
display(df_leido)
```

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos (Edición Para No Ingenieros)</i>
  </p>
</div>
