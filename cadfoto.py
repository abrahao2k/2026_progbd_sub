from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog

##################
import mariadb
conexao = mariadb.connect(host="localhost",user="root",
                          password="", database="imagens")
cursor = conexao.cursor()
##################

class Ui_CadCliente(object):
    def setupUi(self, CadCliente):
        CadCliente.setObjectName("CadCliente")
        CadCliente.resize(309, 173)
        self.centralwidget = QtWidgets.QWidget(CadCliente)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit_nome = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_nome.setObjectName("lineEdit_nome")
        self.gridLayout.addWidget(self.lineEdit_nome, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit_foto = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_foto.setObjectName("lineEdit_foto")
        self.gridLayout.addWidget(self.lineEdit_foto, 1, 1, 1, 1)
        self.pushButton_selecionar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_selecionar.setObjectName("pushButton_selecionar")
        
        self.pushButton_selecionar.clicked.connect(self.selecionar)
        
        self.gridLayout.addWidget(self.pushButton_selecionar, 1, 2, 1, 1)
        self.pushButton_salvar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_salvar.setObjectName("pushButton_salvar")
        
        self.pushButton_salvar.clicked.connect(self.salvar)
        
        self.gridLayout.addWidget(self.pushButton_salvar, 2, 2, 1, 1)
        CadCliente.setCentralWidget(self.centralwidget)

        self.retranslateUi(CadCliente)
        QtCore.QMetaObject.connectSlotsByName(CadCliente)

    def retranslateUi(self, CadCliente):
        _translate = QtCore.QCoreApplication.translate
        CadCliente.setWindowTitle(_translate("CadCliente", "Cadastro de Cliente"))
        self.label.setText(_translate("CadCliente", "Nome:"))
        self.label_2.setText(_translate("CadCliente", "Foto:"))
        self.pushButton_selecionar.setText(_translate("CadCliente", "Selecionar"))
        self.pushButton_salvar.setText(_translate("CadCliente", "SALVAR"))

    def selecionar(self):
        caminho, tmp = QFileDialog.getOpenFileName(None,
                                   "Selecione o arquivo")
        self.lineEdit_foto.setText(caminho)
    
    
    def salvar(self):
        nome = self.lineEdit_nome.text()
        
        # ABRIR OS DADOS DO ARQUIVO ###################
        caminho = self.lineEdit_foto.text()
        arq = open(caminho, "rb")   # abre o arquivo para leitura
        foto = arq.read()           # lê os dados

        # USAR %s para passar os dados no formato correto
        sql = "INSERT INTO cliente VALUES(null, %s, %s)"
        
        cursor.execute(sql, (nome, foto) )
        conexao.commit()
        
        msg = QMessageBox()
        msg.setText("Gravado com sucesso.")
        msg.exec_()
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CadCliente = QtWidgets.QMainWindow()
    ui = Ui_CadCliente()
    ui.setupUi(CadCliente)
    CadCliente.show()
    sys.exit(app.exec_())