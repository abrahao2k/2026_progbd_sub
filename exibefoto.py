from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

##################
import mariadb
conexao = mariadb.connect(host="localhost",user="root",
                          password="", database="imagens")
cursor = conexao.cursor()
##################

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(311, 350)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 10, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 40, 111, 23))
        self.pushButton.setObjectName("pushButton")
        
        self.pushButton.clicked.connect(self.carregar)
        
        self.label_nome = QtWidgets.QLabel(self.centralwidget)
        self.label_nome.setGeometry(QtCore.QRect(20, 80, 150, 13))
        self.label_nome.setObjectName("label_nome")
        self.label_foto = QtWidgets.QLabel(self.centralwidget)
        self.label_foto.setGeometry(QtCore.QRect(20, 110, 200, 200))
        self.label_foto.setObjectName("label_foto")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Cliente"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "código"))
        self.pushButton.setText(_translate("MainWindow", "Carregar"))
        self.label_nome.setText(_translate("MainWindow", "Nome:"))
        self.label_foto.setText(_translate("MainWindow", "Foto"))

    def carregar(self):
        codigo = self.lineEdit.text()
        sql = "SELECT nome, foto FROM cliente WHERE codigo = " + codigo
        cursor.execute(sql)
        nome, foto = cursor.fetchone() # separa os dados em variávies
        
        self.label_nome.setText("Nome: " + nome)
        
        if foto:
            pixmap = QPixmap()        # cria o objeto
            pixmap.loadFromData(foto) # carrega a foto no objeto
            
            # redimensionar a imagem
            pixmap = pixmap.scaled(200, 200,
                     Qt.KeepAspectRatio, Qt.SmoothTransformation)
            
            self.label_foto.setPixmap(pixmap) # aplica o objeto da foto no label
        
        else:
            self.label_foto.setText("Sem foto.")
        
        
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())