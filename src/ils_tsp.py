import random
import math
import matplotlib.pyplot as plt

# Fonction pour calculer la distance entre deux villes
def calculer_distance(ville1, ville2):
    x1, y1 = ville1
    x2, y2 = ville2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Fonction pour calculer la distance totale du parcours
def distance_totale(parcours, villes):
    distance = 0
    for i in range(len(parcours) - 1):
        distance += calculer_distance(villes[parcours[i]], villes[parcours[i + 1]])
    distance += calculer_distance(villes[parcours[-1]], villes[parcours[0]])  # Retour au départ
    return distance

# Recherche locale 2-opt optimisée
def recherche_locale(parcours, villes):
    meilleur_parcours = parcours.copy()
    meilleure_distance = distance_totale(parcours, villes)
    improved = True
    
    while improved:
        improved = False
        for i in range(len(parcours) - 1):
            for j in range(i + 2, len(parcours)):  # Évite les inversions inutiles de voisins
                nouveau_parcours = parcours[:i] + parcours[i:j][::-1] + parcours[j:]
                nouvelle_distance = distance_totale(nouveau_parcours, villes)
                if nouvelle_distance < meilleure_distance:
                    meilleur_parcours = nouveau_parcours
                    meilleure_distance = nouvelle_distance
                    improved = True
        parcours = meilleur_parcours.copy()
    return meilleur_parcours

# Perturbation avec contrôle de l'intensité
def perturbation(parcours, strength=0.3):
    nouveau_parcours = parcours.copy()
    n_swaps = max(1, int(strength * len(parcours)))
    for _ in range(n_swaps):
        i, j = random.sample(range(len(parcours)), 2)
        nouveau_parcours[i], nouveau_parcours[j] = nouveau_parcours[j], nouveau_parcours[i]
    return nouveau_parcours

# ILS avec critère d'acceptation inspiré du recuit simulé
def recherche_locale_iteree(villes, iterations_max=1000, temp_initiale=10.0, force_perturbation=0.3):
    # Initialisation aléatoire
    parcours = list(range(len(villes)))
    random.shuffle(parcours)

    parcours = recherche_locale(parcours, villes)
    distance_parcours = distance_totale(parcours, villes)
    meilleur_parcours = parcours.copy()
    meilleure_distance = distance_parcours
    distances = [meilleure_distance]

    temp = temp_initiale

    for iteration in range(iterations_max):
        # Perturber la solution courante, puis appliquer la recherche locale.
        candidat = perturbation(parcours, strength=force_perturbation)
        candidat = recherche_locale(candidat, villes)
        distance_candidate = distance_totale(candidat, villes)

        # Le critère d'acceptation compare le candidat à la solution courante.
        delta = distance_candidate - distance_parcours
        if delta < 0 or random.random() < math.exp(-delta / temp):
            parcours = candidat
            distance_parcours = distance_candidate

        # La meilleure solution globale est conservée séparément.
        if distance_parcours < meilleure_distance:
            meilleur_parcours = parcours.copy()
            meilleure_distance = distance_parcours

        distances.append(meilleure_distance)

        temp *= 0.995  # Refroidissement progressif

    return meilleur_parcours, meilleure_distance, distances



# Exemple d'utilisation
if __name__ == "__main__":
    # Coordonnées des villes (exemple)
    villes = [(0, 0), (1, 2), (2, 4), (3, 3), (5, 0), (4, 1), (2, 0)]
    
    # Exécution de l'ILS
    meilleur_parcours, meilleure_distance, distances = recherche_locale_iteree(
        villes, iterations_max=1000)
    
    # Affichage des résultats
    print(f"Meilleur parcours : {meilleur_parcours}")
    print(f"Distance totale optimisée : {meilleure_distance:.2f}")
    
    # Visualisation
    plt.figure(figsize=(14, 6))
    
    # 1. Graphique du parcours optimal
    plt.subplot(1, 2, 1)
    x = [villes[i][0] for i in meilleur_parcours] + [villes[meilleur_parcours[0]][0]]
    y = [villes[i][1] for i in meilleur_parcours] + [villes[meilleur_parcours[0]][1]]
    plt.plot(x, y, 'o-', markersize=8, linewidth=2, color='royalblue', markerfacecolor='red')
    
    # Ajout des numéros des villes
    for i, (xi, yi) in enumerate(villes):
        plt.text(xi, yi, str(i), ha='center', va='bottom', fontsize=10)
    
    plt.title("Parcours optimal", fontsize=14)
    plt.xlabel("Coordonnée X", fontsize=12)
    plt.ylabel("Coordonnée Y", fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)

    # 2. Graphique de convergence
    plt.subplot(1, 2, 2)
    plt.plot(distances, linewidth=2, color='darkorange')
    plt.title("Convergence de l'ILS", fontsize=14)
    plt.xlabel("Itérations", fontsize=12)
    plt.ylabel("Distance totale", fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)

    plt.tight_layout()
    plt.savefig("resultat_ILS.png")  # Sauvegarde l'image
    plt.show()
