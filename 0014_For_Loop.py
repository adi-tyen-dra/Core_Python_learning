# A for loop works by iterating over some set of values. 
# It assigns each of the values, one by one, to one or more variables. 
# It then executes a block of code once for each value.
# The set of values comes from a sequence or some other iterable object.
# iterable obj is anything than can be iterated over; sequence is also an iterable
parrot = "Norwegian Blue"  # sequence string
for character in parrot:  # for loop
    print(character)

num = "9,456;348:254 569,339:908"
separators = ""
for char in num:
    if not char.isnumeric():  # isnumeric returns true if the var stores a number
        separators = separators+char
print(separators)
values = "".join(char if char not in separators else " " for char in num).split()  # code that returns separated numbers
print([int(val) for val in values])

num = input('enter your string with any separators')  # input to try- "1, 3 4::78'9080
separators = ""
for char in num:
    if not char.isnumeric():      # isnumeric returns true if the var stores a number
        separators = separators + char

print(separators)

values = "".join(char if char not in separators else " " for char in num).split()  # code that returns numerics
print(sum([int(val) for val in values]))  # edited to return sum

# Note: in lang like c++ or java, for loops work differently 
# as they work with a starting and ending value with a variable being incremented each time around the loop whereas,
# in python the approach is much more flexible although similar effect from those lang can be achieved by
# -iterating a loop over a range in python.

# Ranges:
# ranges with for loop-

for i in range(1, 12):  # similar to slicing it doesn't iterate for the 12th time(end val) 
    print("i is now {}"
          .format(i))  # prints 1 to 11

for i in range(10, 0, -2):  # similar to slicing it has step values as well
    print(i)  # prints no. 10 to 1 with a step of 2

for i in range(10):  # will take 0 as the default start value and run ten times
    print(i)  # prints no.  0 to 9

# MINI Challenge
# write the prog to print all no. from 0 to 100, divisible by 7, (without using if)

# sol1
for i in range(0, 101, 7):
    print(i)
# sol2
for i in range(101)[::7]:  # it uses slicing
    print(i)

# Nested for loop-
for i in range(1, 13):  # 'i' is not defined outside this loop
    for j in range(1, 13):  # j is not defined outside this loop
        print("{0:02} times {1:02} is {2:03} "
              .format(i, j, i*j))
    print("------------------------")

# mini challenge: what if?
# case1: print("------") line is given indentation of 4 more space
# solution-
for i in range(1, 13):
    for j in range(1, 13):
        print("{0:02} times {1:02} is {2:03} "
              .format(i, j, i*j))
        print("------------------------")  # here in case1, line will be drawn after every record

# case2: print("------") line is given no indentation
# solution-
for i in range(1, 13):
    for j in range(1, 13):
        print("{0:02} times {1:02} is {2:03} "
              .format(i, j, i*j))
print("------------------------")  # here in case2, line will be drawn only once at the very last

# CONTINUE and BREAK statements-

# Continue Statement

shopping_list = ["milk", 
                 "bread",
                 "sugar",
                 "spam",
                 "rice",
                 "blueberry"]  # list
# following two code prints everything except spam

# for item in shopping_list:
#     if item!="spam":
#         print("buy" + 
#         item)

for item in shopping_list:
    if item == "spam":
        continue
    print("buy "+item)
# continue statement simply skips the entire followed code of an iteration if encountered
# continue statement is not a necessary statement in python and 
# -always have an alternative but can be used to increase readability

# Break statement
# it can be a useful component for searching code
item_to_find = "spam"
found_at = None  # simply means that this var doesn't have a value yet
for index in range(len(shopping_list)):  # len func gives length of the list
    if shopping_list[index] == item_to_find:
        found_at = index
        break    # break statement simply terminates the loop it is present in.
print("spam was found at index position {}".format(found_at))

# optimizing the same code incase item is not present in the list
item_to_find = "hammer"  # not in the list
found_at = None  # this time it can be used to optimise the code
for index in range(len(shopping_list)):
    if shopping_list[index] == item_to_find:
        found_at = index
        break
if found_at is not None:
    print("spam was found at index position {}".format(found_at))
else:
    print("could not find {} in the list".format(item_to_find))

# optimizing the code without for loop
if item_to_find in shopping_list:
    found_at = shopping_list\
        .index(item_to_find)  # index func for a seq types returns the index of the particular element
if found_at is not None:
    print("spam was found at index position {}"
          .format(found_at))
else:
    print("could not find {} in the list"
          .format(item_to_find))
   
# For Loop with Else

# Note: this else statement is different from the else from if-else blocks.
# here the else follows the for statement instead of an if statement

numbers = [1, 25, 56, 76, 81]  # list with 8's multiple

for number in numbers:
    if number % 8 == 0:
        print("we don't need these numbers")
        break  # if multiple of 8 found then loop terminated

# in above code, multiple of 8 is found and the loop is terminated with the print message
# but incase the no multiple is found and loop runs throughout, this situation is ambiguous
# inorder to provide a message only when the loop runs throughout we may use else s follows:

numbers_2 = [1, 25, 55, 76, 81]  # list without 8's multiple

for number in numbers:
    if number % 8 == 0:
        print("we don't need these numbers")
        break # if multiple of 8 found then loop terminated
else:
    print("every thing worked fine")  # this code block executes only when the loop ran throughout

# in above example, notice the indentation of else block is associated with for loop instead of if statement
# as formerly stated, this else block only executes if the entire loop ran throughout. in any case if the loop
# -is terminated before, this else statement won't be executed


