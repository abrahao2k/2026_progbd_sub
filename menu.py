from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Menu(object):
    def setupUi(self, Menu):
        Menu.setObjectName("Menu")
        Menu.resize(364, 394)
        self.centralwidget = QtWidgets.QWidget(Menu)
        self.centralwidget.setObjectName("centralwidget")
        Menu.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Menu)
        self.statusbar.setObjectName("statusbar")
        Menu.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(Menu)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 364, 21))
        self.menubar.setObjectName("menubar")
        self.menuCadastro = QtWidgets.QMenu(self.menubar)
        self.menuCadastro.setObjectName("menuCadastro")
        self.menuRelat_rio = QtWidgets.QMenu(self.menubar)
        self.menuRelat_rio.setObjectName("menuRelat_rio")
        Menu.setMenuBar(self.menubar)
        self.actionUsuario = QtWidgets.QAction(Menu)
        self.actionUsuario.setObjectName("actionUsuario")
        self.actionProduto = QtWidgets.QAction(Menu)
        self.actionProduto.setObjectName("actionProduto")
        
        # associar o menu a uma função
        self.actionProduto.triggered.connect(self.cadastrar_produto)
        
        self.actionSair = QtWidgets.QAction(Menu)
        self.actionSair.setObjectName("actionSair")
        self.actionUsu_rio_2 = QtWidgets.QAction(Menu)
        self.actionUsu_rio_2.setObjectName("actionUsu_rio_2")
        self.actionProduto_2 = QtWidgets.QAction(Menu)
        self.actionProduto_2.setObjectName("actionProduto_2")
        
        self.actionProduto_2.triggered.connect(self.pesquisar_produto)
        
        self.menuCadastro.addAction(self.actionUsuario)
        self.menuCadastro.addAction(self.actionProduto)
        self.menuCadastro.addSeparator()
        self.menuCadastro.addAction(self.actionSair)
        self.menuRelat_rio.addAction(self.actionUsu_rio_2)
        self.menuRelat_rio.addAction(self.actionProduto_2)
        self.menubar.addAction(self.menuCadastro.menuAction())
        self.menubar.addAction(self.menuRelat_rio.menuAction())

        self.retranslateUi(Menu)
        QtCore.QMetaObject.connectSlotsByName(Menu)

    def retranslateUi(self, Menu):
        _translate = QtCore.QCoreApplication.translate
        Menu.setWindowTitle(_translate("Menu", "Menu do Sistema"))
        self.menuCadastro.setTitle(_translate("Menu", "Cadastro"))
        self.menuRelat_rio.setTitle(_translate("Menu", "Relatório"))
        self.actionUsuario.setText(_translate("Menu", "Usuário"))
        self.actionProduto.setText(_translate("Menu", "Produto"))
        self.actionProduto.setShortcut(_translate("Menu", "Alt+P"))
        self.actionSair.setText(_translate("Menu", "Sair"))
        self.actionUsu_rio_2.setText(_translate("Menu", "Usuário"))
        self.actionProduto_2.setText(_translate("Menu", "Produto"))

    def cadastrar_produto(self):
        #print("A janela de cadastro do produto foi aberta.")
        
        # exibe o texto no status / tempo em milisegundos
        self.statusbar.showMessage("Abriu o Cadastro de Produto",3000)
        #self.statusbar.clearMessage() # apaga manualmente
        
        # abrir outra janela
        from tela_cadastro import Ui_MainWindow
        self.tela = QtWidgets.QMainWindow()
        self.cad = Ui_MainWindow()
        self.cad.setupUi(self.tela)
        self.tela.show()
    
    def pesquisar_produto(self):
        from pesquisa import Ui_Pesquisar
        self.tela2 = QtWidgets.QMainWindow()
        self.pesq = Ui_Pesquisar()
        self.pesq.setupUi(self.tela2)
        self.tela2.show()
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Menu = QtWidgets.QMainWindow()
    ui = Ui_Menu()
    ui.setupUi(Menu)
    Menu.show()
    sys.exit(app.exec_())