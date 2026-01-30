def remove_vowels(s):
    new_str = ''
    for i in range(len(s)):
        if s[i] not in 'aeiou':
            new_str = new_str + s[i]
    return(new_str)
            
# Example usage:
print(remove_vowels("jello"))  # 'jll'
print(remove_vowels("sensitivity"))  # 'snstvty'
print(remove_vowels("cellar door"))  # 'cllr dr'

