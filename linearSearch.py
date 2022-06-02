# Searching an element in a list/array in python
# can be simply done using \'in\' operator
# Example:
# if x in arr:
# print arr.index(x)

# If you want to implement Linear Search in python

# Linearly search x in arr[]
# If x is present then return its location
# else return -1

#A program is called recursive when an entity calls itself. A program is call iterative when there is a loop (or repetition).

def search(arr, x):

	for i in range(len(arr)):

		if arr[i] == x:
			return i

	return -1

# This is similar to the above one, with the only difference
# being that it is using the recursive approach instead of iterative.


def search(arr, curr_index, key):
	if curr_index == -1:
		return -1
	if arr[curr_index] == key:
		return curr_index
	return search(arr, curr_index-1, key)
