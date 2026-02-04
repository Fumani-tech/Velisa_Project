#Write a function `letter_map` that accepts:

#- a string
#- a dictionary

#The function should return a new string where characters that appear as keys in the dictionary are replaced with their corresponding values.

def letter_map(string, mapping):
    new_string = ""
    for char in string:
        if char in mapping:
            new_string += mapping[char]
        else:
            new_string += char
    return new_string

print(letter_map("symbolic", {"y":"i","o":"a","c":"k" }))
# 'simbalik'

print(letter_map("colossal", {"o":"x","s":"p" }))
# 'cxlxppal'

print(letter_map("miniscule", {"u":"t","i":"f","e":"q" }))
# 'mfnfsctlq'
