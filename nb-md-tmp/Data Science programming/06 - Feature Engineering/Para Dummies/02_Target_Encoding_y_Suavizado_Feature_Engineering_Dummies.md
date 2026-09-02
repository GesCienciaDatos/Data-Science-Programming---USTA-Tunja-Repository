# 02_Target_Encoding_y_Suavizado_Feature_Engineering_Dummies

<table style="width: 100%; border-collapse: collapse; border: none; background: #fffbeb; border-left: 6px solid #f59e0b; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #78350f; font-size: 2em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        💡 02. Target Encoding y Suavizado
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
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/06%20-%20Feature%20Engineering/Para%20Dummies/02_Target_Encoding_y_Suavizado_Feature_Engineering_Dummies.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## El Problema del One-Hot Encoding con Muchas Ciudades 💥

Si tienes una columna con `1,100 municipios de Colombia`, el One-Hot Encoding crearía **1,100 columnas nuevas llenas de ceros**, volviendo tu tabla gigantesca y lenta.

### 💡 La Solución: Target Encoding
En lugar de crear 1,100 columnas, reemplazas el nombre de cada municipio por el **promedio histórico de lo que queremos predecir** (por ejemplo, el precio promedio de las casas en ese municipio).

- Si en *Chía* el precio promedio de una casa es `\\$450M`, reemplazas `"Chía"` por `450`.
- Si en *Tunja* el precio promedio es `\\$220M`, reemplazas `"Tunja"` por `220`.

> ⚠️ **El Peligro del Sobreajuste (Overfitting):** Si en un pueblo remoto solo vendiste 1 casa por `\\$1,000M` porque era una mansión única, no quieres que el modelo asuma que *todas* las casas de ese pueblo valen mil millones. Para eso aplicamos **Suavizado (*Smoothing*)**, mezclando el promedio del pueblo con el promedio nacional.

```python
import pandas as pd

df_inmuebles = pd.DataFrame({
    "Ciudad": ["Tunja", "Bogotá", "Tunja", "Medellín", "Bogotá", "Tunja", "Medellín"],
    "Precio_Millones": [210, 450, 230, 380, 520, 200, 400]
})

print("Inmuebles Originales:")
display(df_inmuebles)

# Calculamos el Target Encoding directo (media de precio por ciudad):
encoding_media = df_inmuebles.groupby("Ciudad")["Precio_Millones"].transform("mean")
df_inmuebles["Ciudad_Target_Encoded"] = encoding_media.round(1)

print("\nInmuebles con Target Encoding Aplicado:")
display(df_inmuebles)
```

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos (Edición Para No Ingenieros)</i>
  </p>
</div>
