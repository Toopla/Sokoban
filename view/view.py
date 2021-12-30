#view

import time
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QGridLayout, QWidget, QMenu, QAction, QDialog, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import QUrl, Qt, QDir, QCoreApplication
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaPlaylist, QSound

class View(QMainWindow):
    def __init__(self):
        """
        TODO
        """
        self.__model = None
        self.__controller = None

        super().__init__()

        self.setWindowTitle("Sokoban")
        self.setFixedSize(500, 600)
        self.statusBar().showMessage("Nombre de pas : ", 0)

        self.__playlist = QMediaPlaylist()
        self.__playlist.addMedia(QMediaContent(QUrl.fromLocalFile(QDir.current().absoluteFilePath("sound/level.mp3"))))
        self.__playlist.setPlaybackMode(QMediaPlaylist.Loop)
        self.__levelSound = QMediaPlayer()
        self.__levelSound.setPlaylist(self.__playlist)
        self.__levelSound.play()

        self.__window = QWidget()
        self.setCentralWidget(self.__window)
        self.__gridLayout = QGridLayout()
        self.__gridCase = []
        self.__window.setLayout(self.__gridLayout)

        menuBar = self.menuBar()
        gameMenu = QMenu("&Jeu", self)
        menuBar.addMenu(gameMenu)

        helpMenu = QAction("&Help", self)
        helpMenu.triggered.connect(self.helpView)
        menuBar.addAction(helpMenu)

        accueil = QAction(self)
        accueil.setText("&Accueil")
        gameMenu.addAction(accueil)
        accueil.triggered.connect(self.accueil)

        restart = QAction(self)
        restart.setText("&Restart")
        gameMenu.addAction(restart)
        restart.triggered.connect(self.restart)

        level1 = QAction(self)
        level1.setText("&Niveau 1")
        gameMenu.addAction(level1)
        level1.triggered.connect(lambda x: self.level(1))

        level2 = QAction(self)
        level2.setText("&Niveau 2")
        gameMenu.addAction(level2)
        level2.triggered.connect(lambda x: self.level(2))

        level3 = QAction(self)
        level3.setText("&Niveau 3")
        gameMenu.addAction(level3)
        level3.triggered.connect(lambda x: self.level(3))

        level4 = QAction(self)
        level4.setText("&Niveau 4")
        gameMenu.addAction(level4)
        level4.triggered.connect(lambda x: self.level(4))

        exitProgram = QAction(self)
        exitProgram.setText("&Quit")
        gameMenu.addAction(exitProgram)
        exitProgram.triggered.connect(self.close)

        rect = self.geometry()

        self.__w = rect.width() / 10.20 + (rect.width() % 10.20)
        self.__h = rect.height() / 12.45 + (rect.height() % 12.45)

        self.__sol = QPixmap.fromImage(QImage("img/sol.png", 'png')).scaled(self.__w, self.__h)
        self.__mur = QPixmap.fromImage(QImage("img/mur.png", "png")).scaled(self.__w, self.__h)
        self.__cible = QPixmap.fromImage(QImage("img/case_cible.png")).scaled(self.__w, self.__h)
        self.__playerH = QPixmap.fromImage(QImage("img/player/H.png", "png")).scaled(self.__w, self.__h)
        self.__playerD = QPixmap.fromImage(QImage("img/player/D.png", "png")).scaled(self.__w, self.__h)
        self.__playerB = QPixmap.fromImage(QImage("img/player/B.png", "png")).scaled(self.__w, self.__h)
        self.__playerG = QPixmap.fromImage(QImage("img/player/G.png", "png")).scaled(self.__w, self.__h)
        self.__caisse = QPixmap.fromImage(QImage("img/caisse.png", "png")).scaled(self.__w, self.__h)
        self.__caisse2 = QPixmap.fromImage(QImage("img/caisse_2.png", "png")).scaled(self.__w, self.__h)
        self.__herbe = QPixmap.fromImage(QImage("img/grass0.png", "png")).scaled(self.__w, self.__h)

        for i in range(11):
            tmp = []
            for j in range(10):
                case = QLabel()
                case.setPixmap(self.__sol)
                case.setFixedSize(self.__w, self.__h)
                tmp.append(case)
                self.__gridLayout.addWidget(case, i, j)
            self.__gridCase.append(tmp)

    def level(self, x):
        """
        TODO
        """
        print("Passage au niveau ", x)
        self.__model.setMatrix(x)
        self.updateView()

    def restart(self):
        """
        TODO
        """
        self.__controller.restartGame()

    def helpView(self):
        """
        TODO
        """
        dialog = QDialog()
        dialog.setAttribute(Qt.WA_DeleteOnClose)
        dialog.setWindowTitle("Help")

        msg = "Error, file not found"
        with open('view/help.html') as reader:
            msg = reader.read()

        htmltest = QLabel(msg, parent=dialog)
        htmltest.show()
        dialog.exec_()

    def keyPressEvent(self, event):
        """
        Cet event s'active à chaque touche appuyé
        Les touches q et fleche de Gauche font aller le personnage à gauche
        Les touches d et fleche de Droite font aller le personnage à droite
        Les touches z et fleche de Haut font aller le personnage à haut
        Les touches s et fleche de Bas font aller le personnage à bas
        """

        key = event.key()
        if key == Qt.Key_Left or key == Qt.Key_Q:
            if self.__controller.isValidPlay(3):
                self.__controller.move(3)
                self.addNbPas()

        elif key == Qt.Key_Right or key == Qt.Key_D:
            if self.__controller.isValidPlay(1):
                self.__controller.move(1)
                self.addNbPas()

        elif key == Qt.Key_Up or key == Qt.Key_Z:
            if self.__controller.isValidPlay(0):
                self.__controller.move(0)
                self.addNbPas()

        elif key == Qt.Key_Down or key == Qt.Key_S:
            if self.__controller.isValidPlay(2):
                self.__controller.move(2)
                self.addNbPas()
        else:
            return

        if self.__controller.isDefeated():
            self.statusBar().showMessage("Nombre de pas: {}. Vous avez perdu ! ".format(self.__model.getNbPas()))
            self.__levelSound.stop()
            self.__playlist = QMediaPlaylist()
            self.__playlist.addMedia(QMediaContent(QUrl.fromLocalFile(QDir.current().absoluteFilePath("sound/soundGameOver.wav"))))
            self.__levelSound = QMediaPlayer()
            self.__levelSound.setPlaylist(self.__playlist)
            self.__levelSound.play()
            time.sleep(1)
            self.closeWindow()

        if self.__controller.isWin():
            if self.__model.getLastLevel() :
                self.statusBar().showMessage("Nombre de pas: {}. Vous avez gagné ! ".format(self.__model.getNbPas()))
                self.GGWP()

            else:
                self.closeWindow()

    def addNbPas(self):
        """
        Cette fonction rajoute 1 pas au compteur à chaque fois qu'il est appelé
        """
        self.__model.setNbPas(self.__model.getNbPas()+1)
        self.statusBar().showMessage("Nombre de pas: {} ".format(self.__model.getNbPas()))

    def updateView(self):
        """
        TODO
        """
        assert self.__model != None
        matrice = self.__model.getMatrix()
        """
        numérotation des cases :
        9 = OutMap
        0 = Espace Vide
        1 = Mur
        2 = Caisse
        3 = Cible 
        4 = Personnage sur une cible 
        5 = Caisse sur une cible
        """
        for ligne in range(len(matrice)):
            for colonne in range(len(matrice[0])):
                if (matrice[ligne][colonne] == 9):
                    self.__gridCase[ligne][colonne].setPixmap(self.__herbe)
                elif (matrice[ligne][colonne] == 0):
                    self.__gridCase[ligne][colonne].setPixmap(self.__sol)
                elif (matrice[ligne][colonne] == 1):
                    self.__gridCase[ligne][colonne].setPixmap(self.__mur)
                elif (matrice[ligne][colonne] == 2):
                    self.__gridCase[ligne][colonne].setPixmap(self.__caisse)
                elif (matrice[ligne][colonne] == 3):
                    self.__gridCase[ligne][colonne].setPixmap(self.__cible)
                elif (matrice[ligne][colonne] == 5):
                    self.__gridCase[ligne][colonne].setPixmap(self.__caisse2)

        pos = self.__model.getPlayerPos()  # Pour choisir l'image en fonction de l'orientation du joueur.
        if (pos[2] == 0):  # Orientation vers le haut
            self.__gridCase[pos[0]][pos[1]].setPixmap(self.__playerH)
        elif (pos[2] == 1):  # Orientation vers la droite
            self.__gridCase[pos[0]][pos[1]].setPixmap(self.__playerD)
        elif (pos[2] == 2):  # Orientation vers le bas
            self.__gridCase[pos[0]][pos[1]].setPixmap(self.__playerB)
        elif (pos[2] == 3):  # Orientation vers la gauche
            self.__gridCase[pos[0]][pos[1]].setPixmap(self.__playerG)
        else:  # Orientation par défaut (bas)
            self.__gridCase[pos[0]][pos[1]].setPixmap(self.__playerB)

    def closeWindow(self):
        self.fenetre = View()
        self.__levelSound.stop()
        self.close()
        self.fenetre.setModel(self.__model)
        self.fenetre.setController(self.__controller)
        self.__controller.setView(self.fenetre)
        self.__model.setView(self.fenetre)
        self.__model.setNbPas(0)
        self.fenetre.level(self.__model.getLevel())
        self.fenetre.show()

    def setModel(self, model):
        self.__model = model
        if self.__model.getBoolAccueil():
            self.accueil()
            self.__model.setBoolAccueil(False)
        else:
            self.level(self.__model.getLevel())

    def setController(self, controller):
        self.__controller = controller

    def accueil(self):
        self.__levelSound.stop()
        self.__windowAccueil=QWidget()
        conteneur=QVBoxLayout()
        label=QLabel()
        label.setPixmap(QPixmap(QImage('img/logo.png')))
        label.setAlignment(Qt.AlignCenter)
        conteneur.addWidget(label)
        hconteneur=QVBoxLayout()
        button2=QPushButton('Démarer')
        button1 = QPushButton('Quitter')
        hconteneur.addWidget(button2)
        hconteneur.addWidget(button1)
        conteneur.addLayout(hconteneur)
        self.__windowAccueil.setLayout(conteneur)
        self.setCentralWidget(self.__windowAccueil)
        self.setFixedSize(self.geometry().width(),self.geometry().height())
        button2.clicked.connect(self.closeWindow)
        button1.clicked.connect(self.close)

    def GGWP(self):
        self.__levelSound.stop()
        self.__playlist = QMediaPlaylist()
        self.__playlist.addMedia(QMediaContent(QUrl.fromLocalFile(QDir.current().absoluteFilePath("sound/level1.mp3"))))
        self.__levelSound = QMediaPlayer()
        self.__levelSound.setPlaylist(self.__playlist)
        self.__levelSound.play()
        self.__windowAccueil=QWidget()
        conteneur=QVBoxLayout()
        label=QLabel()
        label.setPixmap(QPixmap(QImage('img/victory.jpg')))
        label.setAlignment(Qt.AlignCenter)
        conteneur.addWidget(label)
        hconteneur=QVBoxLayout()
        button1 = QPushButton('Quitter')
        hconteneur.addWidget(button1)
        conteneur.addLayout(hconteneur)
        self.__windowAccueil.setLayout(conteneur)
        self.setCentralWidget(self.__windowAccueil)
        self.setFixedSize(self.geometry().width(),self.geometry().height())
        button1.clicked.connect(self.close)