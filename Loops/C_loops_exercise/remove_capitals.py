# Write a function `remove_capitals(text)` that returns a new string with all
# capital letters removed.
# Example:

def remove_capitals(text):
	ch = ""
	for ch in text:
		if ch.lower() == ch:
			print(ch)

remove_capitals("fOrEver")     #-> 'frver'
remove_capitals("raiNCoat")    #-> 'raioat'
remove_capitals("cElLAr Door") #-> 'clr oor'
