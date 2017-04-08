#!/usr/bin/python3

from math import *

import sys

# a = sys.argv[1]
# b = sys.argv[2]
# c = sys.argv[3]
# print('a ' + str(a) + ' b ' + str(b) + ' c ' + str(c))
# x = int(a) + 2 * int(b) + 2 * int(c)
# y = 2 * int(a) + int(b) + 2 * int(c)
# z = 2 * int(a) + 2 * int(b) + 3 * int(c)
# print('x ' + str(x) + ' y ' + str(y) + ' z ' + str(z))
# print(' x2 + y2 == z2')
# print(int(x)**2 + int(y)**2 == int(z)**2)
# print(x + y + z)

a = 1
while a <= 500:
    if (1000 * (500-a) % (1000-a)) == 0:
        print(a, 1000*(500-a) / (1000-a))
    a =  a + 1

#x = (r + s)
#y = (r + t)
#z = (r + s + t)
#x + y + z = 1000
#3r + 2t + 2s = 1000
#6st + 2t + 2s = 1000
#3st + s + t = 500
