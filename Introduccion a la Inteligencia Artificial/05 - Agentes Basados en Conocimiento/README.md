# Módulo 05: Agentes Basados en Conocimiento 🧠⚙️

<p align="center">
  <img src="https://img.shields.io/badge/Discipline-Logica%20Proposicional-4f46e5?style=for-the-badge&logo=semanticweb&logoColor=white" alt="Lógica Proposicional"/>
  <img src="https://img.shields.io/badge/Process-Model%20Checking%20%26%20Resolucion-0ea5e9?style=for-the-badge" alt="Process"/>
  <img src="https://img.shields.io/badge/Course-Introduccion%20a%20la%20IA-6366f1?style=for-the-badge" alt="Course"/>
  <img src="https://img.shields.io/badge/Institution-USTA%20Tunja-1e3a8a?style=for-the-badge" alt="USTA"/>
</p>

Bienvenido al módulo más orientado a **código** de la asignatura **Introducción a la Inteligencia Artificial** de la *Especialización en Ciencia de Datos* de la **Universidad Santo Tomás — Seccional Tunja**.

---

## 🧭 ¿Qué son los Agentes Basados en Conocimiento?

Un **agente basado en conocimiento** (*knowledge-based agent*) es un agente inteligente cuyo componente central es una **base de conocimiento**: un conjunto de sentencias, escritas en un lenguaje de representación formal, que describen hechos sobre el mundo y que el agente combina —mediante un motor de inferencia— para deducir información que nunca fue programada explícitamente.

En este módulo construimos, **desde cero y en Python puro** (sin librerías externas de lógica simbólica), toda la maquinaria necesaria para representar conocimiento con **lógica proposicional**, verificarlo mediante **model checking** por fuerza bruta, y realizar inferencia eficiente mediante **Forma Normal Conjuntiva (CNF)** y **resolución**.

---

## 📚 Estructura Curricular del Módulo

### 🎓 1. Cuadernos Académicos Estándar:
1. [**00_Logica_Proposicional_y_Agentes.ipynb**](00_Logica_Proposicional_y_Agentes.ipynb): Agentes basados en conocimiento (TELL/ASK), sintaxis de la lógica proposicional, modelos y mundos posibles, implicación lógica y verificación de modelos por fuerza bruta.
2. [**01_Bases_de_Conocimiento_en_Python.ipynb**](01_Bases_de_Conocimiento_en_Python.ipynb): Patrón de implementación de bases de conocimiento en Python, con los casos aplicados de razonamiento por descarte y encadenamiento de reglas.
3. [**02_Inferencia_CNF_y_Resolucion.ipynb**](02_Inferencia_CNF_y_Resolucion.ipynb): Costo computacional del model checking, encadenamiento hacia adelante/atrás, conversión a Forma Normal Conjuntiva (CNF) y resolución como regla de inferencia, con dos acertijos lógicos resueltos y comparados.

---

### 📝 2. Taller Práctico Evaluativo (*Hands-On*):
* [**../homeworks/05_Agentes_Conocimiento_Hands_On.ipynb**](../homeworks/05_Agentes_Conocimiento_Hands_On.ipynb): Ejercicio evaluativo integrador sobre construcción de bases de conocimiento, verificación de modelos y resolución.

---

### 🧸 3. Ruta Didáctica: Para Dummies:
Ubicada en la subcarpeta [`Para Dummies/`](Para%20Dummies/):
1. [**00_Logica_Proposicional_Dummies.ipynb**](Para%20Dummies/00_Logica_Proposicional_Dummies.ipynb): ¡Enséñale a pensar a la computadora! El detective de bolsillo que revisa todos los universos posibles.
2. [**01_Bases_Conocimiento_Dummies.ipynb**](Para%20Dummies/01_Bases_Conocimiento_Dummies.ipynb): Armando historias con lógica: la doctora de turno y la clase que se vuelve virtual por la lluvia.
3. [**02_CNF_Resolucion_Dummies.ipynb**](Para%20Dummies/02_CNF_Resolucion_Dummies.ipynb): El truco rápido del detective: cómo resolver acertijos sin revisar universo por universo.

---

## 🐍 Librería y Casos de Aplicación en Python

En la raíz de este módulo se incluyen 5 archivos standalone, ejecutables de forma independiente con `python3 archivo.py`:

* [`logic.py`](logic.py): mini-librería de lógica proposicional construida desde cero (sin dependencias externas de lógica simbólica). Implementa las clases `Symbol`, `Not`, `And`, `Or`, `Implication` y `Biconditional` (cada una con `.evaluate(model)` y `.formula()`), el motor de verificación de modelos por fuerza bruta `model_check()`, y el pipeline completo de conversión a Forma Normal Conjuntiva (`to_cnf`, `to_clauses`) junto con el algoritmo de inferencia por resolución (`resolve`, `resolution_entails`). Es la base que reutilizan los tres cuadernos estándar.
* [`medico_o_clase.py`](medico_o_clase.py): caso de razonamiento por descarte — ¿la doctora Camila está de turno o en clase de anatomía?
* [`programando.py`](programando.py): caso de encadenamiento de reglas — un agente decide si la sesión de laboratorio se dicta de forma presencial o virtual según el clima.
* [`futbol.py`](futbol.py): acertijo lógico — ¿qué equipo ganó el partido?, resuelto y comparado con `model_check` y `resolution_entails`.
* [`perdidos.py`](perdidos.py): acertijo lógico — ¿cuál de los tres estudiantes se perdió en la salida de campo?, resuelto y comparado con `model_check` y `resolution_entails`.

---

<div align="center">
  <p style="font-size: 0.9em; color: #64748b;">
    © 2026 <b>Universidad Santo Tomás — Seccional Tunja</b><br>
    <i>Especialización en Ciencia de Datos | Asignatura: Introducción a la Inteligencia Artificial</i>
  </p>
</div>
