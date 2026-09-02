# 02b_Estructuras_Diccionarios_Dummies

<table style="width: 100%; border-collapse: collapse; border: none; background: #fffbeb; border-left: 6px solid #f59e0b; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #78350f; font-size: 2em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        💡 02b. Colecciones Nativas II: Diccionarios
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
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/01%20-%20Python/Para%20Dummies/02b_Estructuras_Diccionarios_Dummies.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## 1. ¿Qué es un Diccionario en Python? 📖

### 💡 La Analogía de la Agenda de Contactos
En tu teléfono celular, tú no buscas el número de tu mamá diciendo: *"quiero el número que está en la posición número 47"*.
Tú buscas directamente por la palabra **"Mamá"** (*la clave*), y el teléfono te devuelve su número telefónico `315-123-4567` (*el valor*).

Un **Diccionario** en Python funciona exactamente así: guarda pares de **`Clave : Valor`** entre llaves `{ }`.

```python
# Creando el perfil de un cliente en un diccionario:
cliente = {
    "nombre": "Mariana Rentería",
    "edad": 29,
    "ciudad": "Tunja",
    "profesion": "Médica",
    "score_crediticio": 780
}

# Consultamos los datos usando la clave entre corchetes:
print("Nombre del cliente:", cliente["nombre"])
print("Ciudad de residencia:", cliente["ciudad"])
print("Puntaje de crédito:", cliente["score_crediticio"])
```

---
## 2. Modificar, Agregar y Eliminar Datos en un Diccionario ✏️

* **Agregar / Modificar:** `diccionario["nueva_clave"] = valor`
* **Consultar de forma segura:** `diccionario.get("clave", valor_por_defecto)` (no genera error si no existe).
* **Eliminar:** `del diccionario["clave"]`

```python
# Agregamos el correo electrónico:
cliente["email"] = "mariana.renteria@hospital.org"

# Modificamos su score crediticio porque pagó su tarjeta:
cliente["score_crediticio"] = 810

# Consultamos una clave que tal vez no existe con .get() de forma segura:
antiguedad = cliente.get("antiguedad_anios", "No registrada")

print("Email agregado:", cliente["email"])
print("Nuevo Score:", cliente["score_crediticio"])
print("Antigüedad:", antiguedad)
```

---
## 3. Recorrer un Diccionario con un Bucle 🔄

Podemos explorar las claves, los valores o ambos a la vez usando `.items()`:

```python
# Inventario de frutas en una tienda con su stock en kilogramos:
inventario = {
    "Manzanas": 50,
    "Naranjas": 30,
    "Peras": 15,
    "Fresas": 8
}

print("📦 Reporte de Inventario de la Tienda:")
for fruta, kilos in inventario.items():
    print(f"- {fruta}: {kilos} kg disponibles")
```

---
## 🛠️ Práctica: Reporte de Calificaciones de un Curso

**Problema:**
Tienes un diccionario con las notas definitivas de 4 estudiantes:
`notas = {"Andrés": 4.5, "Beatriz": 3.2, "Camilo": 2.8, "Diana": 4.8}`.
1. Calcula la nota promedio del grupo.
2. Identifica quiénes aprobaron (nota mayor o igual a 3.0).

```python
# Solución práctica:
notas = {"Andrés": 4.5, "Beatriz": 3.2, "Camilo": 2.8, "Diana": 4.8}

# 1. Promedio:
suma_notas = sum(notas.values())
total_estudiantes = len(notas)
promedio = suma_notas / total_estudiantes

print(f"📊 Nota promedio del grupo: {promedio:.2f}")

# 2. Aprobados:
print("\n✅ Estudiantes Aprobados:")
for nombre, nota in notas.items():
    if nota >= 3.0:
        print(f"  • {nombre} pasó con nota de {nota}")
```

<details>
<summary>💡 Ver explicación de la solución</summary>

1. `notas.values()` nos extrae solo los números `[4.5, 3.2, 2.8, 4.8]`.
2. Usamos `sum(...)` y `len(...)` para calcular el promedio aritmético rápidamente.
3. Con `notas.items()` revisamos cada estudiante y aplicamos la condición `if nota >= 3.0`.
</details>

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos (Edición Para No Ingenieros)</i>
  </p>
</div>
