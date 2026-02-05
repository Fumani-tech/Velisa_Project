# Write a function `object_add` that accepts **two dictionaries** containing numeric values.

# Rules:

# - If a key appears in **both dictionaries**, sum their values
# - If a key appears in **only one dictionary**, keep its value as-is
# - Return a **new dictionary**

def object_add(dic1, dic2):
    new_dic= {}
    for el in dic1:
        if el in dic2:
            new_dic[el] = dic2[el] + dic1[el]
    return new_dic

obj1 = {"x":3,"y":10 }
obj2 = {"y":2,"x":1 }

print(object_add(obj1, obj2))
# { "x": 4, "y": 12 }

obj3 = {"a":3,"b":2,"c": -1 }
obj4 = {"b":5,"c":1,"e":4 }

print(object_add(obj3, obj4))
# { "b": 7, "c": 0}
