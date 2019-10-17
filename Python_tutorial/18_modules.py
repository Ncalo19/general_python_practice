# module: python code library (the files on the side)
# there are around 50 modules built into python
# modules built into python: https://docs.python.org/3/py-modindex.html

# bring another module into this module
import module_used # second to last module on left hand side of screen

# run a function from another module
module_used.function1(5)

# print a collection/array from another module
x = module_used.list1 # does not use parenthesis
print(x)

# print a dictionary item from another module
x = module_used.dict1['make']
print(x)

# change the name used to reference another module for this module
import module_used as m

# list all the function names in a module
print(dir(module_used)) # dir : gives you the directory of a module

# import a specific collection/array from another module
from module_used import dict1
print(dict1)
