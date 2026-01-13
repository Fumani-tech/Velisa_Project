#snippet 1
def greet():
    print("hey")
    print("programmers")

def whistle():
    print("doot")

print("first")
print("second")
greet()
print("third")
print("fourth")
whistle()

#snippet 2
def how_many():
    return 42

print(how_many)
print(how_many())

the_answer = how_many()
print(the_answer)

def how_much():
    5   # does nothing

print(how_much())

#snippet 3
def average(num1, num2):
    print("calculating...")
    return (num1 + num2) / 2

print(average(5, 10))
print(average(20, 26))
print(average(50, 100) + 2)

a = 21 + 3
b = 20
n = average(a, b)
print(average(n, 18))

#snippet 4
def exclaim(s):
    capitalized = s.upper()
    return capitalized + "!!"

result = exclaim("potato")
print(result)
print(len(result))
print(result[0])
print(result[-1])





