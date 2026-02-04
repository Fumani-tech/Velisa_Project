#Write a function `most_common_letter` that accepts a string as an argument.

#The function should return the character that appears **most frequently** in the string.

#You may assume:

#- There are **no ties**
#- The string contains only lowercase letters

def most_common_letter(string):
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    max_count = 0
    most_common_char = ""
    for char, count in char_count.items():
        if count > max_count:
            max_count = count
            most_common_char = char

    return most_common_char

print(most_common_letter("building"))
# 'i'

print(most_common_letter("shoestring"))
# 's'

print(most_common_letter("preparedness"))
# 'e'
