class FraudulentAcitivityNotation:
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

	def sol1(self,expenditure,d):
		n = len(expenditure)
		count = 0
		for i in range(d,n):
			quicksort(expenditure,i-d,i-1)
			if d % 2 == 1:
				mid = 2 * expenditure[i-d+int(d/2)]
			else:
				mid = expenditure[i-d+int(d/2)] \
				+ expenditure[i-d-1+int(d/2)]
			if expenditure[i] > mid:
				count += 1
		return count 

	def sol2(self,expenditure,d):
		n = len(expenditure)
		count = 0
		quicksort(expenditure,0,d-1)
		for i in range(d,n):
			if d % 2 == 1:
				mid = 2 * expenditure[i-d+int(d/2)]
			else:
				mid = expenditure[i-d+int(d/2)] \
				+ expenditure[i-d-1+int(d/2)]
			if expenditure[i] > mid:
				count += 1
		tag = expenditure[i]
		index = -1
		for j in range(i-d,i):
			if tag <= expenditure[j]:
				index = j
				break
		if index != - 1 and index + 1 <n:
			expenditure[index+1:i+1] = expenditure[index:i]
			expenditure[index] = tag
		return count


# THE most efficient solution!!!!!!!
import math
import os
import random
import re
import sys
from collections import deque

# Complete the activityNotifications function below.

class Proprocessing:
	def __init__(self,Length):
		self.countarr = [0] * 201
		self.queue = deque()
		self.length = Length

	def add(self,v):
		self.queue.append(v)
		self.countarr[v] += 1
		if len(self.queue) > self.length:
			val = self.queue.popleft()
			self.countarr[val] -= 1

	def get_median(self):
		index1 = int(self.length/2)
		index2 = index1 + 1
		count = 0
		mid1 = None
		mid2 = None
		for index,num in enumerate(self.countarr):
			count += num 
			if count >= index1 and mid1 == None:
				mid1 = index 
			if count >= index2 and mid2 == None:
				mid2 = index
				break
		if self.length % 2 == 0:
			return (mid1 + mid2)/2
		else:
			return mid2         

def activityNotifications(expenditure, d):
	pre = Proprocessing(d)
	count = 0
	for i in expenditure[:d]:
		pre.add(i)
	for i,num in enumerate(expenditure[d:]):
		if num >= 2*pre.get_median():
			count += 1
		pre.add(num)
	return count













