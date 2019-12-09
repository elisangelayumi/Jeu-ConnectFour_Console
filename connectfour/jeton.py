from colorama import *
from termcolor import colored

'''
Ligne permettant de contourner un problème d'affichage des
boutons sur Windows dans certains cas.

Si vous n'avez pas de problème, laissez là en commentaire. Sinon,
décommentez là et les jetons devraient s'afficher correctement.

Merci à votre comparse Yan Bilodeau pour l'aide.
'''
# init(convert=True)


class Jeton:
    '''
    Classe représentant un jeton.

    On crée un jeton avec Jeton("jaune") par exemple.
    '''

    def __init__(self, couleur):
        self.symbole = u"\u25CF"
        self.couleur = couleur
        self.couleur_affichage = "yellow" if couleur == "jaune" else "red"

    def surligner(self):
        self.couleur_affichage = "green"

    def __str__(self):
        return ' {} '.format(colored(text=self.symbole,
                                     color=self.couleur_affichage))


