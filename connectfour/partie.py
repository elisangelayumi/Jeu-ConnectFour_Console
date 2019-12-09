from grille import Grille
from joueur import JoueurOrdinateur, JoueurHumain


class PartieConnectFour:
    def __init__(self, nom_fichier=None):
        '''
        Méthode d'initialisation d'une partie.
        '''
        self.grille = Grille()

        self.gagnant_partie = None
        self.partie_nulle = False

        if nom_fichier is not None:
            self.charger(nom_fichier)
        else:
            self.initialiser_joueurs()

    def initialiser_joueurs(self):
        '''
        On initialise ici quatre attributs : joueur_jaune,
        joueur_rouge, joueur_courant et couleur_joueur_courant.

        joueur_courant est initialisé par défaut au joueur_jaune
        et couleur_joueur_courant est initialisée à "jaune".

        Pour créer les objets joueur, faites appel à
        creer_joueur().

        Pycharm vous sortira probablement des messages d'erreur à
        cette fonction car vous initialisez des attributs en
        dehors de la fonction __init__(), mais vous pouvez les
        ignorer.
        '''

        self.joueur_jaune = self.creer_joueur("jaune")

        self.joueur_rouge = self.creer_joueur("rouge")

        self.joueur_courant = self.joueur_jaune

        self.couleur_joueur_courant = "jaune"



    def creer_joueur(self, couleur):
        '''
        Demande à l'usager quel type de joueur ('Humain' ou
        'Ordinateur') il désire pour le joueur de la couleur en
        entrée.

        Tant que l'entrée n'est pas valide, on continue de
        demander à l'utilisateur.

        Faites appel à self.creer_joueur_selon_type() pour créer
        le joueur lorsque vous aurez le type.

        Args :
            couleur, la couleur pour laquelle on veut le type
                de joueur.

        Returns :
            Un objet Joueur, de type JoueurHumain
            si l'usager a entré 'Humain', JoueurOrdinateur s'il a
            entré 'Ordinateur'.
        '''


        choix_correct = False

        while choix_correct == False:
            demander_jouer = input("Quel type de joueur désirez-vous pour la couleur {}? Entrez Humain ou Ordinateur?  ".format(couleur))
            if demander_jouer == "Humain" or demander_jouer == "Ordinateur":
                choix_correct = True
                return self.creer_joueur_selon_type(demander_jouer,couleur)


    def creer_joueur_selon_type(self, type_joueur, couleur):
        '''
        Crée l'objet Joueur approprié, selon le type passé en
        paramètre.

        Pour créer les objets, vous n'avez qu'à faire appel à
        leurs constructeurs, c'est-à-dire à
        JoueurHumain(couleur), par exemple.

        Args :
            type, le type de joueur, "Ordinateur" ou "Humain"
            couleur, la couleur du pion joué par le jouer,
                "jaune" ou "rouge"

        Returns :
            Un objet JoueurHumain si le
            type est "Humain", JoueurOrdinateur sinon
        '''

        if type_joueur == "Humain":
            return JoueurHumain(couleur)
        if type_joueur == "Ordinateur":
            return JoueurOrdinateur(couleur)

    def jouer(self):
        '''
        Méthode représentant la boucle principale de jeu.

        Celle-ci fonctionne comme une boucle infinie. Pour chaque
        itération, on affiche la grille avec print(self.grille)
        et on joue un tour. Si la partie est terminée, on quitte
        la boucle. Sinon, on change de joueur.

        Quand on sort de la boucle principale, on fait le
        traitement de la fin de partie.

        Utilisez les fonctions partie_terminee(), jouer_tour(),
        changer_joueur() et traitement_fin_partie() pour vous
        faciliter la tâche.
        '''


        while not self.partie_terminee():
            print(self.grille)
            self.jouer_tour()
            self.changer_joueur()


        self.changer_joueur()
        self.traitement_fin_partie()


    def jouer_tour(self):
        '''
        Cette méthode commence par afficher à quel joueur c'est
        tour de jouer. Ensuite, on fait jouer le joueur courant
        sur la grille.
        '''

        print("C'est au tour du joueur {} de jouer".format(self.couleur_joueur_courant))
        self.joueur_courant.jouer_sur_grille(self.grille)


    def partie_terminee(self):
        '''
        Méthode vérifiant si la partie est terminée.

        Si la grille est pleine, on ajuste l'attribut
        partie_nulle à True.

        Si la grille possède un gagnant, on assigne la couleur du
        joueur courant à l'attribut gagnant_partie.

        Returns :
            True si la partie est terminée, False sinon
        '''


        if self.grille.possede_un_gagnant():
            self.gagnant_partie = self.couleur_joueur_courant
            return True
        elif self.grille.est_pleine():
            self.partie_nulle = True
            return  True
        else:
            return False



    def changer_joueur(self):
        '''
        En fonction de la couleur du joueur courant actuel, met à
        jour les attributs joueur_courant et couleur_joueur_courant.
        '''

        if self.joueur_courant is self.joueur_jaune:
            self.joueur_courant = self.joueur_rouge
            self.couleur_joueur_courant = self.joueur_rouge.couleur
        else:
            self.joueur_courant = self.joueur_jaune
            self.couleur_joueur_courant = self.joueur_jaune.couleur



    def traitement_fin_partie(self):
        '''
        Méthode qui gère le comportement de fin de partie.

        Si l'attribut gagnant_partie n'est pas None, on surligne
        la séquence gagnante de la grille et on affiche un
        message approprié pour féliciter le gagnant en plus
        d'afficher la grille avec la séquence gagnante surlignée.

        Sinon, on affiche le message d'un match nul.
        '''

        if self.grille.sequence_gagnante is not None:
            self.grille.surligner_sequence_gagnante()
            print("Le gagnant de la partie est le joueur {}! ".format(self.couleur_joueur_courant))
            print("Voici la ligne lui ayant permis de gagner! ")
            print(self.grille)
        else:
            print("match nul!")


    def sauvegarder(self, nom_fichier):
        '''
        Sauvegarde une partie dans un fichier. Le fichier
        contiendra:
        - Une ligne indiquant la couleur du joueur courant.
        - Une ligne contenant le type du joueur jaune.
        - Une ligne contenant le type du joueur rouge.
        - Le reste des lignes correspondant à la grille. Voir la
          méthode convertir_en_chaine de la grille pour le
          format.

        Args :
            nom_fichier, le string du nom du fichier où sauvegarder.
        '''

        nom_string = self.couleur_joueur_courant + "\n"
        nom_string += self.joueur_jaune.obtenir_type_joueur() + "\n"
        nom_string += self.joueur_rouge.obtenir_type_joueur() + "\n"
        nom_string += self.grille.convertir_en_chaine()

        with open(nom_fichier, "w") as mon_fichier:
            mon_fichier.write(nom_string)

    def charger(self, nom_fichier):
        '''
        Charge une partie dans à partir d'un fichier. Le fichier
        a le même format que la méthode de sauvegarde.

        Pycharm vous sortira probablement des messages d'erreur à
        cette fonction car vous initialisez des attributs en
        dehors de la fonction __init__(), mais vous pouvez les
        ignorer.

        Args:
            nom_fichier: Le string du nom du fichier à charger.
        '''

        myline = []

        with open(nom_fichier, "r") as mon_fichier:

            myline = mon_fichier.read().splitlines()


        self.joueur_jaune = self.creer_joueur_selon_type(myline[1],"jaune")
        self.joueur_rouge = self.creer_joueur_selon_type(myline[2], "rouge")
        self.couleur_joueur_courant = myline[0]

        if self.couleur_joueur_courant == "jaune":
            self.joueur_courant = self.joueur_jaune
        else:
            self.joueur_courant = self.joueur_rouge


        self.grille.charger_dune_chaine("\n".join(myline[3:]))


