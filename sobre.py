from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogSobre(object):
    def setupUi(self, DialogSobre):
        DialogSobre.setObjectName("DialogSobre")
        DialogSobre.setWindowModality(QtCore.Qt.ApplicationModal)
        DialogSobre.resize(302, 257)
        DialogSobre.setModal(True)
        self.pushButton = QtWidgets.QPushButton(DialogSobre)
        self.pushButton.setGeometry(QtCore.QRect(210, 220, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(DialogSobre)
        self.label.setGeometry(QtCore.QRect(20, 10, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(DialogSobre)
        self.commandLinkButton.setGeometry(QtCore.QRect(20, 50, 111, 41))
        self.commandLinkButton.setObjectName("commandLinkButton")

        self.retranslateUi(DialogSobre)
        QtCore.QMetaObject.connectSlotsByName(DialogSobre)

    def retranslateUi(self, DialogSobre):
        _translate = QtCore.QCoreApplication.translate
        DialogSobre.setWindowTitle(_translate("DialogSobre", "Sobre"))
        self.pushButton.setText(_translate("DialogSobre", "FECHAR"))
        self.label.setText(_translate("DialogSobre", "Sistema Top v.1.0"))
        self.commandLinkButton.setText(_translate("DialogSobre", "Meu site"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DialogSobre = QtWidgets.QDialog()
    ui = Ui_DialogSobre()
    ui.setupUi(DialogSobre)
    DialogSobre.show()
    sys.exit(app.exec_())