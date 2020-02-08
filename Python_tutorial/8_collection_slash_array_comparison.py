# Constructing collections/arrays:
list1 = list(('dog', 'cat', 'fish'))
tuple1 = tuple(('yellow', 'orange', 'red'))
set1 = set(('pokemon', 'yughio', 'digimon'))
dict1 = dict(make = 'audi', model = 'A8', year = 2019)

list1 = ['dog', 'cat', 'fish']
tuple1 = ('yellow', 'orange', 'red')
set1 = {'pokemon', 'yughio', 'digimon'}
dict1 = {
'make' : 'audi',
'model' : 'A8',
'year' : 2019
}

# Add values to the collections/arrays
# list (append, insert, extend)
list1.append('bird')
list1.insert(2, 'hamster')
list1.extend(['gerbal', 'hamster']) # can also add another list
# tuple: unchangable
# set
set1.add('green')
set1.update(['brown', 'maroon']) # can also add another set
# dictionary
dict1['color'] = 'blue'
dict1.update({'owners' : 2, 'mileage' : 20000})

# Changing values in collections/arrays
#list
list1[6] = 'frog'
# tuple: unchangable
# set
    # set1.update(set2) merge two sets (duplicates only listed as one item)
    # set1.difference_update(set2): removes values from set1 that are in both set1 and set2
    # set1.intersection_update(set2): change the values of set1 to the values that are in both set1 and set2
    # set1.symmetric_difference_update(set2): change the values of set1 to the unique values between set1 and set2
# dict
dict1['year'] = 2020


# deleting items from collections/arrays
# list
list1.remove('dog')
del list1[0] # use to delete multiple list items (ex. [1:])
list1.pop() # the last item is popped
list1.pop(0) # can add an index for a popped list item
# tuple: unchangable
# set
set1.remove('pokemon')
set1.discard('yughio')
set1.pop() # the last item is popped (random because sets have no order)
# dictionary
dict1.pop('make') # cannot be blank (use to delete multiple value pairs)
del dict1['model']
dict1.popitem() # removes last added value pair

# create a list both ways
# create a dict both ways
# add multiple values to a list, set, and dict
# del items from a list
# del items from a dict
# change values in collections
