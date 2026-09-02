# 01_Variables_Categoricas_Feature_Engineering_Dummies

<table style="width: 100%; border-collapse: collapse; border: none; background: #fffbeb; border-left: 6px solid #f59e0b; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #78350f; font-size: 2em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        💡 01. Manejo de Variables Categóricas
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
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/06%20-%20Feature%20Engineering/Para%20Dummies/01_Variables_Categoricas_Feature_Engineering_Dummies.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## ¿Por qué las computadoras no entienden palabras directamente? 🏷️

Los modelos matemáticos solo pueden sumar, restar y multiplicar números. No pueden multiplicar `"Rojo"` por `3.5`. Debemos traducir cada categoría a números de manera inteligente.

---
## Los 3 Enfoques Clásicos para Categorías:

| Enfoque | 💡 Analogía Cotidiana | ¿Cuándo usarlo? | Ejemplo |
|---|---|---|---|
| **1. Eliminar Columna** | Tirar la toalla: si no sé qué hacer con el texto, lo borro. | Casi nunca (pierdes información valiosa). | Borrar la columna "Color". |
| **2. Ordinal Encoding** | La talla de ropa o podio olímpico: hay un orden natural claro (Oro=1, Plata=2, Bronce=3). | Cuando las categorías tienen **jerarquía u orden implícito**. | Tallas: `S=1, M=2, L=3, XL=4`. |
| **3. One-Hot Encoding** | Formulario de casillas Sí/No: creas una columna por cada opción disponible. | Cuando **no hay orden** entre las categorías (colores, ciudades, marcas). | `Es_Tunja: [1, 0]`, `Es_Bogota: [0, 1]`. |

```python
import pandas as pd
from sklearn.preprocessing import OrdinalEncoder, OneHotEncoder

df_ropa = pd.DataFrame({
    "Prenda_ID": [1, 2, 3, 4],
    "Talla": ["S", "L", "M", "S"],           # Tiene orden natural (Ordinal)
    "Color": ["Rojo", "Azul", "Verde", "Rojo"] # No tiene orden (One-Hot)
})

print("Dataset Original:")
display(df_ropa)

# 1. Ordinal Encoding para 'Talla':
orden_tallas = [["S", "M", "L"]]
oe = OrdinalEncoder(categories=orden_tallas)
df_ropa["Talla_Num"] = oe.fit_transform(df_ropa[["Talla"]])

# 2. One-Hot Encoding para 'Color' usando get_dummies de Pandas (Súper fácil):
df_dummies = pd.get_dummies(df_ropa["Color"], prefix="Color", dtype=int)

df_final = pd.concat([df_ropa[["Prenda_ID", "Talla_Num"]], df_dummies], axis=1)
print("\nDataset Transformado Listo para Machine Learning:")
display(df_final)
```

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos (Edición Para No Ingenieros)</i>
  </p>
</div>
