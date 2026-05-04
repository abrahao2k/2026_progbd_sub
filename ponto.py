from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QDateTime

import mariadb
conexao = mariadb.connect(host="localhost",user="root",
                          password="", database="empresa")
cursor = conexao.cursor()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(277, 106)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        
        self.pushButton.clicked.connect(self.marcar)
        
        self.gridLayout.addWidget(self.pushButton, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Relógio de Ponto"))
        self.label.setText(_translate("MainWindow", "Matrícula"))
        self.pushButton.setText(_translate("MainWindow", "Marcar Ponto"))
    
    def marcar(self):
        matricula = self.lineEdit.text()
        
        datahora = QDateTime.currentDateTime().toString("yyyy-MM-dd HH:mm:ss")
        
        sql = f'''INSERT INTO ponto2
                  VALUES(null, {matricula}, '{datahora}' );'''
        cursor.execute(sql)
        conexao.commit()
        
        msg = QMessageBox()
        msg.setText(f"PONTO MARCADO \n {datahora}")
        msg.exec_()
        
        self.lineEdit.setText("")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())