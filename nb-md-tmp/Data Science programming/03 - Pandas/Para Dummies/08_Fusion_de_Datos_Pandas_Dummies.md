# 08_Fusion_de_Datos_Pandas_Dummies

<table style="width: 100%; border-collapse: collapse; border: none; background: #fffbeb; border-left: 6px solid #f59e0b; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #78350f; font-size: 2em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        💡 08. Fusión de Datos (Merge, Join y Concat)
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
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/03%20-%20Pandas/Para%20Dummies/08_Fusion_de_Datos_Pandas_Dummies.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## ¿Cómo unir dos tablas diferentes? 🤝

En la vida real, la información de clientes está en una tabla y sus compras están en otra. Necesitamos cruzarlas usando una **clave común (como el ID del cliente o la cédula)**.

| Tipo de Unión | 💡 Analogía Cotidiana | ¿Qué filas quedan? |
|---|---|---|
| **`Inner Join` (Por defecto)** | El apretón de manos: solo los que coinciden en ambas partes. | Solo clientes que **tienen compras registradas**. |
| **`Left Join`** | La lista de la clase: conservas a **todos** los alumnos, y si alguno no entregó tarea, le pones `NaN`. | Todos los de la tabla izquierda. |
| **`Outer Join`** | La reunión comunitaria total: nadie se queda por fuera. | Todos los registros de ambas tablas. |
| **`Concat` (Apilar)** | Poner una hoja encima de otra (vertical) o pegarlas con cinta al lado (horizontal). | Apila registros de la misma estructura. |

```python
import pandas as pd

# Tabla 1: Clientes
df_clientes = pd.DataFrame({
    "Cliente_ID": [1, 2, 3, 4],
    "Nombre": ["Andrea", "Camilo", "Daniela", "Eduardo"],
    "Ciudad": ["Tunja", "Bogotá", "Duitama", "Tunja"]
})

# Tabla 2: Pedidos realizados
df_pedidos = pd.DataFrame({
    "Pedido_ID": [501, 502, 503],
    "Cliente_ID": [1, 2, 1],  # El cliente 1 hizo 2 pedidos, el cliente 2 hizo 1 pedido
    "Monto": [150000, 320000, 80000]
})

print("Clientes:")
display(df_clientes)
print("Pedidos:")
display(df_pedidos)

# Hacemos un Left Merge para ver qué compró cada cliente (o si no ha comprado nada):
df_cruce = pd.merge(df_clientes, df_pedidos, on="Cliente_ID", how="left")
print("\nResultado del Cruce (Left Merge):")
display(df_cruce)
```

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos (Edición Para No Ingenieros)</i>
  </p>
</div>
