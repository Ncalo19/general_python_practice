# tuple: ordered and unchangable collection (uses ())

tuple1 = ('sedan', 'suv', 'truck')
print(tuple1)

# create a tuple without parenthesis
tuple2 = 'Nick', 'Jon', 'Andrew'
print(tuple2)
print(type(tuple2))

# accesss tuple items
print(tuple1[2])

# loop through the tuple
for x in tuple1:
    print(x)

# if an item is in the tuple, print a string
if 'sedan' in tuple1:
    print('hell yeah we got sedans')

# length of tuple
print(len(tuple1))

# tuple constructor (other way to write tuple code)
tuple2 = tuple(('water', 'mud', 'mud', 'oil'))
print(tuple2)

# return the # of times a specified value occurs in a tuple
x = tuple2.count('mud')
print(x)

# find the position of a specific value in a tuple
y = tuple2.index('water')
print(y)

# define a one integer tuple
tuple2 = (7,)
print(tuple2)
print(type(tuple2))

# del a tuple
del tuple1
print(tuple1) # gives error
