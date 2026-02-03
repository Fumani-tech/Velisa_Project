# Write a function `email_parse` that accepts an email address string.

# The function should return a dictionary containing:

# - `username`
# - `domain`


def email_parse(email):
    list = email.split('@')
    return {'username':list[0], 'domain': list[1]}


print(email_parse("coolcoder42@goodmail.com"))
# { 'username': 'coolcoder42', 'domain': 'goodmail.com' }

print(email_parse("az@woohoomail.com"))
# { 'username': 'az', 'domain': 'woohoomail.com' }

print(email_parse("1337pr0graMmer@coldmail.edu"))
# { 'username': '1337pr0graMmer', 'domain': 'coldmail.edu' }
