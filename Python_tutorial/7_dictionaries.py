# dictionary; unordered, changeable, and indexed (by keys) (braces {} and colons :)

dict1 = {
'brand' : 'audi', # both keys and values must be scripts
'model' : 'A7',
'year' : 2020
}


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

# loop through dictionary 'keys - values' (two ways)
for x, y in dict1.items():
    print(x, '-', y)

for x, y in dict1.items():
    print(f'{x} - {y}')

# print a script if a key is in the dictionary (two ways)
if 'year' in dict1:
    print('yes it is')
if 'year' in dict1.keys():
    print('yes it is')

# adding an item to the dictionary (two ways)
dict1['color'] = 'brown'
print(dict1)
dict1.update({'transmission': 'stick'})
print(dict1)

# add multiple key value pairs to the dict
dict1.update({'color': 'red', 'transmission': 'stick'})
print(dict1)

# removing specific items from dictionary (two ways)
dict1.pop('color')
print(dict1)

del dict1['year']
print(dict1)

# remove last inserted key value pair
dict1.popitem()
print(dict1)
# print the item being popped off
print(dict1.popitem())

# make a copy of a dict
dict5 = dict1.copy()
print(dict5)

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

# print dict values
print(dict1.values())

# print the value of a specified key, but list a value to print in case there is no value for the key
print(dict1.setdefault('brand', 'ferrari'))

# remove all items from a dict
dict1.clear()
print(dict1)

# delete a dict
del dict1

'''
# removing items from dictionary (two ways)
# make a copy of a dict
# create a multi key dictionary all with the same value
# print the value of a specified key, but list a value to print in case there is no value for the key
# loop through dictionary 'keys - values' (two ways)
'''
