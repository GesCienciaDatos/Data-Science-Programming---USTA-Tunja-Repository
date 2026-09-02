# 04_PCA_Feature_Engineering_Dummies

<table style="width: 100%; border-collapse: collapse; border: none; background: #fffbeb; border-left: 6px solid #f59e0b; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #78350f; font-size: 2em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        💡 04. PCA: Reducción de Dimensionalidad
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
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/06%20-%20Feature%20Engineering/Para%20Dummies/04_PCA_Feature_Engineering_Dummies.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## ¿Qué es PCA y cómo entenderlo sin dolor? 🗿 🔦

Imagina que tienes una estatua tridimensional compleja en una habitación oscura.
Si enciendes una linterna en el ángulo exacto, proyectas una **sombra en la pared plana (2D)** que captura casi todos los detalles y rasgos reconocibles de la estatua.

En Ciencia de Datos:
- Tienes una tabla con **50 columnas numéricas** (muy pesada y difícil de visualizar).
- **PCA (Análisis de Componentes Principales)** encuentra los mejores "ángulos de luz" para comprimir esas 50 columnas en **2 o 3 súper-columnas principales (PC1, PC2)** conservando el 90% de la información y variación original.

```python
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import seaborn as sns

# Usamos el dataset de flores Iris (4 medidas: largo/ancho de sépalo y pétalo):
df_iris = sns.load_dataset("iris")
X = df_iris.drop(columns=["species"])

# 1. Siempre estandarizamos antes de PCA (vital):
X_std = StandardScaler().fit_transform(X)

# 2. Comprimimos las 4 variables en solo 2 Componentes Principales:
pca = PCA(n_components=2)
componentes = pca.fit_transform(X_std)

df_pca = pd.DataFrame(componentes, columns=["Componente_1", "Componente_2"])
df_pca["Especie"] = df_iris["species"]

print(f"📊 Varianza total explicada por los 2 componentes: {pca.explained_variance_ratio_.sum():.1%}")
display(df_pca.head())
```

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos (Edición Para No Ingenieros)</i>
  </p>
</div>
