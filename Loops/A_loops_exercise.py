#Snippet 1

print("hello")

for i in range(5):
    print("code")

print("goodbye")

#Snippet 2

print("hi")

for i in range(3, 8):
    print("program")
    print(i)

print("bye")

#Snippet 3
def foo():                         # function definition
    for num in range(10, 0, -2):    # loop from 10 to 1, step -2
        print(num)                  # print num in each iteration

print("begin")                      # calling the function
foo()                               # calling the function again
print("end")                    # calling the function a third time
foo()                               #

#Snippet 4
word = "street"                 # string variable

for i in range(len(word)):      # loop through indices of the string
    print(i)
    print(word[i])



