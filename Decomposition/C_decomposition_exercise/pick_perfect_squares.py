# Write a function `pick_perfect_squares` that accepts a list of numbers.
# The function should return a list containing only the perfect squares.
#
# A perfect square is a number that can be written as n * n.
def pick_perfect_squares(nums):
    perfect_squares = []
    for num in nums:
        if int(num ** 0.5) ** 2 == num:
            perfect_squares.append(num)
    return perfect_squares

print(pick_perfect_squares([6,4,81,21,36]))
# [4, 81, 36]

print(pick_perfect_squares([100,24,144]))
# [100, 144]

print(pick_perfect_squares([30,25]))
# [25]
