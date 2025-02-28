from scipy.optimize import linprog

# Coefficients de la fonction objectif (dual)
c_dual = [400, 50]

# Coefficients
A_dual = [
    [-10, -1],
    [-20, -1],  # 20y1 + y2 >= -110000 devient -20y1 - y2 <= 110000
    [-6, -1],
]

b_dual = [91500, 110000, 15900]

# Contraintes des variables (y1, y2 >= 0)
bounds = [(0, None), (0, None)]

# Résolution
result = linprog(c_dual, A_ub=A_dual, b_ub=b_dual, bounds=bounds, method="highs")


print("Solution du problème dual :")
print("y1 =", result.x[0])
print("y2 =", result.x[1])
print("Valeur optimale W =", result.fun)
