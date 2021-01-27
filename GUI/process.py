# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 23:41:13 2021

@author: Arpita
"""

import os
import cv2
import numpy as np

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QPixmap, QPalette, QPainter
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter
from PyQt5.QtWidgets import*

from original_gui import Ui_MainWindow

class process_img(Ui_MainWindow):
    
    def __init__(self, MainWindow):
        super(process_img, self).__init__(MainWindow)
        
        self.fileName = ""
        self.img = ""
        
        self.actionOpen.triggered.connect(self.open_img)
        #self.actionSave.triggered.connect(self.save_img)
        #self.pushButton.clicked.connect(self.convert)
        
    def open_img(self):
        option=QFileDialog.Options()
        widget=QWidget()
        fileName=QFileDialog.getOpenFileName(widget,"Open Single File","Default File", 'Images (*.png, *.xmp *.jpg)',options=option)
        self.label.setPixmap(QtGui.QPixmap(fileName[0]))
        self.img=cv2.imread(fileName[0],0)
        #cv2.imwrite('output.jpg',img)
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = process_img(MainWindow)
    #ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
