#main

from view.view import View
from model.model import Model
from controller.controller import Controller

import sys
from PyQt5.QtWidgets import QApplication

app = QApplication(sys.argv)

model = Model()
view = View()
controller = Controller()

model.setView(view)
view.setModel(model)
view.setController(controller)
controller.setModel(model)
controller.setView(view)
model.setMatrix(1)
view.show()
sys.exit(app.exec_())
