# a simple list
computer_parts = ["computer",
                  "monitor",
                  "keyboard",
                  "cpu",
                  "mouse"
                  ]
# iterating over a list
for part in computer_parts:
    print(part)
print()
# indexing an item of the list
# index starts at 0
print(computer_parts[2])
print(computer_parts[-1])  # -ve index
# slicing over a list
print(computer_parts[2:4])

# Note: above func seem to run same both for str type and list type
# -but one fundamental difference between the two is, list are mutable and strings are immutable
# -i.e- contents of string can not be changed once fixed but can be changed in case of lists

# IMMUTABLE AND MUTABLE OBJECTS

# immutable

# if an object is defined to be immutable that means it can't be changed
# following are the immutable types build into python
# int
# float
# bool
# str
# tuple
# frozenset
# bytes

# for a simple example in case of int,
# the value of 5 (int) can't be changed, we can add or subtract something from it to get a new value
# -but 5 will always remain 5, same can be stated for float


# in case of bool lets see this with another example:
# ID function returns the identity of an object.
# object's identity: it is an integer, which is guaranteed to be
# -unique and constant for this object during its lifetime.
# The documentation doesn't state that it should be the object's address
# -but Cpython (an interpreter and compiler) does return the object's memory address
# -but that's not true for other pythons.
# As stated, the ID for an object may be different each time we run the program,
# -but while your program is running, the object will have the same id.
# If python has to destroy the object and re-create it, then it's ID will also change.
# That gives us a good way to tell if an object is changed, or if python has to create a new object.
result = True
another_result = result
print(id(result))
print(id(another_result))  # produces the same identity as both are bound to the same address
# Now,if bool values could be changed, then changing the values should mean that the ID doesn't change.
result = False  # an attempt to change the bool
print(id(result))  # produces different ID
# instead of changing the bool, python rebound result to a new value - False
# assigning a new value to a boolean variable. that would be true in other languages. In C or Java, for example,
# -you can assign new values to boolean variables.
# In Python, though, that's not the case. Instead, we've attached the name result, to a new value.

# checking in case of string
result = "hello"
another_result = result
print(id(result))
print(id(another_result)) # produces same identity
result += "ish"
print(id(result))  # produces different identity
print(id(another_result))  # produces same identity as before
# Because strings are immutable, Python couldn't change the string hello.
# -What it did instead was created a new string, and bind the name result to this new string.

# mutable

# if an object is defined to be mutable that means it can be changed
# following are the mutable types build into python
# list
# dict
# set
# Bytearray

# we can change the value of mutable objects, without the object being destroyed and re-created.
# an example in case of list

computer_parts = ["computer",
                  "monitor",
                  "keyboard",
                  "cpu",
                  "mouse"
                  ]
another_computer_parts = computer_parts
print(id(computer_parts))
print(id(another_computer_parts))  # produces same id as in any other case

computer_parts += ["printer"]  # concatenating the list using augmented assignment
print(computer_parts)
print(another_computer_parts)  # both the list have been changed
print(id(computer_parts))  # identity remains the same
# it's because lists are mutable and Python was able to add a new item to the end of the list
# -without creating a new list.

# conclusion:
# An immutable object can't be changed. You can create a new object,
# -and use the same variable name for it, but you can't change the value of an immutable object.
# Mutable objects, such as lists, can be changed.

# BINDING MULTIPLE NAMES TO A LIST

shopping_list =["veggies",
                "milk",
                "fruits"
                ]

a = b = c = d = e = shopping_list 

# adding an item to b with append func
b.append("cream")
print(a)
print(c)
print(d)
print(e)
print(shopping_list)  # all will produce the same edited result


