#Write sum_upto(n)
#Return the sum of numbers from 1 → n.

def sum_upto(n):
	s = 0
	for i in range(1, n+1):
		s += i
	return s
print(sum_upto(5))   # 15
print(sum_upto(10))  # 55