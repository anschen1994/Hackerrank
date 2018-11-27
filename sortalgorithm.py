class SortArray:

	def bubble_sort(self,arr):
		n = len(arr)
		for i in range(n-1):
			for j in range(n-1):
				if arr[j] > arr[j+1]:
					arr[j],arr[j+1] = arr[j+1],arr[j]
					swapped = True
			if swapped:
				swapped = False
			else:
				break
		return arr

	def insert_sort(self,arr):
		arr0 = [arr[0]]
		for i in arr:
			for index,j in enumerate(arr0):
				if i < j:
					arr0.insert(index,i)
					break
		return arr0

	def partition(self,arr,left,right,pivotindex):
		pivot = arr[pivotindex]
		arr[right],arr[pivotindex] = arr[pivotindex],arr[right]
		storeindex = left
		for i in range(left,right):
			if arr[i] < pivot:
				arr[i],arr[storeindex] = arr[storeindex],arr[i]
				storeindex += 1
		arr[storeindex],arr[right] = arr[right],arr[storeindex]
		return storeindex


	def quick_sort(self,arr,left,right):
		if left >= right:
			return
		pivotindex = int((left+right)/2)
		storeindex = self.partition(arr,left,right,pivotindex)
		self.quick_sort(arr,left,storeindex-1)
		self.quick_sort(arr,storeindex+1,right)

	def quicksort(self,array,left,right):
		if left >= right:
			return
		low = left 
		high = right
		key = array[low]
		while left < right:
			while left < right and array[right] > key:
				right -= 1
			array[left] = array[right]
			while left < right and array[left] <= key:
				left += 1
			array[right] = array[left]
		array[right] = key
		self.quicksort(array,low,left - 1)
		self.quicksort(array,left + 1,high)





if __name__ == '__main__':
	arr = [5,4,2,2,0,1]
	sort = SortArray()
	sort.quick_sort(arr,0,len(arr)-1)
	print(arr)

