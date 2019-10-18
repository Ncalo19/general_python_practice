# lambda: a small anonymous function

# single variable/argument function
x = lambda a : a + 5
print(x(5))

# multi variable/argument function
x = lambda a, b, c : a * b + c
print(x(1, 3, 4))

# make multiple functions with multiple varaibles in the same program (lambda in a function)
def function1(x):
    return lambda a, b : (a + b) * x
sumdoubler = function1(2)
sumtripler = function1(3)
print(sumdoubler(1,2))
print(sumtripler(1,2))

# make a single line lambda function
print((lambda x, y: x + y)(5, 3))
