# for loops: loops through a sequence (collection/array or string)

# looping through a string
for x in 'usa':
    print(x)

# looping through a collection/array
set1 = {'dog', 'cat', 'fish'}
for x in set1:
    print(x)

# looping through a range
for x in range(3):
    print(x)
print('range 1 done')

for x in range(3, 5):
    print(x)
print('range 2 done')

# loop through a range of numbers moving by multiples of a specified #
for x in range(3, 30, 3):
    print(x)
print('range 3 done')

# continue & break
for x in range(3, 30, 3):
    if x == 6:
        continue
    if x > 25:
        break
    print(x)
print('hello')
# nested loops (two arrays/collections in a merged loop)
size = ('small', 'medium', 'large')
speed = ('slow', 'average', 'fast')
for x in size:
    for y in speed:
        print(x, y, 'turtle')

# extract all numbers from a string
string1 = 'hello world 123456'
for x in string1:
    if x.isdigit():
        print(x)

# create a dictionary using a for loop
list1 = [1, 2, 3, 4, 5]
dict1 = {}
for x in list1:
    if x % 2 == 1: # if x modulus 2 (remainder of x/2) == 1
        dict1[x] = x ** 2
print(dict1)
