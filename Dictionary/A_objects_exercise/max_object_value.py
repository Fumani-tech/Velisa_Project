# Write a function `max_object_value` that accepts a dictionary where:

# - keys are strings
# - values are numbers

# Return a list containing:
# - the key with the highest value
# - the highest value itself

def max_object_value(dic1):
    result = []
    counter = 0
    max_key = ""
    for key, value in dic1.items():
        if value > counter:
            counter = value
            max_key = key
    result.append(max_key)
    result.append(counter)

    return result

print(max_object_value({"a":5,"b":2,"c":6,"d":7,"e":4 }))
# ['d', 7]

print(max_object_value({"lychee":11,"rambutan":13,"papaya":9 }))
# ['rambutan', 13]
