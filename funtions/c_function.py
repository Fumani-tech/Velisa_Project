#Write a function divisible (num1, num2) that returns True if num1 is divisible by num2 otherwise False

from itertools import count


def divisible(num1, num2):
    if num1 % num2 == 0:
        return True
    else:
        return False
print(divisible(12, 3))    # True
print(divisible(12, 5))    # False
print(divisible(60, 4))    # True
print(divisible(60, 11))   # False
print(divisible(21, 7))    # True
print(divisible(21, 6))    # False

#Write a function case_change(text, make_upper):
#if make_upper is True return the string in uppercase
#if False return it in lowercase

def case_change(text,make_upper):
	if (make_upper == True):
		return text.upper()
	else:
		return text.lower()

print(case_change("Super", True))      # SUPER
print(case_change("Super", False))     # super
print(case_change("tAmBourine", True)) # TAMBOURINE
print(case_change("tAmBourine", False))# tambourine


#write a function in_range(min_val, max_val, n)
#Return True if n is between min_val and max_val(inclusive)

def in_range(min_val, max_val , n):
	if (n >= min_val) and (n <= max_val):
		return True
	else:
		return False

print(in_range(5, 13, 8))     # True
print(in_range(5, 13, 29))    # False
print(in_range(100, 125, 100))# True
print(in_range(100, 125, 99)) # False
print(in_range(40, 45, 44))   # True
print(in_range(40, 45, 45))   # True
print(in_range(40, 45, 46))   # False


#Write average_of_four(a,b,c,d) that returns the average of four numbers.

def average_of_four(a,b,c,d):
	return (a+b+c+d)/4  

print(average_of_four(10, 4, 12, 3))     # 7.25
print(average_of_four(-20, 50, 4, 21))   # 13.75
print(average_of_four(5, 5, 3, 7))       # 5

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

#Write a function larger(a,b)
#return the larger of the two numbers

def larger(a,b):
	if a > b:
		return a
	else:
		return b

print(larger(256, 400))   # 400
print(larger(31, 4))      # 31
print(larger(-6, 7))      # 7
print(larger(11.3, 11.2)) # 11.3
print(larger(-10, -3))    # -3


#Write a function `contains(str1, str2)` that:

#- Returns **True** if `str2` is found inside `str1`
#- Ignore capitalization differences

def contains(str1,str2):
	if str2.lower() in str1.lower():
		return True
	else:
		return False

print(contains("caterpillar", "pill"))     # True
print(contains("lion's share", "on"))      # True
print(contains("SORRY", "or"))             # True
print(contains("tangent", "gem"))          # False
print(contains("clock", "ok"))             # False

#Write a function reverse_string(text) that returns the reversed string.

def reverse_string(s):
	return s[::-1]
print(reverse_string("hello"))   # olleh
print(reverse_string("Python"))  # nohtyP


#Write `count_vowels(text)`

#Return how many vowels are in the string.

def count_vowels(text):
    vowels = "a", "e", "i", "o", "u" 
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

print(count_vowels("hello"))        # 2
print(count_vowels("Programming"))  # 3