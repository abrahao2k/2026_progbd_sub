from PyQt5 import QtCore, QtGui, QtWidgets

import mariadb
conexao = mariadb.connect(host="localhost", user="root",
                          password="", database="escola")
cursor = conexao.cursor()

class Ui_Pesquisar(object):
    def setupUi(self, Pesquisar):
        Pesquisar.setObjectName("Pesquisar")
        Pesquisar.resize(349, 190)
        self.centralwidget = QtWidgets.QWidget(Pesquisar)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        
        self.pushButton.clicked.connect(self.pesquisar)
        
        self.gridLayout.addWidget(self.pushButton, 0, 2, 1, 1)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout.addWidget(self.plainTextEdit, 1, 0, 1, 3)
        Pesquisar.setCentralWidget(self.centralwidget)

        self.retranslateUi(Pesquisar)
        QtCore.QMetaObject.connectSlotsByName(Pesquisar)

    def retranslateUi(self, Pesquisar):
        _translate = QtCore.QCoreApplication.translate
        Pesquisar.setWindowTitle(_translate("Pesquisar", "Pesquisar"))
        self.label.setText(_translate("Pesquisar", "Nome:"))
        self.pushButton.setText(_translate("Pesquisar", "Pesquisar"))


    def pesquisar(self):
        nome = self.lineEdit.text()
        
        sql = f"""SELECT * FROM alunos
                  WHERE nome LIKE '%{nome}%'
                  OR curso LIKE '%{nome}%'; """
        
        cursor.execute(sql)
        
        
        texto = ""
        
        for linha in cursor:
            texto += "Código: " + str(linha[0])+ "\n"
            texto += "Nome: " + linha[1]+ "\n"
            texto += "Curso: " + linha[2]+ "\n"
            texto += "Série: " + str(linha[3]) + "\n\n"
        
        texto += str(cursor.rowcount) + " resultado(s) encontrado(s)."
        
        self.plainTextEdit.setPlainText(texto)
        
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Pesquisar = QtWidgets.QMainWindow()
    ui = Ui_Pesquisar()
    ui.setupUi(Pesquisar)
    Pesquisar.show()
    sys.exit(app.exec_())