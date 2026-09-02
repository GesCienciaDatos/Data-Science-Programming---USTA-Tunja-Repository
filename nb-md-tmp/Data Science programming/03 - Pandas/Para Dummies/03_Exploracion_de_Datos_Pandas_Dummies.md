# 03_Exploracion_de_Datos_Pandas_Dummies

<table style="width: 100%; border-collapse: collapse; border: none; background: #fffbeb; border-left: 6px solid #f59e0b; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #78350f; font-size: 2em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        💡 03. Exploración Inicial de Datos
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
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/03%20-%20Pandas/Para%20Dummies/03_Exploracion_de_Datos_Pandas_Dummies.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## El Kit Médico de Primeros Auxilios de Pandas 🩺

Cuando te entregan un conjunto de datos nuevo, necesitas responder rápidamente 4 preguntas:
1. ¿Cuántas filas y columnas tiene? $ightarrow$ `df.shape`
2. ¿Cómo se ven las primeras filas? $ightarrow$ `df.head()`
3. ¿Faltan datos y qué tipos de datos son? $ightarrow$ `df.info()`
4. ¿Cuáles son los números clave (media, min, max)? $ightarrow$ `df.describe()`

```python
import pandas as pd

# Creemos un dataset realista de ventas para explorar:
df_ventas = pd.DataFrame({
    "Transaccion_ID": range(1, 11),
    "Vendedor": ["Carlos", "María", "Carlos", "Pedro", "María", "Carlos", "Ana", "Pedro", "Ana", "María"],
    "Monto": [150000, 320000, 210000, 89000, 450000, 190000, 620000, 110000, 340000, 280000],
    "Calificacion_Servicio": [5, 4, 5, 3, 5, 4, 5, 2, 4, 5]
})

print("1. Forma del DataFrame (Filas, Columnas):", df_ventas.shape)
print("\n2. Primeras 5 filas (head):")
display(df_ventas.head())

print("\n3. Resumen estadístico (describe):")
display(df_ventas.describe())

print("\n4. Conteo de transacciones por vendedor:")
display(df_ventas["Vendedor"].value_counts())
```

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos (Edición Para No Ingenieros)</i>
  </p>
</div>
