"""
programando.py
===============
Caso de aplicación: un agente basado en conocimiento que decide cómo se
dicta la sesión de laboratorio de programación según el clima.

Reglas del mundo:
  1. Hay clase de campo (salida a terreno) SI Y SOLO SI no llueve.
  2. Si NO hay clase de campo, la sesión se dicta de manera virtual.
  3. Hoy, el reporte meteorológico confirma que SÍ está lloviendo.

A partir de estas tres reglas, un agente basado en conocimiento debe poder
encadenar la inferencia: llueve -> no hay clase de campo -> sesión virtual,
sin que nadie se lo diga explícitamente. Eso es exactamente lo que hace
model_check() al enumerar todos los mundos posibles.

Ejecutar:  python3 programando.py
"""

from logic import Symbol, Not, And, Implication, Biconditional, model_check

# --- Símbolos proposicionales -----------------------------------------
LLUEVE = Symbol("Llueve")                  # "Hoy llueve"
CLASE_CAMPO = Symbol("ClaseDeCampo")       # "Hoy hay clase de campo"
SESION_VIRTUAL = Symbol("SesionVirtual")   # "La sesión se dicta de forma virtual"

# --- Base de conocimiento -----------------------------------------------
knowledge = And(
    Biconditional(CLASE_CAMPO, Not(LLUEVE)),        # Regla 1: clase de campo <-> no llueve.
    Implication(Not(CLASE_CAMPO), SESION_VIRTUAL),  # Regla 2: sin clase de campo -> virtual.
    LLUEVE                                           # Hecho observado: hoy llueve.
)


def main():
    print("=" * 70)
    print("CASO: ¿Cómo se dicta hoy el laboratorio de programación? 🌧️💻")
    print("=" * 70)
    print(f"\nBase de conocimiento:\n  {knowledge.formula()}")

    consultas = {
        "¿Llueve hoy?": LLUEVE,
        "¿Hay clase de campo hoy?": CLASE_CAMPO,
        "¿NO hay clase de campo hoy?": Not(CLASE_CAMPO),
        "¿La sesión se dicta de forma virtual?": SESION_VIRTUAL,
    }

    print("\nInferencias (model_check por fuerza bruta):")
    resultados = {}
    for pregunta, query in consultas.items():
        resultado = model_check(knowledge, query)
        resultados[pregunta] = resultado
        print(f"  {pregunta:<42} -> {resultado}")

    # --- Verificaciones de consistencia lógica --------------------------
    assert resultados["¿Llueve hoy?"] is True
    assert resultados["¿Hay clase de campo hoy?"] is False
    assert resultados["¿NO hay clase de campo hoy?"] is True
    assert resultados["¿La sesión se dicta de forma virtual?"] is True

    print("\n✅ Conclusión: el agente encadenó tres reglas y dedujo, sin ayuda "
          "externa, que la sesión de hoy se dicta de forma VIRTUAL.")


if __name__ == "__main__":
    main()
