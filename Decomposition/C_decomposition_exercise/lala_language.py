# Write a function `lala_language` that accepts a sentence string as an argument.
# The function should return a new sentence where words longer than 3 characters
# are modified.
#
# Modified words should have each vowel followed by 'l' and the same vowel again.
# See the examples below.

def lala_language(string):
    new_sentence = ''
    separate = string.split(' ')
    for el in separate:
        if len(el) > 3:
            new_word = ''
            for char in el:
                if char in 'aeiou':
                    new_word += char + 'l' + char
                else:
                    new_word += char
        else:
            new_word = el
        new_sentence += new_word + ' '
    else:
        new_sentence += el + ' '
    return new_sentence.strip()

print(lala_language('this is pretty strange'))
# 'thilis is preletty stralangele'

print(lala_language('can you speak our language'))
# 'can you spelealak our lalangulualagele'
