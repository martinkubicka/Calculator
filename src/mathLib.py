## @file mathLib.py
# @date 17.03.2022
# @author Martin Kubicka (xkubic45)
# @author Dominik Petrik (xpetri25)
# @author Matej Macek (xmacek27)
# @brief Library with basic math functions
from decimal import Decimal

import exceptionMessages as em

## Function for addition two numbers
#
#@param x first addend
#@param y second addend
#
#@return sum of paramater x and y
def add(x,y):
    return Decimal(x)+Decimal(y)

## Function for substract two numbers
#
#@param x first minuend
#@param y second subtrahend
#
#@return difference of paramater x and y
def substract(x,y):
    return Decimal(x)-Decimal(y)

## Function for multiplying two numbers
#
# @param x first factor
# @param y second factor
#
# @return product of parameter x and y
def multiply(x, y):
    return round(Decimal(x)*Decimal(y), 5)

## Function for dividing two numbers
#
# @param x divident
# @param y divisor
#
# @return ratio of parameter x and y
def divide(x, y):

    if Decimal(y) == 0:
        raise Exception(em.DIVISION_BY_ZERO)
    else:
        return round(Decimal(x)/Decimal(y), 5)

## Function for nth power of number
#
#@param x first base
#@param y second exponent
#
#@return power of paramater x and y
def power(x,y):
    if Decimal(y) == 0:
        return 1
    return pow(Decimal(x), Decimal(y))

## Function for n root of  number
#
#@param x first radicand
#@param y second degree
#
#@return root of paramater x and y
def root(x,y):
    #if - x and y is not %2 == 1 break and return warning
    if Decimal(y) % 2 == 0 and Decimal(x) < 0:
        raise Exception(em.ROOT_INVALID_INPUT)
    if Decimal(y) % 2 == 1 and Decimal(x) < 0:
        tmp = round(-((-Decimal(x))** (1/Decimal(y))),5)
        return tmp
    
    else:
        tmp = round((Decimal(x))**(1/Decimal(y)), 5)
    return tmp

## Function for calculation factorial
#
# @param n factorialized number
#
# @return result of factorial
def factorial(n):
    n = Decimal(n)
    if n % 1 != 0 or n < 0:
        raise Exception(em.FACTORIAL_INVALID_INPUT)
    elif n > 50:
        raise Exception(em.FACTORIAL_MAX_INPUT)
    elif n == 0:
        return 1
    else:
        result = n
        n = int(n)

        for i in range(1, n):
            result = result*i
        return result

## Function for calculation Fibonacci sequence
#
# @param n a number which will start Fibonacci sequence
#
# @return Fibonacci number
def fibonacci(n):
    n = Decimal(n)
    if n % 1 != 0 == False or n < 0:
        raise Exception(em.FIBONACCI_INVALID_INPUT)
    elif n > 30:
        raise Exception(em.FIBONACCI_MAX_INPUT)
    elif n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

### End of mathLib.py ####
