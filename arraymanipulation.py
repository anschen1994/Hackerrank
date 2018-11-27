class ArrayManipulation:

	def sol1(self,n,queries):
		arr = [0 for i in range(n)]
		for query in queries:
			for i in range(query[0]-1,query[1]):
				arr[i] += query[2]
		return max(arr)

	def sol2(self,n,queries):
		'very very very nice'
		l = [0] * n 
		for query in queries:
			l[query[0] - 1] += query[2]
			if query[1] < n:
				l[query[1]] += -query[2]
		res = 0 
		x = 0
		for i in l:
			x += i 
			res = max(x,res)
		return res 