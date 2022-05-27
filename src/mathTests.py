## @file math-tests.py
# @date 17.03.2022
# @author Martin Kubicka (xkubic45)
# @author Dominik Petrik (xpetri25)
# @author Matej Macek (xmacek27)
# @brief Script for testing math library

import mathLib as math
import unittest
import exceptionMessages as em

##run: python ./math-tests.py

class AddTest(unittest.TestCase):
    def testAddPositiveIntegers(self):
        self.assertEqual(float(math.add(2,2)), 4) ##Add two positive integers
    
    def testAddNegativeIntegers(self):
        self.assertEqual(float(math.add(-2,1)), -1) ##Add two negative integers

    def testAddLargeIntegers(self):
        self.assertEqual(float(math.add(164828224684,474848444858)),639676669542) ##Add two large integers

    def testAddDecimal(self):
        self.assertAlmostEqual(float(math.add(1.175,2.145)),3.32000) ##Add two decimals

class SubstractTest(unittest.TestCase):
    def testSubstractPositiveIntegers(self):
        self.assertEqual(float(math.substract(2,4)),-2) ##Substract two positive integers

    def testSubstractNegativeIntegers(self):
        self.assertEqual(float(math.substract(-8,-4)),-4) ##Substract two negative integers

    def testSubstractDecimal(self):
        self.assertAlmostEqual(float(math.substract(1.1120,2.4200)),-1.30800) ##Substract two decimals
    
class MultiplyTest(unittest.TestCase):
    def testMultiplyPositiveIntegers(self):
        self.assertEqual(float(math.multiply(2,8)),16) ##Multiply two positive integers

    def testMultiplyNegativeIntefers(self):
        self.assertEqual(float(math.multiply(-2,-5)),10) ##Multiply two negative integers

    def testMultiplyDecimal(self):
        self.assertEqual(float(math.multiply(0.25, 0.32)), 0.08) ##Multiply two decimals

    def testMultiplyByZero(self):
        self.assertEqual(float(math.multiply(3,0)),0) ##Multiply by zero
        self.assertEqual(float(math.multiply(0,3)),0)

class DivideTest(unittest.TestCase):
    def testDividePositiveIntegers(self):
        self.assertEqual(float(math.divide(8,4)), 2) ##Divide two positive integers
    
    def testDivideNegativeIntegers(self):
        self.assertEqual(float(math.divide(-3,-2)), 1.5) ##Divide two negative integers
    
    def testDivideDecimals(self):
        self.assertEqual(float(math.divide(0.4,1.5)), 0.26667) ##Divide two decimals

    def testDivideByZero(self):
        with self.assertRaises(Exception):
            math.divide(2,0) ##Divide by zero

class PowerTest(unittest.TestCase):
    def testPowerOfPositiveInteger(self):
        self.assertEqual(float(math.power(2,2)),4) ##Positive integer to the power of positive integer

    def testPowerOfPositiveInteger(self):
        self.assertEqual(float(math.power(4,-2)),0.0625) ##Positive Integer to the power of negative integer
        self.assertEqual(float(math.power(-2,4)),16) ##Negative Integer to the power of positive integer

    def testPowerOfDecimal(self):
        self.assertEqual(float(math.power(16,0.5)),4) ##Integer to the power of decimal

    def testPowerOfZero(self):
        self.assertEqual(float(math.power(7,0)), 1) ##Integer to the power of zero

class RootTest(unittest.TestCase):
    def testSquareRootOfPositiveInteger(self):
        self.assertEqual(float(math.root(4,2)),2) ##Square root of positive integer
        self.assertEqual(float(math.root(3,2)),1.73205)

    def testNthRootOfPositiveInteger(self):
        self.assertEqual(float(math.root(8,3)),2.0) ##Nth root of positive integer
        self.assertEqual(float(math.root(9,3)),2.08008)

    def testNthRootOfZero(self):
        self.assertEqual(float(math.root(0,3)),0.0) ##Nth root of zero

    def testEvenRootOfNegativeInteger(self):
        with self.assertRaises(Exception):
            math.root(-4,2) ##Even root of negative integer

    def testOddRootOfNegativeInteger(self):
        self.assertEqual(float(math.root(-8,3)), -2.0) ##Odd root of negative integer
        
class FactorialTest(unittest.TestCase):
    def testValidInputFactorial(self):
        self.assertEqual(float(math.factorial(0)), 1) ##Positive integer as input
        self.assertEqual(float(math.factorial(2)),2)
        self.assertEqual(float(math.factorial(4)),24)
        self.assertEqual(float(math.factorial(10)),3628800)

    def testInvalidInputFactorial(self):
        with self.assertRaises(Exception):
            math.factorial(-1) ##Negative integer as input
        with self.assertRaises(Exception):
            math.factorial(-10)
        with self.assertRaises(Exception):
            math.factorial(0.1) ##Decimal as input

    def testMaxInputFactorial(self):
        with self.assertRaises(Exception):
            math.factorial(51) ##Maximal input
        with self.assertRaises(Exception):
            math.factorial(1000)

class FibonacciTest(unittest.TestCase):
    def testValidInputFibonacci(self):
        self.assertEqual(float(math.fibonacci(0)),0) ##Positive integer as input
        self.assertEqual(float(math.fibonacci(1)),1)
        self.assertEqual(float(math.fibonacci(2)),1)
        self.assertEqual(float(math.fibonacci(7)),13)
        self.assertEqual(float(math.fibonacci(15)),610)
        self.assertEqual(float(math.fibonacci(30)),832040)

    def testNonValidInputFibonacci(self):
        with self.assertRaises(Exception):
             math.fibonacci(-1) ##Negative integer as input
        with self.assertRaises(Exception):
             math.fibonacci(-10)
        with self.assertRaises(Exception):
             math.fibonacci(0.5)##Decimal as input

    def testMaxInputFibonacci(self):
        with self.assertRaises(Exception):
                math.fibonacci(31) ##Maximal input
        with self.assertRaises(Exception):
                math.fibonacci(100)


if __name__ == '__main__':
    unittest.main()



