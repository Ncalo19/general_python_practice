# comprehensions: using lists, sets, and dicts to create lists, sets, and dicts
# dict comprehension: using lists, sets, and dicts to create dicts

# print a dict comprehension using a number list as the keys : and the square of the number list as the values
list1 = [1, 2, 3, 4, 5] # can also use a set (numbers will stay ordered either way)
dictcomp1 = {x:x ** 2 for x in list1}
print(dictcomp1)

# print a dict comprehension using a number list as the keys : and the square of the number list as the values
# and add a limit (filter)
list1 = [1, 2, 3, 4, 5] # can also use a set
dictcomp2 = {x:x ** 2 for x in list1 if x**2 < 10}
print(dictcomp2)

# create a dict using two lists
state = ['NY', 'CA', 'TX']
capital = ['Albany', 'Sacramento', 'Austin']
dictcomp3 = {key:value for (key, value) in zip(state, capital)}
print(dictcomp3)
