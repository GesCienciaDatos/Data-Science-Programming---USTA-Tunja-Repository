# 02_Escalado_Caracteristicas_Data_Preparation_Dummies

<table style="width: 100%; border-collapse: collapse; border: none; background: #fffbeb; border-left: 6px solid #f59e0b; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #78350f; font-size: 2em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        💡 02. Escalado de Características (Feature Scaling)
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
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/05%20-%20Data%20Preparation/Para%20Dummies/02_Escalado_Caracteristicas_Data_Preparation_Dummies.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## ¿Por qué es necesario Escalar? ⚖️

### 💡 La Analogía del Gigante y la Hormiga:
Imagina que quieres clasificar perfiles de clientes usando dos datos:
1. **Edad:** Va de `18` a `70` años (números de dos dígitos).
2. **Salario Anual:** Va de `\$20,000,000` a `\$150,000,000` COP (números de ocho dígitos).

Los algoritmos matemáticos calculan distancias numéricas. Si no escalas los datos, el algoritmo pensará que una diferencia de \$5,000,000 en el salario es **500,000 veces más importante** que una diferencia de 10 años en la edad, ¡aplastando por completo a la variable edad!

---
## Los 2 Métodos Principales de Escalado:

| Método | Fórmula Intuitiva | Rango Final | ¿Cuándo usarlo? |
|---|---|---|---|
| **Min-Max Scaling (`MinMaxScaler`)** | Comprime todo entre 0 y 1: el valor más pequeño se vuelve 0 y el más alto se vuelve 1. | `[0, 1]` | Redes neuronales, algoritmos que requieren valores acotados. |
| **Estandarización (`StandardScaler`)** | Centra la media en 0 y la desviación estándar en 1 (Z-Score). | Sin límite fijo (generalmente $[-3, +3]$) | Regresión Lineal, Logística, SVM, KNN, PCA. |

```python
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler

df_ejemplo = pd.DataFrame({
    "Edad": [20, 30, 40, 50],
    "Salario_Mensual": [2000000, 3500000, 6000000, 10000000]
})

# 1. MinMax Scaler (0 a 1):
minmax = MinMaxScaler()
df_minmax = pd.DataFrame(minmax.fit_transform(df_ejemplo), columns=df_ejemplo.columns)

# 2. Standard Scaler (Media=0, Std=1):
scaler_std = StandardScaler()
df_standard = pd.DataFrame(scaler_std.fit_transform(df_ejemplo), columns=df_ejemplo.columns)

print("Original:")
display(df_ejemplo)

print("\n1. Min-Max Scaled (Todos entre 0 y 1):")
display(df_minmax.round(3))

print("\n2. StandardScaler (Centrados en media 0):")
display(df_standard.round(3))
```

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos (Edición Para No Ingenieros)</i>
  </p>
</div>
