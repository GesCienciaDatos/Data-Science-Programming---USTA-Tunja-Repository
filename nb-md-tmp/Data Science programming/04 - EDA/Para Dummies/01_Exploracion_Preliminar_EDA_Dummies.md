# 01_Exploracion_Preliminar_EDA_Dummies

<table style="width: 100%; border-collapse: collapse; border: none; background: #fffbeb; border-left: 6px solid #f59e0b; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #78350f; font-size: 2em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        💡 01. Exploración Preliminar y Anscombe
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
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/04%20-%20EDA/Para%20Dummies/01_Exploracion_Preliminar_EDA_Dummies.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## La Fábula del Cuarteto de Anscombe 🧙‍♂️

En 1973, el estadístico Francis Anscombe creó 4 conjuntos de datos diferentes que tenían **exactamente el mismo promedio, la misma varianza y la misma correlación**.

Cualquier persona que solo mirara los números en una tabla pensaría: *"Estos 4 grupos de datos son idénticos"*.
Pero cuando los graficas en un plano... ¡uno es una línea recta, otro es una curva perfecta, otro tiene un dato atípico gigante y el último es una pared vertical!

### 💡 La Lección para no ingenieros:
**"Una gráfica vale más que mil promedios"**. Nunca tomes decisiones de negocio basándote únicamente en un promedio sin ver la distribución de los datos.

```python
import seaborn as sns
import matplotlib.pyplot as plt

# Cargamos el famoso dataset de Anscombe:
df_anscombe = sns.load_dataset("anscombe")

print("Resumen de las primeras filas:")
display(df_anscombe.head())

# Mostramos el promedio de X e Y en cada uno de los 4 grupos:
print("\nPromedios por Grupo:")
display(df_anscombe.groupby("dataset").mean())
```

---
### Resolviendo el Misterio: Graficando los 4 Grupos 🎨

```python
# Graficamos los 4 grupos a la vez usando FacetGrid de Seaborn:
g = sns.lmplot(
    data=df_anscombe, x="x", y="y", col="dataset",
    hue="dataset", col_wrap=2, ci=None, height=3.5
)
g.set_axis_labels("Variable X", "Variable Y")
plt.suptitle("El Cuarteto de Anscombe en Gráficas", y=1.03, fontsize=14, fontweight="bold")
plt.show()
```

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos (Edición Para No Ingenieros)</i>
  </p>
</div>
