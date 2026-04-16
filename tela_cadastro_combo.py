from conexaobd import *

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

lista_cursos = list()  # lista vazia dos cursos

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(247, 156)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_curso = QtWidgets.QLabel(self.centralwidget)
        self.label_curso.setObjectName("label_curso")
        self.gridLayout.addWidget(self.label_curso, 1, 0, 1, 1)
        self.label_serie = QtWidgets.QLabel(self.centralwidget)
        self.label_serie.setObjectName("label_serie")
        self.gridLayout.addWidget(self.label_serie, 2, 0, 1, 1)
        self.label_nome = QtWidgets.QLabel(self.centralwidget)
        self.label_nome.setObjectName("label_nome")
        self.gridLayout.addWidget(self.label_nome, 0, 0, 1, 1)
        self.lineEdit_nome = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_nome.setObjectName("lineEdit_nome")
        self.gridLayout.addWidget(self.lineEdit_nome, 0, 1, 1, 1)
        self.lineEdit_serie = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_serie.setObjectName("lineEdit_serie")
        self.gridLayout.addWidget(self.lineEdit_serie, 2, 1, 1, 1)
        self.pushButton_salvar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_salvar.setObjectName("pushButton_salvar")
        
        self.pushButton_salvar.clicked.connect(self.salvar)
        
        self.gridLayout.addWidget(self.pushButton_salvar, 3, 1, 1, 1)

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        
        self.carregar_cursos()
        
        self.gridLayout.addWidget(self.comboBox, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Cadastro de Aluno"))
        self.label_curso.setText(_translate("MainWindow", "Curso:"))
        self.label_serie.setText(_translate("MainWindow", "Serie:"))
        self.label_nome.setText(_translate("MainWindow", "Nome:"))
        self.pushButton_salvar.setText(_translate("MainWindow", "SALVAR"))

    def carregar_cursos(self):
        cursor.execute("SELECT * FROM cursos ORDER BY nome")
        for linha in cursor:
            self.comboBox.addItem(linha[1]) # nome do curso
            lista_cursos.append(linha[0])   # código do curso

    def salvar(self):
        nome  = self.lineEdit_nome.text()
        #curso = self.comboBox.currentText() # texto do item selecionado
        
        posicao = self.comboBox.currentIndex()
        curso = lista_cursos[posicao]  # pega o código do curso
        
        serie = self.lineEdit_serie.text()
        
        sql = f"""INSERT INTO alunos VALUES
              (null,'{nome}', '{curso}', {serie}); """
        
        cursor.execute(sql)
        conexao.commit()
        
        msg = QMessageBox()         # msg confirmação
        msg.setWindowTitle("Aviso")
        msg.setText("Cadastrado com sucesso.")
        msg.exec()
        
        self.lineEdit_nome.setText("") # limpar campos
        self.comboBox.setCurrentIndex(-1) # limpar o combo
        self.lineEdit_serie.setText("")
        
        self.lineEdit_nome.setFocus() # selecionar o campo nome


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())