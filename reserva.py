from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate

## Conexao BD ##
import mariadb
conexao = mariadb.connect(host="localhost",user="root",
                          password="",database="hotel")
cursor = conexao.cursor()
####

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(252, 152)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.dateEdit_entrada = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_entrada.setCalendarPopup(True)
        self.dateEdit_entrada.setObjectName("dateEdit_entrada")
        #define a data atual
        self.dateEdit_entrada.setDate(QDate.currentDate()) 
        
        self.gridLayout.addWidget(self.dateEdit_entrada, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.dateEdit_saida = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_saida.setCalendarPopup(True)
        self.dateEdit_saida.setObjectName("dateEdit_saida")
        #define a data atual
        self.dateEdit_saida.setDate(QDate.currentDate())
        
        self.gridLayout.addWidget(self.dateEdit_saida, 2, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        # função do botão
        self.pushButton.clicked.connect(self.salvar)
        
        self.gridLayout.addWidget(self.pushButton, 3, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Reserva"))
        self.label.setText(_translate("MainWindow", "Cliente:"))
        self.label_2.setText(_translate("MainWindow", "Data Entrada:"))
        self.label_3.setText(_translate("MainWindow", "Data Saída:"))
        self.pushButton.setText(_translate("MainWindow", "SALVAR"))

    def salvar(self):
        cliente = self.lineEdit.text()
        dt_entrada = self.dateEdit_entrada.date().toString("yyyy-MM-dd")
        dt_saida = self.dateEdit_saida.date().toString("yyyy-MM-dd")
        
        sql = f'''INSERT INTO reserva VALUES
                (null, '{cliente}', '{dt_entrada}', '{dt_saida}'); '''
        cursor.execute(sql)
        conexao.commit()
        print("Gravado com sucesso.")
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())