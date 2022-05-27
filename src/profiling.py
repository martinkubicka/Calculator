## @file profiling.py
# @date 29.03.2022
# @author Martin Kubicka (xkubic45)
# @author Dominik Petrik (xpetri25)
# @author Matej Macek (xmacek27)
# @brief Program for profiling mathLib.py

##run: python ./profiling.py input (for example: python ./profiling < data10.txt)

import sys
sys.path.insert(0, '../src/')
import mathLib as math

## @brief Function for getting data from stdin
#
# @return array with processed data
def getData():
    data = []
    for line in sys.stdin:
        for i in line.split(" "):
            data.append(i.replace("\n", "").replace("\t", ""))
    return data

## @brief Function for calculating average number from data array
#
# @return average number from data array
def getAverage():
    result = 0
    for i in data:
        result = math.add(result, i)
    return math.divide(result, len(data))

## @brief Function for calculating variance
#
# @return variance
def getVariance():
    result = 0
    for i in data:
        result += math.power(math.substract(i, average), 2)
    return math.divide(result, len(data))

## @brief Function for calculating standart deviation
#
# @return standart deviation
def getStandartDeviation():
    return math.root(variance, 2)

if __name__ == "__main__":
    data = getData()
    average = getAverage()
    variance = getVariance()
    print(getStandartDeviation())

### End of profiling.py ###