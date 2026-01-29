#B_nesting_loops
# Write a function `print2d(matrix)` that accepts a 2D list and prints all inner elements.

def print2d(matrix):
    for row in matrix:
        for item in row:
            print(item)

array1 = [
    ["a", "b", "c", "d"],
    ["e", "f"],
    ["g", "h", "i"]
]

print2d(array1)
# prints:
# a
# b
# c
# d
# e
# f
# g
# h
# i

def print2d(array2):
    for row in array2:
        for item in row:
            print(item)

array2 = [[9, 3, 4],
            [11],
            [42, 100]]
print2d(array2)
# prints:
# 9
# 3
# 4
# 11
# 42
# 100

