# set: unordered and unindexed (assigned using braces {}) (no duplicate items)
set1 = {'charmander', 'squirtle', 'bulbasaur'}
print(set1)

# loop set
for x in set1:
    print(x)

# check for a value
print('pikachu' in set1)

# if a value is in a set, return a script
if 'squirtle' in set1:
    print('squirt')

# add a value to set
set1.add('pidgey')
print(set1)

# add multiple valuses to a set
set1.update(['mew', 'mewtwo'])
print(set1)

# add a set to a set
set2 = {'artichuno', 'zapados'}
set1.update(set2)
print(set1)

# len
print(len(set1))

# remove a set item (two somewhat different ways)
set1.remove('mew') # will give an error if the item is not in the set
set1.discard('mewtwo') # no error if item not in set
# remove the last item (random since sets are unordered)
set1.pop()
print(set1)

# set constructor (other way to build a set)
set2 = set(('chikorita', 'cyndaquil', 'totodile', 'squirtle'))
print(set2)

# find similarities btwn sets
a = set1.intersection(set2)
print(a) #(squirtle is the answer, unless it was previously deleted)
# find similarities between >= 2 sets
b = set.intersection(set1, set2)
print(b) #(squirtle is the answer, unless it was previously deleted)

# return the items that exist in 1 set and not the other
z = set1.difference(set2)
print(z)

# return the items that exist in 1 set and not other sets
set3 = {'charmander', 'chikorita'}
z = set.difference(set1, set2, set3)
print(z)

# removes values from set1 that are also in set2
set1.difference_update(set2)
print(set1) #(squirtle will now never appear, since it's in both sets)



set3 = {'artichuno', 'zapados', 'moltres', 'hoho'}
set4 = set(('zapados', 'hoho', 'mew', 'mewtwo'))
print(set3, set4)
for x in set3, set4:
    print(x)

# print values unique to each set
n = set3.symmetric_difference(set4)
print(n)

# determine if no items are present in both sets (both sets are unique from eachother)
n = set3.isdisjoint(set4)
print(n)

# determine if one set is a subset or superset of another
print(set3)
print(set4)
n = set3.issubset(set4)
print(n) # true because
n = set3.issuperset(set4)
print(n)

set3 = {'artichuno', 'zapados', 'moltres', 'hoho'}
set4 = set(('zapados', 'hoho', 'mew', 'mewtwo'))

# Change the values in a set to the unique values between two sets
set3.symmetric_difference_update(set4)
print(set3)

# create a new set made up of two already defined sets (sets do not have duplicate values)
set5 = set3.union(set4)
print(set5)

'''
# add multiple values to a set
# find similarities between >= 2 sets
# print values unique to both sets
# change the values in a set to the unique values between two sets
# create a new set made up of two already defined sets (sets do not have duplicate values)
'''
