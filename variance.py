## calculate dispersion

import math

def getAverage(arr):
    result = 0
    numberOfelements = len(arr)
    for i in arr:
        result += i
    try:
        return result / numberOfelements
    except ZeroDivisionError:
        print('Division by zero')

def getVarianceValues(averageValue, arr):
    resultValues = []
    for i in arr:
        resultValues.append(pow(i - averageValue, 2))
    return resultValues

def calculateVarience(varienceArr):
    sumVarience = 0
    divider = abs(len(varianceArr) - 1)
    for i in varienceArr:
        sumVarience += i
    try:
        return math.sqrt(sumVarience / divider)
    except ZeroDivisionError:
        print('Division by zero')



try:
    valuesArray = list(map(int, input().split()))
except Exception:
    print('Please, use "space" for enter')

avgVal = int(getAverage(valuesArray))
varianceArr = getVarianceValues(avgVal, valuesArray)
variance = calculateVarience(varianceArr)

print(variance)

