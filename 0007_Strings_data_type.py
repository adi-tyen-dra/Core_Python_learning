# extra: Square brackets are used for 4 reasons in python, indexing, slicing,,

# indexing and negative indexing-

parrot = "Norwegian Blue"
print(parrot)
print(parrot[3])  # gives the fourth character of the string 'w', 
# -because counting for string characters usually starts from 0

# #MINI CHALLENGE# #
# using the above var to print "we win" with all char in separate line using indexing 
# -then repeat the challenge using negative index

# my solution-

print(parrot + 
      "\n" + 
      parrot[3] + 
      "\n" + 
      parrot[4] +
      parrot[9] + 
      "\n" + 
      parrot[3] +
      "\n" +
      parrot[6] +
      "\n" +
      parrot[8])

print(parrot + 
      "\n" +
      parrot[-11] +
      "\n" +
      parrot[-10] +
      "\n" +
      parrot[-5] +
      "\n" +
      parrot[-11] +
      "\n" +
      parrot[-8] +
      "\n" +
      parrot[-6])

# negative index of a char = (length of the string) - (char's positive index)

# Slicing

# slicing comprises start, stop and a step value 
# slicing without step value => string[start_index:stop_index]
# Note: the char where the slicing stops isn't included in the end result

# Slicing with positive index.
a = "hello there, how are you?"
print(a[0:3])  # start=0; stop=3 so, "ans = hel"
print(a[5:7])  # here start = 5 and stop = 7 so "ans = <blank>t"
print(a[:5])  # another way to specify the start of slicing at index of first char, "ans = hello"
print(a[7:])  # another way to specify the end of slicing at index of last char+1, "ans = here, how are you?"
n = 4  # just a random var
print(a[:])  # this prints the entire string as it is

print(a[n:] +
      a[:n])  # irrespective of n, such setup will always produce the entire string

print(a[2:4] + 
      a[7:9])  # ll+he = 'llhe'

# Slicing with negative index.

abc = "abcdefghijklmnopqrstuvwxyz"
print(abc[-4:-1])  # ans= wxy
print(abc[-4:25])  # ans= wxy
print(abc[-4:21])  # ans= <nothing>, occurs irrespective of the positive or negative index, 
# cuz the stop index lies leftwards w.r.t the start index 

# Slicing with step value => string[start_index:stop_index:steps]

print(abc[0:10:3])  # ans = 'adgj' here 3 becomes the step so every third char is printed within start and stop
# default step is 1

# minor application demonstration 

num = "9,567:345-654.698,456;342 223-345"
separators = num[1::4]  # all the punctuation marks collected
print(separators)

values = "".join(char if char not in separators else " " for char in num).split()
print([int(val) for val in values])
# the code above brings out the values separately removing all the punctuation marks;

# Backward slicing
# note: forward slicing- start_index towards left of stop_index and step = +ve
# note: back slicing- start_index towards left of stop_index and step = -ve
backwards = abc[25:0:-1]  # all the alphabets will be printed backwards due to neg step value, 
# -not printing "a" as it's the stop value
print(backwards)
print(abc[25::-1])  # to include 'a' we need to omit the stop value
print(abc[::-1])  # same result will be produced if we omit both start and stop value

# MINI CHALLENGE
# => using the abc string produce the followed string using slicing, 
# qpo; edcba; last eight alphabets in rev order

# my solution-
print(abc[-10:-13:-1])  # produces qpo
print(abc[-22::-1])  # produces edcba
print(abc[25:17:-1])  # produces last eight alphabets in rev order

# common notion-
x = 2
print(abc[-x:])  # prints last x characters till the end of string
# works for all values of x less than string length

print(abc[:x])  # prints first x characters till x within the string
# if x exceeds the limit of string length nothing more will be printed
