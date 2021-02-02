# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 21:19:30 2021

@author: Arpita
"""

import os
import sys
import cv2
import numpy as np

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QPixmap, QPalette, QPainter
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter
from PyQt5.QtWidgets import*

from threshold_gui import Ui_MainWindow

class thresh(Ui_MainWindow):
    
    def __init__(self, MainWindow):
        super(thresh, self).__init__(MainWindow)
        
        self.fileName = ""
        
        self.actionOpen.triggered.connect(self.open_img)
        #self.actionSave.triggered.connect(self.save_img)
        
        
    def open_img(self):
        option=QFileDialog.Options()
        widget=QWidget()
        self.fileName=QFileDialog.getOpenFileName(widget,"Open Single File","Default File", 'Images (*.png, *.xmp *.jpg)',options=option)
        self.label.setPixmap(QtGui.QPixmap(self.fileName[0]))
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = thresh(MainWindow)
    #ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
        