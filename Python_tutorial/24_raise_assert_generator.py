# raise an error and stop the program if x is lower than 0:
x = -3
if x < 0:
    raise Exception('No numbers below zero')

# if a condition is false, raise an AssertionError
x = 'hello'
assert x is 'hello'
assert x is 'goodbye'

# if a condition is false, raise an AssertionError and a message
x = 'hello'
assert x is 'hello'
assert x is 'goodbye', 'x is not goodbye'

# generator function: executes the last called value. A return statement conversely
# restarts from the beginning each time it is called. Generators take up less space (memory)
# can convert any function into a genrator by utilizing yield instead of return
# return will end a function, yield (generator) will not

# create a generator function that multiplies numbers by 2
def generatorfunction1(x):
    yield x * 2
print(generatorfunction1(7))
print(generatorfunction1(20))


# run a number list through a generator function and return the answers as a loop (not sure this is actually a generator)
list1 = [3, 4, 5]
doubler = (x*2 for x in list1) # this would be a function if [] used
for x in doubler:
    print(x)

def generatorfunction1():
    a = 1
    while a <= 10:
        doubler = a * 2
        yield doubler
        a += 1
for x in generatorfunction1():
    print(x)
