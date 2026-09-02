# 05_Clases_y_Objetos

<table style="width: 100%; border-collapse: collapse; border: none; background: #f8fafc; border-left: 6px solid #1e3a8a; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #0f172a; font-size: 2.1em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        Programación Orientada a Objetos (POO) en Python 🏛️
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
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/01%20-%20Python/05_Clases_y_Objetos.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---

## Fundamentos de POO: Clases y Objetos 

Los **objetos** son una encapsulación de variables y funciones en una sola entidad. Los objetos obtienen sus variables y funciones de las clases. Las **clases** son esencialmente una plantilla (o molde) para crear tus objetos.

> 🤓 **¿Por qué usar Clases y Objetos?:** La programación orientada a objetos (POO) permite organizar el código de manera modular y reutilizable. Encapsula datos y funcionalidades relacionadas en una sola unidad (haciendo el código más fácil de mantener). En Python, la POO es opcional, pero radicalmente útil para ahorrar tiempo de desarrollo en proyectos a largo plazo.

---

**Desglose de Componentes**

* **Definición de Clase (`class`):** Se utiliza la palabra clave `class` seguida del nombre para crear la plantilla. Todo lo que esté indentado debajo formará parte de esta estructura.
* **Instanciación de Objetos:** Es el proceso de crear un objeto individual a partir de la clase (ej. `mi_objeto = MiClase()`). Cada objeto contiene copias independientes de las variables de la clase matriz.
* **Atributos (Variables de Objeto):** Variables asociadas al objeto. Definen su estado o características y se accede a ellas usando la notación de punto (ej. `mi_objeto.variable`).
* **Métodos (Funciones de Objeto):** Funciones definidas dentro de la clase que describen el comportamiento del objeto. Al igual que los atributos, se llaman con un punto (ej. `mi_objeto.funcion()`).
* **El Constructor (`__init__`):** Es una función especial que se llama automáticamente cuando la clase está siendo instanciada. Se utiliza para asignar los valores iniciales. Requiere el parámetro `self` para referirse al objeto mismo.

---

**Estructura y Sintaxis**

| Componente | Descripción | Sintaxis Básica |
| :--- | :--- | :--- |
| **`class`** | Declaración de la plantilla inicial. | `class MiClase:` |
| **Instanciación** | Asignación de la clase a un objeto. | `objeto = MiClase()` |
| **Atributos** | Acceso y modificación de variables. | `objeto.variable = "valor"` |
| **Métodos** | Llamada a acciones/funciones del objeto. | `objeto.metodo()` |
| **Constructor** | Función de inicio para asignar valores. | `def __init__(self, param):` |

### 1. Definiendo una Clase y Creando Objetos
Una clase muy básica se vería algo así:

```python
class MiClase:
    variable = "blah"

    def funcion(self):
        print("Este es un mensaje dentro de la clase.")
```

Explicaremos por qué tienes que incluir ese `self` como parámetro un poco más adelante. Primero, para asignar la clase anterior (plantilla) a un objeto, harías lo siguiente:

```python
class MiClase:
    variable = "blah"

    def funcion(self):
        print("Este es un mensaje dentro de la clase.")

mi_objetox = MiClase()
```

Ahora la variable `mi_objetox` contiene un objeto de la clase `MiClase` que incluye la variable y la función definidas dentro de dicha clase.

---

### 2. Accediendo a Variables y Funciones

Para acceder a la variable dentro del objeto recién creado `mi_objetox`, harías lo siguiente:

```python
class MiClase:
    variable = "blah"

    def funcion(self):
        print("Este es un mensaje dentro de la clase.")

mi_objetox = MiClase()
print(mi_objetox.variable)
```

Puedes crear múltiples objetos diferentes que sean de la misma clase (es decir, que tengan las mismas variables y funciones definidas). Sin embargo, cada objeto contiene copias independientes de las variables. Por ejemplo, si definiéramos otro objeto con la clase `MiClase` y luego cambiáramos el string en la variable:

```python
class MiClase:
    variable = "blah"

    def funcion(self):
        print("Este es un mensaje dentro de la clase.")

mi_objetox = MiClase()
mi_objetoy = MiClase()

mi_objetoy.variable = "yackity"

# Luego imprimimos ambos valores
print(mi_objetox.variable)
print(mi_objetoy.variable)
```

Para acceder a una función dentro de un objeto, usas una notación similar a la de acceder a una variable:

```python
class MiClase:
    variable = "blah"

    def funcion(self):
        print("Este es un mensaje dentro de la clase.")

mi_objetox = MiClase()
mi_objetox.funcion()
```

### 3. El Constructor (`__init__`) y `self`

La función `__init__()` es una función especial que se llama automáticamente cuando la clase está siendo instanciada (cuando se crea el objeto). Se utiliza principalmente para asignar valores iniciales en una clase (el constructor).

```python
class ContenedorNumeros:
   def __init__(self, numero):
       self.numero = numero

   def retornar_numero(self):
       return self.numero

var = ContenedorNumeros(7)
print(var.retornar_numero()) # Imprime '7'
```

---
### **🤓 ¿Por qué usar clases y objetos?**

La programación orientada a objetos (POO - el uso de clases y objetos) es útil porque permite a los programadores organizar el código de una manera modular y reutilizable.

En la POO, el código se organiza alrededor de objetos, que son instancias de clases. Cada objeto tiene sus propias propiedades y métodos que definen su comportamiento. Esto nos permite encapsular datos y funcionalidades relacionadas en una sola unidad, haciendo que el código sea más fácil de entender, mantener y modificar. Además, la POO permite la **herencia**, lo que significa que podemos crear una nueva clase que herede propiedades y métodos de una clase existente. Esto puede ahorrar tiempo y reducir la duplicación de código, ya que podemos reutilizar la funcionalidad y personalizarla según sea necesario.

Una nota por adelantado: en Python, la POO es completamente opcional, y no necesitas usar clases para empezar. Puedes lograr mucho con construcciones más simples como funciones, o scripts de nivel superior. Debido a que usar bien las clases requiere algo de planificación inicial, tienden a ser de mayor interés para quienes trabajan en modo estratégico (desarrollo a largo plazo) que para quienes trabajan en modo táctico (donde el tiempo es muy escaso). Aún así, las clases resultan ser una de las herramientas más útiles de Python. Cuando se usan bien, pueden reducir radicalmente el tiempo de desarrollo.

---
### 4. Un ejemplo del mundo real

Digamos que queremos crear un programa para representar autos. Podemos usar clases y objetos para hacer esto.

Primero, creamos una clase llamada `Auto` que defina las propiedades y métodos de un auto. Esta clase podría tener propiedades como `marca`, `modelo` y `color`, así como métodos como `encender_motor` y `apagar_motor`.

```python
class Auto:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.motor_encendido = False

    def encender_motor(self):
        if not self.motor_encendido:
            self.motor_encendido = True
            print("Motor encendido.")
        else:
            print("El motor ya está encendido.")

    def apagar_motor(self):
        if self.motor_encendido:
            self.motor_encendido = False
            print("Motor apagado.")
        else:
            print("El motor ya está apagado.")
```

Luego, podemos crear una instancia de la clase `Auto`, que podemos pensar como un auto individual. Este objeto tendrá sus propios valores para las propiedades definidas en la clase.

```python
# Crear una nueva instancia de la clase Auto
mi_auto = Auto("Toyota", "Camry", "azul")
```

Podemos llamar a los métodos definidos en la clase `Auto` sobre nuestro objeto `mi_auto`.

```python
# Llamar al método encender_motor en el objeto mi_auto
mi_auto.encender_motor()

# ¡Y también podemos apagar el motor!
mi_auto.apagar_motor()
```

Al usar clases y objetos, podemos crear múltiples instancias, cada una con su propio conjunto único de valores, y ejecutar métodos en cada objeto de forma individual.

```python
auto_de_riccardo = Auto("Fiat", "Punto", "Negro")
```

#### 🛠️ Práctica: Clases Básicas

**Ejercicio 1:**
Crea una clase llamada `Libro` que reciba en su `__init__` el `titulo` y el `autor`. Añade un método llamado `mostrar_info` que imprima un mensaje como: `"El libro '1984' fue escrito por George Orwell"`. Finalmente, instancia un libro y llama a su método `mostrar_info`.

```python
# Ejercicio 1
# Tu solución aquí
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
# Ejercicio 1
class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        
    def mostrar_info(self):
        print(f"El libro '{self.titulo}' fue escrito por {self.autor}")

mi_libro = Libro("Cien años de soledad", "Gabriel García Márquez")
mi_libro.mostrar_info()


print("\n" + "-"*30 + "\n")

```
</details>

**Ejercicio 2:**
Tenemos una clase definida para vehículos (`Vehiculo`).
Crea dos nuevos vehículos instanciando la clase (llamados `auto1` y `auto2`).
Configura sus variables internas de forma que:
- `auto1` sea un auto convertible rojo que valga \\$60,000.00 con el nombre de "Fer".
- `auto2` sea una camioneta azul llamada "Jump" que valga \\$10,000.00.
Finalmente, llama al método `.descripcion()` en ambos e imprímelo.

```python
# Ejercicio 2
class Vehiculo:
    nombre = ""
    tipo = "auto"
    color = ""
    valor = 100.00

    def descripcion(self):
        desc_str = "%s es un(a) %s %s que vale $%.2f." % (self.nombre, self.tipo, self.color, self.valor)
        return desc_str

# Tu código para auto1 y auto2 va aquí


# Código de prueba
# print(auto1.descripcion())
# print(auto2.descripcion())
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python

# Ejercicio 2
class Vehiculo:
    nombre = ""
    tipo = "auto"
    color = ""
    valor = 100.00

    def descripcion(self):
        desc_str = "%s es un(a) %s %s que vale $%.2f." % (self.nombre, self.tipo, self.color, self.valor)
        return desc_str

auto1 = Vehiculo()
auto1.nombre = "Fer"
auto1.tipo = "convertible"
auto1.color = "rojo"
auto1.valor = 60000.00

auto2 = Vehiculo()
auto2.nombre = "Jump"
auto2.tipo = "camioneta"
auto2.color = "azul"
auto2.valor = 10000.00

print(auto1.descripcion())
print(auto2.descripcion())
```
</details>

--- 
### 5. Atributos de Clase y Encapsulamiento 🛠️

A diferencia de los atributos de instancia (propios de cada objeto), los **atributos de clase** se comparten entre todos los objetos. Además, en Python usamos guiones bajos `_` o `__` para indicar que un atributo o método es **privado** (encapsulamiento por convención).

```python
class CuentaBancaria:
    # Atributo de Clase (Compartido por todas las cuentas)
    banco = "Banco Pythonico"
    
    def __init__(self, titular, saldo):
        self.titular = titular
        # Un guión bajo indica que es un atributo 'protegido' (convención)
        # Dos guiones bajos lo hacen 'privado' (name mangling)
        self.__saldo = saldo 
        
    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            
    def consultar_saldo(self):
        return self.__saldo

cuenta = CuentaBancaria("Ana", 1000)
cuenta.depositar(500)

print("Banco:", CuentaBancaria.banco) # Acceso al atributo de clase
print("Saldo Seguro:", cuenta.consultar_saldo())

# Si intentamos imprimir cuenta.__saldo directamente, dará un error AttributeError
# print(cuenta.__saldo)
```

#### 🛠️ Práctica: Atributos y Encapsulamiento

**Problema:**
Crea una clase `Coche` con un atributo de clase `ruedas = 4`. En el constructor, inicializa la `marca` (pública) y el `__kilometraje` (privado) empezando en 0.
Añade un método `conducir(km)` que sume los kilómetros al kilometraje privado, y un método `mostrar_estado()` que imprima la marca, la cantidad de ruedas y los kilómetros recorridos.

```python
# Tu solución aquí
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
class Coche:
    ruedas = 4
    
    def __init__(self, marca):
        self.marca = marca
        self.__kilometraje = 0
        
    def conducir(self, km):
        if km > 0:
            self.__kilometraje += km
            
    def mostrar_estado(self):
        print(f"{self.marca} | {Coche.ruedas} ruedas | {self.__kilometraje} km")

mi_coche = Coche("Toyota")
mi_coche.conducir(150)
mi_coche.mostrar_estado()
```

</details>

--- 
### 6. Herencia y Polimorfismo 🧠

La **Herencia** permite crear nuevas clases basadas en clases existentes (reutilizando su código). El **Polimorfismo** permite que clases hijas tengan métodos con el mismo nombre pero comportamientos distintos.

```python
# Clase Padre (Superclase)
class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def trabajar(self):
        return f"{self.nombre} está realizando labores generales."

# Clase Hija (Subclase) hereda de Empleado
class Desarrollador(Empleado):
    def __init__(self, nombre, salario, lenguaje):
        # super() llama al __init__ de la clase padre
        super().__init__(nombre, salario)
        self.lenguaje = lenguaje

    # Sobreescritura de método (Polimorfismo)
    def trabajar(self):
        return f"{self.nombre} está escribiendo código en {self.lenguaje}."

emp_normal = Empleado("Carlos", 2000)
dev = Desarrollador("Ana", 3500, "Python")

print(emp_normal.trabajar())
print(dev.trabajar())
```

#### 🛠️ Práctica: Herencia y Polimorfismo

**Problema:**
Tenemos una clase padre `Figura` con el método `area()` que simplemente retorna 0.
Crea una clase hija `Cuadrado` que herede de `Figura`. Su constructor debe recibir el `lado`. Sobreescribe el método `area()` para que devuelva el área real del cuadrado (lado * lado).

```python
class Figura:
    def area(self):
        return 0

# Tu solución aquí
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
class Figura:
    def area(self):
        return 0

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado
        
    def area(self):
        return self.lado ** 2

cuad = Cuadrado(5)
print("Área del cuadrado:", cuad.area())
```

</details>

--- 
### 7. Decoradores de Clase (@property, @classmethod, @staticmethod) 💎

- `@property`: Permite usar un método como si fuera un atributo (ideal para getters/setters elegantes sin romper código viejo).
- `@classmethod`: Método que recibe la clase misma (`cls`) en lugar de la instancia (`self`). Útil para constructores alternativos.
- `@staticmethod`: Método utilitario que no usa ni la instancia ni la clase.

```python
class Temperatura:
    def __init__(self, celsius):
        self._celsius = celsius

    # Transforma el método en un atributo de solo lectura
    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32

    # Método de clase (Constructor alternativo)
    @classmethod
    def desde_fahrenheit(cls, f):
        c = (f - 32) * 5/9
        return cls(c)

    # Método estático (No recibe ni self ni cls)
    @staticmethod
    def es_valida(celsius):
        return celsius >= -273.15  # Cero absoluto

t1 = Temperatura(25)
print("Fahrenheit:", t1.fahrenheit) # Sin paréntesis! Se accede como atributo

t2 = Temperatura.desde_fahrenheit(100)
print("Celsius de T2:", t2._celsius)

print("¿Es válido -300C?", Temperatura.es_valida(-300))
```

#### 🛠️ Práctica: Decoradores de Clase

**Problema:**
Crea una clase `Usuario` que guarde un `_username` privado.
1. Usa `@property` para exponer un método `username` que devuelva el `_username` en mayúsculas.
2. Usa `@staticmethod` para crear una función `validar_username(user)` que retorne True si el string tiene más de 4 letras.

```python
# Tu solución aquí
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
class Usuario:
    def __init__(self, username):
        self._username = username
        
    @property
    def username(self):
        return self._username.upper()
        
    @staticmethod
    def validar_username(user):
        return len(user) > 4

u = Usuario("paco")
print("Username Property:", u.username)
print("¿Es válido 'paco'?", Usuario.validar_username("paco"))
print("¿Es válido 'alberto'?", Usuario.validar_username("alberto"))
```

</details>

--- 
### 8. Métodos Mágicos (Dunder Methods) 🏆

Los *Dunder methods* (Double Underscore) permiten que nuestros objetos interactúen con las funciones integradas de Python, como si fueran tipos nativos. (Ej: `len()`, `print()`, el operador `+`, etc).

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Modifica lo que sale cuando hacemos print() o str()
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    # Permite sumar dos vectores con el operador '+'
    def __add__(self, otro_vector):
        return Vector(self.x + otro_vector.x, self.y + otro_vector.y)

    # Permite verificar si dos vectores son iguales con '=='
    def __eq__(self, otro_vector):
        return self.x == otro_vector.x and self.y == otro_vector.y

v1 = Vector(2, 4)
v2 = Vector(3, 1)

print("Impresión amigable:", v1)

v3 = v1 + v2
print("Suma de vectores:", v3)

print("¿Son iguales v1 y v2?", v1 == v2)
```

#### 🛠️ Práctica: Métodos Mágicos

**Problema:**
Crea una clase `Playlist` que reciba en el constructor un atributo `canciones` (una lista de strings).
Implementa el método mágico `__len__` de modo que si hacemos `len(mi_playlist)`, devuelva la cantidad de canciones en la lista.
Implementa el método mágico `__str__` para que al hacer print, devuelva: `"Playlist con X canciones"`.

```python
# Tu solución aquí
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
class Playlist:
    def __init__(self, canciones):
        self.canciones = canciones
        
    def __len__(self):
        return len(self.canciones)
        
    def __str__(self):
        return f"Playlist con {len(self.canciones)} canciones"

mi_lista = Playlist(["Bohemian Rhapsody", "Hotel California", "Stairway to Heaven"])
print("Largo (len):", len(mi_lista))
print("String:", mi_lista)
```

</details>

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos</i>
  </p>
</div>
