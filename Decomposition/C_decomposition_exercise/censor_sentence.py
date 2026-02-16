# Write a function `censor_sentence(sentence, target_words)` that accepts:
# - a sentence string
# - a list of target words
#
# The function should return a new sentence where each target word
# is replaced with '*' characters of the same length.

def censor_sentence(sentence, target_words):
    new_sentence = ''
    separate = sentence.split(' ')
    for el in separate:
        if el in target_words:
            new_sentence += '*' * len(el) + ' '
        else:
            new_sentence += el + ' '
    return new_sentence.strip()

print(censor_sentence('where the heck is my celery', ['heck','celery']))
# 'where the **** is my ******'

print(censor_sentence('why you little sweetheart', ['sweetheart','salad']))
# 'why you little **********'
