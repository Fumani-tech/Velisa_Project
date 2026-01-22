# Write a function `total(numbers)` that accepts a list of numbers as an argument.
# The function should return the sum of all elements in the list.

# Example:

def total(numbers):
	result = 0
	#for n in numbers:
	for i in range(len(numbers)):
		result = result + numbers[i]
	print(result)	

total([3, 2, 8]) #-> 13
total([-5, 7, 4, 6]) #-> 12
total([7]) #-> 7
total([]) #-> 0