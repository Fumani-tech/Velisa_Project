# 1. int
x = 10
print(type(x))   # <class 'int'>

# 2. float
y = 3.14
print(type(y))   # <class 'float'>

# 3. complex
z = 2 + 3j
print(type(z))   # <class 'complex'>

# 4. bool
is_valid = True
print(type(is_valid))   # <class 'bool'>

# 5. str
name = "Python"
print(type(name))   # <class 'str'>


# 6. list
fruits = ["apple", "banana", "cherry"]
print(type(fruits))   # <class 'list'>

# 7. tuple
coordinates = (10, 20)
print(type(coordinates))   # <class 'tuple'>

# 8. set
unique_numbers = {1, 2, 3, 3}
print(unique_numbers)      # {1, 2, 3}
print(type(unique_numbers))   # <class 'set'>

# 9. frozenset
frozen = frozenset([1, 2, 3])
print(type(frozen))   # <class 'frozenset'>

# 10. dict
person = {"name": "Alice", "age": 25}
print(type(person))   # <class 'dict'>


# 11. bytes
b = b"hello"
print(type(b))   # <class 'bytes'>

# 12. bytearray
ba = bytearray([65, 66, 67])
print(type(ba))   # <class 'bytearray'>

# 13. memoryview
mv = memoryview(b"hello")
print(type(mv))   # <class 'memoryview'>

# 14. NoneType
nothing = None
print(type(nothing))   # <class 'NoneType'>
