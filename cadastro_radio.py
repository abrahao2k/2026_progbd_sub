from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

import mariadb
conexao = mariadb.connect(host="localhost",
                          user="root",
                          password="",
                          database="loja")
cursor = conexao.cursor()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(465, 237)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout.addWidget(self.plainTextEdit, 4, 1, 1, 1)
        self.radioButton_fisica = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_fisica.setObjectName("radioButton_fisica")
        self.gridLayout.addWidget(self.radioButton_fisica, 1, 1, 1, 1)
        self.label_pessoa = QtWidgets.QLabel(self.centralwidget)
        self.label_pessoa.setObjectName("label_pessoa")
        self.gridLayout.addWidget(self.label_pessoa, 1, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label_obs = QtWidgets.QLabel(self.centralwidget)
        self.label_obs.setObjectName("label_obs")
        self.gridLayout.addWidget(self.label_obs, 4, 0, 1, 1)
        self.label_status = QtWidgets.QLabel(self.centralwidget)
        self.label_status.setObjectName("label_status")
        self.gridLayout.addWidget(self.label_status, 5, 0, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 5, 1, 1, 1)
        self.label_nome = QtWidgets.QLabel(self.centralwidget)
        self.label_nome.setObjectName("label_nome")
        self.gridLayout.addWidget(self.label_nome, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        ##
        self.pushButton.clicked.connect(self.salvar)        
        ##
        self.gridLayout.addWidget(self.pushButton, 5, 2, 1, 1)
        self.radioButton_juridica = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_juridica.setObjectName("radioButton_juridica")
        self.gridLayout.addWidget(self.radioButton_juridica, 2, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Cadastro de Cliente"))
        self.radioButton_fisica.setText(_translate("MainWindow", "Física"))
        self.label_pessoa.setText(_translate("MainWindow", "Pessoa:"))
        self.label_obs.setText(_translate("MainWindow", "Observação: "))
        self.label_status.setText(_translate("MainWindow", "Status:"))
        self.checkBox.setText(_translate("MainWindow", "Ativo"))
        self.label_nome.setText(_translate("MainWindow", "Nome: "))
        self.pushButton.setText(_translate("MainWindow", "SALVAR"))
        self.radioButton_juridica.setText(_translate("MainWindow", "Jurídica"))

    def salvar(self):
        
        nome = self.lineEdit.text()
        
        pessoa = ""
        
        if self.radioButton_fisica.isChecked():
            pessoa = "Física"
        
        elif self.radioButton_juridica.isChecked():
            pessoa = "Jurídica"
        
        obs = self.plainTextEdit.toPlainText()
        
        ativo = "Não"
        
        if self.checkBox.isChecked():
            ativo = "Sim"

        sql = f'''INSERT INTO cliente VALUES(
                null, '{nome}', '{pessoa}',
                '{obs}', '{ativo}'); '''
        
        cursor.execute(sql)
        conexao.commit()
        #from PyQt5.QtWidgets import QMessageBox
        
        msg = QMessageBox()         # msg confirmação
        msg.setWindowTitle("Aviso")
        msg.setText("Cadastrado com sucesso.")
        msg.exec()
        
        ## LIMPAR O FORMULÁRIO ##
        self.lineEdit.setText("")
        self.plainTextEdit.setPlainText("")
        self.checkBox.setChecked(False)
        
        # RadioButton, precisa desativar a auto-exclusão
        self.radioButton_fisica.setAutoExclusive(False)
        self.radioButton_juridica.setAutoExclusive(False)
        self.radioButton_fisica.setChecked(False)
        self.radioButton_juridica.setChecked(False)
        self.radioButton_fisica.setAutoExclusive(True)
        self.radioButton_juridica.setAutoExclusive(True)
        
        self.lineEdit.setFocus() # marca o campo do nome
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())