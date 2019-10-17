# Inheritance: used to assign methods & properties of parent class to child class

# assign a class function to an object (not inheritence yet)
class class1:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def function1(self):
        print(self.fname, self.lname)

p1 = class1('Nick', 'Calo')
p1.function1()

# create a child class that will inherit all the properties of the parent class (three ways)
# (pass, class, super)
class class2(class1):
    pass

p2 = class2('Jon', 'Calo')
p2.function1()

class class3(class1):
  def __init__(self, fname, lname):
    class1.__init__(self, fname, lname)

p3 = class3('Andrew', 'Calo')
p3.function1()

class class3(class1):
    def __init__(self, fname, lname):
        super().__init__(fname, lname) #do not need to include self when using super

p4 = class3('Sarah', 'Calo')

# add a new static property (ex. graduation year) to the child class, and create a new function with it
class class4(class1):
    def __init__(self, fname, lname):
        class1.__init__(self, fname, lname)
        self.graduationyear = 2019

    def function2(self):
        print('Welcome', 'to the class of', self.graduationyear, self.fname, self.lname)
p4 = class4('Sarah', 'Calo')
p4.function2()

# add an assignable property (a variable) to the child class and create a new function
class class5(class1):
    def __init__(self, fname, lname, graduationyear):
        class1.__init__(self, fname, lname)
        self.graduationyear = graduationyear
    def function3(self):
        print('My name is', self.fname, self.lname, 'and I graduated in', self.graduationyear)

p5 = class5('Mishelle', 'Calo', 1988)
p5.function3()
