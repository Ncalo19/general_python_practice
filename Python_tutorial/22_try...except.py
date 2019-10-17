# print an undefined variable and return a custom error message
try:
    print(x)
except: # exception: an error occured
    print('x not defined')

# print a custom response if no exceptions occur
try:
    print('hello')
except:
    print('printing error')
else:
    print('no issues')

# print a custom response regardless of the existance of an exception
try:
    print(x)
except:
    print('printing error')
else:
    print('no issues')
finally:
    print('this prints regardless of the existance of an exception')

# (finally can be used to close objects after the object is utilized)
