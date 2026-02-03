#snippet 1

movie = {
"title":"Fight Club",
"year":1999,
"genre": ["drama","thriller"],
"starring": ["Brad Pitt","Edward Norton"],
}

print(movie["year"])
print(movie["title"])
print(movie["genre"])
print(movie["genre"][0])
print(movie["genre"][1])

print(movie.get("duration"))
print(movie["starring"][1])
print(len(movie["starring"]))

#snippet 2
restaurant = {
"name":"Bob's Burgers",
"location":"123 Ocean Avenue",
"owners": ["Bob Belcher","Linda Belcher"],
"established":2011,
"menu": ["burgers","fries","shakes"],
}

print("owners" in restaurant)
print("employees" in restaurant)

some_key ="menu"
print (some_key in restaurant)

print(restaurant["menu"])
print(restaurant.get("menu"))
print(restaurant[some_key])
print(restaurant.get("some_key")) #will return None because some_key is not a key in the dictionary

print("fries"in restaurant["menu"])

#snippet 3
dog = {
"name":"Manny",
"age":5,
"breed":"pug",
"color":"fawn",
"favoriteFoods": ["bacon"],
}

print(dog["age"])
print(dog["breed"])
print(dog["favoriteFoods"])

dog["age"] +=1
dog["breed"] = dog["breed"].upper()
dog["favoriteFoods"].append("sausage")

print(dog["age"])
print(dog["breed"])
print(dog["favoriteFoods"])

for key in dog:
    print(key,"is", dog[key])

#snippet 4
recipe = {
"name":"Old Fashioned Pancakes",
"difficulty":"easy",
"tasty":True,
"ingredients": ["eggs","milk","butter","flour","sugar"],
}

print(recipe["name"])
print(recipe["name"])
print(len(recipe["ingredients"]))
print(recipe.get("calories"))

some_variable ="difficulty"
print(recipe[some_variable])
print(recipe.get("some_variable"))

for ingredient in recipe["ingredients"]:
    print(ingredient)

