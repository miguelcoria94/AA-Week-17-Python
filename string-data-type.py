# you can wrap strings with single and double quotes

# multiline strings - python allows strings to span multiple lines using what's called triple quotes

print('''My instructions are very long so to make them
more readable in the code I am putting them on
more than one line. I can even include "quotes"
of any kind because they won't get confused with
the end of the string!''')

# calculating length - check how long a string is using len()

print(len("Spaghetti"))

# indexing a string - python starts at 0 too (zero-based indexing)

print("Spaghetti"[0])
print("Spaghetti"[4])

# python allows negative indexes to access a charater from the end of the string

print("hello"[-1])
print("hello"[-4])

#python also lets you get the range of indexes

print("Spaghetti"[1:4])  # => pag
print("Spaghetti"[4:-1])    # => hett
print("Spaghetti"[4:4])  # => (empty string)

#A shortcut for the beginning of the string is to omit the first number.

print("Spaghetti"[:4])  # => Spag
print("Spaghetti"[:-1])    # => Spaghett

#range does not through errors if it is out of bounds

# USING STRING FUNCTIONS