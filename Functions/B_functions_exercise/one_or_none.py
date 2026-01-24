# Write a function `one_or_none` that accepts two boolean values.
# Return True if EXACTLY ONE of them is True.
# Return False if both are True OR both are False.

def one_or_none(bool1,bool2):
	if (bool1 == True and bool2 == False) or (bool1 == False and bool2 == True):
		return True
	else:
		return False


print(one_or_none(False, False))   # False
print(one_or_none(True, False))    # True
print(one_or_none(False, True))    # True
print(one_or_none(True, True))     # False