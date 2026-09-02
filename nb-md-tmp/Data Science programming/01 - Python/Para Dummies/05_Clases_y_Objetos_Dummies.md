# 05_Clases_y_Objetos_Dummies

<table style="width: 100%; border-collapse: collapse; border: none; background: #fffbeb; border-left: 6px solid #f59e0b; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #78350f; font-size: 2em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        💡 05. Clases y Objetos (POO)
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
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/01%20-%20Python/Para%20Dummies/05_Clases_y_Objetos_Dummies.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## ¿Qué es la Programación Orientada a Objetos (POO)? 🍪

La Programación Orientada a Objetos puede sonar a un concepto intimidante de ingeniería de software, pero en realidad es **la forma más natural de modelar la vida real en código**.

### 💡 La Analogía del Molde de Galletas y las Galletas:
- **La Clase (`class`):** Es el **molde metálico** con forma de estrella. El molde define cómo serán todas las estrellas (tendrán 5 puntas, tamaño estándar, masa de vainilla).
- **El Objeto (Instancia):** Es cada **galleta real horneada**. Una galleta puede tener chispas de chocolate, otra glaseado de fresa, otra puede estar decorada con azúcar... pero todas nacieron del mismo molde y comparten la misma estructura básica.

---
### Conceptos Clave sin Complicaciones:
* **Atributos (Características / Sustantivos):** Lo que el objeto *tiene* (ej. `marca`, `color`, `saldo`, `velocidad_maxima`).
* **Métodos (Acciones / Verbos):** Lo que el objeto *puede hacer* (ej. `acelerar()`, `frenar()`, `depositar()`, `calcular_interes()`).
* **`self`:** Significa *"yo mismo"*. Es la forma en que cada galleta se refiere a sus propios datos sin confundirse con la galleta del lado.

```python
# 1. Definimos el molde (Clase CuentaBancaria):
class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        '''El constructor: se ejecuta cada vez que creamos una cuenta nueva.'''
        self.titular = titular        # Atributo
        self.saldo = saldo_inicial    # Atributo
    
    def depositar(self, cantidad):
        '''Método para sumar dinero'''
        if cantidad > 0:
            self.saldo += cantidad
            print(f"💵 ${cantidad:,.2f} depositados en la cuenta de {self.titular}. Saldo actual: ${self.saldo:,.2f}")
        else:
            print("⚠️ El monto a depositar debe ser mayor a 0.")
            
    def retirar(self, cantidad):
        '''Método para sacar dinero'''
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"🏧 ${cantidad:,.2f} retirados. Saldo restante: ${self.saldo:,.2f}")
        else:
            print(f"❌ Fondos insuficientes. Intentaste retirar ${cantidad:,.2f} pero solo tienes ${self.saldo:,.2f}")

# 2. Horneamos 2 objetos reales a partir del molde:
cuenta_carlos = CuentaBancaria("Carlos Mendoza", 50000)
cuenta_valeria = CuentaBancaria("Valeria Torres", 200000)

print(f"Cuenta 1: {cuenta_carlos.titular} tiene ${cuenta_carlos.saldo:,.2f}")
print(f"Cuenta 2: {cuenta_valeria.titular} tiene ${cuenta_valeria.saldo:,.2f}")
```

---
### Probando los Métodos de Nuestras Cuentas 💳

```python
# Carlos deposita dinero:
cuenta_carlos.depositar(30000)

# Valeria hace un retiro:
cuenta_valeria.retirar(75000)

# Carlos intenta retirar más de lo que tiene:
cuenta_carlos.retirar(150000)
```

---
## 2. Herencia: Reutilizar Moldes Existentes 🧬

### 💡 La Analogía de la Herencia Familiar
Un automóvil y una motocicleta son ambos **Vehículos** (tienen motor, frenos, velocidad). En lugar de construir todo desde cero, creamos una clase base `Vehiculo` y luego clases hijas que heredan todo lo bueno y agregan sus detalles particulares.

```python
# Clase Padre:
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def describir(self):
        return f"🚗 Vehículo: {self.marca} {self.modelo}"

# Clase Hija (Hereda de Vehiculo):
class AutoElectrico(Vehiculo):
    def __init__(self, marca, modelo, autonomia_km):
        super().__init__(marca, modelo)  # Llama al molde padre
        self.autonomia_km = autonomia_km # Característica propia
        
    def describir(self):
        base = super().describir()
        return f"{base} | ⚡ 100% Eléctrico con autonomía de {self.autonomia_km} km"

mi_tesla = AutoElectrico("Tesla", "Model Y", 510)
print(mi_tesla.describir())
```

---
## 🛠️ Práctica: Sistema de Productos para una Tienda

**Problema:**
Crea una clase llamada `Producto` que tenga:
- Atributos: `nombre`, `precio_unitario`, `stock`.
- Un método `vender(unidades)` que reste el stock si hay suficiente disponibilidad y muestre el total a pagar, o avise si no hay suficiente inventario.
- Pruébala creando un producto `"Laptop Gamer"` con precio de `\\$3,500,000` y stock de `5` unidades.

```python
# Solución guiada:
class Producto:
    def __init__(self, nombre, precio_unitario, stock):
        self.nombre = nombre
        self.precio_unitario = precio_unitario
        self.stock = stock
        
    def vender(self, unidades):
        if unidades <= self.stock:
            self.stock -= unidades
            total = unidades * self.precio_unitario
            print(f"✅ Venta exitosa: {unidades} unidades de '{self.nombre}' por un total de ${total:,.2f}.")
            print(f"📦 Stock restante: {self.stock} unidades.")
        else:
            print(f"❌ Stock insuficiente de '{self.nombre}'. Solicitaste {unidades} pero solo quedan {self.stock}.")

# Prueba:
laptop = Producto("Laptop Gamer", 3500000, 5)
laptop.vender(2)
laptop.vender(4)  # Debe avisar que no alcanza
```

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos (Edición Para No Ingenieros)</i>
  </p>
</div>
