#controller

from view.view import View
from model.model import Model

class Controller:
    def __init__(self):
        self.__model = None
        self.__view = None

    def setModel(self, model):
        self.__model = model

    def setView(self, view):
        self.__view = view

    def restartGame(self):
        """
        TODO
        """
        self.__model.setMatrix(self.__model.getLevel())  # On reset La Matrice
        self.__model.setNbPas(0)
        self.__view.updateView()  # On update la view

    def isValidPlay(self, o):
        player = self.__model.getPlayerPos()
        if o == 0:
            caseHaut = self.__model.getElement(player[0] - 1, player[1])
            casePlusHaut = self.__model.getElement(player[0] - 2, player[1])
            return caseHaut == 0 or caseHaut == 3 or ((caseHaut == 5 or caseHaut == 2) and (
                        casePlusHaut != 1 and casePlusHaut != 2 and casePlusHaut != 5))
        if o == 1:
            caseDroite = self.__model.getElement(player[0], player[1] + 1)
            casePlusDroite = self.__model.getElement(player[0], player[1] + 2)
            return caseDroite == 0 or caseDroite == 3 or ((caseDroite == 5 or caseDroite == 2) and (
                        casePlusDroite != 1 and casePlusDroite != 2 and casePlusDroite != 5))
        if o == 2:
            caseBas = self.__model.getElement(player[0] + 1, player[1])
            casePlusBas = self.__model.getElement(player[0] + 2, player[1])
            return caseBas == 0 or caseBas == 3 or (
                        (caseBas == 5 or caseBas == 2) and (casePlusBas != 1 and casePlusBas != 2 and casePlusBas != 5))
        if o == 3:
            caseGauche = self.__model.getElement(player[0], player[1] - 1)
            casePlusGauche = self.__model.getElement(player[0], player[1] - 2)
            return caseGauche == 0 or caseGauche == 3 or ((caseGauche == 5 or caseGauche == 2) and (
                        casePlusGauche != 1 and casePlusGauche != 2 and casePlusGauche != 5))

    def move(self, o):
        """
        Cette méthode déplace les objets dans la matrice et modifie la position du joueur.
        Elle n'est appelée que si le coup est valide.
        :param o:
        :return void:
        """
        player = self.__model.getPlayerPos()
        if o == 0:
            CH = self.__model.getElement(player[0] - 1, player[1])
            CEH = self.__model.getElement(player[0] - 2, player[1])
            if (CH == 2 or CH == 5):
                if (CH == 2):
                    self.__model.set(player[0] - 1, player[1], 0)
                    self.__model.set(player[0] - 2, player[1], 2)
                elif (CH == 5):
                    self.__model.set(player[0] - 1, player[1], 3)
                    self.__model.set(player[0] - 2, player[1], 2)
                if (CEH == 3):
                    self.__model.set(player[0] - 2, player[1], 5)
                else:
                    self.__model.set(player[0] - 2, player[1], 2)
            self.__model.setPlayerPos(player[0] - 1, player[1], 0)
        elif o == 1:
            CD = self.__model.getElement(player[0], player[1] + 1)
            CED = self.__model.getElement(player[0], player[1] + 2)
            if (CD == 2 or CD == 5):
                if (CD == 2):
                    self.__model.set(player[0], player[1] + 1, 0)
                    self.__model.set(player[0], player[1] + 2, 2)
                elif (CD == 5):
                    self.__model.set(player[0], player[1] + 1, 3)
                    self.__model.set(player[0], player[1] + 2, 2)
                if (CED == 3):
                    self.__model.set(player[0], player[1] + 2, 5)
                else:
                    self.__model.set(player[0], player[1] + 2, 2)
            self.__model.setPlayerPos(player[0], player[1] + 1, 1)
        elif o == 2:
            CB = self.__model.getElement(player[0] + 1, player[1])
            CEB = self.__model.getElement(player[0] + 2, player[1])
            if (CB == 2 or CB == 5):
                if (CB == 2):
                    self.__model.set(player[0] + 1, player[1], 0)
                    self.__model.set(player[0] + 2, player[1], 2)
                elif (CB == 5):
                    self.__model.set(player[0] + 1, player[1], 3)
                    self.__model.set(player[0] + 2, player[1], 2)
                if (CEB == 3):
                    self.__model.set(player[0] + 2, player[1], 5)
                else:
                    self.__model.set(player[0] + 2, player[1], 2)
            self.__model.setPlayerPos(player[0] + 1, player[1], 2)
        elif o == 3:
            CG = self.__model.getElement(player[0], player[1] - 1)
            CEG = self.__model.getElement(player[0], player[1] - 2)
            if (CG == 2 or CG == 5):
                if (CG == 2):
                    self.__model.set(player[0], player[1] - 1, 0)
                    self.__model.set(player[0], player[1] - 2, 2)
                elif (CG == 5):
                    self.__model.set(player[0], player[1] - 1, 3)
                    self.__model.set(player[0], player[1] - 2, 2)
                if (CEG == 3):
                    self.__model.set(player[0], player[1] - 2, 5)
                else:
                    self.__model.set(player[0], player[1] - 2, 2)
            self.__model.setPlayerPos(player[0], player[1] - 1, 3)
        self.__view.updateView()

    def isDefeated(self):
        """
        Cette méthode vérifie si la partie est impossible à finir ou non.
        :return boolean:
        """
        matrix = self.__model.getMatrix()
        if(self.__model.getNbPas() > self.__model.getMaxPas()):
            return True
        return False

    def isWin(self):
        """
        Cette méthode vérifie si la partie est gagnée.
        :return boolean:
        """
        matrix = self.__model.getMatrix()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 2:
                    return False

        if self.__model.getLevel() < 4:
            self.__model.addLevel()

        return True
