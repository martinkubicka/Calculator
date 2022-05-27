## @file parserTests.py
# @date 24.04.2022
# @author Dominik Petrik (xpetri25)
# @brief Script for testing parser module

import unittest
import parser as p
"×","÷"
testStrings = {"2+2" : "4",
               "2+2+2" : "6",
               "2-8" : "-6",
               "2-423+12-18+7" : "-420",
               "2×2" : "4",
               "2×2×2" : "8",
               "2+7×8-6" : "52",
               "16÷2": "8",
               "12÷10+57×12÷15÷4×62+14": "722",
               }

class Test(unittest.TestCase):
    def testValidInputs(self):
        for input in testStrings:
            self.assertEqual(p.parse(input), testStrings[input])


if __name__ == '__main__':
    unittest.main()
