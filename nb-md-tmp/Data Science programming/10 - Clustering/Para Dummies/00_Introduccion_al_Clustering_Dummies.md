# 00_Introduccion_al_Clustering_Dummies

<table style="width: 100%; border-collapse: collapse; border: none; background: #fffbeb; border-left: 6px solid #f59e0b; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #78350f; font-size: 2em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        💡 00. Introducción al Clustering Para Dummies: El Cajón Desordenado 💡
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
        💡 Para Dummies • Módulo 10
      </span><br>
      <span style="color: #78350f; font-size: 0.85em;">Docente: Santiago A. Zúñiga M.</span><br>
      <a href="mailto:gestorvirtualcienciadatos@ustatunja.edu.co" style="color: #b45309; font-size: 0.8em; text-decoration: none; font-weight: 500;">gestorvirtualcienciadatos@ustatunja.edu.co</a>
    </td>
  </tr>
</table>

<div align="center" style="margin-top: 15px; margin-bottom: 15px;">
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/10%20-%20Clustering/Para%20Dummies/00_Introduccion_al_Clustering_Dummies.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Abrir en Google Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## ¿Qué es el Clustering en Palabras Sencillas? 🧦

Imagina que vacías sobre tu cama un canasto con **200 calcetines revueltos** de toda la familia. Nadie te dio una lista de marcas ni de nombres, pero de forma completamente natural tu cerebro empieza a armar montoncitos:

* Los calcetines blancos deportivos en un montón.
* Los calcetines negros elegantes en otro montón.
* Los calcetines gruesos de lana para el frío en un tercer montón.

**Eso es el Clustering:** Tomar un montón de datos sin etiquetas ni respuestas correctas previas y descubrir grupos naturales de cosas que se parecen entre sí.

---
## ¿Para Qué Sirve en la Vida Real y en el Campo? 🚜

* 🛍️ **En el Comercio y Marketing:** Agrupar a los clientes en *"cazadores de ofertas"*, *"compradores impulsivos"* o *"clientes VIP"* para enviarles promociones que de verdad les interesen.
* 🚜 **En la Agricultura de Precisión:** Conectar sensores en un cultivo para agrupar los sectores de la finca que tienen la misma humedad y regar únicamente donde hace falta, ahorrando miles de litros de agua.
* 🎵 **En la Música:** ¿Cómo sabe Spotify qué poner en tu *Daily Mix*? Agrupa canciones que tienen ritmos, instrumentos y velocidades similares a lo que escuchas a diario.

```python
# Demostración intuitiva: Cómo la computadora ve los datos
import numpy as np
import pandas as pd

# Datos de 4 clientes: [Edad, Gasto Promedio Mensual en Miles de COP]
clientes_tienda = pd.DataFrame({
    "Cliente": ["Carlos (Joven)", "Ana (Joven)", "Don Pedro (Adulto)", "Doña Marta (Adulto)"],
    "Edad": [22, 24, 60, 62],
    "Gasto_Mensual_Miles": [50, 55, 500, 520]
})

print("Tabla de Clientes en la Tienda:")
display(clientes_tienda)
```

---
## 🛠️ Reto Práctico Para Dummies

Observa la tabla anterior. Sin usar matemáticas complejas, ¿cuáles clientes formarían el **Grupo 1** y cuáles el **Grupo 2**? Verifica tu razonamiento desplegando la solución:

<details>
<summary><b>💡 Haz clic aquí para ver la explicación paso a paso...</b></summary>

```
Grupo 1 (Jóvenes Ahorradores): Carlos (22 años, $50k) y Ana (24 años, $55k).
Grupo 2 (Adultos con Alto Poder Adquisitivo): Don Pedro (60 años, $500k) y Doña Marta (62 años, $520k).

¡Eso es exactamente lo que hace un algoritmo de Clustering de forma automática con millones de filas!
```
</details>

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos (Edición Conceptual Para Dummies)</i>
  </p>
</div>
