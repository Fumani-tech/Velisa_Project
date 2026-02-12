# Write a function `trendy_text` that accepts a sentence string as an argument.
# The function should return the sentence where the last vowel of every word
# is removed.

def trendy_text(sentence):
    new_sentence = sentence.split(' ')
    for i in range(len(new_sentence)):
        new_string = remove_last_vowel(new_sentence[i])
        new_sentence[i] = new_string
    return ' '.join(new_sentence)


def remove_last_vowel(str1):
    for i in range(len(str1)-1,-1,-1):
        if str1[i] in 'aeiou' :
            first = str1[0:i]
            last = str1[i+1:]
            return first + last
    return str1


print(trendy_text("the concert will be epic"))
# 'th concrt wll be epc'

print(trendy_text("breakfast food is wonderful"))
# 'breakfst fod s wonderfl'

print(trendy_text("the weather will improve hopefully"))
# 'th weathr wll improv hopeflly'
