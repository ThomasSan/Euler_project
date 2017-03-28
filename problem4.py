#!/usr/local/bin/python3

import sys

#number = sys.argv[1]
start = 999
end = 999
res = 0

while (end > 99):
	string = str(start * end)
	if (string == string[::-1] and int(string) > res):
		print(str(start) + ' * ' + str(end) + ' = ' + string)
		res = int(string)
	start = start - 1
	if start < 100:
		end = end - 1 
		start = 999

print('max == ' + str(res))
