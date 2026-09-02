# 01_Estructuras_de_Datos_Pandas_Dummies

<table style="width: 100%; border-collapse: collapse; border: none; background: #fffbeb; border-left: 6px solid #f59e0b; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #78350f; font-size: 2em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        💡 01. Estructuras de Datos: Series y DataFrames
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
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/03%20-%20Pandas/Para%20Dummies/01_Estructuras_de_Datos_Pandas_Dummies.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## 1. La `Series`: Una Columna con Superpoderes 📊

Una `Series` es una lista unidimensional donde cada elemento tiene una **etiqueta de identificación llamada índice (`index`)**.

```python
import pandas as pd

# Creando una Serie con las ventas de un almacén en 3 años:
ventas_anuales = pd.Series([1200, 1850, 2400], index=["2023", "2024", "2025"], name="Ventas_Millones_COP")

print("Nuestra primera Serie:")
display(ventas_anuales)

print("\nConsultar por su etiqueta ('2024'):", ventas_anuales["2024"])
print("Promedio de ventas en los 3 años:", ventas_anuales.mean())
```

---
## 2. El `DataFrame`: La Tabla Completa 📋

Un `DataFrame` se construye comúnmente a partir de un diccionario de Python donde cada **clave es el nombre de la columna** y el **valor es la lista de datos**.

```python
# Construimos una tabla de clientes:
datos_tienda = {
    "Cliente": ["Sofía Alarcón", "Mateo Gómez", "Valentina Ríos", "Juan Morales"],
    "Edad": [28, 35, 22, 41],
    "Ciudad": ["Tunja", "Duitama", "Sogamoso", "Tunja"],
    "Gasto_Total_COP": [450000, 1200000, 180000, 890000],
    "Es_VIP": [True, True, False, True]
}

df_clientes = pd.DataFrame(datos_tienda)
print("DataFrame Creado:")
display(df_clientes)
```

---
## 🛠️ Práctica: Creando una Ficha de Productos

**Problema:**
Crea un `DataFrame` llamado `df_productos` con 3 productos de tecnología:
- Columnas: `"Producto"`, `"Precio"`, `"Stock_Disponible"`.
- Muestra el DataFrame en pantalla y calcula el precio promedio de los artículos.

```python
# Solución guiada:
df_productos = pd.DataFrame({
    "Producto": ["Laptop Lenovo", "Monitor 27 Pulgadas", "Teclado Mecánico"],
    "Precio": [2800000, 950000, 250000],
    "Stock_Disponible": [12, 8, 25]
})

display(df_productos)
print(f"💰 Precio Promedio: ${df_productos['Precio'].mean():,.2f} COP")
```

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos (Edición Para No Ingenieros)</i>
  </p>
</div>
