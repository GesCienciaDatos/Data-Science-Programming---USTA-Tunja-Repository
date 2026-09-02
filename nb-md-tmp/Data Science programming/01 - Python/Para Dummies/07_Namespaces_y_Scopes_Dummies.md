# 07_Namespaces_y_Scopes_Dummies

<table style="width: 100%; border-collapse: collapse; border: none; background: #fffbeb; border-left: 6px solid #f59e0b; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #78350f; font-size: 2em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        💡 07. Namespaces y Scopes (Ámbitos de Variables)
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
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/01%20-%20Python/Para%20Dummies/07_Namespaces_y_Scopes_Dummies.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## 1. ¿Qué es un Scope (Ámbito)? 🌐

### 💡 La Analogía del Nombre en tu Casa vs en el Mundo
Si en tu casa alguien grita: *"¡Mamá!"*, todos saben a quién se refiere porque están en el **ámbito local** de tu casa.
Pero si sales a la plaza principal de Tunja y gritas *"¡Mamá!"*, nadie sabrá de quién hablas.
En cambio, el Presidente del país tiene un nombre **global** que todos en cualquier rincón del territorio reconocen.

En Python ocurre lo mismo: **las variables creadas dentro de una función solo existen y se reconocen dentro de esa función (Locales)**. Las variables creadas afuera son visibles en todo el archivo (Globales).

```python
# Variable Global:
tasa_iva_nacional = 0.19  # Visible en todo el programa

def calcular_factura(subtotal):
    # Variable Local: solo vive mientras esta función se ejecuta
    valor_iva_local = subtotal * tasa_iva_nacional
    total = subtotal + valor_iva_local
    return total

print("Factura de $100,000:", calcular_factura(100000))
print("Tasa IVA Global:", tasa_iva_nacional)

# Si intentas hacer: print(valor_iva_local) afuera, Python dará error porque no existe afuera.
```

---
## 2. La Regla LEGB de Búsqueda de Variables 🔍

Cuando usas una variable, Python la busca en este orden estricto:

| Letra | Nivel de Ámbito | 💡 Significado Cotidiano |
|---|---|---|
| **L** | **Local** | Lo que está definido dentro de la función actual. |
| **E** | **Enclosing** | Lo que está en una función externa que contiene a otra función. |
| **G** | **Global** | Lo que está definido en el nivel principal del archivo. |
| **B** | **Built-in** | Las funciones nativas que ya vienen instaladas con Python (`print`, `len`, `sum`, `range`). |

```python
# Demostración del alcance LEGB:
variable_global = "🌍 Soy la variable GLOBAL"

def funcion_externa():
    variable_enclosing = "🏠 Soy la variable ENCLOSING (Función Externa)"
    
    def funcion_interna():
        variable_local = "🚪 Soy la variable LOCAL (Habitación propia)"
        print(variable_local)
        print(variable_enclosing)
        print(variable_global)
        
    funcion_interna()

funcion_externa()
```

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos (Edición Para No Ingenieros)</i>
  </p>
</div>
