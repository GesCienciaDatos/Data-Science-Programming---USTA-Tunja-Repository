# 00_Introduccion_y_Conceptos_Basicos

<table style="width: 100%; border-collapse: collapse; border: none; background: #f8fafc; border-left: 6px solid #1e3a8a; border-radius: 8px; padding: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">
  <tr style="border: none;">
    <td style="vertical-align: middle; border: none; padding: 15px 20px;">
      <h1 style="margin: 0; color: #0f172a; font-size: 2.1em; font-family: system-ui, -apple-system, sans-serif; font-weight: 800; letter-spacing: -0.02em;">
        Introducción a Python y Conceptos Básicos 🐍
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
  <a href="https://colab.research.google.com/github/sazuniga06/Data-Science-Programming---USTA-Tunja-Repository/blob/main/Data%20Science%20programming/01%20-%20Python/00_Introduccion_y_Conceptos_Basicos.ipynb" target="_parent">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align: middle;"/>
  </a>
</div>

---
## Objetivos de Aprendizaje 🔎

En este primer módulo sentaremos las bases fundamentales del lenguaje **Python**, con un enfoque 100% orientado al análisis, procesamiento y la Ciencia de Datos. El material está organizado de forma progresiva en los siguientes cuadernos interactivos:

1. **[Introducción y Conceptos Básicos](00_Introduccion_y_Conceptos_Basicos.ipynb)** *(Este cuaderno)*: Fundamentos de la programación, pensamiento algorítmico y el rol de Python en Data Science.
2. **[Sintaxis, Variables y Tipos de Datos](01_Sintaxis_Variables_y_Tipos_de_Datos.ipynb)**: Reglas de sintaxis, variables, operadores aritméticos/lógicos y tipos primitivos (`int`, `float`, `bool`, `str`).
3. **[Estructuras Nativas I: Listas, Tuplas y Conjuntos](02a_Estructuras_Listas_Tuplas_Conjuntos.ipynb)**: Colecciones ordenadas, inmutables y conjuntos no duplicados.
4. **[Estructuras Nativas II: Diccionarios](02b_Estructuras_Diccionarios.ipynb)**: Estructuras clave-valor para mapeo y recuperación eficiente de información.
5. **[Flujo de Control](03_Flujo_de_Control.ipynb)**: Lógica condicional (`if`, `elif`, `else`) y ciclos de iteración (`for`, `while`, `comprehensions`).
6. **[Funciones](04_Funciones.ipynb)**: Modularización, paso de parámetros (`*args`, `**kwargs`), funciones anónimas (`lambda`) y funciones puras.
7. **[Clases y Objetos](05_Clases_y_Objetos.ipynb)** 🧗: Programación Orientada a Objetos (POO), métodos especiales (`dunder methods`) y encapsulamiento.
8. **[Manipulación de Cadenas de Texto](06_Manipulacion_de_Cadenas_de_Texto.ipynb)**: Métodos de limpieza de texto, `f-strings`, formateo y expresiones regulares básicas.
9. **[Namespaces y Scopes](07_Namespaces_y_Scopes.ipynb)** 🧗: La regla LEGB (Local, Enclosing, Global, Built-in) y el ciclo de vida de variables en memoria.
10. **[Módulos y Paquetes](08_Modulos_y_Paquetes.ipynb)**: Estructura de proyectos, importaciones y aprovechamiento de la biblioteca estándar de Python.

> 🧗 **Nota:** Los temas con mayor nivel de abstracción y complejidad están identificados con el ícono de escalador.

---
## Recursos Recomendados 📚

### 📖 Libros de Referencia:
- [Python Crash Course: A Hands-On, Project-Based Introduction to Programming](https://ehmatthes.github.io/pcc/) — *Eric Matthes*
- [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/) — *Al Sweigart*
- [Fluent Python: Clear, Concise, and Effective Programming](https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/) — *Luciano Ramalho*

### 🌐 Enlaces y Documentación Oficial:
- [Documentación Oficial de Python 3 (Tutorial en Español)](https://docs.python.org/es/3/tutorial/)
- [Real Python Tutorials (Guías prácticas de alto nivel)](https://realpython.com/)
- [The Python Enhancement Proposals (PEP 8 — Guía de Estilo Oficial)](https://peps.python.org/pep-0008/)

---
## 1. ¿Qué es la Programación y el Pensamiento Computacional? 💻

La **programación** es el proceso de diseñar, escribir, probar y mantener instrucciones precisas (código fuente) que una computadora puede ejecutar para resolver un problema específico o automatizar una tarea.

El **pensamiento computacional** se compone de cuatro pilares fundamentales aplicados a la Ciencia de Datos:
1. **Descomposición:** Dividir un problema complejo (ej. predecir el precio de una vivienda) en subproblemas más pequeños (adquisición, limpieza, ingeniería de variables, modelado y evaluación).
2. **Reconocimiento de Patrones:** Identificar tendencias, distribuciones estadísticas y correlaciones en los datos o en la lógica de negocio.
3. **Abstracción:** Enfocarse en las variables verdaderamente relevantes y filtrar el ruido o detalles secundarios irrelevantes.
4. **Diseño de Algoritmos:** Desarrollar una secuencia lógica paso a paso, determinista y replicable para procesar la información.

> 📌 **Concepto Clave:** En Ciencia de Datos, programar no se trata solo de escribir sintaxis, sino de traducir preguntas de investigación empíricas en pipelines computacionales robustos y reproducibles.

---
## 2. ¿Por qué Python es el Lenguaje Líder en Ciencia de Datos? 🐍

Python fue creado por **Guido van Rossum** a principios de los años 90 con una filosofía centrada en la **legibilidad y elegancia del código** (*"Readability counts"* — El Zen de Python).

Hoy en día es el estándar absoluto de la industria en Ciencia de Datos, Inteligencia Artificial y Machine Learning gracias a:
* 📉 **Sintaxis Expresiva y Limpia:** Reduce la sobrecarga cognitiva permitiendo a los científicos enfocarse en la modelación matemática.
* 📦 **Ecosistema Científico Inigualable:** Integración nativa con librerías de alto rendimiento escritas en C/C++ y Fortran (`NumPy`, `Pandas`, `Matplotlib`, `Seaborn`, `Scikit-Learn`, `PyTorch`, `TensorFlow`).
* 🌍 **Comunidad Global y Estandarización:** Millones de desarrolladores, documentación abierta y repositorio masivo de paquetes (`PyPI`).
* ⚡ **Versatilidad Integral:** Desde scripts de automatización e ingesta de datos hasta arquitecturas distribuidas y despliegue de APIs productivas.

---
## 3. Características Técnicas Clave de Python ⚙️

| Característica | Descripción Técnica | Impacto en Data Science |
|---|---|---|
| **Lenguaje Interpretado** | El código se compila a *bytecode* y se ejecuta instrucción por instrucción mediante la máquina virtual de Python (CPython), sin compilación estática previa. | Prototipado rápido y exploración interactiva mediante cuadernos Jupyter. |
| **Tipado Dinámico** | Los tipos de datos se asocian a los objetos en memoria en tiempo de ejecución, no a los identificadores de variables. | Máxima agilidad al manipular datos de tipos mixtos. |
| **Tipado Fuerte** | Python no realiza conversiones de tipo implícitas no seguras (ej. `'5' + 3` genera `TypeError`). | Previene errores silenciosos y corrupción de valores en pipelines analíticos. |
| **Multiplataforma** | El mismo código se ejecuta idénticamente en Linux, macOS y Windows. | Fácil migración desde entornos de desarrollo locales a servidores en la nube o clusters. |
| **Gestión Automática de Memoria** | Emplea conteo de referencias y un recolector de basura (*Garbage Collector*) cíclico. | Liberación automática de recursos sin gestión manual de punteros. |

---
## Configuración del Entorno y Verificación 🛠️

Verifiquemos que nuestro entorno de ejecución de Python y Jupyter esté correctamente configurado.

```python
import sys
import platform

# Configuración de interacción en Jupyter Notebooks
try:
    from IPython.core.interactiveshell import InteractiveShell
    InteractiveShell.ast_node_interactivity = "all"
except ImportError:
    pass

print("✅ Entorno de Python configurado correctamente.")
print(f"🐍 Versión de Python: {platform.python_version()}")
print(f"💻 Sistema Operativo: {platform.system()} {platform.release()} ({platform.machine()})")
print(f"📍 Ruta del intérprete: {sys.executable}")
```

---
### Tu Primera Instrucción en Python

La función nativa `print()` envía un mensaje o valor formateado a la salida estándar.

```python
# Mensaje de bienvenida
mensaje = "¡Bienvenidos al curso de Programación para Ciencia de Datos! 🚀"
print(mensaje)
```

---
<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Programación para Ciencia de Datos</i>
  </p>
</div>
