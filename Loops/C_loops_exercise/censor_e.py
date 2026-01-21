# Write a function `censor_e(text)` that returns a new string where all 'e' characters
# are replaced with '*'.

# Example:

def censor_e(text):
	#ch = ""
	for ch in text:
		if ch == "e":
			print("*")
		else:
			print(ch)

censor_e("speedy")  #-> 'sp**dy'
censor_e("pending") #-> 'p*nding'
censor_e("scene")   #-> 'sc*n*'
censor_e("heat")    #-> 'h*at'
