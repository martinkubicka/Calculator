# @file parser.py
# @date 27.04.2022
# @author Martin Kubicka (xkubic45)
# @author Dominik Petrik (xpetri25)
# @author Matej Macek (xmacek27)
# @brief Parse calculator input string

from decimal import Decimal, getcontext
import mathLib as math
import AntioznukCalculator
import uiFunctions

##Reads chars from string
#
#@param string string to read from
#@param index where to start reading from
#@param direction in what direction to read in
#
#@return read substring
def peek(string,index,direction):
    if(direction < 0):
        string = string[:index] 
        string = string[::-1] 
    else:
        string = string[index+1:] 
    
    output = ""
    for i,char in enumerate(string):
        if char.isdigit() or char == "." or (char == "-" and i == 0 or( direction == -1 and i == index - 1)): #minus operator edge case check
           output = output + char
        else:
            break
        
    length = len(output)
        
    if(direction < 0):
        return output[::-1],length
    return output, length

##Decide which binary operation to perform and call appropriate function 
#
#@param string 
#@param index where to start reading from
#@param direction in what direction to read in
#
#@return read substring
def binaryOperation(string,operator, index):
    leftInput,leftLength = peek(string,index,-1)
    rightInput, rightLength = peek(string,index,1)
    totalLength = leftLength + rightLength + 1
    start = index - leftLength
        
    if(leftInput == ""):
        if operator == "√":
            output = str(math.root(rightInput,2))
        elif operator == "-":
            output = "-" + rightInput
    elif(rightInput == ""):
        output = leftInput
    elif operator == "+":
        output = str(math.add(leftInput,rightInput))
    elif operator == "-":
        output = str(math.substract(leftInput,rightInput))
    elif operator == "÷":
        output = str(math.divide(leftInput,rightInput))
    elif operator == "×":
        output = str(math.multiply(leftInput,rightInput))
    elif operator == "√":
        output = str(math.root(rightInput,leftInput))
    elif operator == "^":
        output = str(math.power(leftInput,rightInput))
    
    return str(trimDecimal(output)),totalLength,start
    
##Decide which function to perform and call appropriate function 
#
#@param string 
#@param index where to start reading from
#@param direction in what direction to read in
#
#@return read substring
def specialOperation(string,operator,index):
    if operator == "FIB":
        input,length = peek(string,index + 2,1)
        totalLength = length + 3
        start = index
        if (input == ""):
            return ""
        output =str(math.fibonacci(input))
        
        return output,totalLength, start
    if operator == "!":
        input,length = peek(string,index,-1)
        totalLength = length + 1
        start = index - (totalLength -1)
        output = str(math.factorial(input))
        
        return str(trimDecimal(output)),totalLength, start
    
    
def trimDecimal(string):
        dec = Decimal(string)
        if dec - int(dec) == 0:
            return int(dec)
        return dec
##Iterate through a string and replace operators and their inputs with calculated values
#
#@param string
#
#@return calculated value as a string
def parse(string):  
    #parse fibbonaci
    while "FIB" in string:
        for index,char in enumerate(string):
            try:
                if char == "F" and string[index + 1] == "I" and string[index + 2] == "B":
                    replace,length,start = specialOperation(string,"FIB",index)
                    string = string[:start] + replace + string[start + length:]
                    break
            except Exception as e:
                raise Exception(e, index,string)
            
    operatorsWithoutMinus = ["+","×","÷","√","^","FIB","!"] #to handle minus operator, it's different from other ops
    
    #parse factorial and higher priority operators
    while any(op in string for op in ["!","√","^"]):
        try:
            for index,char in enumerate(string):
                if char in ["√","^"]:
                    replace,length,start = binaryOperation(string,char,index)
                    string = string[:start] + replace + string[start + length:]
                    break
                if char in ["!"]:
                    replace,length,start = specialOperation(string,char,index)
                    string = string[:start] + replace + string[start + length:]
                    break
        except Exception as e:
            raise Exception(e, index,string)
        #parse medium priority operators
    while any(op in string for op in ["÷","×"]):
        try:
            for index,char in enumerate(string):
                if char in ["×","÷"]:
                    replace,length,start = binaryOperation(string,char,index)
                    string = string[:start] + replace + string[start + length:]
                    break
        except Exception as e:
            raise Exception(e, index,string)
        
        #parse lowest priority operators
    while any(op in string for op in ["+","-"]) and (string[0] != "-" or string.count("-") > 1 or any(op in string for op in operatorsWithoutMinus)):
        try:
            for index,char in enumerate(string):
                if char in ["+","-"]:
                    if index == 0:
                        continue
                    replace,length,start = binaryOperation(string,char,index)
                    string = string[:start] + replace + string[start + length:]
                    break
        except Exception as e:
            raise Exception(e, index,string)
    getcontext().prec=100
    
    string = Decimal(string).quantize(Decimal("0.1"))
    string = str(trimDecimal(string))
    return str(string)