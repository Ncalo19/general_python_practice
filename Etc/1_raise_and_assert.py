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
