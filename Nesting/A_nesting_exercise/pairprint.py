# Write a function `pair_print(arr)` that accepts a list and prints all unique pairs
# of elements in the list. It doesn't need to return anything.

def pair_print(list):
    for i in range(len(list)):
        for j in range(i+1,len(list)):
            print(list[i],list[j])

# Example:
pair_print(["artichoke", "broccoli", "carrot", "daikon"])
# prints
# artichoke - broccoli
# artichoke - carrot
# artichoke - daikon
# broccoli - carrot
# broccoli - daikon
# carrot - daikon
