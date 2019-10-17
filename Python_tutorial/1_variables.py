# creating variables
word1 = ('Rangers ')
word2 = ('Suck ')
word3 = ('Dick ')
word4 = ('8------->')
sentence = (word1 + word2 + word3 + word4)
print(sentence)

# average of number variables (simple)
andrew = 8
sarah = 6
average = (andrew + sarah)/2
print(average)

# uppercase and lowercase of string value
name1 = 'Jo,e'
name2 = 'Nick'
name3 = 'Marciano'
print(name1.upper(),name2.lower())
# use a period after the object when extracting info about a class or performing an action on a script or array

# replace a script value (one letter)
print(name3.replace('M','J'))

# split a script value
print(name1.split(','))

# create a list
list1 = ['cup', 'bowl','plate']
print(list)

# print a string value from a specific point (called a slice)
print(name2[1:])

# count the # of string values
colors = ['red', 'blue', 'green']
print(len(colors))

# print specific strings in a list
print(colors[:-1])

# print the 3rd list item to the end
print(list[2:])

# simultaneously assign A VALUE to multiple variables
x = y = z = 'orange'
print(x, y, z)

# simultaneously assign VALUES to multiple variables
x, y, z = 'orange', 'vanilla', 'grape'
print(x, y, z)

# combining scripts and variables (text variables)
x = '   is   '
y = 'awesome'
print('python ' + x + ' '  + y)

# remove white space at beginning and end of a variable
print(x.strip())

# combining string and numbers
age = 23
opinion = 'which is young'
x = 'Nick is {} {}' # the {} are necessary)
print(x.format(age, opinion))

# can use numbers to id position in curly braces
x = 'Nick is {1} {0}'
print(x.format(age, opinion))
