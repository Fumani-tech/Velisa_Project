#snippet 1
if True:
    print("foo")

if False:
    print("bar")

#snippet 2
if False or False:
    print("boop")

if True or False:
    print("beep")

#snippet 3
num = 40

if num > 0:
    print("zip")

if num % 2 == 0:
    print("zoop")

#snippet 4
word = "jeep"

if word[0] == "d":
    print("yer")
else:
    print("nah")

#snippet 5
sentence = "roger that"

if sentence[-1] == "t":
    print("ends in t")
else:
    print("does not end in t")

if len(sentence) <= 4:
    print("short")
else:
    print("long")

