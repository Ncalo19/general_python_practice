'''
def generatorfunction1():
    a = 1
    while a <= 10000:
        doubler = a + 1
        yield doubler
        a * 2
for x in generatorfunction1():
    print(x)


for x in range(1, 10000):
    print(x * 2)

def function1():
    x = 1
    while x <= 10000:
        x += 1
        return x

def function1():
    if x <= 10000:
        x *= 2
    else:
        x = 1

print(function1())

def function1(x):
    while x > 0:
        result = x * function1(x - 1) #(1! = 1, 2! = 2*1=2, 3! = 3*2=6,  4! = 4*6=24, 5! = 5*24=120)
        print(result)
    else:
        result = 1
    yield result
test = function1(x)
for x in test:
    print(x)

def generatorfunction1():
    a = 1
    while a <= 100000:
        doubler = a * 2
        yield doubler
        a += 1
for x in generatorfunction1():
    print(x)

print('testing 1 2 3')
'''

class Pet(object):
   def my_method(self):
      print("I am a Cat")
cat = Pet()
cat.my_method()
