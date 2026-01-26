#write a function:
#if number is even return half
#If number is odd return double

def number_change(number):
	if number % 2 == 0:
		return number/2
	else:
		return number*2

print(number_change(6))   # 3
print(number_change(7))   # 14
print(number_change(16))  # 8
print(number_change(21))  # 42