'''
Module de lancement du package connectfour. 

C'est ce module que nous allons exécuter pour démarrer votre jeu.
'''

from partie import PartieConnectFour

if __name__ == '__main__':


    partie = PartieConnectFour()

    # Pour charger d'une partie déjà sauvegardée
    #partie = PartieConnectFour("partie_sauvegardee.txt")

    # Pour sauvegarder une partie
    # partie.sauvegarder("partie_sauvegardee.txt")

    partie.jouer()