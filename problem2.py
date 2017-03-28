total = 2
fibo = 2
tmp = fibo
prev = 1
while (fibo + prev < 4000000):
	tmp = fibo
	fibo = fibo + prev
	if fibo % 2 == 0:
		total = total + fibo
	print('prev ' + str(prev) + 'fibo ' + str(fibo))
	prev = tmp
print ('total ' + str(total))
