# 00_Introduccion_Classification_Dummies

<table style="width: 100%; border-collapse: collapse; border: none; background: #fffbeb; border-left: 6px solid #f59e0b; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #78350f; font-size: 2em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        💡 Introducción a la Clasificación [Edición Dummies] 🎯
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
        💡 Para Dummies • Módulo 08
      </span><br>
      <span style="color: #78350f; font-size: 0.85em;">Docente: Santiago A. Zúñiga M.</span><br>
      <a href="mailto:gestorvirtualcienciadatos@ustatunja.edu.co" style="color: #b45309; font-size: 0.8em; text-decoration: none; font-weight: 500;">gestorvirtualcienciadatos@ustatunja.edu.co</a>
    </td>
  </tr>
</table>

<div align="center" style="margin-top: 15px; margin-bottom: 15px;">
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/08%20-%20Classification/Para%20Dummies/00_Introduccion_Classification_Dummies.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## 🌟 ¿Qué es la Clasificación? (La Analogía del Semáforo y el Correo Spam)

Imagina que eres el encargado de organizar la correspondencia:
* En **Regresión** intentabas predecir *un número continuo* (ejemplo: ¿cuántos gramos pesa el paquete? $\to 342.5\text{ g}$).
* En **Clasificación** tu trabajo es asignarle *una categoría o etiqueta* al paquete (ejemplo: ¿es urgente o normal? ¿es correo legítimo o es basura/spam?).

### 🚦 El mundo de las decisiones cotidianas:
* **El médico:** ¿El paciente tiene la afección (*Positivo*) o está sano (*Negativo*)?
* **El banco:** ¿Aprobamos el préstamo (*Sí*) o lo rechazamos (*No*)?
* **Netflix:** ¿Le gustará la película (*Recomendada*) o la ignorará?

---
## 🧠 ¿Por qué una simple regla recta no sirve para predecir probabilidades?

Una probabilidad **siempre debe estar entre el 0% (imposible) y el 100% (seguro)**.
* Si usamos una regla recta rígida, para valores altos te diría *"hay 140% de probabilidad"* o para valores bajos *"-25%"*.
* Por eso los científicos de datos usan la **curva en forma de 'S' (la Sigmoide)** que se adapta suavemente y garantiza porcentajes entre 0% y 100%.

```python
import numpy as np
import matplotlib.pyplot as plt

# Puntaje acumulado de evidencia (desde muy negativo hasta muy positivo)
puntaje = np.linspace(-6, 6, 200)

# Fórmula de la curva Sigmoide en porcentaje (%)
probabilidad_porcentaje = (1 / (1 + np.exp(-puntaje))) * 100

plt.figure(figsize=(8.5, 4))
plt.plot(puntaje, probabilidad_porcentaje, color='#f59e0b', lw=3.5, label='Probabilidad calculada (%)')
plt.axhline(50, color='#64748b', linestyle='--', label='Punto de duda total (50% de probabilidad)')
plt.axhline(100, color='green', linestyle=':', label='100% Seguro')
plt.axhline(0, color='red', linestyle=':', label='0% Imposible')

plt.title("💡 La Curva en 'S': Convierte cualquier evidencia en una probabilidad segura", fontsize=11, fontweight='bold')
plt.xlabel("Evidencia a favor o en contra")
plt.ylabel("Probabilidad de Ocurrencia (%)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
```

---
##### 🎯 Reto Práctico para Dummies: El Semáforo Inteligente

**Situación:** Imagina que un semáforo calcula la probabilidad de que haya congestión según la cantidad de carros esperando.
* La fórmula de evidencia es: `evidencia = -4.0 + 0.5 * carros`
* Si hay **2 carros**, ¿qué porcentaje de probabilidad de trancón calcula el semáforo?
* ¿Y si hay **15 carros**?

```python
# =========================================================================
# TU SOLUCIÓN: Reto Dummies 0 - El Semáforo Inteligente
# =========================================================================

# 1. Definir cantidad de carros
# carros_pocos = 2
# carros_muchos = 15

# 2. Calcular evidencia
# e_pocos = -4.0 + 0.5 * carros_pocos
# e_muchos = -4.0 + 0.5 * carros_muchos

# 3. Calcular porcentaje con la sigmoide
# prob_pocos = (1 / (1 + np.exp(-e_pocos))) * 100
# prob_muchos = ...
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución explicada...</b></summary>

```python
import numpy as np

def calcular_probabilidad_semaforo(num_carros):
    evidencia = -4.0 + 0.5 * num_carros
    prob = (1 / (1 + np.exp(-evidencia))) * 100
    return prob

prob_2 = calcular_probabilidad_semaforo(2)
prob_15 = calcular_probabilidad_semaforo(15)

print(f"🚦 Con 2 carros:  {prob_2:.1f}% de probabilidad de congestión (Tráfico Fluido ✅)")
print(f"🚦 Con 15 carros: {prob_15:.1f}% de probabilidad de congestión (¡Trancón Seguro 🚨!)")
```
</details>

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Guía Práctica e Intuitiva</i>
  </p>
</div>
