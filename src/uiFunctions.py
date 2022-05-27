## @file uiFunctions.py
# @date 22.04.2022
# @author Martin Kubicka (xkubic45)
# @author Dominik Petrik (xpetri25)
# @author Matej Macek (xmacek27)
# @brief Script where are declared functions for ui.py script

from email.errors import MessageError
import webbrowser
import parser

error = False
originalString = ""

## @brief function for appedning number to label
#  @param num digit appended to label 
def addNumber(self, num):
    self.label.setText(self.label.text() + num)
## @brief function for deleting last character from label
def delete(self):
    global error
    if error:
            self.label.setText(originalString)
            normalState(self)
    try:
            if self.label.text()[-1] == "B":
                    self.label.setText(self.label.text()[:-3])
            else:
                    self.label.setText(self.label.text()[:-1])
    except:
            pass
def equals(self):
    equalsSymbolList = ["+", "-", "÷", "×", "FIB", "√", "^"]
    if(len(self.label.text()) > 0 and not error and self.label.text()[-1] not in equalsSymbolList):
        try:
                result = parser.parse(self.label.text())
                self.label.setText(result)
        except Exception as e:
                errorState(self,e)
## @brief function for deleting all characters from label
def allClear(self):
    normalState(self)
    self.label.setText("")
## @brief function for appedning + to label
def addPlus(self):
    if not error:
        try:
                if self.label.text()[-1].isdigit() == True:
                        self.label.setText(self.label.text() + "+")
        except:
                pass
## @brief function for appedning - to label
def addMinus(self):
    if not error:
        self.label.setText(self.label.text() + "-")
    
## @brief function for appedning divide symbol to label
def addDivide(self):
    if not error:
        try:
                if self.label.text()[-1].isdigit() == True:
                        self.label.setText(self.label.text() + "÷")
        except:
                pass
## @brief function for appedning multiply symbol to label
def addMultiply(self):
    if not error:
        try:
                    if self.label.text()[-1].isdigit() == True:
                            self.label.setText(self.label.text() + "×")
        except:
                    pass
## @brief function for appedning . to label
def addDot(self):
    if not error:
        symbolList = ["+", "-", "÷", "×", "!", "FIB", "√", "^"]
        try:
                if self.label.text()[-1].isdigit() == True: 
                        index = -2
                        dotInString = False
                        ## check if in last entered number has dot (avoid for example 125.4.5) 
                        while (len(self.label.text())+1 != abs(index) and (not self.label.text()[index] in symbolList)):
                                if self.label.text()[index] == ".":
                                        dotInString = True
                                        break
                                index -= 1
                        if dotInString == False:
                                self.label.setText(self.label.text() + ".") 
        except:
                pass
## @brief function for appedning ! to label
def addFactorial(self):
    if not error:
        try:
                    if self.label.text()[-1].isdigit() == True:
                            self.label.setText(self.label.text() + "!")
        except:
                    pass
## @brief function for appedning fibonacci shortcut to label
def addFibonacci(self):
    if not error:
        if (len(self.label.text()) == 0 or not self.label.text()[-1].isdigit()):
                self.label.setText(self.label.text() + "FIB")
## @brief function for appedning root symbol to label
def addRoot(self):
    if not error:
        self.label.setText(self.label.text() + "√")
## @brief function for appedning power symbol to label
def addPower(self):
    if not error:
        try:
                    if self.label.text()[-1].isdigit() == True:
                            self.label.setText(self.label.text() + "^")
        except:
                    pass

## @brief function for opening user manual
def openUserManual(self):
    webbrowser.open_new("../dokumentace.pdf")
    
## @brief function for printing error to user   
def errorState(self, message):
        global error
        global originalString
        self.label.setStyleSheet("background-color: rgb(36, 36, 36);\n"
"border: 1px solid rgb(223, 102, 103);\n"
"border-radius: 10;\n"
"color: rgb(255,255,255);\n"
"font: 50pt \"Arial\";\n"
"padding-left :15px;\n"
"padding-right :25px;")
       
        error = True
        originalString = message.args[2]
        beforeError = message.args[2][:message.args[1]]
        onError = message.args[2][message.args[1]]
        afterError = message.args[2][message.args[1] + 1:]
        
        self.label.setText("""
                       {}<span style="color: rgb(223, 102, 103);">{}</span>{} 
                       """.format(beforeError,onError,afterError))
        
        self.errorLabel.setText(str(message.args[0]))

## @brief function for returning back to normal state   
def normalState(self):
        global error
        error = False
        self.label.setStyleSheet("background-color: rgb(36, 36, 36);\n"
"border: none;\n"
"border-radius: 10;\n"
"color: rgb(255,255,255);\n"
"font: 50pt \"Arial\";\n"
"padding-left :15px;\n"
"padding-right :25px;")
        self.errorLabel.setText("")