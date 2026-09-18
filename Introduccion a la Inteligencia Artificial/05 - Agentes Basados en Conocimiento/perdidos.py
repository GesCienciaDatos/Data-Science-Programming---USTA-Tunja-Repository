"""
perdidos.py
===========
Caso de aplicación: acertijo lógico de ubicación ("¿quién se perdió?"),
resuelto de DOS maneras distintas -y comparadas entre sí- con la mini-
librería logic.py:

    1. Verificación de modelos por fuerza bruta (model_check).
    2. Inferencia por Resolución sobre la Forma Normal Conjuntiva
       (resolution_entails).

Contexto del acertijo:
  Durante una salida de campo geológica, el guía nota que exactamente UNO
  de los tres estudiantes -Ana, Beto o Caro- se perdió en la montaña (los
  tres casos son mutuamente excluyentes: no pudieron perderse dos a la vez).

  Pistas recogidas por el guía:
    Pista 1: El guía vio personalmente a Beto cruzando el río a las 3:00 pm,
             por lo tanto Beto NO se perdió.
    Pista 2: Ana envió un mensaje de texto confirmando que llegó sana y
             salva al campamento base, por lo tanto Ana NO se perdió.

  Pregunta: ¿fue Caro quien se perdió?

Ejecutar:  python3 perdidos.py
"""

from logic import (
    Symbol, Not, And, Or, model_check, resolution_entails,
    to_cnf, to_clauses, formula_of_clause,
)

# --- Símbolos proposicionales -----------------------------------------
PA = Symbol("AnaPerdida")   # "Ana se perdió"
PB = Symbol("BetoPerdido")  # "Beto se perdió"
PC = Symbol("CaroPerdida")  # "Caro se perdió"

# --- Base de conocimiento -----------------------------------------------
knowledge = And(
    Or(PA, PB, PC),         # Alguno de los tres se perdió.
    Not(And(PA, PB)),       # Exclusión mutua: no pudieron perderse Ana y Beto a la vez.
    Not(And(PA, PC)),       # Exclusión mutua: no pudieron perderse Ana y Caro a la vez.
    Not(And(PB, PC)),       # Exclusión mutua: no pudieron perderse Beto y Caro a la vez.
    Not(PB),                # Pista 1: el guía vio a Beto cruzando el río -> Beto no se perdió.
    Not(PA),                # Pista 2: Ana confirmó por mensaje que llegó al campamento.
)


def main():
    print("=" * 70)
    print("CASO: ¿Quién se perdió en la salida de campo? 🧭 (Model Checking vs. Resolución)")
    print("=" * 70)
    print(f"\nBase de conocimiento (pistas del guía):\n  {knowledge.formula()}")

    cnf = to_cnf(knowledge)
    clausulas = to_clauses(cnf)
    print("\nForma Normal Conjuntiva (CNF) de la base de conocimiento:")
    for c in clausulas:
        print(f"  {formula_of_clause(c)}")

    query = PC
    resultado_mc = model_check(knowledge, query)
    resultado_res = resolution_entails(knowledge, query)

    print(f"\nConsulta: '¿Se perdió Caro?' -> {query.formula()}")
    print(f"  [Model Checking / fuerza bruta] -> {resultado_mc}")
    print(f"  [Resolución sobre CNF]          -> {resultado_res}")

    assert resultado_mc is True
    assert resultado_res is True
    assert resultado_mc == resultado_res

    print("\n✅ Ambos métodos de inferencia coinciden: ¡Caro fue quien se perdió!")


if __name__ == "__main__":
    main()
