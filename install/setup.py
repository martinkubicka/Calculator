## @file widget.py
# @date 27.04.2022
# @author Martin Kubicka (xkubic45)
# @author Dominik Petrik (xpetri25)
# @author Matej Macek (xmacek27)
# @brief code for installator interface

from tabnanny import check
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

        self.header = QtWidgets.QLabel("Antioznuk Calculator Installer", self)
        self.header.move(170, 10)
        self.header.resize(300, 200)
        self.header.setFont(QFont('Arial', 15))
        
        self.check_box = QtWidgets.QCheckBox("Do you want to create desktop shortcut?",self)
        self.check_box.move(50, 200)
        self.check_box.resize(320,40)
        self.check_box.stateChanged.connect(self.clickBox)

        self.button_install = QtWidgets.QPushButton("Install", self.centralwidget)
        self.button_install.setGeometry(QtCore.QRect(250, 400, 100, 50))
        self.button_install.setStyleSheet(styleGreen40)

        self.button_install.clicked.connect(self.install)

        #installing page
        self.label = QtWidgets.QLabel("Progress:", self)
        self.label.move(30, 10)
        self.label.resize(300, 100)
        self.label.setFont(QFont('Arial', 20))
        self.label.hide()

        self.button_exit = QtWidgets.QPushButton("Exit", self.centralwidget)
        self.button_exit.setGeometry(QtCore.QRect(400, 420, 100, 50))
        self.button_exit.setStyleSheet(styleGreen40)
        self.button_exit.clicked.connect(self.exit_app)
        self.button_exit.hide()

        self.cmd = QtWidgets.QPlainTextEdit(self)
        self.cmd.setDisabled(True)
        self.cmd.move(30, 90)
        self.cmd.resize(540, 300)
        self.cmd.hide()

        MainWindow.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def clickBox(self): 
        if self.check_box.isChecked():
            self.checkbox_value = 1
        else:
            self.checkbox_value = 0
    
    def install(self):
        self.check_box.hide()
        self.button_install.hide()
        self.header.hide()

        self.button_exit.show()
        self.label.show()
        self.cmd.show()

        self.run_commands()
    
    def exit_app(self):
        self.close()

    def run_commands(self):  
        cur_path=os.getcwd()

        self.cmd.setDisabled(False)
        self.cmd.insertPlainText("Command: rm -r build\n")
        p = subprocess.Popen("rm -r build", stdout=subprocess.PIPE, shell=True)
        p.wait()
        self.cmd.insertPlainText("Removing build directory..\n")


        self.cmd.insertPlainText("Command: rm -r dist\n")
        p = subprocess.Popen("rm -r dist", stdout=subprocess.PIPE, shell=True)
        p.wait()
        self.cmd.insertPlainText("Removing dist directory..\n")
        
        self.cmd.insertPlainText("Command: pip3 install pyinstaller\n")
        p = subprocess.Popen("pip3 install pyinstaller", stdout=subprocess.PIPE, shell=True)
        p.wait()
        self.cmd.insertPlainText("Installing pyinstaller..\n")

        self.cmd.insertPlainText("Command: python3 -m PyInstaller --paths={pth} --icon=oznukIcon.ico ../repo/src/AntioznukCalculator.py\n".format(pth=cur_path.replace("/install", "/repo")+"/src"))
        p = subprocess.Popen("python3 -m PyInstaller --icon=oznukIcon.ico --paths={pth} ../repo/src/AntioznukCalculator.py".format(pth=cur_path.replace("/install", "/repo")+"/src"), stdout=subprocess.PIPE, shell=True)
        p.wait()
        self.cmd.insertPlainText("Creating executable file..\n")

        file = open("AntioznukCalculator.desktop", "w")
        file.write("[Desktop Entry]\nName=AntioznukCalculator\nComment=Calculator\nTerminal=false\nType=Application\n")
        file.write("Exec="+cur_path+"/dist/AntioznukCalculator/AntioznukCalculator\n")
        file.write("Icon="+cur_path+"/oznukIcon.ico\n")
        file.close()

        p = subprocess.Popen("cp AntioznukCalculator.desktop ~/.local/share/applications", stdout=subprocess.PIPE, shell=True)
        p.wait()

        if self.checkbox_value == 1:
            self.cmd.insertPlainText("Command: ln -s {pth} ~/Desktop/".format(pth=cur_path+"/dist/AntioznukCalculator/AntioznukCalculator")+"\n")
            p = subprocess.Popen("ln -s {pth} ~/Desktop/".format(pth=cur_path+"/dist/AntioznukCalculator/AntioznukCalculator"), stdout=subprocess.PIPE, shell=True)
            p.wait()
            self.cmd.insertPlainText("Creating desktop shortcut..\n")

        self.cmd.insertPlainText("Installation was successful!\n")
        self.cmd.insertPlainText("Execulable file you can find in: {pth} \n".format(pth=cur_path+"/dist/AntioznukCalculator/AntioznukCalculator\n"))
        self.cmd.insertPlainText("You can exit by clicking exit button or closing window!\n")
        self.cmd.setDisabled(True)

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