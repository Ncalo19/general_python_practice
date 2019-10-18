# generator function: executes the last called value. A return statement conversely
# restarts from the beginning each time it is called. Generators take up less space (memory)
# can convert any function into a genrator by utilizing yield instead of return
# return will end a function, yield (generator) will not (pauses a function)
# generators generate values on the fly. Uses () instead of []
# generators (yield) allow you to not have to restart your function every time it is called
# not used in try clauses because there is no guarantee the generator will ever be resumed

# create a generator function that multiplies numbers by 2
def genfunction1(x):
    yield x * 2 # generators use yield instead of return (only returns the generator object)
print(genfunction1(7))
print(genfunction1(20))

# yield the first three instances of a generator function
def genfunction2():
    yield 1
    yield 2
    yield 3
for num in genfunction2():
    print(num * num)


# run a number list through a generator function and return the answers as a loop (not sure this is actually a generator)
list1 = [3, 4, 5]
doubler = (x*2 for x in list1) # this would be a function if [] used
for x in doubler:
    print(x)

def genfunction3():
    a = 1
    while a <= 10:
        doubler = a * 2
        yield doubler
        a += 1
for x in genfunction3():
    print(x)

# A Python program to generate squares from 1
# to 100 using yield and therefore generator

# An infinite generator function that prints
# next square number. It starts with 1
def nextSquare():
    i = 1;

    # An Infinite loop to generate squares
    while True:
        yield i*i
        i += 1  # Next execution resumes
                # from this point

# A Python program to generate squares from 1
# to 100 using yield and therefore generator

# An infinite generator function that prints
# next square number. It starts with 1
def nextSquare():
    i = 1;

    # An Infinite loop to generate squares
    while True:
        yield i*i
        i += 1  # Next execution resumes
                # from this point

# Driver code to test above generator
# function
for num in nextSquare():
    if num > 1000000:
         break
    print(num)
