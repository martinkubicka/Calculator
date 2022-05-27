## @file widget.py
# @date 27.04.2022
# @author Martin Kubicka (xkubic45)
# @author Dominik Petrik (xpetri25)
# @author Matej Macek (xmacek27)
# @brief code for installator interface

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import os, sys
import subprocess
    
class Ui_MainWindow(QMainWindow):    
    checkbox_value = 0   
    def setupUi(self, MainWindow):
        styleGreen40 = "QPushButton:hover{background-color: rgb(8, 114, 79);}QPushButton{background-color: rgb(18, 134, 99);font: 20pt Arial;color: rgb(255, 255, 255);border-radius: 15px;border: none;selection-color: rgb(80, 49, 255);}"

        self.process = QtCore.QProcess()

        self.setStyleSheet("background-color: white;")
        self.setObjectName("MainWindow")
        self.setFixedSize(600, 500)
        self.setWindowTitle("Antioznuk Calculator Installer")
        self.statusBar().setVisible(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.header = QtWidgets.QLabel("Antioznuk Calculator Uninstaller", self)
        self.header.move(160, 10)
        self.header.resize(300, 200)
        self.header.setFont(QFont('Arial', 15))
        
        self.button_install = QtWidgets.QPushButton("Uninstall", self.centralwidget)
        self.button_install.setGeometry(QtCore.QRect(250, 400, 120, 50))
        self.button_install.setStyleSheet(styleGreen40)

        self.button_install.clicked.connect(self.install)

        #installing page
        self.label = QtWidgets.QLabel("Successfully uninstalled", self)
        self.label.move(150, 10)
        self.label.resize(300, 200)
        self.label.setFont(QFont('Arial', 20))
        self.label.hide()

        self.button_exit = QtWidgets.QPushButton("Exit", self.centralwidget)
        self.button_exit.setGeometry(QtCore.QRect(400, 420, 100, 50))
        self.button_exit.setStyleSheet(styleGreen40)
        self.button_exit.clicked.connect(self.exit_app)
        self.button_exit.hide()


        MainWindow.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def install(self):
        self.button_install.hide()
        self.header.hide()

        self.button_exit.show()
        self.label.show()

        self.run_commands()
    
    def exit_app(self):
        self.close()
        p = subprocess.Popen("rm -r ../install" , stdout=subprocess.PIPE, shell=True)

    def run_commands(self):  
        p = subprocess.Popen("rm -r ~/Desktop/AntioznukCalculator", stdout=subprocess.PIPE, shell=True)
        p.wait()
        p = subprocess.Popen("rm -r ~/.local/share/applications/AntioznukCalculator.desktop", stdout=subprocess.PIPE, shell=True)
        p.wait()
        p = subprocess.Popen("rm -r dist", stdout=subprocess.PIPE, shell=True)
        p.wait()
        p = subprocess.Popen("rm -r build", stdout=subprocess.PIPE, shell=True)
        p.wait()
        p = subprocess.Popen("rm -r oznukIcon.ico", stdout=subprocess.PIPE, shell=True)
        p.wait()
        p = subprocess.Popen("rm -r setup", stdout=subprocess.PIPE, shell=True)
        p.wait()
        p = subprocess.Popen("rm -r AntioznukCalculator.spec", stdout=subprocess.PIPE, shell=True)
        p.wait()
        p = subprocess.Popen("rm -r AntioznukCalculator.desktop", stdout=subprocess.PIPE, shell=True)
        p.wait()
        p = subprocess.Popen("rm -r ../repo", stdout=subprocess.PIPE, shell=True)
        p.wait()
        p = subprocess.Popen("rm -r ../doc", stdout=subprocess.PIPE, shell=True)
        p.wait()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    
    ui.setAttribute(Qt.WA_NoSystemBackground, True)
    ui.setAttribute(Qt.WA_TranslucentBackground, True)
    ui.setupUi(ui)

    ui.show()
    sys.exit(app.exec_())