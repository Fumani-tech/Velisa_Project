# Write a function `bleep_vowels(text)` that accepts a string and returns
# a new string where all vowels (a, e, i, o, u) are replaced with '*'.
# Example:

def bleep_vowels(text):
	new_string=""
	for i in range(len(text)):
		if text[i] in "aeiou":
			new_string= new_string + "*"
		else:
			new_string= new_string + text[i]
	print (new_string)

bleep_vowels("skateboard") #-> 'sk*t*b**rd'
bleep_vowels("slipper") #-> 'sl*pp*r'
bleep_vowels("range") #-> 'r*ng*'
bleep_vowels("brisk morning") #-> 'br*sk m*rn*ng'