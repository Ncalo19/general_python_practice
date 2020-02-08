# List: ordered and changeble. uses square brackets [ ]
list1 = ['orange', 'tomato', 'pepper']
print(list1)
# other way to write a list (list constructor)
otherlist1 = list(('sour', 'spicy', 'umami'))
print(otherlist1)

# print the third item
print(list1[2])

# change an item
list1[1] = 'asparagus'
print(list1[1])

# loop through a list
for x in list1:
    print(x)

# check if item exists in a list
print('pepper' in list1)

# if an item exists in a list, print a response
if 'pepper' in list1:
    print('it is a fruit')

# len of a list
print(len(list1))

# position of a value
print(list1.index('pepper'))

# alphabetize a list
list1.sort()
print(list1)

# reverse the order of a list
list1.reverse()
print(list1)

# add an item to the end of a list (two ways)
list1.append('cranberry')

list1.extend('plum')

# add item in a specific position
list1.insert(2,'rasberry')
print(list1)

# add a list to the end of a list
list2 = ['cucumber', 'tomato']
list1.extend(list2) # must use a list (cannot use multiple scripts)

# remove an item by it's script
list1.remove('asparagus')
# remove a specified index (two ways)
del list1[2]
list1.pop(0)
print(list1)
# remove last item from list without specifying the index
list1.pop()

# remove multiple indexes
list1 = ['orange', 'tomato', 'pepper']
del list1[1:]
print(list1)


# reference a list (list being referenced must be after the = sign)
list2 = list1 # same memory location. list2 is pointing to list2, it is the same object (It has the same memory location) (list 2 is list1)
print(list2)

# copy a list
list3 = list1.copy() # different memory location. list3 is just a copy, not the same object (it has a different memory location) (list 3 is not list1)
print(list3)

list4 = list(list1)
print(list4)

# empty the list
list1.clear()
print(list1)

print('should be an error below:')

# delete the list
del list1
print(list1)

'''
# position of a value
# alphabetize a list
# reverse the order of a list
# remove a specified index (two ways)
# remove last item from list without specifying the index
# copy a list
'''
