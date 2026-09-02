# 07_Agrupacion_y_Ordenamiento_Pandas_Dummies

<table style="width: 100%; border-collapse: collapse; border: none; background: #fffbeb; border-left: 6px solid #f59e0b; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #78350f; font-size: 2em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        💡 07. Agrupación y Ordenamiento (Group By)
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
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/03%20-%20Pandas/Para%20Dummies/07_Agrupacion_y_Ordenamiento_Pandas_Dummies.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## ¿Qué es GroupBy? 👥

### 💡 La Analogía del Clasificador de Correo:
Imagina una montaña de 10,000 cartas.
1. **Split (Dividir):** Las separas en pilas según la ciudad de destino (Pila Tunja, Pila Bogotá, Pila Medellín).
2. **Apply (Aplicar cálculo):** Cuentas cuántas cartas hay en cada pila o sumas el peso de cada pila.
3. **Combine (Combinar):** Entregas una pequeña hoja de resumen con el total de cada ciudad.

En Pandas se hace en una sola línea mágica: `df.groupby('Ciudad')['Ventas'].mean()`.

```python
import pandas as pd

df_ventas = pd.DataFrame({
    "Sucursal": ["Tunja", "Bogotá", "Tunja", "Medellín", "Bogotá", "Tunja", "Medellín"],
    "Categoria": ["Tecnología", "Hogar", "Hogar", "Tecnología", "Tecnología", "Ropa", "Hogar"],
    "Venta_COP": [1200000, 450000, 380000, 2100000, 1500000, 280000, 620000]
})

print("1. Total de ventas por cada Sucursal:")
ventas_por_sucursal = df_ventas.groupby("Sucursal")["Venta_COP"].sum().sort_values(ascending=False)
display(ventas_por_sucursal)

print("\n2. Resumen completo (Total y Promedio) por Sucursal:")
resumen = df_ventas.groupby("Sucursal")["Venta_COP"].agg(["count", "sum", "mean"])
display(resumen)
```

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos (Edición Para No Ingenieros)</i>
  </p>
</div>
