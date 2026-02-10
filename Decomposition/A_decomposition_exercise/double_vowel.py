# Write a function `double_vowel` that accepts a string as an argument.

# The function should return a new string where **every vowel** in the original string is repeated **twice consecutively**.

# Vowels are: `a, e, i, o, u`

def double_vowel(string):
    ans_str = ''
    for el in string:
        if el in 'aeiou':
            ans_str = ans_str + el + el
        else:
            ans_str += el
    return ans_str

print(double_vowel("runner"))
# 'ruunneer'

print(double_vowel("stoplight"))
# 'stoopliight'

print(double_vowel("gardener"))
# 'gaardeeneer'
