"""
logic.py
=========
Mini-librería de Lógica Proposicional en Python puro, construida desde cero
(sin dependencias externas de lógica simbólica) para el Módulo 05 —
"Agentes Basados en Conocimiento" de la asignatura Introducción a la
Inteligencia Artificial (Especialización en Ciencia de Datos, USTA Tunja).

Provee:
    * Clases para representar sentencias de lógica proposicional:
        Symbol, Not, And, Or, Implication, Biconditional
      Cada una implementa:
        - evaluate(model): evalúa la sentencia bajo un modelo (dict símbolo->bool)
        - formula():        representación textual en notación infija
        - symbols():        conjunto de símbolos atómicos involucrados

    * model_check(knowledge, query): motor de verificación de modelos por
      fuerza bruta que determina si  knowledge ⊨ query  (la base de
      conocimiento implica lógicamente la consulta), enumerando TODOS los
      modelos posibles sobre los símbolos involucrados.

    * Utilidades de Forma Normal Conjuntiva (CNF) y Resolución:
        to_cnf(sentence):        convierte una sentencia a CNF.
        to_clauses(cnf_sentence): aplana una sentencia CNF en una lista de
                                   cláusulas (cada cláusula = frozenset de
                                   literales (nombre, polaridad)).
        resolve(c1, c2):          aplica la regla de resolución entre dos
                                   cláusulas y devuelve el conjunto de
                                   resolventes.
        resolution_entails(knowledge, query): algoritmo de inferencia por
                                   refutación mediante resolución (PL-Resolution).

Autor: Material docente — Especialización en Ciencia de Datos, USTA Tunja.
"""

from itertools import combinations


# ---------------------------------------------------------------------------
# 1. JERARQUÍA DE SENTENCIAS (Sintaxis de la Lógica Proposicional)
# ---------------------------------------------------------------------------

class Sentence:
    """Clase base abstracta para toda sentencia de lógica proposicional."""

    def evaluate(self, model):
        raise NotImplementedError("Las subclases deben implementar evaluate().")

    def formula(self):
        raise NotImplementedError("Las subclases deben implementar formula().")

    def symbols(self):
        raise NotImplementedError("Las subclases deben implementar symbols().")

    def __repr__(self):
        return self.formula()

    @staticmethod
    def _parenthesize(sub):
        """Envuelve en paréntesis la fórmula de una sub-sentencia compuesta
        para que la representación textual sea inequívoca."""
        if isinstance(sub, (Symbol, Not)):
            return sub.formula()
        return f"({sub.formula()})"


class Symbol(Sentence):
    """Un símbolo proposicional atómico, p. ej. Symbol('Llueve')."""

    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return isinstance(other, Symbol) and self.name == other.name

    def __hash__(self):
        return hash(("symbol", self.name))

    def evaluate(self, model):
        try:
            return bool(model[self.name])
        except KeyError:
            raise EvaluationException(f"El símbolo '{self.name}' no está definido en el modelo.")

    def formula(self):
        return self.name

    def symbols(self):
        return {self.name}


class Not(Sentence):
    """Negación lógica: ¬operand."""

    def __init__(self, operand):
        self.operand = operand

    def __eq__(self, other):
        return isinstance(other, Not) and self.operand == other.operand

    def __hash__(self):
        return hash(("not", self.operand))

    def evaluate(self, model):
        return not self.operand.evaluate(model)

    def formula(self):
        return "¬" + self._parenthesize(self.operand)

    def symbols(self):
        return self.operand.symbols()


class And(Sentence):
    """Conjunción lógica variádica: c1 ∧ c2 ∧ ... ∧ cn."""

    def __init__(self, *conjuncts):
        if len(conjuncts) == 0:
            raise ValueError("And requiere al menos un operando.")
        self.conjuncts = list(conjuncts)

    def __eq__(self, other):
        return isinstance(other, And) and self.conjuncts == other.conjuncts

    def __hash__(self):
        return hash(("and", tuple(self.conjuncts)))

    def evaluate(self, model):
        return all(c.evaluate(model) for c in self.conjuncts)

    def formula(self):
        if len(self.conjuncts) == 1:
            return self._parenthesize(self.conjuncts[0])
        return " ∧ ".join(self._parenthesize(c) for c in self.conjuncts)

    def symbols(self):
        result = set()
        for c in self.conjuncts:
            result |= c.symbols()
        return result


class Or(Sentence):
    """Disyunción lógica variádica: d1 ∨ d2 ∨ ... ∨ dn."""

    def __init__(self, *disjuncts):
        if len(disjuncts) == 0:
            raise ValueError("Or requiere al menos un operando.")
        self.disjuncts = list(disjuncts)

    def __eq__(self, other):
        return isinstance(other, Or) and self.disjuncts == other.disjuncts

    def __hash__(self):
        return hash(("or", tuple(self.disjuncts)))

    def evaluate(self, model):
        return any(d.evaluate(model) for d in self.disjuncts)

    def formula(self):
        if len(self.disjuncts) == 1:
            return self._parenthesize(self.disjuncts[0])
        return " ∨ ".join(self._parenthesize(d) for d in self.disjuncts)

    def symbols(self):
        result = set()
        for d in self.disjuncts:
            result |= d.symbols()
        return result


class Implication(Sentence):
    """Implicación material: antecedent → consequent."""

    def __init__(self, antecedent, consequent):
        self.antecedent = antecedent
        self.consequent = consequent

    def __eq__(self, other):
        return (isinstance(other, Implication)
                and self.antecedent == other.antecedent
                and self.consequent == other.consequent)

    def __hash__(self):
        return hash(("implies", self.antecedent, self.consequent))

    def evaluate(self, model):
        return (not self.antecedent.evaluate(model)) or self.consequent.evaluate(model)

    def formula(self):
        return f"{self._parenthesize(self.antecedent)} → {self._parenthesize(self.consequent)}"

    def symbols(self):
        return self.antecedent.symbols() | self.consequent.symbols()


class Biconditional(Sentence):
    """Bicondicional: left ↔ right (equivalencia lógica)."""

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __eq__(self, other):
        return (isinstance(other, Biconditional)
                and self.left == other.left
                and self.right == other.right)

    def __hash__(self):
        return hash(("iff", self.left, self.right))

    def evaluate(self, model):
        return self.left.evaluate(model) == self.right.evaluate(model)

    def formula(self):
        return f"{self._parenthesize(self.left)} ↔ {self._parenthesize(self.right)}"

    def symbols(self):
        return self.left.symbols() | self.right.symbols()


class EvaluationException(Exception):
    """Se lanza cuando un modelo no asigna un valor a un símbolo requerido."""
    pass


# ---------------------------------------------------------------------------
# 2. VERIFICACIÓN DE MODELOS POR FUERZA BRUTA (MODEL CHECKING)
# ---------------------------------------------------------------------------

def enumerate_models(symbols):
    """Genera, uno a uno, TODOS los modelos posibles (2^n) para el conjunto
    de nombres de símbolos dado. Cada modelo es un dict {nombre: bool}."""
    symbols = sorted(symbols)
    n = len(symbols)
    for bits in range(2 ** n):
        model = {}
        for i, name in enumerate(symbols):
            model[name] = bool((bits >> i) & 1)
        yield model


def model_check(knowledge, query):
    """Determina, por fuerza bruta, si  knowledge ⊨ query  (la base de
    conocimiento implica lógicamente la consulta).

    Enumera TODOS los mundos posibles (2^n, con n = número de símbolos
    involucrados) y verifica que en TODO modelo donde `knowledge` es
    verdadera, `query` también lo sea. Si no existe ningún modelo donde
    knowledge sea verdadera, la implicación se considera vacuamente cierta.
    """
    symbols = knowledge.symbols() | query.symbols()

    def check_all(remaining_symbols, model):
        if not remaining_symbols:
            if knowledge.evaluate(model):
                return query.evaluate(model)
            return True  # Vacuamente verdadero: knowledge es falsa en este modelo.
        remaining = set(remaining_symbols)
        p = remaining.pop()

        model_true = dict(model)
        model_true[p] = True
        model_false = dict(model)
        model_false[p] = False

        return check_all(remaining, model_true) and check_all(remaining, model_false)

    return check_all(symbols, {})


# ---------------------------------------------------------------------------
# 3. FORMA NORMAL CONJUNTIVA (CNF) Y RESOLUCIÓN
# ---------------------------------------------------------------------------
#
# Pipeline clásico de conversión a CNF (equivalente al usado en libros de
# texto de IA como Russell & Norvig):
#   1) Eliminar bicondicionales:  a ↔ b   ==>  (a → b) ∧ (b → a)
#   2) Eliminar implicaciones:    a → b   ==>  ¬a ∨ b
#   3) Mover las negaciones hacia adentro (Leyes de De Morgan + doble negación)
#   4) Distribuir ∨ sobre ∧ hasta obtener una conjunción de disyunciones.
# ---------------------------------------------------------------------------

def _eliminate_biconditional(s):
    if isinstance(s, Symbol):
        return s
    if isinstance(s, Not):
        return Not(_eliminate_biconditional(s.operand))
    if isinstance(s, And):
        return And(*[_eliminate_biconditional(c) for c in s.conjuncts])
    if isinstance(s, Or):
        return Or(*[_eliminate_biconditional(d) for d in s.disjuncts])
    if isinstance(s, Implication):
        return Implication(_eliminate_biconditional(s.antecedent),
                            _eliminate_biconditional(s.consequent))
    if isinstance(s, Biconditional):
        left = _eliminate_biconditional(s.left)
        right = _eliminate_biconditional(s.right)
        return And(Implication(left, right), Implication(right, left))
    raise TypeError(f"Tipo de sentencia no soportado: {type(s)}")


def _eliminate_implication(s):
    if isinstance(s, Symbol):
        return s
    if isinstance(s, Not):
        return Not(_eliminate_implication(s.operand))
    if isinstance(s, And):
        return And(*[_eliminate_implication(c) for c in s.conjuncts])
    if isinstance(s, Or):
        return Or(*[_eliminate_implication(d) for d in s.disjuncts])
    if isinstance(s, Implication):
        a = _eliminate_implication(s.antecedent)
        b = _eliminate_implication(s.consequent)
        return Or(Not(a), b)
    raise TypeError(f"Sentencia inesperada (¿bicondicional sin eliminar?): {type(s)}")


def _move_not_inward(s):
    if isinstance(s, Symbol):
        return s
    if isinstance(s, Not):
        operand = s.operand
        if isinstance(operand, Symbol):
            return Not(operand)
        if isinstance(operand, Not):
            return _move_not_inward(operand.operand)  # ¬¬a == a
        if isinstance(operand, And):
            return Or(*[_move_not_inward(Not(c)) for c in operand.conjuncts])
        if isinstance(operand, Or):
            return And(*[_move_not_inward(Not(d)) for d in operand.disjuncts])
        raise TypeError(f"No se esperaba {type(operand)} bajo una negación en esta etapa.")
    if isinstance(s, And):
        return And(*[_move_not_inward(c) for c in s.conjuncts])
    if isinstance(s, Or):
        return Or(*[_move_not_inward(d) for d in s.disjuncts])
    raise TypeError(f"Sentencia inesperada: {type(s)}")


def _distribute_or_over_and(s):
    if isinstance(s, Symbol):
        return s
    if isinstance(s, Not) and isinstance(s.operand, Symbol):
        return s
    if isinstance(s, And):
        return And(*[_distribute_or_over_and(c) for c in s.conjuncts])
    if isinstance(s, Or):
        parts = [_distribute_or_over_and(d) for d in s.disjuncts]
        for i, p in enumerate(parts):
            if isinstance(p, And):
                others = parts[:i] + parts[i + 1:]
                other = Or(*others) if others else None
                new_conjuncts = []
                for c in p.conjuncts:
                    combined = Or(c, other) if other is not None else c
                    new_conjuncts.append(_distribute_or_over_and(combined))
                return _distribute_or_over_and(And(*new_conjuncts))
        return Or(*parts)
    raise TypeError(f"Sentencia inesperada: {type(s)}")


def _flatten(s):
    """Aplana anidamientos redundantes de And-dentro-de-And y Or-dentro-de-Or
    generados por la distribución, dejando la CNF en su forma canónica."""
    if isinstance(s, And):
        parts = []
        for c in s.conjuncts:
            fc = _flatten(c)
            if isinstance(fc, And):
                parts.extend(fc.conjuncts)
            else:
                parts.append(fc)
        return And(*parts)
    if isinstance(s, Or):
        parts = []
        for d in s.disjuncts:
            fd = _flatten(d)
            if isinstance(fd, Or):
                parts.extend(fd.disjuncts)
            else:
                parts.append(fd)
        return Or(*parts)
    return s


def to_cnf(sentence):
    """Convierte cualquier sentencia proposicional a Forma Normal Conjuntiva
    (una conjunción de disyunciones de literales)."""
    s = _eliminate_biconditional(sentence)
    s = _eliminate_implication(s)
    s = _move_not_inward(s)
    s = _distribute_or_over_and(s)
    s = _flatten(s)
    return s


def _literal_of(s):
    """Convierte un literal (Symbol o Not(Symbol)) a la tupla (nombre, polaridad)."""
    if isinstance(s, Symbol):
        return (s.name, True)
    if isinstance(s, Not) and isinstance(s.operand, Symbol):
        return (s.operand.name, False)
    raise TypeError(f"'{s.formula()}' no es un literal válido en CNF.")


def to_clauses(cnf_sentence):
    """Aplana una sentencia en CNF en una lista de cláusulas. Cada cláusula
    es un frozenset de literales (nombre_símbolo, polaridad_bool)."""

    def clause_of(s):
        if isinstance(s, Or):
            return frozenset(_literal_of(d) for d in s.disjuncts)
        return frozenset([_literal_of(s)])

    if isinstance(cnf_sentence, And):
        return [clause_of(c) for c in cnf_sentence.conjuncts]
    return [clause_of(cnf_sentence)]


def formula_of_clause(clause):
    """Representación textual legible de una cláusula (para impresión)."""
    if not clause:
        return "☐ (cláusula vacía / contradicción)"
    literals = sorted(clause)
    return "(" + " ∨ ".join(name if positive else f"¬{name}" for name, positive in literals) + ")"


def resolve(c1, c2):
    """Aplica la regla de resolución entre dos cláusulas: si c1 contiene un
    literal y c2 contiene su complemento, produce la cláusula resolvente
    (unión de ambas, sin el par complementario). Devuelve el conjunto de
    todos los resolventes posibles entre c1 y c2 (puede ser vacío si no hay
    literales complementarios)."""
    resolvents = set()
    for literal in c1:
        complement = (literal[0], not literal[1])
        if complement in c2:
            new_clause = (c1 - {literal}) | (c2 - {complement})
            resolvents.add(frozenset(new_clause))
    return resolvents


def resolution_entails(knowledge, query):
    """Determina si knowledge ⊨ query mediante RESOLUCIÓN POR REFUTACIÓN
    (algoritmo PL-Resolution, Russell & Norvig):

        knowledge ⊨ query   <=>   (knowledge ∧ ¬query) es INSATISFACIBLE

    Se convierte (knowledge ∧ ¬query) a CNF y se aplican resoluciones entre
    pares de cláusulas hasta derivar la cláusula vacía (☐ = contradicción,
    lo que confirma la implicación) o hasta que ya no se generen cláusulas
    nuevas (lo que refuta la implicación)."""
    combined = And(knowledge, Not(query))
    clauses = set(to_clauses(to_cnf(combined)))

    while True:
        new_clauses = set()
        clause_list = list(clauses)
        for c1, c2 in combinations(clause_list, 2):
            resolvents = resolve(c1, c2)
            if frozenset() in resolvents:
                return True  # Cláusula vacía derivada => contradicción => KB ⊨ query
            new_clauses |= resolvents
        if new_clauses.issubset(clauses):
            return False  # No hay cláusulas nuevas => no se pudo derivar contradicción
        clauses |= new_clauses


# ---------------------------------------------------------------------------
# 4. DEMOSTRACIÓN AUTOCONTENIDA (python3 logic.py)
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("=" * 70)
    print("DEMO — logic.py: Lógica Proposicional en Python puro")
    print("=" * 70)

    Lluvia = Symbol("Lluvia")
    Paraguas = Symbol("Paraguas")

    kb = And(
        Implication(Lluvia, Paraguas),  # Si llueve, entonces llevo paraguas.
        Lluvia                           # Hoy llueve.
    )

    print(f"\nBase de conocimiento: {kb.formula()}")
    print(f"Consulta: {Paraguas.formula()}")
    print(f"¿KB ⊨ Paraguas?  (Model Checking) -> {model_check(kb, Paraguas)}")
    print(f"¿KB ⊨ Paraguas?  (Resolución CNF) -> {resolution_entails(kb, Paraguas)}")

    cnf = to_cnf(kb)
    clauses = to_clauses(cnf)
    print(f"\nCNF de la base de conocimiento: {cnf.formula()}")
    print("Cláusulas: " + "  ∧  ".join(formula_of_clause(c) for c in clauses))

    assert model_check(kb, Paraguas) is True
    assert resolution_entails(kb, Paraguas) is True
    assert model_check(kb, Not(Paraguas)) is False
    assert resolution_entails(kb, Not(Paraguas)) is False

    print("\n✅ Todas las auto-verificaciones internas pasaron correctamente.")
