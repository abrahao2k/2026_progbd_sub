from PyQt5 import QtCore, QtGui, QtWidgets

import mariadb
conexao = mariadb.connect(host="localhost",user="root",
                          password="", database="sistematop")
cursor = conexao.cursor()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(239, 133)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit_usuario = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_usuario.setObjectName("lineEdit_usuario")
        self.gridLayout.addWidget(self.lineEdit_usuario, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit_senha = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_senha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_senha.setObjectName("lineEdit_senha")
        self.gridLayout.addWidget(self.lineEdit_senha, 1, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        
        self.pushButton.clicked.connect(self.entrar)
        
        self.gridLayout.addWidget(self.pushButton, 2, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login"))
        self.label.setText(_translate("MainWindow", "Usuário:"))
        self.label_2.setText(_translate("MainWindow", "Senha:"))
        self.pushButton.setText(_translate("MainWindow", "ENTRAR"))
    
    def entrar(self):
        usu = self.lineEdit_usuario.text()
        sen = self.lineEdit_senha.text()
        
        sql = f'''SELECT * FROM usuarios
                  WHERE usuario = '{usu}'
                  AND senha = MD5('{sen}'); '''
        
        cursor.execute(sql)
        dados = cursor.fetchall()
        
        if len(dados) == 0 :
            #print('ACESSO NEGADO')
            from PyQt5.QtWidgets import QMessageBox
            msg = QMessageBox()
            msg.setText("ACESSO NEGADO")
            msg.setWindowTitle("Erro")
            msg.exec_()
            
        else:
            #print('ACESSO PERMITIDO')
            from menu import Ui_Menu
            
            self.tela = QtWidgets.QMainWindow()
            self.tmenu = Ui_Menu()
            self.tmenu.setupUi(self.tela)
            self.tela.show()
            MainWindow.close() # fecha a tela de login
            

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())