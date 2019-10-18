# comprehensions: using lists, sets, and dicts to create lists, sets, and dicts
# set comprehension: using lists, sets, and dicts, to create sets
# same as list comprehension, but replaces [ ] with { }

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # can also use a set (set and list will return a random number order)

# use a set comprehension to print values in a number list multiplied by 5 in a set format
print({x * 5 for x in list1})

# use a set comprehension to print the square of numbers values in a number list in a set format
# and add a limit (a filter)
print({x ** 2 for x in list1 if x * x < 40})

# multiply every part of a list by three and assign it to a new set
list1 = [3, 4, 5]
triple = {item*3 for item in list1}
print(triple)

# create a function that doubles numbers in a range
def double(x):
    return x*2
print({double(x) for x in range(10)})
