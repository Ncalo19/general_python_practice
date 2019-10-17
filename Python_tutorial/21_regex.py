# RegEx: (Regular Expression) a sequence of characters used to form a search pattern
# if there is no match, None will be returned
# findall, search, split, sub

# import the regular expression module
import re

# return a list containing all matches from a string
string1 = 'The rain in Spain falls'
print(re.findall('ai', string1))

# if a match is found, print a specific string
string1 = 'I like to play hockey'
x = re.findall('hockey', string1)
if x:
    print('Plays hockey')
else:
    print('Does not play hockey')

# if some of the strings in an array exist in another string, print a specific string
string1 = 'I like to play hockey'
x = re.findall('[xyyz]', string1)
if x:
    print('X, y, or z are in the string')
else:
    print('They are not')

# if every specified letter is in a string, print a specific string
string1 = 'I like to play hockey'
a = ['c', 'k']
if all(x in string1 for x in a):
    print('The letters', a, 'are in the string')
else:
    print('The letters', a, 'are not in the string')

# locate where the first matching character is in a string
string1 = 'I like to play hockey'
print(re.search('k', string1))

# locate the start of the first matching character in a string
string1 = 'I like to play hockey'
x = re.search('k', string1)
print('K is located at space', x.start()) # .end to locate the end of the first matching character

# split the string at every space
string1 = 'I like to play hockey'
print(re.split('\s', string1))

# split a string for a set number of occurences (maxsplit parameter)
string1 = 'I like to play hockey'
print(re.split('\s', string1, 2))

# replace spaces with a letter, number, or symbol
string1 = 'I like to play hockey'
print(re.sub('\s', '-', string1))

# replace a set number of spaces with a letter, number, or symbol (count parameter)
string1 = 'I like to play hockey'
print(re.sub('\s', '-', string1, 3))

# list the start and end positions of a match # r'\bS\w+' (r'\bS\w+')
string1 = 'The rain in Spain falls'
x = re.search(r'\bS\w+', string1)
print(x.span()) # span() prints the position as a tuple

# print the string passed into the function
string1 = 'The rain in Spain falls'
x = re.search('ai', string1)
print(x.string)

# print the part of the string containing the match (r'\bc\w+')
string1 = 'The rain in Spain falls'
x = re.search(r'\bS\w+', string1)
print(x.group())

"""
https://www.w3schools.com/python/python_regex.asp#sub
(https://blog.bitsrc.io/a-beginners-guide-to-regular-expressions-regex-in-javascript-9c58feb27eb4)

Metacharacters
Character	Description   Example
[]	A set of characters	"[a-m]"
\	Signals a special sequence (can also be used to escape special characters)	"\d"
.	Any character (except newline character)	"he..o"
^	Starts with	"^hello"
$	Ends with	"world$"
*	Zero or more occurrences	"aix*"
+	One or more occurrences	"aix+"
{}	Exactly the specified number of occurrences	"al{2}"
|	Either or	"falls|stays"
()	Capture and group

x = re.search(r'\bS\w+', string1)

Special Sequences
Character	Description   Example
\A	Returns a match if the specified characters are at the beginning of the string	"\AThe"
\b	Returns a match where the specified characters are at the beginning or at the end of a word	r"\bain" r"ain\b"
\B	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word	r"\Bain" r"ain\B"
\d	Returns a match where the string contains digits (numbers from 0-9)	"\d"
\D	Returns a match where the string DOES NOT contain digits	"\D"
\s	Returns a match where the string contains a white space character	"\s"
\S	Returns a match where the string DOES NOT contain a white space character	"\S"
\w	Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)	"\w"
\W	Returns a match where the string DOES NOT contain any word characters	"\W"
\Z	Returns a match if the specified characters are at the end of the string	"Spain\Z"

Sets
Set    Description    Example
[arn]	Returns a match where one of the specified characters (a, r, or n) are present
[a-n]	Returns a match for any lower case character, alphabetically between a and n
[^arn]	Returns a match for any character EXCEPT a, r, and n
[0123]	Returns a match where any of the specified digits (0, 1, 2, or 3) are present
[0-9]	Returns a match for any digit between 0 and 9
[0-5][0-9]	Returns a match for any two-digit numbers from 00 and 59
[a-zA-Z]	Returns a match for any character alphabetically between a and z, lower case OR upper case
[+]	In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string
"""
