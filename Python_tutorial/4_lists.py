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

# check if item exists
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

# add an item to the end of a list
list1.append('cranberry')
# add item in a specific position
list1.insert(2,'rasberry')
print(list1)

# add item or list to the end of a list (two ways to do it)
list2 = ['cucumber', 'tomato']
list1.extend(list2)

# remove an item
list1.remove('asparagus')
# removes specified index or last item from list if not specified
list1.pop()
# deletes a specified index
del list1[2]
print(list1)

# reference a list (list being referenced must be after the = sign)
list2 = list1
print(list2)

# copy a list
list3 = list1.copy()
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
