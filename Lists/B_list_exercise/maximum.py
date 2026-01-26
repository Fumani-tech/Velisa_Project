# Write a function `maximum(numbers)` that accepts a list of numbers.
# The function should return the largest number in the list.
# If the list is empty, return None.

def maximum(num):
	if len(num) == 0:
			return "None"
	large = 0
	for i in range(len(num)):
		if num[i] > large:
			large = num[i]
	return large

# Example:
print(maximum([5, 6, 3, 7])) #-> 7
print(maximum([17, 15, 19, 11, 2])) #-> 19
print(maximum([])) #-> None