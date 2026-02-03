# Write a function `key_pair` that accepts:

# - two dictionaries
# - a key string

# Return a list containing the values for the given key from both dictionaries.

def key_pair(dic1, dic2, key):
    return [dic1[key], dic2[key]]

cat1 = {"name":"jinkee","breed":"calico" }
cat2 = {"name":"garfield","breed":"red tabby" }

print(key_pair(cat1, cat2,"breed"))
# ['calico', 'red tabby']

print(key_pair(cat1, cat2,"name"))
# ['jinkee', 'garfield']