# operators are used to perform operations on variables and values
#Types: arithmetic, assignment, comparison, logical, identity, membership, bitwise

# arithmetic operators
x = 22
y = 5
# simple ones: +, -, *, /
# modulus: gives you the remainder from dividing the first number by the second
print(x % y)
# exponentiation (exponent)
print(x ** y)
# floor division: division that rounds down to nearest integer
print(x // y)

# assignment operators (assign a value to = itself operated on by another number)
# (ex. a = a * 8)
a = 5
a += 5 # a = a + 5
a *= 5 # a = a * 5
a %= 5 # a = a % 3
# (other assignment operators are the same,
# they just start with different aritmetic operators before the = sign)

# comparison operators (return a true or false statment)
p = 5
q = 7
#  are two numbers/variables equal
print(p == q)
#  are two numbers/variables inequal
print(p!=q)
# greater than, less than, greater than or equal to, less than or equal to
print(p > q)
print(p < q)
print(p >= q)
print(p <= q)

# logical operators : and, or, not
x = 12
print(x > 7 and x < 15)
print(x < 8 or x > 9)
print(not(x > 7 and x < 15))

# identity operators : is, is not (must be same object, not just ==)
x = 'dog'
y = 'dog'
z = x
print(x is y)
print(x is z)
print(x is not z)
print(x == y)

# membership operators : in, not in
x = 'car', 'boat', 'plane'
print('plane' in x)
print('speace ship' not in x)

# (bitwise operators : &, |, ^, ~, <<, >>)

# & : bitwise and (looks at code representing the two numbers and returns a 0
# when two bits are different (0 and 1)) (false, they are not the same)
print(12 & 22)

# | : bitwise or (looks at code representing the two numbers and returns a 1
# when two bits are different (0 and 1)) (true, they are different)
print(12 | 22)

# ^ : bitwise xor (looks at code representing the two numbers and returns a 1 in the
# code for any bits that are different at the same decimal place. A 0 is returned when
# bits at the same decimal place are the same)
print(12 ^ 22)

# ~ : compliment (gives the compliment to the number listed(0:1, -1:2, -2:3...))
# computers always store positive numbers
print(~25)

# << : left shift (shift the bits two zero bits to the left (add two 0s to the end))
print(10 << 2)

# >>: right shift (shift the bits two zero bits to the right (take away two bits from
# the end))
print(10 >> 2)
