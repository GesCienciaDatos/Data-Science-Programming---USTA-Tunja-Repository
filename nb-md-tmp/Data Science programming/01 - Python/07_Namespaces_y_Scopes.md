# 07_Namespaces_y_Scopes

<table style="width: 100%; border-collapse: collapse; border: none; background: #f8fafc; border-left: 6px solid #1e3a8a; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #0f172a; font-size: 2.1em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        Namespaces, Ámbitos y la Regla LEGB en Python 🔍
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
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/01%20-%20Python/07_Namespaces_y_Scopes.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

## Namespaces y Scopes en Python

### 1. Fundamentos de Namespaces y Scopes 🌱

#### 1.1 ¿Qué es un Namespace y un Scope?
Comprender cómo Python guarda y busca las variables detrás de escena es uno de los pasos más importantes para dominar el lenguaje y evitar errores lógicos frustrantes. Aquí es donde entran en juego dos conceptos íntimamente relacionados: los **Namespaces** y los **Scopes**.

*   **Namespace (Espacio de Nombres):** Imagina que es un diccionario interno gigante que Python mantiene en la memoria. Las "claves" son los nombres que tú le das a tus variables o funciones, y los "valores" son los objetos reales en la memoria. Python utiliza diferentes Namespaces simultáneamente para asegurar que dos variables llamadas exactamente igual no colisionen si están en contextos distintos.
*   **Scope (Alcance):** Es la zona física o la región estricta de tu código donde un Namespace en particular es accesible directamente. Es decir, el Scope dicta desde qué línea hasta qué línea existe tu variable y dónde puedes llamarla.

> 🤓 **La Regla LEGB:** Cuando intentas acceder a una variable, Python no busca a ciegas. Sigue una jerarquía de Scopes muy estricta y ascendente conocida como la regla **LEGB**. Busca en este orden exacto y se detiene en el momento en que encuentra el nombre:
> 1.  **L**ocal (Local): Nombres asignados de cualquier forma dentro de la función actual.
> 2.  **E**nclosing (Envolvente/Anidado): Nombres en el Scope de cualquier función "padre" que envuelva a la función actual.
> 3.  **G**lobal (Global): Nombres asignados en el nivel superior de un archivo de módulo.
> 4.  **B**uilt-in (Integrado): Nombres preasignados por el propio Python (como `print()`, `len()`, `True`).

---

#### 1.2 Construyendo y Usando Scopes

*   **Variables de Scope Local:** Cada vez que llamas a una función, Python crea un nuevo Namespace exclusivo para ella. Cualquier variable creada allí nace y muere dentro de esa función. Desde el exterior, esa variable simplemente no existe.
*   **Variables de Scope Global:** Se definen en el cuerpo principal de tu archivo (`script`). Son excelentes para constantes o configuraciones generales, ya que cualquier función dentro del archivo puede **leerlas**. Sin embargo, si intentas **modificarlas** directamente dentro de una función, Python pensará que quieres crear una variable *Local* nueva con el mismo nombre.
*   **La palabra clave `global`:** Es un permiso explícito. Si la usas dentro de una función (ej. `global mi_variable`), le estás diciendo a Python: *"No crees una variable local nueva, búscame la del Scope Global y déjame modificarla"*.
*   **La palabra clave `nonlocal`:** Se utiliza exclusivamente cuando tienes funciones anidadas (una función dentro de otra). Le dice a Python: *"Quiero modificar la variable de la función padre (Scope Enclosing), no la Global, ni crear una nueva Local"*.

---

#### 1.3 Estructura y Sintaxis

| Palabra Clave / Contexto | Función Principal | Sintaxis de Ejemplo |
| :--- | :--- | :--- |
| **Local** (Por defecto) | Crea/Modifica variables solo en la función actual. | `x = 10` (dentro de `def`) |
| **Lectura Global** | Lee la variable exterior sin modificarla. | `print(variable_exterior)` |
| **`global`** | Da permisos para modificar una variable Global. | `global contador` <br> `contador += 1` |
| **`nonlocal`** | Da permisos para modificar una variable Enclosing. | `nonlocal texto_padre` <br> `texto_padre = "nuevo"` |
---

### 2. La Regla LEGB 🛠️

#### 2.1 Entendiendo la Regla LEGB (Solo lectura)
Vamos a ver cómo Python busca una variable de adentro hacia afuera si no la encuentra localmente.

```python
x = "Soy GLOBAL"

def funcion_padre():
    # Descomenta la siguiente línea para ver cómo Python se detiene en el Scope Enclosing
    # x = "Soy ENCLOSING"
    
    def funcion_hija():
        # Descomenta la siguiente línea para ver cómo Python se detiene en el Scope Local
        # x = "Soy LOCAL"
        
        # Python busca 'x' aquí adentro (Local). Si no está, sube a la función padre (Enclosing).
        # Si tampoco está, sube al archivo (Global). Si no está, busca en las palabras de Python (Built-in).
        print(x) 

    funcion_hija()

# Esto imprimirá "Soy GLOBAL" a menos que desmarques las variables internas.
funcion_padre()
```

--- 
### 3. Modificando Scopes con `global` y `nonlocal` 🧠

Leer es fácil, pero para modificar el comportamiento cambia por seguridad.

```python
# --- USO DE GLOBAL ---
vidas_jugador = 3

def perder_vida():
    # Sin la palabra 'global', Python daría el error "UnboundLocalError" al intentar restar
    global vidas_jugador 
    vidas_jugador -= 1
    print(f"Perdiste una vida. Te quedan: {vidas_jugador}")

perder_vida() # Salida: Te quedan 2


# --- USO DE NONLOCAL ---
def crear_cuenta():
    saldo = 100 # Esta variable está en el Scope Enclosing de hacer_retiro()
    
    def hacer_retiro(cantidad):
        # Necesitamos nonlocal para modificar 'saldo' que pertenece a crear_cuenta()
        nonlocal saldo 
        if cantidad <= saldo:
            saldo -= cantidad
            print(f"Retiro exitoso. Nuevo saldo: ${saldo}")
        else:
            print("Fondos insuficientes.")
            
    # Llamamos a la función interna
    hacer_retiro(40)

crear_cuenta() # Salida: Retiro exitoso. Nuevo saldo: $60
```

### 🛠️ Práctica: Namespaces y Scopes

Estás desarrollando la lógica de un carrito de compras. Tienes una variable global total_compras que lleva el registro del dinero total gastado en la sesión. Además, tienes una función principal `iniciar_carrito` que contiene una función anidada `agregar_producto`.

Tu objetivo es usar las palabras clave `global` y `nonlocal` de forma correcta para que la función anidada logre actualizar ambas variables sin causar errores.

```python
total_compras = 0.0

def iniciar_carrito():
    cantidad_articulos = 0 # Scope Enclosing
    
    def agregar_producto(precio):
        # 1. Tu código va aquí:
        # Declara que vas a modificar la variable global 'total_compras'
        
        
        # 2. Tu código va aquí:
        # Declara que vas a modificar la variable envolvente 'cantidad_articulos'
        
        
        # Simulamos la suma del producto
        total_compras += precio
        cantidad_articulos += 1
        print(f"Agregado 1 artículo. Llevas {cantidad_articulos} artículos. Total: ${total_compras}")

    # Simulamos agregar un par de productos
    agregar_producto(15.50)
    agregar_producto(20.00)

# Código de prueba
iniciar_carrito()

# El resultado final debería imprimir:
# Agregado 1 artículo. Llevas 1 artículos. Total: $15.5
# Agregado 1 artículo. Llevas 2 artículos. Total: $35.5
```

<details>
<summary><b>💡 Haz clic aquí para ver la solución guiada...</b></summary>

```python
total_compras = 0.0

def iniciar_carrito():
    cantidad_articulos = 0 # Scope Enclosing
    
    def agregar_producto(precio):
        # 1. Tu código va aquí:
        global total_compras
        
        # 2. Tu código va aquí:
        nonlocal cantidad_articulos
        
        # Simulamos la suma del producto
        total_compras += precio
        cantidad_articulos += 1
        print(f"Agregado 1 artículo. Llevas {cantidad_articulos} artículos. Total: ${total_compras}")

    # Simulamos agregar un par de productos
    agregar_producto(15.50)
    agregar_producto(20.00)

iniciar_carrito()
```
</details>

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos</i>
  </p>
</div>
