# JSON (JavaScript Object Notation) is a syntacx used to store and exchange JavaScript (JSON) date
# parsing: splitting a sequence of characters or values into smaller parts

# import the json package (needed to work with json data)
import json # must import the json package
# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'
# parse x (convert JSON date to usable python data):
a = json.loads(x) # loads: parses json data (takes an object from JavaScript
# and converts it into a python object)
print(a) # the transformed json data is now a python dictionary

# print a dictionary item from the converted json data
print(a['age'])

# convert from python to json
a = json.dumps(x) # dumps: takes python object and produces a string
print(a)
# The followng object types can be converted into json strings:
# string, int, float, True, False, None, list, tuple, dict (note imaginary number and set not listed)
print(json.dumps("hello")) # string
print(json.dumps(42)) # int
print(json.dumps(31.76)) # float
print(json.dumps(True)) # True
print(json.dumps(False)) # False
print(json.dumps(None)) # None
print(json.dumps(['apple', 'bananas'])) # list
print(json.dumps(('apple', 'bananas'))) # tuple
print(json.dumps({'name' : 'John', 'age' : 30})) # dict

# convert a Python object containing all the convertible data types to json:
print(' ')
print('1. Convert a Python object containing all the convertible data types to json:')
import json
x = {
  'name' : 'John',
  'age' : 30,
  'weight' : 185.33,
  'married' : True,
  'divorced' : False,
  'pets' : None,
  'hair_color' : ['brown', 'black'],
  'children' : ('Ann', 'Billy'),
    'cars' : [
    {'model' : 'BMW 230', 'mpg' : 27},
    {'model' : 'Ford Edge', 'mpg' : 24}
    ]
}
a = json.dumps(x)
print(a)

# indent the above script
print(' ')
print('2. Add a line break and indent the above script')
print(json.dumps(x, indent = 1)) # adds the listed # of indents to each line
# set = 0 for line breaks with no indents

# change the default seperator
print(' ')
print('3. Change the default separator')
print(json.dumps(x, separators = (" (object) ", " is "))) # objects from other objects, keys from their values

# sort the converted script (sorts alphabetically)
print(' ')
print('4. Sort the converted script')
print(json.dumps(x, sort_keys = True))

# indent, change seperators, and sort the converted script
print(' ')
print('5. Indent, change separators, and sort the converted script')
print(json.dumps(x, indent = 4, separators = (" (object) ", " is "), sort_keys = True))



# COPY AND PASTE BELOW FOR JSON TRAINING
##########################################

# import the json package (needed to work with json data)

# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'
# parse x (convert JSON date to usable python data):
a = json.loads(x)
print(a)

# print a dictionary item from the converted json data

# convert from python to json


# The followng object types can be converted into json strings:
'''

'''

# convert a Python object containing all the convertible data types to json:
print(' ')
print('1. Convert a Python object containing all the convertible data types to json:')
import json
x = {
  'name' : 'John',
  'age' : 30,
  'weight' : 185.33,
  'married' : True,
  'divorced' : False,
  'pets' : None,
  'hair_color' : ['brown', 'black'],
  'children' : ('Ann', 'Billy'),
    'cars' : [
    {'model' : 'BMW 230', 'mpg' : 27},
    {'model' : 'Ford Edge', 'mpg' : 24}
    ]
}

# indent the above script
print(' ')
print('2. Add a line break and indent the above script')


# change the default seperator
print(' ')
print('3. Change the default separator') # objects from other objects, keys from their values


# sort the converted script (sorts alphabetically)
print(' ')
print('4. Sort the converted script')


# indent, change seperators, and sort the converted script
print(' ')
print('5. Indent, change separators, and sort the converted script')
