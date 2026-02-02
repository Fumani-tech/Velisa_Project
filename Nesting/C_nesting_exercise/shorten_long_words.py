# Write a function `shorten_long_words(sentence)` that accepts a string and returns
# the same sentence where words longer than 4 characters have their vowels removed.

def shorten_long_words(sentence):
    new_sentence = sentence.split(" ")
    ans = ''
    for word in new_sentence:
        if len(word) <= 4:
            ans+= word + ' '
        else:
            ans += remove_vowels(word) + ' '
    return ans

def remove_vowels(s):
    new_str = ''
    for i in range(len(s)):
        if s[i] not in 'aeiou':
            new_str = new_str + s[i]
    return(new_str)       

# Example usage:
print(shorten_long_words("they are very noble people"))  # 'they are very nbl ppl'
print(shorten_long_words("stick with it"))  # 'stck with it'
print(shorten_long_words("ballerina, you must have seen her"))  # 'bllrna, you must have seen her'
