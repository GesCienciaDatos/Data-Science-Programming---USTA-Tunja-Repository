# 06_Manipulacion_de_Cadenas_de_Texto

<table style="width: 100%; border-collapse: collapse; border: none; background: #f8fafc; border-left: 6px solid #1e3a8a; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #0f172a; font-size: 2.1em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        Manipulación y Formateo de Cadenas de Texto en Python 📝
      </h1>
      <p style="margin: 6px 0 0 0; color: #1e3a8a; font-size: 1.15em; font-weight: 600; font-family: system-ui, -apple-system, sans-serif;">
        Especialización en Ciencia de Datos | Programación para Ciencia de Datos
      </p>
      <p style="margin: 4px 0 0 0; color: #64748b; font-size: 0.95em; font-family: system-ui, -apple-system, sans-serif;">
        Universidad Santo Tomás — Seccional Tunja
      </p>
    </td>
    <td style="text-align: right; vertical-align: middle; border: none; padding: 15px 20px; width: 30%;">
      <span style="background: #1e3a8a; color: #ffffff; padding: 6px 14px; border-radius: 20px; font-size: 0.85em; font-weight: 700; display: inline-block; margin-bottom: 8px;">
        Módulo 01
      </span><br>
      <span style="color: #64748b; font-size: 0.85em;">Docente: Santiago A. Zúñiga M.</span><br>
      <a href="mailto:gestorvirtualcienciadatos@ustatunja.edu.co" style="color: #2563eb; font-size: 0.8em; text-decoration: none; font-weight: 500;">gestorvirtualcienciadatos@ustatunja.edu.co</a>
    </td>
  </tr>
</table>

<div align="center" style="margin-top: 15px; margin-bottom: 15px;">
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/01%20-%20Python/06_Manipulacion_de_Cadenas_de_Texto.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## Cadenas de Caracteres en Python

El manejo de texto (strings) es una de las tareas más comunes en programación, especialmente en Ciencia de Datos para la limpieza de datos (Data Cleaning). En este notebook aprenderemos desde cómo declarar un texto, hasta cómo formatearlo, limpiarlo y validarlo de forma profesional.

---
### 1. Creación, Índices y Longitud 🌱

Las cadenas de caracteres se pueden definir con comillas simples, dobles o triples (para múltiples líneas). En Python, los *strings* son secuencias, lo que significa que podemos acceder a cada letra por su posición (índice).

```python
# Creación
simple = 'Hola'
doble = "Mundo"
multilinea = """
Este es un texto
que ocupa varias
líneas.
"""

mensaje = "Python"

# Acceso por índices (Empieza en 0)
print("Primera letra:", mensaje[0])
print("Tercera letra:", mensaje[2])

# Índices negativos (Empieza desde el final con -1)
print("Última letra:", mensaje[-1])

# Longitud de la cadena
print("Longitud total:", len(mensaje))
```

#### 🛠️ Práctica: Cadenas Básicas

**Problema:**
Dada la variable `palabra = "DataScience"`:
1. Imprime la longitud de la palabra.
2. Imprime la primera y la última letra utilizando índices positivos y/o negativos.

```python
palabra = "DataScience"

# Tu solución aquí
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
palabra = "DataScience"
print("Longitud:", len(palabra))
print("Primera letra:", palabra[0])
print("Última letra:", palabra[-1])
```

</details>

--- 
### 2. Slicing (Rebanado) y Operadores 🛠️

El *slicing* nos permite extraer subcadenas usando la sintaxis `[inicio:fin:paso]`. Además, podemos usar operadores matemáticos básicos como `+` (concatenar) y `*` (repetir).

```python
texto = "Programación"

# Slicing: [inicio : fin (no incluido)]
print("Primeras 4 letras:", texto[0:4])
print("Desde el índice 4 hasta el final:", texto[4:])

# Slicing con paso: [inicio : fin : paso]
print("Saltando de 2 en 2:", texto[0::2])

# Truco: Invertir un string rápidamente
print("Texto invertido:", texto[::-1])

# Concatenación y Repetición
saludo = "Hola" + " " + "Python"
eco = "Ja! " * 3

print("Concatenación:", saludo)
print("Repetición:", eco)
```

#### 🛠️ Práctica: Slicing y Operadores

**Problema:**
Tienes la cadena `codigo = "ID-12345-X"`.
Utilizando slicing, extrae:
1. Solo los números (`12345`) y guárdalos en `numeros`.
2. Imprime la cadena al revés usando slicing.

```python
codigo = "ID-12345-X"

# Tu solución aquí
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
codigo = "ID-12345-X"
numeros = codigo[3:8]
print("Números extraídos:", numeros)
print("Invertido:", codigo[::-1])
```

</details>

--- 
### 3. Limpieza, Transformación y Búsqueda 🧠

Python incluye potentes métodos integrados para procesar texto (muy útiles antes de guardar datos en una base de datos o modelo analítico).

```python
sucio = "   Hola, Este es un TEXTO.   "

# Limpieza de espacios en blanco (inicio y final)
limpio = sucio.strip()
print(f"Limpio: '{limpio}'")

# Transformación de mayúsculas/minúsculas
print("Mayúsculas:", limpio.upper())
print("Minúsculas:", limpio.lower())
print("Capitalizado:", limpio.capitalize())
print("Formato Título:", limpio.title())

# Reemplazar y Buscar
frase = "Me gusta el café, el té y el chocolate."
print("\nReemplazo:", frase.replace("el", "un"))
print("Conteo de 'el':", frase.count("el"))
print("Índice de 'café':", frase.find("café")) # Retorna -1 si no existe
```

#### 🛠️ Práctica: Limpieza de Textos

**Problema:**
Tienes un correo electrónico escrito por un usuario descuidado: `email_sucio = "   UsUaRiO@dominio.COM   "`.
1. Elimina los espacios en blanco sobrantes.
2. Conviértelo todo a minúsculas.
3. Imprime el correo ya limpio y listo para ser guardado.

```python
email_sucio = "   UsUaRiO@dominio.COM   "

# Tu solución aquí
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
email_sucio = "   UsUaRiO@dominio.COM   "

# Se pueden encadenar métodos
email_limpio = email_sucio.strip().lower()
print("Email correcto:", email_limpio)
```

</details>

--- 
### 4. Formateo de Cadenas 💎

Existen múltiples formas de inyectar variables dentro de un string, pero las **F-Strings** (introducidas en Python 3.6) son las más rápidas, legibles y recomendadas.

```python
nombre = "Ana"
edad = 28
pi = 3.14159265

# 1. Estilo Antiguo (%)
antiguo = "Hola, me llamo %s y tengo %d años." % (nombre, edad)

# 2. Estilo .format() (Python 3.0+)
medio = "Hola, me llamo {} y tengo {} años.".format(nombre, edad)

# 3. Estilo Moderno: f-strings (Python 3.6+) - ¡El Recomendado!
moderno = f"Hola, me llamo {nombre} y tengo {edad} años."

print("Antiguo:", antiguo)
print("Format: ", medio)
print("F-String:", moderno)

# Truco Pro con f-strings: Formateo numérico (redondear a 2 decimales)
print(f"\nEl valor de Pi redondeado es: {pi:.2f}")

# Truco Pro para Debugging (Python 3.8+)
print(f"{nombre=}, {edad=}")
```

#### 🛠️ Práctica: Formateo de Cadenas

**Ejercicio 1: Descuento**
Dadas las variables `producto = "Laptop"`, `precio = 1500.5` y `descuento = 0.15`.
Usa **F-strings** para imprimir un mensaje que diga:
`"El producto Laptop tiene un precio final de \\$1275.42"`
*(Nota: Debes calcular el precio restando el descuento y asegurarte de que el resultado se muestre exactamente con 2 decimales).*

```python
# Ejercicio 1
producto = "Laptop"
precio = 1500.5
descuento = 0.15
# Tu solución aquí
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
# Ejercicio 1
producto = "Laptop"
precio = 1500.5
descuento = 0.15
precio_final = precio * (1 - descuento)
print(f"El producto {producto} tiene un precio final de ${precio_final:.2f}")

print("\n" + "-"*30 + "\n")

```
</details>

**Ejercicio 2: Ticket de Compra**
Utiliza el método `.format()` para generar un ticket. Asegúrate de que el precio unitario y el total se muestren con dos decimales (`:.2f`), y la cantidad como entero (`:d`).

```python
# Ejercicio 2
producto_ticket = "Café de Especialidad"
cantidad = 3
precio_unitario = 15.5
precio_total = cantidad * precio_unitario

# Agrega los especificadores de formato dentro de las llaves {} donde sea necesario
ticket = "Compraste {} unidades de {} a ${} c/u. Total: ${}".format(
    cantidad, 
    producto_ticket, 
    precio_unitario, 
    precio_total
)
print(ticket)
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python


# Ejercicio 2
producto_ticket = "Café de Especialidad"
cantidad = 3
precio_unitario = 15.5
precio_total = cantidad * precio_unitario

ticket = "Compraste {:d} unidades de {} a ${:.2f} c/u. Total: ${:.2f}".format(
    cantidad, 
    producto_ticket, 
    precio_unitario, 
    precio_total
)
print(ticket)

print("\n" + "-"*30 + "\n")

```
</details>

**Ejercicio 3: Estadísticas Gamer**
En un videojuego, necesitas mostrar las estadísticas de un jugador en la pantalla. Transforma las variables en un solo mensaje utilizando f-strings asegurándote de que la tasa de victoria se muestre únicamente con dos decimales.

```python
# Ejercicio 3
jugador = "coder_ninja"
nivel = 42
tasa_victoria = 0.65873

# Reemplaza las comillas vacías con una f-string. El mensaje debe decir:
# "Jugador: coder_ninja | Nivel: 42 | Tasa de victoria: 0.66"
mensaje = ""
print(mensaje)
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python

# Ejercicio 3
jugador = "coder_ninja"
nivel = 42
tasa_victoria = 0.65873
mensaje = f"Jugador: {jugador} | Nivel: {nivel} | Tasa de victoria: {tasa_victoria:.2f}"
print(mensaje)
```
</details>

--- 
### 5. Separación/Unión y Validaciones 🏆

Dividir textos, volver a unirlos y comprobar qué tipo de caracteres contienen es esencial para parsear archivos CSV, Logs o cualquier texto estructurado.

```python
# Split: Convertir string a lista (Por defecto separa por espacios)
csv_line = "Carlos,25,Ingeniero,Madrid"
datos = csv_line.split(",")
print("Lista separada (split):", datos)

# Join: Unir elementos de una lista en un string usando un separador
nuevo_csv = ";".join(datos)
print("Nuevo string (join):", nuevo_csv)

# Validaciones de contenido
alfa = "Python"
num = "12345"
alfa_num = "Python3"

print("\n¿'Python' son solo letras?", alfa.isalpha())
print("¿'12345' son solo números?", num.isdigit())
print("¿'Python3' es alfanumérico?", alfa_num.isalnum())

# Validar inicios y finales (Muy útil para rutas de archivos o URLs)
archivo = "reporte_ventas.pdf"
print("\n¿Termina en .pdf?", archivo.endswith(".pdf"))
print("¿Empieza con 'reporte'?", archivo.startswith("reporte"))
```

#### 🛠️ Práctica: Separación y Validaciones

**Problema:**
Tienes la variable `ruta = "/usr/local/bin/python3"`.
1. Usa el método correcto para dividir la ruta usando el separador `/` e imprime la lista resultante.
2. Luego, extrae el último elemento de esa lista (el nombre del archivo, que será `python3`).
3. Valida e imprime si el nombre del archivo extraído es alfanumérico o no.

```python
ruta = "/usr/local/bin/python3"

# Tu solución aquí
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
ruta = "/usr/local/bin/python3"

# 1. Dividir
partes = ruta.split("/")
print("Partes:", partes)

# 2. Extraer archivo
archivo = partes[-1]
print("Archivo:", archivo)

# 3. Validar si es alfanumérico
print("¿Es alfanumérico?", archivo.isalnum())
```

</details>

---
### 🏆 Reto Integrador: Arregla la Cadena

En este ejercicio pondrás a prueba todo lo que aprendiste combinando índices, `len()`, `count()`, slicing, métodos de limpieza y más.

Intenta arreglar el código original (que falla) para que el `print()` muestre la información correcta, simplemente cambiando el valor de la variable `s`.

```python
# Cambia el valor de s para que las sentencias debajo funcionen correctamente
s = "Hey there! what should this string be?"

# La longitud debería ser 20
print("Longitud de s = %d" % len(s))

# La primera aparición de "a" debería estar en el índice 8
print("La primera aparición de la letra a = %d" % s.index("a"))

# El número de 'a's debería ser 2
print("a ocurre %d veces" % s.count("a"))

# Rebanando la cadena en pedazos
print("Los primeros cinco caracteres son '%s'" % s[:5]) # Del inicio al 5
print("Los siguientes cinco caracteres son '%s'" % s[5:10]) # Del 5 al 10
print("El decimotercer carácter es '%s'" % s[12]) # Solo el número 12
print("Los caracteres con índice impar son '%s'" %s[1::2]) #(Indexación basada en 0)
print("Los últimos cinco caracteres son '%s'" % s[-5:]) # Del 5to desde el final hasta el final

# Convertir todo a mayúsculas
print("Cadena en mayúsculas: %s" % s.upper())

# Convertir todo a minúsculas
print("Cadena en minúsculas: %s" % s.lower())

# Comprobar cómo comienza una cadena
if s.startswith("Str"):
    print("La cadena comienza con 'Str'. ¡Bien!")

# Comprobar cómo termina una cadena
if s.endswith("ome!"):
    print("La cadena termina con 'ome!'. ¡Bien!")

# Dividir la cadena en tres cadenas separadas,
# cada una conteniendo solo una palabra
print("Dividir las palabras de la cadena: %s" % s.split(" "))
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
# Solución al Reto
# Esta es una de las muchas cadenas que harían funcionar el código:
s = "Strings are awesome!"

# La longitud debería ser 20
print("Longitud de s = %d" % len(s))

# La primera aparición de "a" debería estar en el índice 8
print("La primera aparición de la letra a = %d" % s.index("a"))

# El número de 'a's debería ser 2
print("a ocurre %d veces" % s.count("a"))

# Rebanando la cadena en pedazos
print("Los primeros cinco caracteres son '%s'" % s[:5]) 
print("Los siguientes cinco caracteres son '%s'" % s[5:10]) 
print("El decimotercer carácter es '%s'" % s[12]) 
print("Los caracteres con índice impar son '%s'" %s[1::2]) 
print("Los últimos cinco caracteres son '%s'" % s[-5:]) 

# Convertir todo a mayúsculas
print("Cadena en mayúsculas: %s" % s.upper())

# Convertir todo a minúsculas
print("Cadena en minúsculas: %s" % s.lower())

if s.startswith("Str"):
    print("La cadena comienza con 'Str'. ¡Bien!")

if s.endswith("ome!"):
    print("La cadena termina con 'ome!'. ¡Bien!")

print("Dividir las palabras de la cadena: %s" % s.split(" "))
```
</details>

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos</i>
  </p>
</div>
