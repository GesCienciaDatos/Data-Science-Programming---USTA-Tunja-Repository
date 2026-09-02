# 03_Visualizacion_de_Datos_EDA_Dummies

<table style="width: 100%; border-collapse: collapse; border: none; background: #fffbeb; border-left: 6px solid #f59e0b; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #78350f; font-size: 2em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        💡 03. Visualización de Datos: El Catálogo de Gráficos
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
        💡 Para Dummies • Módulo 04
      </span><br>
      <span style="color: #78350f; font-size: 0.85em;">Docente: Santiago A. Zúñiga M.</span><br>
      <a href="mailto:gestorvirtualcienciadatos@ustatunja.edu.co" style="color: #b45309; font-size: 0.8em; text-decoration: none; font-weight: 500;">gestorvirtualcienciadatos@ustatunja.edu.co</a>
    </td>
  </tr>
</table>

<div align="center" style="margin-top: 15px; margin-bottom: 15px;">
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/04%20-%20EDA/Para%20Dummies/03_Visualizacion_de_Datos_EDA_Dummies.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## ¿Qué gráfico debo usar según mi objetivo? 🧭

| Tipo de Gráfico | ¿Cuándo usarlo? | 💡 Analogía |
|---|---|---|
| **Histograma (`sns.histplot`)** | Para ver la **forma de la montaña** de una variable numérica (¿dónde se concentra la mayoría?). | Una pirámide de edades o distribución de calificaciones. |
| **Boxplot / Diagrama de Caja (`sns.boxplot`)** | Para detectar **valores atípicos (outliers)** y comparar grupos con cuartiles. | Una radiografía médica que marca con puntitos a quienes tienen fiebre extrema. |
| **Scatter Plot / Dispersión (`sns.scatterplot`)** | Para ver si dos variables van de la mano (correlación). | Altura vs Peso de las personas. |
| **Gráfico de Líneas (`sns.lineplot`)** | Para ver tendencias a lo largo del **tiempo**. | La cotización del dólar en los últimos 12 meses. |

```python
import seaborn as sns
import matplotlib.pyplot as plt

# Dataset de propinas de un restaurante:
df_tips = sns.load_dataset("tips")

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# 1. Histograma del valor total de la cuenta:
sns.histplot(df_tips["total_bill"], kde=True, ax=axes[0], color="#0284c7")
axes[0].set_title("Distribución del Valor de la Cuenta ($)")

# 2. Boxplot comparando propinas según si es fumador o no:
sns.boxplot(data=df_tips, x="smoker", y="tip", ax=axes[1], palette="Blues")
axes[1].set_title("Monto de Propina: Fumadores vs No Fumadores")

plt.tight_layout()
plt.show()
```

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos (Edición Para No Ingenieros)</i>
  </p>
</div>
