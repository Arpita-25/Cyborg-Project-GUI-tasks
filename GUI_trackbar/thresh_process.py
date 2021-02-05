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
        self.thresh_type = ""
        self.thresh_val = ""
        self.slider_type = ""
        self.slider_value = ""
        self.slider_type = int(self.type_slider.value())
        self.slider_value = int(self.value_slider.value())
        
        self.actionOpen.triggered.connect(self.open_img)
        #self.actionSave.triggered.connect(self.save_img)
        #self.type_slider.clicked.connect(self.type_slide)
        self.value_slider.triggered.connect(self.value_slide)
        
    def open_img(self):
        option=QFileDialog.Options()
        widget=QWidget()
        self.fileName=QFileDialog.getOpenFileName(widget,"Open Single File","Default File", 'Images (*.png, *.xmp *.jpg)',options=option)
        self.label.setPixmap(QtGui.QPixmap(self.fileName[0]))
        
            
    def value_slide(self):
        originalImage = cv2.imread(self.fileName[0],0)
        new_im = Image.fromarray(originalImage)
        from PIL.ImageQt import ImageQt
        qim = ImageQt(new_im)
        img = cv2.cvtColor(qim, cv2.COLOR_BGR2GRAY)
        if self.slider_type == 0:
            ret, thresh1 = cv2.threshold(img, self.slider_type, 255, cv2.THRESH_BINARY) 
        if self.slider_type == 1:
            ret, thresh2 = cv2.threshold(img, self.slider_type, 255, cv2.THRESH_BINARY_INV)
        if self.slider_type == 2:
            ret, thresh3 = cv2.threshold(img, self.slider_type, 255, cv2.THRESH_TRUNC)
        if self.slider_type == 3:
            ret, thresh4 = cv2.threshold(img, self.slider_type, 255, cv2.THRESH_TOZERO) 
        if self.slider_type == 4:
            ret, thresh5 = cv2.threshold(img, self.slider_type, 255, cv2.THRESH_TOZERO_INV) 
        
        self.label.setPixmap(QtGui.QPixmap(self.ret))
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = thresh(MainWindow)
    #ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
        
