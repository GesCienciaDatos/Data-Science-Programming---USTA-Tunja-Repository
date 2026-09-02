# 01_Valores_Faltantes_Data_Preparation_Dummies

<table style="width: 100%; border-collapse: collapse; border: none; background: #fffbeb; border-left: 6px solid #f59e0b; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #78350f; font-size: 2em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        💡 01. Tratamiento de Valores Faltantes (NaN)
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
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/05%20-%20Data%20Preparation/Para%20Dummies/01_Valores_Faltantes_Data_Preparation_Dummies.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## ¿Por qué faltan datos y qué hacemos con ellos? 🧩

### 💡 Las 3 Razones por las que un Dato no Está:
1. **Falta Totalmente al Azar (MCAR):** Se cayó la conexión a internet por 1 segundo mientras el sensor enviaba el reporte. No hay un patrón detrás.
2. **Falta por Relación con Otra Variable (MAR):** En una encuesta, los hombres jóvenes casi nunca llenan la casilla de *"peso corporal"*, pero sí llenan su edad y género.
3. **Falta por la Naturaleza del Dato Mismo (MNAR):** Las personas con ingresos extremadamente altos omiten responder *"¿Cuánto dinero gana al mes?"* por temas de privacidad.

---
## ¿Eliminar o Imputar? ⚔️

| Estrategia | 🗣️ ¿En qué consiste? | ¿Cuándo conviene? |
|---|---|---|
| **Eliminar Filas (`dropna`)** | Botar a la basura el registro que tenga datos vacíos. | Cuando faltan muy poquitos datos (<2%) y tienes millones de registros. |
| **Imputar por Media / Mediana** | Rellenar las casillas vacías con el valor típico de la población. | En variables numéricas estándar (usa la mediana si hay datos extremos). |
| **Imputar por Moda** | Rellenar con la categoría más frecuente. | En variables de texto / categóricas (ej. estado civil más común). |
| **Imputación KNN (Vecinos Cercanos)** | Buscar a las 5 personas más parecidas en todo lo demás y ponerle su promedio. | Para imputación de alta precisión técnica. |

```python
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer, KNNImputer

# Dataset con valores nulos simulados:
df_pacientes = pd.DataFrame({
    "Paciente": ["Carlos", "María", "Pedro", "Lucía", "Andrés"],
    "Edad": [25, np.nan, 45, 29, np.nan],
    "Presion_Arterial": [120, 115, np.nan, 125, 118],
    "Fumador": ["No", "No", "Sí", np.nan, "No"]
})

print("Dataset Original con Nulos (NaN):")
display(df_pacientes)

print("\n1. Conteo de Nulos por Columna:")
print(df_pacientes.isna().sum())
```

---
### Imputando Valores Numéricos con la Mediana 🩹

```python
# Copiamos los datos para no alterar el original:
df_limpio = df_pacientes.copy()

# Rellenamos Edad con la mediana de los que sí reportaron edad:
mediana_edad = df_limpio["Edad"].median()
df_limpio["Edad"] = df_limpio["Edad"].fillna(mediana_edad)

# Rellenamos Fumador con la moda ("No"):
moda_fumador = df_limpio["Fumador"].mode()[0]
df_limpio["Fumador"] = df_limpio["Fumador"].fillna(moda_fumador)

print(f"Mediana de edad calculada: {mediana_edad} años | Moda fumador: '{moda_fumador}'")
print("\nDataset Imputado y Limpio:")
display(df_limpio)
```

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos (Edición Para No Ingenieros)</i>
  </p>
</div>
