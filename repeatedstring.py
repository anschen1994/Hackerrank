class RepeatedString:
	def sol(self,s,n):
		num_a = 0
		for letter in s:
			if letter == 'a':
				num_a += 1
		res = num_a * int(n/len(s))
		for letter in s[:n%len(s)]:
			if letter == 'a':
				res += 1
		return res 