# Déclaration des compteurs globaux
iterations_memo = 0
iterations_simple = 0

def coefficient_binomial1(k, n):
    global iterations_simple
    iterations_simple += 1  # Incrémenter le compteur
    if k == 0 or k == n:
        return 1
    return coefficient_binomial1(k - 1, n - 1) + coefficient_binomial1(k, n - 1)

def coefficient_binomial(k, n, memo={}):
    global iterations_memo
    iterations_memo += 1  # Incrémenter le compteur
    # Vérifier si la valeur est déjà calculée
    if (k, n) in memo:
        return memo[(k, n)]

    if k == 0 or k == n:
        return 1

    # Récurrence : C(k, n) = C(k-1, n-1) + C(k, n-1)
    memo[(k, n)] = coefficient_binomial(k - 1, n - 1, memo) + coefficient_binomial(k, n - 1, memo)
    return memo[(k, n)]


# Appels des fonctions
resultat_memo = coefficient_binomial(5, 10)
resultat_simple = coefficient_binomial1(5, 10)

# Affichage des résultats et du nombre d'itérations
print(f"optiC() = {resultat_memo}, Nombre d'itérations (avec mémo) : {iterations_memo}")
print(f"C() = {resultat_simple}, Nombre d'itérations (sans mémo) : {iterations_simple}")
