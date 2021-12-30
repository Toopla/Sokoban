#model

class Model:

    def __init__(self):
        """
        Constructeur du modèle
        """
        self.__view = None
        self.__level = 0
        self.__matrix = []
        self.__nbPas = 0
        self.__playerPos = [3, 3, 2]
        self.__maxPas = 0
        self.__lastLevel = False
        self.__boolAccueil = True

    def setMatrix(self, level):
        """
        numérotation des cases :
        9 = OutMap
        0 = Espace Vide
        1 = Mur
        2 = Caisse
        3 = Cible
        4 = Personnage sur une cible
        5 = Caisse sur une cible

        Cette méthode remplit la matrice en fonction du niveau que l'on souhaite.
        Elle met aussi en place la position du joueur dans la matrice.
        """
        assert level > 0 and level <= 4
        if level == 1:
            self.__matrix = [
                [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
                [9, 9, 9, 1, 1, 1, 1, 1, 9, 9],
                [9, 1, 1, 1, 0, 0, 0, 1, 9, 9],
                [9, 1, 3, 0, 2, 0, 0, 1, 9, 9],
                [9, 1, 1, 1, 0, 2, 3, 1, 9, 9],
                [9, 1, 3, 1, 1, 2, 0, 1, 9, 9],
                [9, 1, 0, 1, 0, 3, 0, 1, 1, 9],
                [9, 1, 2, 0, 5, 2, 2, 3, 1, 9],
                [9, 1, 0, 0, 0, 3, 0, 0, 1, 9],
                [9, 1, 1, 1, 1, 1, 1, 1, 1, 9],
                [9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
            ]
            self.__playerPos = [3, 3, 2]
            self.__level = 1
            self.__maxPas = 50

        elif level == 2:
            self.__matrix = [
                [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
                [9, 1, 1, 1, 1, 1, 9, 9, 9, 9],
                [9, 1, 3, 3, 0, 1, 9, 9, 9, 9],
                [9, 1, 0, 0, 0, 0, 1, 1, 1, 1],
                [9, 1, 0, 0, 0, 0, 1, 1, 3, 1],
                [9, 1, 1, 1, 0, 1, 1, 1, 0, 1],
                [9, 1, 1, 1, 0, 0, 0, 2, 2, 1],
                [9, 1, 0, 2, 2, 0, 0, 0, 0, 1],
                [9, 1, 0, 0, 0, 1, 1, 1, 1, 1],
                [9, 1, 1, 1, 3, 1, 9, 9, 9, 9],
                [9, 9, 9, 1, 1, 1, 9, 9, 9, 9]
            ]
            self.__playerPos = [6, 5, 3]
            self.__level = 2
            self.__maxPas = 60

        elif level == 3:
            self.__matrix = [
                [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
                [9, 1, 1, 1, 1, 1, 1, 1, 1, 9],
                [9, 1, 0, 0, 0, 1, 0, 0, 1, 9],
                [9, 1, 0, 1, 0, 1, 2, 3, 1, 9],
                [9, 1, 0, 0, 0, 0, 2, 3, 1, 9],
                [9, 1, 0, 1, 0, 1, 2, 3, 1, 9],
                [9, 1, 0, 0, 0, 1, 0, 0, 1, 9],
                [9, 1, 1, 1, 1, 1, 0, 0, 1, 9],
                [9, 9, 9, 9, 9, 1, 1, 1, 1, 9],
                [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
                [9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
            ]
            self.__playerPos = [6, 7, 0]
            self.__level = 3
            self.__maxPas = 120

        elif level == 4:
            self.__matrix = [
                [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
                [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
                [9, 1, 1, 1, 1, 1, 1, 1, 9, 9],
                [9, 1, 0, 0, 0, 3, 0, 1, 9, 9],
                [9, 1, 0, 1, 0, 1, 0, 1, 9, 9],
                [9, 1, 0, 2, 0, 2, 0, 1, 9, 9],
                [9, 1, 0, 1, 0, 1, 3, 1, 9, 9],
                [9, 1, 0, 0, 5, 0, 0, 1, 9, 9],
                [9, 1, 1, 1, 1, 1, 1, 1, 9, 9],
                [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
                [9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
            ]
            self.__playerPos = [6, 4, 0]
            self.__level = 4
            self.__maxPas = 80
            self.__lastLevel = True

    def getLevel(self):
        """
        TODO
        :return:
        """
        return self.__level

    def setView(self, view):
        """
        TODO
        """
        self.__view = view

    def getPlayerPos(self):
        """
        Cette fonction return la position position
        """
        return self.__playerPos

    def setPlayerPos(self, ligne, colonne, orientation):
        """
        Setter pour la position du joueur
        :param ligne:
        :param colonne:
        :param orientation:
        :return void:
        """
        self.__playerPos[0] = ligne
        self.__playerPos[1] = colonne
        self.__playerPos[2] = orientation

    def getNbPas(self):
        """
        TODO
        """
        return self.__nbPas

    def setNbPas(self, n):
        """
        TODO
        """
        self.__nbPas = n

    def getMaxPas(self):
        """
        TODO
        """
        return self.__maxPas

    def getElement(self, l, c):
        """
        Cette méthode renvoie la valeur de l'élément aux coordonnées x et y dans la matrice.
        """
        assert l >= 0 and c >= 0
        assert l < len(self.__matrix) and c < len(self.__matrix[0])
        return self.__matrix[l][c]

    def getMatrix(self):
        """
        Cette méthode renvoit la matrice entière
        """
        return self.__matrix

    def set(self, l, c, v):
        """
        Cette méthode affecte aux coordonnées entrées en paramètre la valeur aussi entrée en paramètre.
        """
        assert l >= 0 and c >= 0
        assert l < len(self.__matrix) and c < len(self.__matrix[0])
        assert v in (0, 1, 2, 3, 5)  # A voir si on garde le OutMap dans les autorisations (reponse : non il vaut mieux pas)

        self.__matrix[l][c] = v

    def addLevel(self):
        self.__level += 1

    def getLastLevel(self):
        return self.__lastLevel

    def getBoolAccueil(self):
        return self.__boolAccueil

    def setBoolAccueil(self, boolAccueil):
        self.__boolAccueil = boolAccueil