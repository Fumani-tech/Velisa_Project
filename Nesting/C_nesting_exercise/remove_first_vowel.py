# Write a function `remove_first_vowel(s)` that accepts a string and returns the string
# with its first vowel removed.


def remove_first_vowel(s):
    for i in range(len(s)):
        if s[i] in 'aeiou':
            first = s[:i]
            last = s[i+1:]
            return first + last

# Example usage:
print(remove_first_vowel("volcano"))  # 'vlcano'
print(remove_first_vowel("celery"))  # 'clery'
print(remove_first_vowel("juice"))  # 'jice'

