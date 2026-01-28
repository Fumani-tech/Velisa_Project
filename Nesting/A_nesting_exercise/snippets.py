# Predict what this will print:
# snippet 1
for i in range(1, 5):
    for j in range(1, 4):
        print(i, j)

# snippet 2
for n in range(2):
    print("n=" + str(n))
    for m in range(5):
        print("   m=" + str(m))
    print("n=" + str(n))

# snippet 3
friends = ["philip", "abby", "phelipe", "simcha"]

for i in range(len(friends)):
    for j in range(len(friends)):
        print(friends[i], friends[j])

# snippet 4
locations = ["flatbush", "williamsburg", "bushwick", "greenpoint"]

for i in range(len(locations)):
    for j in range(i + 1, len(locations)):
        print(locations[i], locations[j])

# snippet 5
colors = ["red", "purple", "orange"]

for color_str in colors:
    print(color_str)
    for char in color_str:
        print(char)

