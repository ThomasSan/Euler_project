#!/usr/bin/python

import sys

# Trying to implement the Sieve of Atkin's Algorithm

def isprime(nb):
	i = 3;
	if nb % 2 == 0:
		return False
	while (i < nb / 2):
		if (nb % i == 0):
			return False
		i = i + 2
	return True

limit = 10000000

def primes(n):
	sieve = [True] * (n/2)
	for i in xrange(3, int(n**0.5)+1,2):
		if sieve[i/2]:
			sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
	return [2] + [2*i+1 for i in xrange(1,n/2) if sieve[i]]

total = 0
i = 1

a = primes(limit)
print(a[10000])
