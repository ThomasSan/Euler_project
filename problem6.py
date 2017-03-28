#!/usr/local/bin/python3

from math import *

sumSquare = 0
squareSum = 0
i = 1

while i <= 100:
	squareSum = squareSum + i
	sumSquare = sumSquare + pow(i, 2)
	i = i + 1

squareSum = pow(squareSum, 2)
print (str(sumSquare) + ' - ' + str(squareSum) + ' = ' + str(squareSum - sumSquare));
