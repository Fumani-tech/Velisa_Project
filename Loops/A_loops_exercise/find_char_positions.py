#Write a function that prints all **indexes** where a character appears in a string.

def find_char_positions(str1,str2):
	for i in range(len(str1)):
		if str2 == str1[i]:
			print (i)
		

find_char_positions("banana", "a")
# 1
# 3
# 5
