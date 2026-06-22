from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

import mariadb
conexao = mariadb.connect(host="localhost", user="root",
                          password="", database="esportes")
cursor = conexao.cursor()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(273, 122)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setObjectName("label_1")
        self.gridLayout.addWidget(self.label_1, 0, 0, 1, 1)
        self.lineEdit_codigo = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_codigo.setObjectName("lineEdit_codigo")
        self.gridLayout.addWidget(self.lineEdit_codigo, 0, 1, 1, 1)
        self.pushButton_abrir = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_abrir.setObjectName("pushButton_abrir")
        
        self.pushButton_abrir.clicked.connect(self.abrir)
        
        self.gridLayout.addWidget(self.pushButton_abrir, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit_nome = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_nome.setObjectName("lineEdit_nome")
        self.gridLayout.addWidget(self.lineEdit_nome, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.lineEdit_esporte = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_esporte.setObjectName("lineEdit_esporte")
        self.gridLayout.addWidget(self.lineEdit_esporte, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.lineEdit_participantes = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_participantes.setObjectName("lineEdit_participantes")
        self.gridLayout.addWidget(self.lineEdit_participantes, 3, 1, 1, 1)
        self.pushButton_salvar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_salvar.setObjectName("pushButton_salvar")
        
        self.pushButton_salvar.clicked.connect(self.atualizar)
        
        self.gridLayout.addWidget(self.pushButton_salvar, 3, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Atualizar Time"))
        self.label_1.setText(_translate("MainWindow", "Código:"))
        self.pushButton_abrir.setText(_translate("MainWindow", "ABRIR"))
        self.label_2.setText(_translate("MainWindow", "Nome: "))
        self.label_3.setText(_translate("MainWindow", "Esporte: "))
        self.label_4.setText(_translate("MainWindow", "Participantes:"))
        self.pushButton_salvar.setText(_translate("MainWindow", "SALVAR"))

    def abrir(self):
        cod = self.lineEdit_codigo.text() # capturar código digitado
        sql = "SELECT * FROM times WHERE codigo = " + cod
        cursor.execute(sql)
        if cursor.rowcount == 0:
            QMessageBox.information(None,"Aviso","Código inválido.")
            self.lineEdit_nome.clear()
            self.lineEdit_esporte.clear()
            self.lineEdit_participantes.clear()
        else:
            dados = cursor.fetchone()
            self.lineEdit_nome.setText(dados[1])
            self.lineEdit_esporte.setText(dados[2])
            self.lineEdit_participantes.setText(str(dados[3]))
            #bloquar o campo codigo
            self.lineEdit_codigo.setReadOnly(True)


    def atualizar(self):
        cod = self.lineEdit_codigo.text()
        nome = self.lineEdit_nome.text()
        esporte = self.lineEdit_esporte.text()
        part = self.lineEdit_participantes.text()
        
        sql= f"""UPDATE times SET
                 nome = '{nome}', esporte = '{esporte}',
                 participantes = {part}
                 WHERE codigo = {cod}; """
        cursor.execute(sql)
        conexao.commit()
        QMessageBox.information(None,"Aviso","Atualizado com sucesso.")
        self.lineEdit_nome.clear()
        self.lineEdit_esporte.clear()
        self.lineEdit_participantes.clear()
        #desbloquar o campo codigo
        self.lineEdit_codigo.setReadOnly(False)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())