class CountingValleys:
	def sol1(self,n,s):
		height = 0
		count_valley = 0
		for direct in s:
			if direct == 'U':
				height += 1
			else:
				height -= 1
				if height == -1:
					count_valley += 1
		return count_valley