user = input("Nome do usuário: ")

from PyQt5 import QtCore, QtGui, QtWidgets
from menu import Ui_Menu

import sys
app = QtWidgets.QApplication(sys.argv)

tela = QtWidgets.QMainWindow()
tmenu = Ui_Menu(user) ### CONSTRUTOR MODIFICADO
tmenu.setupUi(tela)
tela.show()

