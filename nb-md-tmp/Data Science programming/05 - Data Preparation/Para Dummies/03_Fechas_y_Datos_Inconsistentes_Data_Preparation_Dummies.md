# 03_Fechas_y_Datos_Inconsistentes_Data_Preparation_Dummies

<table style="width: 100%; border-collapse: collapse; border: none; background: #fffbeb; border-left: 6px solid #f59e0b; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #78350f; font-size: 2em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        💡 03. Fechas y Limpieza Difusa (Fuzzy Matching)
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
        💡 Para Dummies • Módulo 05
      </span><br>
      <span style="color: #78350f; font-size: 0.85em;">Docente: Santiago A. Zúñiga M.</span><br>
      <a href="mailto:gestorvirtualcienciadatos@ustatunja.edu.co" style="color: #b45309; font-size: 0.8em; text-decoration: none; font-weight: 500;">gestorvirtualcienciadatos@ustatunja.edu.co</a>
    </td>
  </tr>
</table>

<div align="center" style="margin-top: 15px; margin-bottom: 15px;">
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/05%20-%20Data%20Preparation/Para%20Dummies/03_Fechas_y_Datos_Inconsistentes_Data_Preparation_Dummies.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## 1. Parseo de Fechas con `pd.to_datetime()` 📅

Una fecha almacenada como texto simple (`"2026-08-31"`) no te permite calcular fácilmente si es lunes, fin de semana o cuántos días pasaron entre dos eventos.
Al convertirla a formato DateTime real con Pandas, desbloqueas superpoderes de tiempo.

```python
import pandas as pd

df_ventas = pd.DataFrame({
    "Factura_ID": [1, 2, 3],
    "Fecha_Texto": ["2026-01-15", "2026-05-20", "2026-11-08"]
})

# Convertimos a DateTime real:
df_ventas["Fecha_Real"] = pd.to_datetime(df_ventas["Fecha_Texto"])

# Extraemos componentes al instante:
df_ventas["Anio"] = df_ventas["Fecha_Real"].dt.year
df_ventas["Mes_Nombre"] = df_ventas["Fecha_Real"].dt.month_name()
df_ventas["Dia_Semana"] = df_ventas["Fecha_Real"].dt.day_name()

display(df_ventas)
```

---
## 2. Coincidencia Difusa de Texto (*Fuzzy Matching*) 🔤

### 💡 La Analogía del Corrector del Celular:
Si un usuario escribe en un formulario `"Kolombia"`, `"colombia "` o `"COLOMBIA"`, el algoritmo de distancia de Levenshtein calcula qué tan cerca está de la palabra oficial `"Colombia"` (por ejemplo, 90% de similitud) y la unifica automáticamente.

```python
# Demostración conceptual de limpieza de categorías inconsistentes:
ciudades_sucias = ["Tunja", "tunja", "TUNJA ", "Duitama", "duitama ", "Sogamoso", "Sogamozo"]

# Estandarización base: minúsculas y sin espacios
ciudades_estandar = [c.strip().capitalize().replace("Sogamozo", "Sogamoso") for c in ciudades_sucias]

print("Ciudades Crudas:", ciudades_sucias)
print("Ciudades Unificadas:", ciudades_estandar)
print("Ciudades Únicas Reales:", set(ciudades_estandar))
```

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos (Edición Para No Ingenieros)</i>
  </p>
</div>
