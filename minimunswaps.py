def MinimumSwaps(arr):
	arrturple = [*enumerate(arr)]
	arrturple.sort(key = lambda it: it[1])
	# print(arrturple)
	# initialize a directed cycle
	n = len(arr)
	v = [False for i in range(n)]
	res = 0
	for i,turple in enumerate(arrturple):
		cycles = 0
		if v[i] or turple[0] == i:
			continue
		j = i 
		while v[j] == False:
			v[j] = True 
			j = arrturple[j][0]
			cycles += 1
		res += cycles - 1
	return res 


arrtest = [2,4,5,1,3]
print(MinimumSwaps(arrtest))