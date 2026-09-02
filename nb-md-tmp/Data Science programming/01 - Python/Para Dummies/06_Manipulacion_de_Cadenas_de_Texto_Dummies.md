# 06_Manipulacion_de_Cadenas_de_Texto_Dummies

<table style="width: 100%; border-collapse: collapse; border: none; background: #fffbeb; border-left: 6px solid #f59e0b; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #78350f; font-size: 2em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        💡 06. Manipulación de Cadenas de Texto (Strings)
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
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/01%20-%20Python/Para%20Dummies/06_Manipulacion_de_Cadenas_de_Texto_Dummies.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## ¿Por qué la Limpieza de Texto es Vital en Ciencia de Datos? 🧼

En el mundo real, los datos de texto ingresados por humanos siempre llegan llenos de problemas: espacios de más al inicio o al final, mezclas de mayúsculas y minúsculas (`"BOGOTA"`, `"bogota"`, `"Bogotá "`), caracteres extraños o formatos desalineados.

Si no limpiamos el texto antes de analizarlo, Python pensará que `"Bogota"` y `"bogota "` son dos ciudades completamente distintas.

---
## 1. Operaciones Básicas: Mayúsculas, Minúsculas y Espacios 🧹

```python
# Texto desordenado típico de un formulario:
texto_sucio = "   uNiVeRsIdAd SaNtO tOmAs TuNjA   "

print("Original:", repr(texto_sucio))
print("1. Quitar espacios sobrantes (.strip()):", repr(texto_sucio.strip()))
print("2. Todo en minúsculas (.lower()):", texto_sucio.strip().lower())
print("3. Todo en mayúsculas (.upper()):", texto_sucio.strip().upper())
print("4. Formato Título (.title()):", texto_sucio.strip().title())
```

---
## 2. Reemplazo y Búsqueda: `.replace()` e `in` 🔍

* `.replace(antiguo, nuevo)`: Sustituye una parte del texto por otra.
* `"palabra" in texto`: Devuelve `True` o `False` si una palabra existe dentro del texto.

```python
frase = "El precio del producto es de $150 USD."

# Cambiamos USD por COP:
frase_modificada = frase.replace("USD", "COP").replace("$150", "$600,000")
print("Frase ajustada:", frase_modificada)

# Verificamos si contiene la palabra 'producto':
print("¿Habla de producto?:", "producto" in frase)
```

---
## 3. Dividir y Unir Cadenas: `.split()` y `.join()` 🧩

### 💡 La Analogía de la Tijera y el Pegamento
- **`.split(",")` (La Tijera):** Corta un texto largo en una lista de pedacitos cada vez que encuentra una coma.
- **`", ".join(lista)` (El Pegamento):** Toma una lista de palabras y las pega todas en un solo texto separadas por comas.

```python
# Datos que vienen de un archivo CSV separados por comas:
registro_csv = "Juan Pérez,Ingeniero,35,Tunja,Activo"

# Cortamos con la tijera (.split):
datos_cliente = registro_csv.split(",")
print("Lista de datos separados:", datos_cliente)
print("Nombre:", datos_cliente[0])
print("Profesión:", datos_cliente[1])

# Ahora tomamos una lista de habilidades y las pegamos con comas:
habilidades = ["Python", "Pandas", "SQL", "Estadística"]
texto_unido = " | ".join(habilidades)
print("Habilidades unidas:", texto_unido)
```

---
## 4. Formateo Moderno con f-strings ✨

Las `f-strings` (`f"texto {variable}"`) son la forma más legible y potente de armar mensajes dinámicos y dar formato a números.

```python
nombre = "Ana María"
puntaje = 0.9458
total_pago = 1250300.5

# Formateamos porcentajes (.1%) y moneda con comas y 2 decimales (:,.2f):
mensaje = f"Estimada {nombre}: Tu precisión en la prueba fue del {puntaje:.1%} y tu pago es de ${total_pago:,.2f} COP."
print(mensaje)
```

---
## 🛠️ Práctica: Estandarizador de Correos Electrónicos

**Problema:**
Un sistema recibió esta lista de correos ingresados por usuarios:
`correos_crudos = ["   CARLOS@GMAIL.COM  ", "  maria.gonzalez@Hotmail.Com", "PEDRO_123@yahoo.es   "]`
1. Limpia cada correo quitando espacios en blanco y convirtiéndolo todo a minúsculas.
2. Imprime la lista de correos limpios y listos para ser guardados en la base de datos.

```python
# Solución guiada:
correos_crudos = ["   CARLOS@GMAIL.COM  ", "  maria.gonzalez@Hotmail.Com", "PEDRO_123@yahoo.es   "]

correos_limpios = [email.strip().lower() for email in correos_crudos]

print("Correos Crudos:", correos_crudos)
print("Correos Limpios y Estandarizados:", correos_limpios)
```

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos (Edición Para No Ingenieros)</i>
  </p>
</div>
