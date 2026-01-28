#Extra 1 — Odd or Even
num = 17

if num % 2 == 0:
    print("even")
else:
    print("odd")

#Extra 2 — Password Strength
password = "Code123"

if len(password) < 4:
    print("too short")
elif password.isalpha():
    print("weak")
elif password.isalnum():
    print("medium")
else:
    print("strong")

#Extra 3 — Temperature Detector
temp = 32

if temp < 0:
    print("freezing")
elif temp < 20:
    print("cold")
elif temp < 30:
    print("warm")
else:
    print("hot")

#Extra 4 — Vowel or Consonant
ch = "e"

if ch.lower() in "aeiou":
    print("vowel")
else:
    print("consonant")

#Extra 5 — Age Group Classifier
age = 14

if age < 13:
    print("child")
elif age < 20:
    print("teen")
elif age < 60:
    print("adult")
else:
    print("senior")

