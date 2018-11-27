class SockMechant:

	def sol1(self,m,ar):
		d = {}
		for index,color in enumerate(ar):
			d[color] = d.get(color,0) + 1
		pairs = 0
		for i in d:
			pairs += int(d[i]/2)
		return pairs