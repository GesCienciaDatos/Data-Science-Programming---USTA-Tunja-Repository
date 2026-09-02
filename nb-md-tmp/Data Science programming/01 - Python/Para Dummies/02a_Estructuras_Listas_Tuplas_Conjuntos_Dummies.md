# 02a_Estructuras_Listas_Tuplas_Conjuntos_Dummies

<table style="width: 100%; border-collapse: collapse; border: none; background: #fffbeb; border-left: 6px solid #f59e0b; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #78350f; font-size: 2em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        💡 02a. Colecciones Nativas I: Listas, Tuplas y Conjuntos
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
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/01%20-%20Python/Para%20Dummies/02a_Estructuras_Listas_Tuplas_Conjuntos_Dummies.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## ¿Por qué necesitamos Colecciones? 🗂️

Hasta ahora guardamos un solo dato en cada variable (como el nombre de un cliente). Pero en la vida real y en Ciencia de Datos, **trabajamos con cientos o miles de datos a la vez**: una lista de precios, un registro de ventas del mes o los nombres de todos los estudiantes.

Python nos ofrece 3 formas fantásticas de agrupar datos:

| Colección | 💡 La Analogía del Mundo Real | Características Clave | Símbolo |
|---|---|---|---|
| **Lista (`list`)** | **La Lista de Compras del Supermercado:** Puedes agregar cosas, tachar productos, cambiar de marca y el orden importa. | **Ordenada y Modificable (Mutable).** Permite elementos duplicados. | Corchetes `[ ]` |
| **Tupla (`tuple`)** | **El Acta de Nacimiento / Coordenadas GPS:** Una vez que se expide, nadie puede alterar los datos legalmente. | **Ordenada e Inmutable (No se puede cambiar).** Muy rápida y segura. | Paréntesis `( )` |
| **Conjunto (`set`)** | **La Bolsa de Dulces / Lista de Invitados VIP:** Si echas dos caramelos iguales, sigue habiendo un solo tipo de caramelo; el orden no importa, solo quién está adentro. | **No ordenada y Sin Duplicados.** Ideal para eliminar repeticiones. | Llaves `{ }` |

---
## 1. Listas (`list`): La navaja suiza de Python 🛒

Las listas te permiten guardar cualquier cantidad de elementos en orden.

```python
# 1. Creando una lista de productos en inventario
frutas = ["Manzana", "Banano", "Naranja", "Fresa"]
print("Lista inicial:", frutas)

# 2. ¿Cómo consultamos elementos? (¡En Python se empieza a contar desde 0!)
print("Primer elemento (índice 0):", frutas[0])
print("Segundo elemento (índice 1):", frutas[1])
print("Último elemento (índice -1):", frutas[-1])
```

---
### Modificando y Agregando Elementos a una Lista

* `.append(nuevo_dato)`: Agrega un elemento al final de la lista.
* `.insert(posicion, nuevo_dato)`: Mete un elemento en una posición específica.
* `.remove(dato)`: Quita la primera aparición de ese valor.
* `pop()`: Saca y elimina el último elemento.

```python
# Agregamos 'Uva' al final
frutas.append("Uva")
print("Después de append:", frutas)

# Insertamos 'Mango' en la posición 1 (segundo lugar)
frutas.insert(1, "Mango")
print("Después de insert:", frutas)

# Cambiamos 'Banano' por 'Kiwi' directamente
frutas[2] = "Kiwi"
print("Después de modificar índice 2:", frutas)

# Eliminamos 'Naranja'
frutas.remove("Naranja")
print("Después de remove:", frutas)
```

---
## 2. Tuplas (`tuple`): Datos protegidos contra cambios 🔒

### 💡 La Analogía del Candado
Imagina las coordenadas de una sucursal bancaria: `(4.570868, -74.297333)`. No quieres que nadie en tu equipo por error cambie la latitud o longitud mientras el programa corre. Para eso usamos una **Tupla**.

```python
# Creando una tupla con las coordenadas de la Universidad Santo Tomás Tunja:
coordenadas_usta = (5.5353, -73.3678)
print("Coordenadas USTA:", coordenadas_usta)
print("Latitud:", coordenadas_usta[0])
print("Longitud:", coordenadas_usta[1])

# ¿Qué pasa si intentamos cambiar un valor?:
# coordenadas_usta[0] = 6.0  <-- ¡Esto daría error porque es inmutable!
```

---
### Desempaquetado de Tuplas (Unpacking) ✨
Es como abrir una caja de regalo y asignar cada objeto a una persona distinta en una sola línea:

```python
# Asignamos latitud y longitud automáticamente en una sola línea:
latitud, longitud = coordenadas_usta

print(f"📍 Latitud extraída: {latitud}")
print(f"📍 Longitud extraída: {longitud}")
```

---
## 3. Conjuntos (`set`): El eliminador automático de duplicados 🧹

### 💡 La Analogía del Filtro de Huellas Digitales
Si una persona pasa 5 veces por un torniquete con el mismo pase, el sistema de seguridad solo cuenta a **1 persona única**. Un `set` hace exactamente eso con tus datos.

```python
# Lista con clientes repetidos que visitaron la tienda hoy:
visitas_hoy = ["Carlos", "Ana", "Carlos", "Pedro", "Ana", "Lucía", "Carlos"]
print("Total de visitas registradas:", len(visitas_hoy))

# Convertimos a conjunto para obtener solo los clientes ÚNICOS:
clientes_unicos = set(visitas_hoy)
print("Clientes únicos que asistieron:", clientes_unicos)
print("Número de personas diferentes:", len(clientes_unicos))
```

---
## 4. List Comprehensions: La forma elegante de transformar listas ⚡

### 💡 La Analogía de la Banda Transportadora
En lugar de tomar cada producto uno por uno con un carrito, pones una banda transportadora que aplica una regla a todo lo que pase.

```python
# Queremos calcular los precios con IVA (19%) de una lista de precios base:
precios_base = [10000, 25000, 50000, 80000]

# Forma elegante en una sola línea (List Comprehension):
precios_con_iva = [precio * 1.19 for precio in precios_base]

print("Precios Base:", precios_base)
print("Precios con IVA:", precios_con_iva)
```

---
## 🛠️ Práctica: Control de Asistencia y Premios

**Problema:**
Una empresa realizó un sorteo entre los asistentes a una conferencia. Los números de boletos ganadores registrados fueron: `[102, 105, 102, 108, 110, 105, 115]`.
1. Elimina los boletos duplicados usando un `set`.
2. Convierte el resultado nuevamente en una lista ordenada.
3. Imprime cuántos ganadores únicos reales hubo y la lista final.

```python
# Escribe tu solución aquí:
boletos_ganadores = [102, 105, 102, 108, 110, 105, 115]

# Paso 1: Obtener únicos
boletos_unicos_set = set(boletos_ganadores)

# Paso 2: Convertir a lista y ordenar
boletos_ordenados = sorted(list(boletos_unicos_set))

print(f"Total boletos originales: {len(boletos_ganadores)}")
print(f"Total ganadores únicos: {len(boletos_ordenados)}")
print(f"Lista de boletos premiados: {boletos_ordenados}")
```

<details>
<summary>💡 Ver explicación de la solución</summary>

1. `set(boletos_ganadores)` remueve instantáneamente los duplicados `102` y `105`.
2. `sorted(...)` toma los elementos del conjunto y los devuelve en una nueva lista ordenada de menor a mayor `[102, 105, 108, 110, 115]`.
</details>

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos (Edición Para No Ingenieros)</i>
  </p>
</div>
