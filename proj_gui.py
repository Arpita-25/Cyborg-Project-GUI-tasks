# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'proj_gui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QPixmap, QPalette, QPainter
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter
from PyQt5.QtWidgets import*

import numpy as np
import os
import cv2

class Ui_Dialog(object):
    def __init__(self):
        super().__init__()
        
        Dialog.setObjectName("Dialog")
        Dialog.resize(801, 603)
        
        self.file = ""
        self.img = img
        
        self.browse = QtWidgets.QPushButton(Dialog)
        self.browse.setGeometry(QtCore.QRect(0, 0, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.browse.setFont(font)
        self.browse.setObjectName("pushButton")
        
        self.process = QtWidgets.QPushButton(Dialog)
        self.process.setGeometry(QtCore.QRect(0, 500, 401, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.process.setFont(font)
        self.process.setObjectName("pushButton_2")
        
        self.save = QtWidgets.QPushButton(Dialog)
        self.save.setGeometry(QtCore.QRect(400, 500, 401, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.save.setFont(font)
        self.save.setObjectName("pushButton_3")
        
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 100, 401, 391))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(410, 90, 391, 401))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        self.browse.clicked.connect(self.browse_img)
        self.process.clicked.connect(self.process_img)
        self.save.clicked.connect(self.save_img)

    def browse_img(self):
        option=QFileDialog.Options()
        widget=QWidget()
        file=QFileDialog.getOpenFileName(widget,"Open Single File","Default File", 'Images (*.png, *.xmp *.jpg)',options=option)
        self.label.setPixmap(QtGui.QPixmap(file[0]))
        self.img=cv2.imread(file[0],0)
        #cv2.imwrite('output.jpg',img)
        
        
    def process_img(self):
        self.label_2.setPixmap(QtGui.QPixmap(self.img))

    def save_img(self):
        dialog = QPrintDialog(self.printer, self)
        if dialog.exec_():
            painter = QPainter(self.printer)
            rect = painter.viewport()
            size = self.imageLabel.pixmap().size()
            size.scale(rect.size(), Qt.KeepAspectRatio)
            painter.setViewport(rect.x(), rect.y(), size.width(), size.height())
            painter.setWindow(self.imageLabel.pixmap().rect())
            painter.drawPixmap(0, 0, self.imageLabel.pixmap())

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.browse.setText(_translate("Dialog", "BROWSE"))
        self.process.setText(_translate("Dialog", "PROCESS AND SHOW"))
        self.save.setText(_translate("Dialog", "SAVE"))
        self.label.setText(_translate("Dialog", "                         Original Image Shows here!"))
        self.label_2.setText(_translate("Dialog", "                          Processed Image Shows here!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    #ui.setupUi(Dialog)
    ui.show()
    sys.exit(app.exec_())

