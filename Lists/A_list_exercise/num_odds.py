# Write a function `num_odds(numbers)` that accepts a list of numbers.
# The function should return the count of odd numbers in the list.
# Example:

def num_odds(numbers):
	count= 0
	for i in range(len(numbers)):
		if numbers[i] % 2 != 0:
			count = count + 1
	print(count)
		
	


num_odds([4, 7, 2, 5, 9]) #-> 3
num_odds([11, 31, 58, 99, 21, 60]) #-> 4
num_odds([100, 40, 4]) #-> 0