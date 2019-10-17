# while loops execute a loop while a condition is true
girlfriends = 0
while girlfriends < 6:
    girlfriends += 1
    print(girlfriends)
print('loop 1 ended')

# end a while-loop when a condition is met
x = 0
while x < 6:
    x += 1
    if (x == 3):
        break
    print(x)
print('loop 2 ended')

# skip a specified iteration in a while loop
x = 0
while x < 6:
    x += 1
    if (x == 3):
        continue
    print(x)
print('loop 3 ended')
