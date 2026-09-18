"""
medico_o_clase.py
==================
Caso de aplicación: razonamiento por descarte con lógica proposicional.

Camila es estudiante de la Especialización y, además, médica general. Un día
cualquiera puede estar de turno en el hospital O tener clase de anatomía,
pero nunca ambas cosas al mismo tiempo. Sabemos con certeza que hoy es
miércoles, día en el que SIEMPRE tiene clase de anatomía obligatoria.

Este caso reproduce el clásico patrón de "razonamiento por descarte" (muy
usado en los cursos introductorios de IA basada en lógica): a partir de una
restricción de exclusión mutua y un hecho observado, el motor de inferencia
por fuerza bruta (model_check) deduce automáticamente el resto de hechos.

Ejecutar:  python3 medico_o_clase.py
"""

from logic import Symbol, Not, And, Or, model_check

# --- Símbolos proposicionales -----------------------------------------
MD = Symbol("MedicaDeTurno")     # "Camila es médica de turno hoy"
CL = Symbol("ClaseDeAnatomia")   # "Camila tiene clase de anatomía hoy"

# --- Base de conocimiento -----------------------------------------------
knowledge = And(
    Not(And(MD, CL)),  # Regla 1: no puede ser médica de turno y estar en clase a la vez.
    Or(MD, CL),         # Regla 2: hoy Camila está de turno o está en clase (una de las dos).
    CL                  # Hecho observado: hoy es miércoles, así que SÍ tiene clase de anatomía.
)


def main():
    print("=" * 70)
    print("CASO: ¿Camila es médica de turno o está en clase? 🩺📚")
    print("=" * 70)
    print(f"\nBase de conocimiento:\n  {knowledge.formula()}")

    consultas = {
        "¿Camila NO es médica de turno hoy?": Not(MD),
        "¿Camila SÍ es médica de turno hoy?": MD,
        "¿Camila tiene clase de anatomía hoy?": CL,
    }

    print("\nInferencias (model_check por fuerza bruta):")
    resultados = {}
    for pregunta, query in consultas.items():
        resultado = model_check(knowledge, query)
        resultados[pregunta] = resultado
        print(f"  {pregunta:<42} -> {resultado}")

    # --- Verificaciones de consistencia lógica --------------------------
    assert resultados["¿Camila NO es médica de turno hoy?"] is True
    assert resultados["¿Camila SÍ es médica de turno hoy?"] is False
    assert resultados["¿Camila tiene clase de anatomía hoy?"] is True

    print("\n✅ Conclusión: la base de conocimiento IMPLICA que Camila NO está de "
          "turno hoy (está en clase de anatomía). Todas las aserciones se cumplieron.")


if __name__ == "__main__":
    main()
