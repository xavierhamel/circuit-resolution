"""
Résolution de circuit électrique de 2e ordre de la forme RCC, RLL ou RCL
"""
import sympy

s = sympy.Symbol('s')

# L'exemple déjà présent dans le fichier est pour un circuit comme celui-ci. La
# méthode utilisé est la méthode des courants circulatoire et on veut trouver
# j_2
#   L2=.25H   L1=0.2H
# +---nnn---+---nnn---+
# | j1 ->   | j2 ->   |
# O V=100  | | R2=100| |
# |   R1=50| |       | |
# |         |         |
# +---------+---------+
#
# On va donc avoir la matrice suivante:
# +-                      -++-  -+   +-  -+
# | R1 + L1s     -R1       || j1 | = | Vs |
# |   -R1    R1 + R2 + L2s || j2 |   | 0  |
# +-                      -++-  -+   +-  -+
#
#
# On veut avoir la réponse de j2 (donc la 2e dans la matrice donc l'index 1 car
# l'indexation débute à 0.
# ===VARIABLE À MODIFIER===
ed_index = 1

# Dans un premier lieu on va rentrer la matrice des equations d'equilibre du
# circuit avec les valeurs et avec la variable `s` pour les dérivés ou
# intégrales si nécessaire. On va ensuite résoudre les matrices
# (equation_equilibre et equation_equilibre_sol) plus loins pour avoir notre
# équation différentielle.
# ===VARIABLE À MODIFIER===
equation_equilibre = [
#   [R1 + L1*s, -R1]
#   [-R1, R1 + R2 + L2*s]
    [50 + 0.25*s, -50],
    [-50, 50+100+0.2*s]
]

# Ensuite les solutions des équations d'équilibre
# ===VARIABLE À MODIFIER===
equation_equilibre_sol = [
#   [Vs, 0]
    100,
    0
]

# ===ON NE TOUCHE PLUS À RIEN===
t = sympy.Symbol('t')

# Si on a une équation avec des matrices:
eq_equilibre_matrix = sympy.matrices.Matrix(equation_equilibre)
eq_sol_matrix = sympy.matrices.Matrix(
    len(equation_equilibre_sol),
    1, 
    equation_equilibre_sol
)

ed = sympy.fraction(
    sympy.simplify(eq_equilibre_matrix.LUsolve(eq_sol_matrix)[ed_index])
)

ed_rhs = sympy.simplify(ed[0])
ed_lhs = sympy.simplify(ed[1])
print("--- ED ---")
print(ed_lhs, " = ", ed_rhs)

is_constant = ed_rhs.is_constant()

if is_constant:
    yp = ed_rhs / ed[1].subs(s, 0)
else:
    yp = 1 / ed[1].subs(s, 0)

print("--- Solution particulière ---")
print(yp)

roots = sympy.solvers.solve(ed_lhs, s)
print("--- Racines s_1 et s_2 ---")
print(roots)

if roots[0] != roots[1]:  # type: ignore
    # Réponse sous la forme yp + A_1e^{s_1t} + A_2e^{s_2t}
    # Ici on trouve les valeurs de A_1 et A_2.
    coeffs_matrix = sympy.matrices.Matrix([[1, 1], roots])
    coeffs_sol_matrix = sympy.matrices.Matrix(2, 1, [-yp, 0])
    coeffs = coeffs_matrix.LUsolve(coeffs_sol_matrix)

    response = yp + coeffs[0] * sympy.E**(roots[0]*t) + coeffs[1] * sympy.E**(roots[1]*t) # type: ignore

else:
    # Réponse sous la forme yp + (B_1 + B_2t)e^{st}
    # Ici on trouve B_1 et B_2
    b_1 = -yp
    b_2 = -b_1 * roots[0] # type: ignore
    response = yp + (b_1 + b_2*t) * sympy.E**(roots[0]*t) # type: ignore
    
print("--- Solution en u(t) ---")
print(f"({sympy.simplify(response)})u(t)")

# On trouve ici comment retourner à la bonne résponse (si la relation
# n'était pas égale à u(t)
if is_constant:
    result = response
else:
    result = 0
    rhs_coeffs = sympy.Poly(ed_rhs).all_coeffs()
    for idx, coeff in enumerate(rhs_coeffs):
        derivative_count = len(rhs_coeffs) - idx - 1
        if derivative_count > 0:
            result += sympy.diff(response, t, derivative_count) * coeff
        else:
            result += response

print("--- Solution ---")
print(f"({sympy.simplify(result)})u(t)")



