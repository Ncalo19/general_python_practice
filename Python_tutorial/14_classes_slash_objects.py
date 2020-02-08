# class is an object blueprint
# create an object blueprint
class class1:
    name = 'Nick' # object: item inside a class
    age = 23
print(class1)

# print an object
print(class1.name)
print(class1.age)
# use a period when extracting info about a class or performing an action on a script or array

# assign values to object properties

class class1:
    def __init__(self, name, age): # self is a reference to the current instance of the class
        self.name = name # self is used to access variables that belong to the class
        self.age = age
p1 = class1('Nicolas', 23) # p1 is the object
p2 = class1('Jonathan', 21)

print(p1.name)
print(p2.age)
# __init__ is a class method
# method: similar to a function, but it is a member of an object or class
# methods are always called with an object (ie. p1.)
# functions are conversely called by their name
# the first parameter of a method is always (self,


# assign a function to an object (an object method)
class class1:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def function1(self):
        print('my name is ' + self.name) # cannot use integers
p1 = class1('Nicolas', 23)
p2 = class1('Jonathan', 21)

p1.function1()
p2.function1()

# change a number or string within an object
p1.name = 'Nick'
p1.age = 52
print(p1.name)
print(p1.age)


# delete a property from an object
del p1.age

# delete an object
del p1
