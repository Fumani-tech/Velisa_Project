#Write `sum_of_range(n)`
#Print the sum of numbers from 1 to n.

def sum_of_range(n):
	total = 0
	for i in range(1,n+1):
		total= total + i
		print(total)

sum_of_range(5)
# prints: 15