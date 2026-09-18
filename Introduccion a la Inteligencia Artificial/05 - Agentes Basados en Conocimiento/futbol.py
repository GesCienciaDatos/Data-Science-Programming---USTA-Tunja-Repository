"""
futbol.py
=========
Caso de aplicación: acertijo lógico sobre el resultado de un partido de
fútbol, resuelto de DOS maneras distintas -y comparadas entre sí- con la
mini-librería logic.py:

    1. Verificación de modelos por fuerza bruta (model_check).
    2. Inferencia por Resolución sobre la Forma Normal Conjuntiva
       (resolution_entails).

Contexto del acertijo:
  El partido entre el equipo Local y el equipo Visitante terminó, y solo
  puede haber ocurrido UNO de estos tres resultados: ganó el Local, ganó el
  Visitante, o hubo Empate (mutuamente excluyentes).

  Pistas recogidas por los periodistas:
    Pista 1: Hubo un gol marcado en el minuto 90 que definió el partido,
             por lo tanto NO terminó en empate.
    Pista 2: Las estadísticas oficiales confirman que el equipo Local no
             logró anotar ningún gol en todo el partido, por lo tanto NO
             ganó el Local.

  Pregunta: ¿ganó el equipo Visitante?

Ejecutar:  python3 futbol.py
"""

from logic import (
    Symbol, Not, And, Or, model_check, resolution_entails,
    to_cnf, to_clauses, formula_of_clause,
)

# --- Símbolos proposicionales -----------------------------------------
LOCAL = Symbol("GanaLocal")            # "Ganó el equipo Local"
VISITANTE = Symbol("GanaVisitante")    # "Ganó el equipo Visitante"
EMPATE = Symbol("Empate")              # "El partido terminó en empate"

# --- Base de conocimiento -----------------------------------------------
knowledge = And(
    Or(LOCAL, VISITANTE, EMPATE),      # Debe ocurrir al menos uno de los 3 resultados.
    Not(And(LOCAL, VISITANTE)),        # Exclusión mutua: no pueden ganar ambos equipos.
    Not(And(LOCAL, EMPATE)),           # Exclusión mutua: ganar Local excluye el empate.
    Not(And(VISITANTE, EMPATE)),       # Exclusión mutua: ganar Visitante excluye el empate.
    Not(EMPATE),                       # Pista 1: hubo gol en el min. 90 -> no fue empate.
    Not(LOCAL),                        # Pista 2: el Local no anotó ningún gol -> no ganó el Local.
)


def main():
    print("=" * 70)
    print("CASO: ¿Quién ganó el partido? ⚽ (Model Checking vs. Resolución)")
    print("=" * 70)
    print(f"\nBase de conocimiento (pistas del partido):\n  {knowledge.formula()}")

    cnf = to_cnf(knowledge)
    clausulas = to_clauses(cnf)
    print("\nForma Normal Conjuntiva (CNF) de la base de conocimiento:")
    for c in clausulas:
        print(f"  {formula_of_clause(c)}")

    query = VISITANTE
    resultado_mc = model_check(knowledge, query)
    resultado_res = resolution_entails(knowledge, query)

    print(f"\nConsulta: '¿Ganó el equipo Visitante?' -> {query.formula()}")
    print(f"  [Model Checking / fuerza bruta] -> {resultado_mc}")
    print(f"  [Resolución sobre CNF]          -> {resultado_res}")

    assert resultado_mc is True
    assert resultado_res is True
    assert resultado_mc == resultado_res

    print("\n✅ Ambos métodos de inferencia coinciden: ¡ganó el equipo VISITANTE!")


if __name__ == "__main__":
    main()
