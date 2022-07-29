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

b.append("cream")  # adding an item to b with append method called upon object b with dot notation.
print(a)
print(c)
print(d)
print(e)
print(shopping_list)  # all will produce the same edited result

# COMMON SEQUENCE OPERATIONS (applicable to all sequence types)

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9.5]

print(min(even))  # min returns the minimum value of the sequence
print(min(odd))
print(max(odd))  # max produces the maximum value of the sequence
print(max(even))
# above won't work for a combination of str and int

print()
# Note: in case of string/char comparison, char wise ascii value is checked for
g = ["9z", "z", "zw", "Z", "w"]
print(max(g))

print()
# len func returns the length of the sequence
print(len(even))
print(len(odd))

print()
# count func returns the count of a provided argument in the sequence
my_list = ["milk", 'milky', 'milk', 'bulky']
print(my_list.count("milk"))  # used to check entire items
# in case of string
print("mississippi".count("iss"))

# COMMON OPERATIONS ON MUTABLE

# Note: A function is a block of organized, reusable code that is used to perform a single, related action.
# A method is also the same except it is bound to an object and called upon it.
# -i.e. without an object a method can't be called.
# basic structure of function: function_name(arguments if any)
# basic structure of method: object_name.method_name(argument if any)

# APPENDING AN ITEM TO THE LIST

# adding a computer part to buying list

choice = "-"  # anything other than valid option; can't use None type here
buying_list = []  # empty list
while choice != "0":
    if choice in "123456":
        print("adding the {} item to your buying list"
              .format(choice))
        if choice == "1":
            buying_list.append("printer")
        elif choice == "2":
            buying_list.append("mouse")
        elif choice == "3":
            buying_list.append("keyboard")
        elif choice == "4":
            buying_list.append("cpu")
        elif choice == "5":
            buying_list.append("monitor")
        elif choice == "6":
            buying_list.append("HDMI cable")
    else:
        print("please add an option from the following list: \n"
              "1: printer\n"
              "2: mouse\n"
              "3: keyboard\n"
              "4: cpu\n"
              "5: monitor\n"
              "6: HDMI cable\n"
              "0: to finish\n")
    choice = input()
print(buying_list)

# ITERATING OVER A LIST

# optimising the previous example with loop over list along with other changes

available_list = ["printer",
                  "mouse",
                  "keyboard",
                  "cpu",
                  "monitor",
                  "HDMI cable",
                  ]
# valid_choices = [str(i) for i in range(1, len(available_list) + 1)]
# -discussed later, above is the optimal way to define valid_choice
valid_choices = []
for i in range(1, len(available_list) + 1):
    valid_choices.append(str(i))  # creates a list of numeric valid choices
choice = "-"
buying_list = []
while choice != "0":
    if choice in valid_choices:
        print("adding the {} item to your buying list"
              .format(choice))
        index = int(choice) - 1
        part = available_list[index]
        buying_list.append(part)
    else:
        print("please add an option from the following list: \n")
        for part in available_list:  # loop over the list
            print("{0}: {1}"
                  .format(available_list.index(part), part))  # not very efficient
            # the index method has to search the entire list for index each time
            # if the list was sorted binary search could've been used
    choice = input()
print(buying_list)

# ENUMERATE FUNCTION

# The "enumerate()" function takes in an iterable as an argument, such as a list, string, tuple, or dictionary,
# and returns the element along with a counter keeping track of the indexes of each element
# -In addition, it can also take in an optional argument, start,
# -which specifies the number we want the count to start at (the default is 0).

# further optimization of earlier code using enumerate function
available_list = ["printer",
                  "mouse",
                  "keyboard",
                  "cpu",
                  "monitor",
                  "HDMI cable",
                  "to finish",
                  ]
valid_choices = []
for i in range(1, len(available_list) + 1):
    valid_choices.append(str(i))
choice = "-"
buying_list = []
while choice != "0":
    if choice in valid_choices:
        print("adding the {} item to your buying list"
              .format(choice))
        index = choice - 1
        part = available_list[index]
        buying_list.append(part)
    else:
        print("please add an option from the following list: \n")
        for num, part in enumerate(available_list):  # example of for loop with multile var iteration
            # each item of loop returns multiple value hence multiple var used in for loop
            print("{0}: {1}"
                  .format(num + 1, part))  # optimized with enumerate 
            # the track of index is alredy kept and we don't need to search the entire list 
    choice = input()
print(buying_list)

# another enumerate example
for index, character in enumerate("abcdefghij"):
    print("{0}: {1}"
          .format(index, character))
