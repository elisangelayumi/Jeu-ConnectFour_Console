from grille import Grille
from partie import PartieConnectFour
from case import Case
from jeton import Jeton
from joueur import *


def obtenir_couleur(n):
    # Retourne "jaune" si n est pair, "rouge" sinon
    return "jaune" if n % 2 == 0 else "rouge"


def grille_pleine():
    grille = grille_base()

    for col in range(grille.N_COLONNES):
        for ligne in range(grille.N_LIGNES):
            couleur = obtenir_couleur(col + ligne)
            grille.cases[(col, ligne)].mettre_jeton(Jeton(couleur))

    grille.position_dernier_coup = (0, 0)
    grille.couleur_dernier_coup = "jaune"

    return grille


def grille_base():
    return Grille()


def grille_colonne0_pleine():
    grille = grille_base()

    for ligne in range(grille.N_LIGNES):
        grille.cases[(0, ligne)].mettre_jeton(Jeton("jaune"))

    grille.position_dernier_coup = (0, 0)
    grille.couleur_dernier_coup = "jaune"

    return grille


def grilles_egales(grille_attendue, grille_retournee):
    if grille_attendue.keys() != grille_retournee.keys():
        return False

    for position, case in grille_attendue.items():
        jeton_attendu = case.jeton
        jeton_retourne = grille_retournee[position].jeton

        if jeton_attendu is None:
            if jeton_retourne is not None:
                return False
        else:
            if not grille_retournee[position].jeton.couleur == case.jeton.couleur:
                return False

    return True


# Tests
def tests_est_pleine():
    assert grille_pleine().est_pleine(), \
        "Grille.est_pleine() devrait retourner True quand la grille est pleine"

    assert not grille_base().est_pleine(), \
        "Grille.est_pleine() devrait retourner False quand la grille n'est pas pleine"


def tests_colonne_pleine():
    assert grille_colonne0_pleine().colonne_est_pleine(0), \
        "Grille.colonne_est_pleine() devrait retourner True pour une colonne pleine"

    assert not grille_colonne0_pleine().colonne_est_pleine(1), \
        "Grille.colonne_est_pleine() devrait retourner False pour une colonne vide"


def tests_coup_dans_les_limites():
    assert not grille_base().coup_dans_les_limites(Grille.N_COLONNES), \
        "Grille.coup_dans_les_limites() devrait retourner False pour une colonne >= N_COLONNES"

    assert grille_base().coup_dans_les_limites(3), \
        "Grille.coup_dans_les_limites() devrait retourner True pour une colonne dans les limites"


def tests_jouer_coup():
    grille_avec_coup = grille_base()

    grille_avec_coup.jouer_coup(3, "jaune")

    position_attendue_coup = (3, Grille.N_LIGNES - 1)

    assert "jaune" == grille_avec_coup.couleur_dernier_coup, \
        "Grille.jouer_coup() devrait incrémenter l'attribut couleur_dernier_coup"

    assert position_attendue_coup == grille_avec_coup.position_dernier_coup, \
        "Grille.jouer_coup() devrait incrémenter l'attribut position_dernier_coup"


def tests_case_est_disponible():
    assert grille_base().case_est_disponible((0, 0)), \
        "Grille.case_est_disponible() devrait retourner True pour une case libre"

    assert not grille_pleine().case_est_disponible((3, 3)), \
        "Grille.case_est_disponible() devrait retourner False pour une case déjà occupée"


def tests_possede_un_gagnant():
    grille_sans_gagnant = grille_base()
    grille_sans_gagnant.jouer_coup(0, "jaune")
    grille_sans_gagnant.possede_un_gagnant()

    assert not grille_sans_gagnant.possede_un_gagnant(), \
        "Grille.possede_un_gagnant() devrait retourner False quand il n'y a pas de gagnant"

    assert grille_sans_gagnant.sequence_gagnante is None, \
        "Grille.possede_un_gagnant() ne devrait pas incrémenter l'attribut sequence_gagnante s'il n'y a pas de gagnant"

    grille_avec_gagnant = grille_colonne0_pleine()

    assert grille_avec_gagnant.possede_un_gagnant(), \
        "Grille.possede_un_gagnant() devrait retourner True quand il y a un gagnant"

    assert grille_avec_gagnant.sequence_gagnante is not None, \
        "Grille.possede_un_gagnant() devrait incrémenter l'attribut sequence_gagnante s'il y a un gagnant"


def tests_obtenir_sequence_vecteur():
    grille = grille_base()
    grille.cases[(0, Grille.N_LIGNES - 1)].mettre_jeton(Jeton("jaune"))

    assert [] == grille.obtenir_sequence_vecteur((0, Grille.N_LIGNES - 1), "jaune", [1, -1]), \
        "Grille.obtenir_sequence_vecteur() devrait retourner une liste vide " + \
        "quand il n'y a pas de jeton dans la direction du vecteur"

    sequence_attendue = []

    for i in range(1, 5):
        position = (i, Grille.N_LIGNES - (i + 1))
        sequence_attendue.append(position)
        grille.cases[position].mettre_jeton(Jeton("jaune"))

    assert sequence_attendue == grille.obtenir_sequence_vecteur((0, Grille.N_LIGNES - 1), "jaune", [1, -1]), \
        "Grille.obtenir_sequence_vecteur() devrait retourner tous les " + \
        "jetons de la bonne couleur dans la direction du vecteur"

    sequence_attendue = [(1, Grille.N_LIGNES - 2), (2, Grille.N_LIGNES - 3)]
    grille.cases[(3, Grille.N_LIGNES - 4)].mettre_jeton(Jeton("rouge"))

    assert sequence_attendue == grille.obtenir_sequence_vecteur((0, Grille.N_LIGNES - 1), "jaune", [1, -1]), \
        "Grille.obtenir_sequence_vecteur() devrait couper sa séquence de jetons " + \
        "lorsqu'un jeton d'une autre couleur est rencontré"


def tests_get_case():
    assert grille_base().get_case((1, 1)) is not None, \
        "Grille.get_case() devrait retourner une case pour une position valide"

    assert grille_base().get_case((-1, -1)) is None, \
        "Grille.get_case() devrait retourner None si la position est invalide"


def tests_chaine():
    chaine_attendue = "0,0,jaune\n0,1,jaune\n0,2,jaune\n0,3,jaune\n0,4,jaune\n0,5,jaune\n"

    assert chaine_attendue == grille_colonne0_pleine().convertir_en_chaine(), \
        "Grille.convertir_en_chaine() devrait retourner une chaine contenant " + \
        "toutes les cases au format spécifié."

    grille_attendue = grille_colonne0_pleine().cases

    grille = Grille()
    grille.charger_dune_chaine(chaine_attendue)

    grille_retournee = grille.cases

    assert grilles_egales(grille_attendue, grille_retournee), \
        "Grille.charger_dune_chaine() devrait retourner une grille contenant " + \
        "toutes les cases contenues dans la chaîne."


tests_chaine()