# Write a function `pick_primes` that accepts a list of numbers.

# The function should return a **new list** containing **only the prime numbers** from the original list.

# You may want to **reuse the `is_prime` function**.

def pick_primes(list1):
    new_list = []
    for el in range(len(list1)):
        if is_prime(list1[el]):
            new_list.append(list1[el])
    return new_list

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


print(pick_primes([12,3,7,18,11]))
# [3, 7, 11]

print(pick_primes([17,23,9,42]))
# [17, 23]

print(pick_primes([4,2048,100,55]))
# []
