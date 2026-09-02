# 01_Python_Hands_On_Dummies

<table style="width: 100%; border-collapse: collapse; border: none; background: #fffbeb; border-left: 6px solid #f59e0b; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #78350f; font-size: 2em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        💡 Taller Práctico 01: Python para No Ingenieros
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
        💡 Taller Dummies • Módulo 01
      </span><br>
      <span style="color: #78350f; font-size: 0.85em;">Docente: Santiago A. Zúñiga M.</span><br>
      <a href="mailto:gestorvirtualcienciadatos@ustatunja.edu.co" style="color: #b45309; font-size: 0.8em; text-decoration: none; font-weight: 500;">gestorvirtualcienciadatos@ustatunja.edu.co</a>
    </td>
  </tr>
</table>

<div align="center" style="margin-top: 15px; margin-bottom: 15px;">
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/homeworks/Para%20Dummies/01_Python_Hands_On_Dummies.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## ¡Bienvenido a tu Primer Taller Práctico! 🎯

Este taller fue diseñado para que pongas en práctica los conceptos de Python sin frustración. Cada ejercicio cuenta con:
1. **El contexto del problema en la vida cotidiana.**
2. **Pistas (*Hints*) para saber qué herramienta de Python usar.**
3. **Tu celda de código con comentarios guía.**
4. **Una solución desplegable explicada paso a paso.**

---
### Ejercicio 1: Calculadora de Propinas y Cuenta Dividida 🍕
**Situación:** Saliste a cenar con 3 amigos (4 personas en total). La cuenta total del restaurante fue de `\\$180,000` COP y decidieron dejar el `10%` de propina voluntaria.
Calcula cuánto debe pagar exactamente cada uno de los 4 comensales.

```python
# 1. Datos iniciales:
cuenta_total = 180000
porcentaje_propina = 0.10
numero_personas = 4

# 2. Tu cálculo:
valor_propina = cuenta_total * porcentaje_propina
total_con_propina = cuenta_total + valor_propina
pago_individual = total_con_propina / numero_personas

print(f"Cuenta base: ${cuenta_total:,.2f}")
print(f"Propina (10%): ${valor_propina:,.2f}")
print(f"👉 Cada persona debe transferir: ${pago_individual:,.2f} COP")
```

<details>
<summary>💡 Ver solución explicada</summary>
Calculamos el 10% multiplicando por 0.10, lo sumamos al total y dividimos entre las 4 personas. Cada uno paga \\$49,500 COP.
</details>

---
### Ejercicio 2: Clasificador de Clientes por Edad 🎂
**Situación:** Tienes una lista de edades de usuarios registrados: `[15, 22, 68, 45, 12, 30]`.
Escribe un bucle que clasifique a cada uno como `"Menor de edad"`, `"Adulto"` o `"Adulto Mayor"` ($\ge 60$ años).

```python
edades = [15, 22, 68, 45, 12, 30]

for edad in edades:
    if edad < 18:
        categoria = "Menor de edad 🧒"
    elif edad < 60:
        categoria = "Adulto 🧑"
    else:
        categoria = "Adulto Mayor 👴"
    print(f"Edad: {edad} años -> {categoria}")
```

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos (Edición Para No Ingenieros)</i>
  </p>
</div>
