# Write a function `remove_first_vowel(s)` that accepts a string and returns the string
# with its first vowel removed.

def remove_first_vowel(s):
    new_str = ''
    vowel_found = False
    for i in range(len(s)):
        if s[i] not in 'aeiou'  :
            new_str+= s[i]
        else:
            vowel_found = True
            break
    if vowel_found:
        new_str += s[i+1:]
    return new_str


# Example usage:
print(remove_first_vowel("volcano"))  # 'vlcano'
print(remove_first_vowel("celery"))  # 'clery'
print(remove_first_vowel("juice"))  # 'jice'

