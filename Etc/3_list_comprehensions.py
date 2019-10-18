# comprehensions: using lists, sets, and dicts to create lists, sets, and dicts
# list comprehension: using lists, sets, and dicts to create sets
# lists are comprehended (created) by an expression (variable) followed by a for clause
# syntax: [ expression for item in list if conditional ]
# vs for loop syntax:
#   for item in list:
#        if conditional:
#            expression

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # can also use a set (set will return a random number order)

# use a list comprehension to print values in a number list multiplied by 5 in a list format
print([x * 5 for x in list1])

# use a list comprehension to print the square of numbers values in a number list in a list format
# and add a limit (a filter)
print([x ** 2 for x in list1 if x * x < 40])

# multiply every part of a list by three and assign it to a new list.
list1 = [3, 4, 5]
triple = [item*3 for item in list1]
print(triple)

# print the first letter of each word
list1 = ['this', 'is', 'a', 'list', 'of', 'words']
first_letters = [word[0] for word in list1]
print(first_letters)

# extract all numbers from a string
string1 = "Hello 123456 world"
numbers = [x for x in string1 if x.isdigit()]
print(numbers)

# extract all letters from a string
string1 = " Hellow 123456 world"
letters = [x for x in string1 if x.isalpha()]
print(letters)

# create a function that doubles numbers in a range
def double(x):
    return x*2
print([double(x) for x in range(10)])
