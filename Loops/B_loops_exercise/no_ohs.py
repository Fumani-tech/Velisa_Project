# Write a function `no_ohs(text)` that prints each character of the string except 'o'.
# The function does not return a value, just prints.

# Example:

def no_ohs(text):
	for i in range(len(text)):
		if text[i] != "o":
			print(text[i])

no_ohs("code")
# c
# d
# e
