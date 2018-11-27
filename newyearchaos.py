class NewYearChaos:
	def __init__(self,q):
		self.q = q

	def sol1(self):
		q = self.q
		for i,num in enumerate(q):
			if num-1-i > 2:
				return 'Too chaotic'
		n = len(q)
		if n == 1:
			return 0
		index_n = q.index(n)
		q.remove(n)
		return n - 1 -index_n + NewYearChaos(q)
	
	def sol2(self):
		q = self.q
		for i, num in enumerate(q):
			if num-1-i > 2:
				print('Too chaotic')
		swaps = 0
		for i in range(len(q)-1):
			for j in range(len(q)- 1):
				if q[j] > q[j+1]:
					q[j],q[j+1] = q[j+1],q[j]
					swaps += 1
					swapped = True
			if swapped:
				swapped = False
			else:
				break
		print(swaps)

New = NewYearChaos([1,2,5,3,7,8,6,4])
New.sol2()