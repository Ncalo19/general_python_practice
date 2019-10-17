# format: used to add numbers to strings

# insert a number into a string
age = 23
string1 = 'I am {}'
print(string1.format(age))

# insert a number into a string and select the number of decimals
age = 23.32
string1 = 'I am {:.1f}'
print(string1.format(age))

# insert more than one number into a script
age = 23
gpa = 3.55
string1 = 'I am {}, and my gpa is {}'
print(string1.format(age, gpa))

# use numbers to assign number values to specific locations in a script
age = 23
gpa = 3.55
string1 = 'My age is {1}, and my gpa is {0}'
print(string1.format(gpa, age))

# use words/names to assign numbers to specific locations in a script
age = 23
gpa = 3.55
string1 = 'My age is {age}, and my gpa is {gpa}'
print(string1.format(age = age, gpa = gpa))
