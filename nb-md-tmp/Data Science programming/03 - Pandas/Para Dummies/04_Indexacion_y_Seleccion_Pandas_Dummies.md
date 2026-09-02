# 04_Indexacion_y_Seleccion_Pandas_Dummies

<table style="width: 100%; border-collapse: collapse; border: none; background: #fffbeb; border-left: 6px solid #f59e0b; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #78350f; font-size: 2em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        💡 04. Indexación y Selección: loc vs iloc
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
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/03%20-%20Pandas/Para%20Dummies/04_Indexacion_y_Seleccion_Pandas_Dummies.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## La Batalla Clásica: `iloc` vs `loc` ⚔️

Para no confundirte nunca jamás, memoriza esta regla sencilla:

| Selector | 💡 ¿Qué significa la 'i'? | ¿Cómo busca? | Ejemplo |
|---|---|---|---|
| **`iloc`** | **`i` = Integer (Posición numérica entera)** | Busca por número de fila y columna (0, 1, 2...). Como las coordenadas numéricas de un mapa. | `df.iloc[0:5, 1:3]` |
| **`loc`** | **`l` = Label (Etiqueta o Nombre)** | Busca por el **nombre de la columna** o por condiciones lógicas (`True/False`). | `df.loc[df['Edad'] >= 18, ['Nombre', 'Ciudad']]` |

```python
import pandas as pd

df = pd.DataFrame({
    "Nombre": ["Laura", "Camilo", "Daniela", "Esteban"],
    "Edad": [23, 31, 19, 45],
    "Ciudad": ["Tunja", "Bogotá", "Tunja", "Medellín"],
    "Salario": [2500000, 4200000, 1800000, 5600000]
}, index=["usr_01", "usr_02", "usr_03", "usr_04"])

display(df)

print("\n1. Con iloc (Fila 0, Columnas 0 y 1 por posición numérica):")
display(df.iloc[0, 0:2])

print("\n2. Con loc (Fila con etiqueta 'usr_02', columnas por nombre):")
display(df.loc["usr_02", ["Nombre", "Salario"]])

print("\n3. Filtrado condicional con loc (Personas de Tunja):")
display(df.loc[df["Ciudad"] == "Tunja"])
```

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos (Edición Para No Ingenieros)</i>
  </p>
</div>
