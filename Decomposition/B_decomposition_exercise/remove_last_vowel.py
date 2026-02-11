## **removeLastVowel**

# Write a function `remove_last_vowel` that accepts a string as an argument.
# The function should return the string with its last vowel removed.
# Vowels are the letters: a, e, i, o, u

def remove_last_vowel(str1):
    for i in range(len(str1)-1,-1,-1):
        if str1[i] in 'aeiou':
            first = str1[0:i]
            last = str1[i+1:]
            return first + last
    return str1
        
    
print(remove_last_vowel("speaker"))# 'speakr'
print(remove_last_vowel("trading"))# 'tradng'
print(remove_last_vowel("thunder"))# 'thundr'
print(remove_last_vowel("myth"))# 'myth'
