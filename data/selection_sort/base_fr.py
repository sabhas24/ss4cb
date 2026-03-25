def tri_par_selection(liste):
    """
    Trie une liste en utilisant l'algorithme du tri par sélection.

    Principe :
    À chaque itération, on cherche le plus petit élément de la partie
    non triée de la liste, puis on l'échange avec l'élément courant.

    liste: List d'éléments comparables à trier
    retour: Liste triée (tri en place)

    Complexité :
    - Temps : O(n^2)
    - Espace : O(1) (tri en place)
    """

    n = len(liste)

    # Parcours de toute la liste
    for i in range(n):
        # On suppose que le minimum est au début de la zone non triée
        indice_min = i

        # Recherche du plus petit élément dans le reste de la liste
        for j in range(i + 1, n):
            if liste[j] < liste[indice_min]:
                indice_min = j

        # Échange si un plus petit élément a été trouvé
        if indice_min != i:
            liste[i], liste[indice_min] = liste[indice_min], liste[i]

    return liste
