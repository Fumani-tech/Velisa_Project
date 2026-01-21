# Write a function `raise_power(base, exponent)` that returns the result of
# base raised to the exponent using loops (do not use ** operator or math.pow).

# Example:

def raise_power(base, exponent):
	total = 1
	for i in range(exponent):
		total = total*base
	print(total)

raise_power(2, 5)  #-> 32
raise_power(4, 3)  #-> 64
raise_power(10, 4) #-> 10000
raise_power(7, 2)  #-> 49