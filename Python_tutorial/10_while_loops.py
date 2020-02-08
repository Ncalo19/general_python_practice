# while loops execute a loop while a condition is true
fish = 0
while fish < 6:
    fish += 1
    print(fish)
    if fish == 6:
        print('You have enough fish')

# end a while-loop when a condition is met
x = 0
while x < 6:
    x += 1
    if (x == 3):
        print('Loop 2 ended')
        break # goes before print
    print(x)

# skip a specified iteration in a while loop
x = 0
while x < 6:
    x += 1
    if (x == 3):
        continue # goes before print
    print(f'{x} sheep')
    if x == 6:
        print('Asleep')

'''
# while loops execute a loop while a condition is true
# end a while-loop when a condition is met
# skip a specified iteration in a while loop
'''
