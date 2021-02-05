# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'threshold.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    
    def __init__(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.type_label = QtWidgets.QLabel(self.centralwidget)
        self.type_label.setGeometry(QtCore.QRect(10, 0, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        
        self.type_label.setFont(font)
        self.type_label.setObjectName("type_label")
        self.type_slider = QtWidgets.QSlider(self.centralwidget)
        self.type_slider.setGeometry(QtCore.QRect(150, 0, 581, 21))
        self.type_slider.setOrientation(QtCore.Qt.Horizontal)
        self.type_slider.setObjectName("type_slider")
        self.type_slider.setMinimum(0)
        self.type_slider.setMaximum(4)
        self.type_slider.setValue(0)
        #self.type_slider.setTickPosition(QSlider.TicksBelow)
        #self.type_slider.setTickInterval(5)
        
        self.value_label = QtWidgets.QLabel(self.centralwidget)
        self.value_label.setGeometry(QtCore.QRect(10, 40, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        
        self.value_label.setFont(font)
        self.value_label.setObjectName("value_label")
        self.value_slider = QtWidgets.QSlider(self.centralwidget)
        self.value_slider.setGeometry(QtCore.QRect(150, 40, 581, 21))
        self.value_slider.setOrientation(QtCore.Qt.Horizontal)
        self.value_slider.setObjectName("horizontalSlider")
        self.value_slider.setMinimum(0)
        self.value_slider.setMaximum(255)
        self.value_slider.setValue(0)
        
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 70, 801, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 80, 801, 461))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label.setScaledContents(True)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.type_label.setText(_translate("MainWindow", "Threshold type:"))
        self.value_label.setText(_translate("MainWindow", "Threshold value:"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(MainWindow)
    # ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
