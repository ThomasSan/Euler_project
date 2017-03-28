#!/usr/local/bin/python3

import sys

def isprime(nb):
	i = 3;
	if nb % 2 == 0:
		return 0
	while (i < nb):
		if (nb % i == 0):
			return 0
		i = i + 2
	return 1

total = 0
number = int(sys.argv[1])
i = 3
while number > 1:
	while i <= number:
		if (isprime(i) and number % i == 0):
			number = number / i
			print('factor ' + str(i))
		i = i + 1
	i = 3
