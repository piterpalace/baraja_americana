# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created: Wed Mar  7 17:03:28 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Fbaraja(object):
    def setupUi(self, Fbaraja):
        Fbaraja.setObjectName(_fromUtf8("Fbaraja"))
        Fbaraja.resize(736, 499)
        self.twclasificacion = QtGui.QTableWidget(Fbaraja)
        self.twclasificacion.setGeometry(QtCore.QRect(10, -10, 321, 501))
        self.twclasificacion.setObjectName(_fromUtf8("twclasificacion"))
        self.twclasificacion.setColumnCount(0)
        self.twclasificacion.setRowCount(0)
        self.gvimagen = QtGui.QGraphicsView(Fbaraja)
        self.gvimagen.setGeometry(QtCore.QRect(340, -10, 256, 192))
        self.gvimagen.setObjectName(_fromUtf8("gvimagen"))
        self.ltexto = QtGui.QLabel(Fbaraja)
        self.ltexto.setGeometry(QtCore.QRect(336, 300, 301, 20))
        self.ltexto.setText(_fromUtf8(""))
        self.ltexto.setObjectName(_fromUtf8("ltexto"))
        self.pbgenerar = QtGui.QPushButton(Fbaraja)
        self.pbgenerar.setGeometry(QtCore.QRect(450, 390, 93, 25))
        self.pbgenerar.setObjectName(_fromUtf8("pbgenerar"))

        self.retranslateUi(Fbaraja)
        QtCore.QMetaObject.connectSlotsByName(Fbaraja)

    def retranslateUi(self, Fbaraja):
        Fbaraja.setWindowTitle(QtGui.QApplication.translate("Fbaraja", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.pbgenerar.setText(QtGui.QApplication.translate("Fbaraja", "Generar", None, QtGui.QApplication.UnicodeUTF8))

