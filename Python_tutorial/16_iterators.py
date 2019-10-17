# Iterator: oject with a countable # of values (can be iterated upon)
# Iterable: can traverse (go through) each value
# lists, tuples, sets, dictionaries, and strings are iterable objects

# iterate through a list (an iterator)
list1 = ['apple', 'bannana', 'cherry']
x = iter(list1)

print(next(x))
print(next(x))
print(next(x))

# loop through a list (an iterator)
for x in list1:
    print(x)

# loop through a string (an iterator)
for x in 'apple':
    print(x)

# Create an iterator that returns numbers, starting with 1, and each sequence will increase by one
class class1:
    def __iter__(self):
        self.a = 1 # a is just a placeholder, can be any letter or word
        return self
    def __next__(self):
        x = self.a
        self.a += 1
        return x
x = iter(class1())

print(next(x))
print(next(x))
print(next(x))

# Create an iterator that returns numbers, starting with 1, and each sequence will increase by one
# and stops at 5
class class1:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a <= 5:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration
for x in iter(class1()):
    print(x)
