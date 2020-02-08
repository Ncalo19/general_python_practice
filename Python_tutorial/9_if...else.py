# if...else: returns specific values or strings dependent on hitting a desired
# range, value, or string

w = 16
x = 7
y = 18
z = 9

# if a condition is met, print a specific string (shorthand if statment)
if x > 0: print('x is a positive number')

# if a condition is met, return a specific string. If not, follow the next if statement.
# if statment with multiple else statments on one line
print('x is greater than y') if x > y else print('y is greater than x') if y > x else print('=')

# and or statments
if z > y and z == y/2:
    print('conditions are met')

if x > z or y > z:
    print('z is not the largest')

# if...else statement (if -> elif(elseif) -> else)
# if neither the if statement nor the elif statement hits, return the string after
# the else statement
tier_1 = 100000 # marry
tier_2 = 50000 # date
tier_3 = 25000 # fuck buddys
tier_4 = 10000 # just friends
tier_5 = 0 # run away

person1 = 5

if person1 >= tier_1:
    print('marry them')
elif person1 >= tier_2:
    print('date them')
elif person1 >= tier_3:
    print('fuck buddys')
elif person1 >= tier_4:
    print('just friends')
else:
    print('run away')

# if...else with multiple variable values using dictionaries
player1 = {
'speed' : 10,
'skill' : 8,
'size' : 10
}
player_profile = sum(player1.values())
print(player_profile)

tier1 = 26
tier2 = 24
tier3 = 22
tier4 = 19
tier5 = 15

if player_profile >= tier1:
    print('we cannot wait to see you next week')
elif player_profile >= tier2:
    print('you made the team')
elif player_profile >= tier3:
    print('practice some more and try again next year')
elif player_profile >= tier4:
    print('practice hard and you might make the team next year')
else:
    print('you did not make the team')

# if...else with multiple variable values using a class
class class1:
    def __init__(self, name, age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa
    def function1(self):
        if self.age < 7 and self.gpa < 2.8:
            print('Your child will be held back')
        elif self.age > 7 and self.gpa < 2.5:
            print('Your child will be held back')
        else:
            print('Your child will be advancing')

p1 = class1('Nick', 6, 3.5)
p2 = class1('Jonathan', 7, 2.6)
p3 = class1('Andrew', 7, 3.2)
p4 = class1('Sarah', 6, 2.9)

p4.function1()

# a different if...else with multiple variable values (not sum)
player_profile = {
'speed' : 10,
'skill' : 6,
'size' : 10
}

if player_profile['speed'] > 7 and player_profile['skill'] > 7 and player_profile['size'] > 7:
    print('You made the team')
elif player_profile['speed'] > 9 and player_profile['skill'] > 5 and player_profile['size'] > 8:
    print('You made the team because of your size and speed')
else:
    print('Better luck next year')

'''
# if statment with multiple else statments on one line
# if...else with multiple variable values using dictionaries
# if...else with multiple variable values using a class
'''
