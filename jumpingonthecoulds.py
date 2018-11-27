class JumpingOnTheClouds:
	def sol1(self,c):
		steps = 0
	n = len(c)
	index = 0
	while index < n - 1:
		steps += 1
		if index == n - 2:
			break
		if c[index + 2] == 1:
			index += 1
		else:
			index += 2
	return steps