# dictionary; unordered, changeable, and indexed (by keys) (braces {} and colons :)

dict1 = {
'brand' : 'audi', # both keys and values must be scripts
'model' : 'A7',
'year' : 2020
}
print(dict1)

# accessing values (two ways)
print(dict1['brand'])
print(dict1.get('year'))

# changing a value in the dictionary
dict1['year'] = 2019
print(dict1)

# print dictionary key loop (two ways)
for x in dict1:
    print(x)
for x in dict1.keys():
    print(x)

# loop dictionary values
for x in dict1.values():
    print(x)

# loop through dictionary 'keys - values'
for x, y in dict1.items():
    print(x, '-', y)

# print a script if a key is in the dictionary (two ways)
if 'year' in dict1:
    print('yes it is')
if 'year' in dict1.keys():
    print('yes it is')

# adding an item to the dictionary
dict1['color'] = 'brown'
print(dict1)

# removing items from dictionary (two ways)
dict1.pop('color')
print(dict1)

del dict1['year']
print(dict1)

# copy a dictionary
dictcopy = dict1.copy()
print(dictcopy)

# make a new dictionary (dictionary constructor)
dict2 = dict(lager = 'sam_adams', ale = 'brooklyn', stout = 'guiness')
# use = and not : , use single parenthesis, and no string literals for keys
print(dict2)

# create a multi key dictionary all with the same value
x = ('key1', 'key2', 'key3')
y = 0
dict3 = dict.fromkeys(x, y)
print(dict3)




dict1 = { # added another dictionary in order to scroll less
'brand' : 'audi',
'model' : 'A7',
'year' : 2020
}

# return key value pairs (items) of dict as tuples (in parenthesis) in an array
# aka print the dictionary items
print(dict1.items())

# print the dictionary keys
print(dict1.keys())

print('testtttttttttttt')
# returns the value of the specified key, but lists a value in case one not in dict
print(dict1.setdefault('brand', 'ferrari'))

# add multiple key value pairs to the dict
dict1.update({'color': 'red', 'transmission': 'stick'})
print(dict1)

# print dict values
print(dict1.values())

# remove last inserted key value pair
dict1.popitem()
print(dict1)
# print the item being popped off
print(dict1.popitem())

# remove all items from a dict
dict1.clear()
print(dict1)

# delete a dict
del dict1
