class MinimumSwaps2:

	def sol1(self,arr):
		n = len(arr)
		swaps = 0
		d = {}
		for i, num in enumerate(arr):
			d[num] = i
		for i in range(n):
			index = d[i+1]
			if index != i:
				d[arr[i]],d[i+1] = index,i
				arr[i],arr[index] = arr[index],arr[i]
				print(arr)
				swaps += 1
		return swaps 

if __name__ == '__main__':
	ar = [1,3,5,2,4,6,7]
	minswap = MinimumSwaps2()
	print(minswap.sol1(ar))
