# Write a function `funny_phrase` that accepts a sentence string.

# The function should return the sentence where **every other word** has its vowels repeated **twice consecutively**.

# Vowels are: `a, e, i, o, u`

def funny_phrase(sentence):
    list1 = sentence.split(' ')
    ans_list = []
    for i in range (len(list1)):
        if i % 2 == 0 :
            ans_list.append(list1[i])
        else:
            double_word = double_vowel(list1[i])
            ans_list.append(double_word)
    return ' '.join(ans_list)

def double_vowel(string):
    ans_str = ''
    for el in string:
        if el in 'aeiou':
            ans_str = ans_str + el + el
        else:
            ans_str += el
    return ans_str

print(funny_phrase("she dreamed of being a runner"))
# 'she dreeaameed of beeiing a ruunneer'

print(funny_phrase("park near the stoplight"))
# 'park neeaar the stoopliight'

print(funny_phrase("we need many gardeners"))
# 'we neeeed many gaardeeneers'
