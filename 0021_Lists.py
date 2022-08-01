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

# sum function
numbers = [1,2,3,4,5,1,4,5]
# start parameter is not provided
Sum = sum(numbers)
print(Sum)  # gives 25
# start = 10
Sum = sum(numbers, 10)
print(Sum)  # givves 35
# TypeError is raised in the case when there is anything other than numbers in the list.

# COMMON OPERATIONS ON MUTABLE

# Note: A function is a block of organized, reusable code that is used to perform a single, related action.
# A method is also the same except it is bound to an object and called upon it.
# -i.e. without an object a method can't be called.
# basic structure of function: function_name(arguments if any)
# basic structure of method: object_name.method_name(argument if any)

# APPENDING AN ITEM TO THE LIST

# adding a computer parts to the buying list
choice = "-"  # anything other than valid option
# we can't use None type here
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

# optimising the previous example with loop over list along with some other changes
available_list = ["printer",
                  "mouse",
                  "keyboard",
                  "cpu",
                  "monitor",
                  "HDMI cable",
                  ]
# valid_choices = [str(i) for i in range(1, len(available_list) + 1)]
# discussed in later files, above is the optimal way to define valid_choice
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
        chosen_part = available_list[index]
        buying_list.append(chosen_part)
    else:
        print("please add an option from the following list: \n")
        for chosen_part in available_list:  # loop over the list
            print("{0}: {1}"
                  .format(available_list.index(chosen_part) + 1, part))  # not very efficient
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

# MINI CHALLENGE
# We have some data that contains a mixture of flowers and shrubs, in a list.
# Our customer would like two separate lists. One, called flowers, will contain only flowers, and
# the other, called shrubs, must contain only shrubs.
# Write code to populate the two lists with the appropriate plants from data.
# question code:
data = [
    "Andromeda - Shrub",
    "Bellflower - Flower",
    "China Pink - Flower",
    "Daffodil - Flower",
    "Evening Primrose - Flower",
    "French Marigold - Flower",
    "Hydrangea - Shrub",
    "Iris - Flower",
    "Japanese Camellia - Shrub"
]
flowers = []
shrubs = []
# my solution & given solution
for datas in data:
    if "Shrub" in datas:
        shrubs.append(datas)
    elif "Flower" in datas:
        flowers.append(datas)
print(shrubs)
print(flowers)

# REMOVING ITEMS FROM A LIST

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
        index = choice - 1
        part = available_list[index]
        if choice in buying_list:  # for removing item click its position again after adding it to list
            print("removing the {} item to your buying list"
                  .format(choice))
            buying_list.remove(part)  # remove func, removes the item from list and returns error if item not in list
        else:
            print("adding the {} item to your buying list"
                  .format(choice))
            buying_list.append(part)
    else:
        print("please add an option from the following list: \n")
        for num, part in enumerate(available_list):
            print("{0}: {1}"
                  .format(num + 1, part))
    choice = input()
print(buying_list)

# SORTING THE LIST

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]
even.extend(odd)  # another way to add items to the list
# extend method is used to add the contents of a list to the target list
print(even)  # the addition happens without any sorting
even.sort()  # method used to sort the list
print(even)
even.sort(reverse=True)  # used to sort in reversed manner
print(even)
# Note: list being mutable, copy of list is not created and the original list is changed

