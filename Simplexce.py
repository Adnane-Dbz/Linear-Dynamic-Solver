def simplexe(c, A, b):

    m = len(A)
    n = len(c)
    tableau = []


    for i in range(m):
        tableau.append(A[i] + [1 if i == j else 0 for j in range(m)] + [b[i]])
    tableau.append(c + [0] * (m + 1))

    step = 0
    while True:

        print(f"Étape {step}:")
        for row in tableau:
            print(["{:.2f}".format(x) for x in row])
        print()

        z_cj = []
        for j in range(len(tableau[0]) - 1):
            z = 0
            for i in range(m):
                z += tableau[i][j] * tableau[-1][n + m]
            z_cj.append(tableau[-1][j] - z)


        if all(val >= 0 for val in z_cj):
            break


        pivot_col = z_cj.index(min(z_cj))

        ratios = []
        for i in range(m):
            if tableau[i][pivot_col] > 0:
                ratios.append(tableau[i][-1] / tableau[i][pivot_col])
            else:
                ratios.append(float('inf'))
        pivot_row = ratios.index(min(ratios))


        pivot_value = tableau[pivot_row][pivot_col]
        tableau[pivot_row] = [val / pivot_value for val in tableau[pivot_row]]


        for i in range(len(tableau)):
            if i != pivot_row:
                factor = tableau[i][pivot_col]
                tableau[i] = [
                    tableau[i][j] - factor * tableau[pivot_row][j]
                    for j in range(len(tableau[i]))
                ]

        step += 1  # Incrémenter le compteur d'étapes

    # Afficher le tableau final
    print(f"Tableau final (Étape {step}):")
    for row in tableau:
        print(["{:.2f}".format(x) for x in row])
    print()

    solution = [0] * n
    for j in range(n):
        column = [tableau[i][j] for i in range(m)]
        if column.count(1) == 1 and column.count(0) == m - 1:
            solution[j] = tableau[column.index(1)][-1]

    return solution, tableau[-1][-1]

c = [-91500, -110000, -15900, 0, 0]
A = [
    [10, 20, 6, 1, 0],
    [1, 1, 1, 0, 1],
]
b = [400, 50]

solution, optimal_value = simplexe(c, A, b)

print("Solution optimale :", solution)
print("Valeur optimale de Z :", -optimal_value)
