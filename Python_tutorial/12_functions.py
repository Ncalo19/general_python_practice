# function is a block of code that only runs when called (def)
# insert a script variable into a sentence (function)
def function1(fname):
    print('knock knock, ' + 'hello it is ' + fname)
function1('Joe')
function1('Nick')

print('')

# function with a default parameter value
def function1(country = 'Argentina'):
    print('I love ' + country)
function1('Italy')
function1('Ireland')
function1()

print('')

# using a list as a function parameter
list1 = ['Sweeden', 'Norway', 'Iceland', 'Denmark', 'Finland']
list2 = ['Croatia', 'Germany']
def function1(country):
    for x in country:
        print('I love ' + x)
function1(list1)
function1(list2)

print('')

# let a function operate on a number using print
def function1(x):
    print(x * 5)
function1(5)

# let a function operate on a number using return
# (print() is a function that causes a side effect (it writes a string in the console),
# but execution resumes with the next statement. return causes the function
# to stop executing and hand a value back to whatever called it.)
# print does not return anything, and return does not print anything
# return gives you a value, print prints a response
def function1(x):
    return x * 5
print(function1(7))
print(function1(20))

print('')

# run a number list through a function and return the answers as a loop (two ways)
list1 = [3, 4, 5]

def function1(doubler):
    for x in doubler:
        print(x * 2)
function1(list1)

doubler = [x*2 for x in list1] # can also write numbers in directly in a list format
for x in doubler:
    print(x)

# run a number list through a function and return the answers as a list
def function1(doubler):
    total = []
    for x in doubler:
        total.append(x * 2)
    return total
print(function1(list1))

# recursion: a defined function calling itself
# create a cumilative recursive function (1+0=1, 2+1=3, 3+3=6)
def function1(x):
  if x > 0:
    result = x + function1(x-1) # 1+0=1, 2+1=3, 3+3=6, 4+6=10, 5+10=15, 6+15=21
    print(result)
  else:
    result = 0
  return result
print("\nRecursion Example Results") #\n gives a space before a string
function1(6)

print('')

# recursive factorial (!) algorithm
def function1(x):
    if x > 0:
        result = x * function1(x - 1) #(1! = 1, 2! = 2*1=2, 3! = 3*2=6,  4! = 4*6=24, 5! = 5*24=120)
        print(result)
    else:
        result = 1
    return result
function1(5)

print(' ')

# iterative factorial (!) algorithm

def function1(x):
    total = 1
    for x in range(1, x+1): # non-inlcusive
        total *= x # total = total * x
    return total
print(function1(5))
