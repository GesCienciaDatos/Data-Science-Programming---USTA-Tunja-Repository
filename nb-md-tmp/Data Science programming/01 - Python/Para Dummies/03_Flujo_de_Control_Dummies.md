# 03_Flujo_de_Control_Dummies

<table style="width: 100%; border-collapse: collapse; border: none; background: #fffbeb; border-left: 6px solid #f59e0b; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #78350f; font-size: 2em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        💡 03. Flujo de Control: Decisiones y Repeticiones
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
        💡 Para Dummies • Módulo 01
      </span><br>
      <span style="color: #78350f; font-size: 0.85em;">Docente: Santiago A. Zúñiga M.</span><br>
      <a href="mailto:gestorvirtualcienciadatos@ustatunja.edu.co" style="color: #b45309; font-size: 0.8em; text-decoration: none; font-weight: 500;">gestorvirtualcienciadatos@ustatunja.edu.co</a>
    </td>
  </tr>
</table>

<div align="center" style="margin-top: 15px; margin-bottom: 15px;">
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/01%20-%20Python/Para%20Dummies/03_Flujo_de_Control_Dummies.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## ¿Qué es el Flujo de Control? 🚦

Por defecto, Python lee un archivo de arriba hacia abajo, línea por línea. Pero los programas inteligentes necesitan:
1. **Tomar decisiones (Bifurcaciones):** *"Si el cliente debe más de \\$100, no permitirle comprar; si no, procesar el pago"*.
2. **Repetir acciones (Bucles / Ciclos):** *"Enviar un correo de confirmación a los 5,000 participantes del evento"*.

---
## 1. Condicionales: `if`, `elif`, `else` ⚖️

### 💡 La Analogía del Semáforo
- **`if` (Si...):** Si la luz está en verde, avanza.
- **`elif` (Sino, si...):** Si la luz está en amarillo, desacelera.
- **`else` (De lo contrario...):** Si está en cualquier otro color (rojo), detente por completo.

```python
# Sistema de clasificación de clientes según su volumen de compras anuales:
compras_anuales = 85000  # Dólares

if compras_anuales >= 100000:
    categoria = "👑 Cliente Diamante (Atención VIP 24/7 + 25% desc)"
elif compras_anuales >= 50000:
    categoria = "🥇 Cliente Oro (15% descuento permanente)"
elif compras_anuales >= 10000:
    categoria = "🥈 Cliente Plata (5% descuento permanente)"
else:
    categoria = "🥉 Cliente Estándar (Sin descuento especial)"

print("Monto de compras:", compras_anuales)
print("Categoría asignada:", categoria)
```

---
## 2. El Bucle `for`: Repetir para cada elemento 🔄

### 💡 La Analogía de la Baraja de Naipes
Imagina que tienes una baraja de cartas. El bucle `for` es como tomar la baraja y decir: *"Para cada carta que saque de la baraja, ponle un sello"*.

```python
# Supongamos que tenemos las ventas diarias de la semana:
ventas_semana = [120, 150, 180, 200, 310, 450, 280]  # Lunes a Domingo
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# Usamos zip() para unir los días con las ventas:
total_ventas = 0
for dia, venta in zip(dias, ventas_semana):
    total_ventas += venta
    print(f"📅 {dia}: {venta} ventas registradas")

print(f"\n👉 Total de la semana: {total_ventas} ventas")
```

---
## 3. El Bucle `while`: Repetir mientras se cumpla una condición ⏳

### 💡 La Analogía de la Batería del Celular
*"Mientras la batería sea mayor a 0%, sigue reproduciendo música; cuando llegue a 0%, apágate"*.

```python
# Simulador de descarga de batería:
nivel_bateria = 30  # Porcentaje

print("🔋 Iniciando reproducción de video...")
while nivel_bateria > 0:
    print(f"  Reproduciendo... Batería restante: {nivel_bateria}%")
    nivel_bateria -= 10  # Consumo de 10% por video

print("🪫 Batería agotada. Por favor conecte el cargador.")
```

---
## 🛠️ Práctica: Clasificador de Temperaturas

**Problema:**
Una estación meteorológica registró las temperaturas máximas de una ciudad durante 5 días: `[18, 26, 32, 14, 29]`.
Escribe un bucle que recorra cada temperatura y clasifique:
- Si es menor a 20°C: `"Frío 🧣"`
- Si está entre 20°C y 30°C: `"Templado / Agradable ☀️"`
- Si es mayor a 30°C: `"Alerta de Calor 🥵"`

```python
# Solución guiada:
temperaturas = [18, 26, 32, 14, 29]

for temp in temperaturas:
    if temp < 20:
        estado = "Frío 🧣"
    elif temp <= 30:
        estado = "Templado / Agradable ☀️"
    else:
        estado = "Alerta de Calor 🥵"
    
    print(f"Temperatura: {temp}°C -> Estado: {estado}")
```

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos (Edición Para No Ingenieros)</i>
  </p>
</div>
