# scope: a variable is only available within the region it was created  (its given scope)
# global variable: variable created in the body of the code
# global scope: a global variable has global scope because it is available within any scope (global or local)

# first create a variable in the global scope and then a variable in the local scope (in a function)
# print the global scope variable after printing the local scope variable
x = 300
def myfunc():
  x = 200
  print(x)
myfunc()
print(x)

# change a global variable while working inside a function
x = 200
def funct1():
    global x
    x = 300
funct1() # function must be performed in order to change global scope
print(x)

# set a global variable while working inside a function
x = 200
def funct1():
    global x
    x = 300
funct1() # function must be performed in order to set global scope
print(x)
