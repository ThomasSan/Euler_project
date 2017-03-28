#!/usr/local/bin/python3

import sys

def divByTwenty(nb, div):
	i = 1
	while i <= div:
		if (nb % i != 0):
			return 0
		i = i + 1
	print("The number " + str(nb) + " is divisible all 1st 20 numbers")
	return 1

res = 0
nb = 2520

while divByTwenty(nb, 20) == 0:
	nb = nb + 60
	#while (nb):
	#	if (nb % 5 == 0 and nb % 3 == 0 and nb % 20 == 0):
	#		break ;
	#	nb = nb + 2

