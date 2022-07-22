#A for loop works by iterating over some set of values. 
#It assigns each of the values, one by one, to one or more variables. 
#It then executes a block of code once for each value.
#The set of values comes from a sequence or some other iterable object.
#iterable obj is anything than can be iterated over; sequence is also an iterable
parrot = "Norweigen Blue" #sequence string
for character in parrot:   #for loop
    print(character)

num = "9,456;348:254 569,339:908"
separators = ""
for char in num:
    if not char.isnumeric():      #isnumeric returns true if the var stores a number
        separators=separators+char     
print(separators)
values = "".join(char if char not in separators else " " for char in num).split()  #code that returns separated numbers
print([int(val) for val in values])

num = input('enter your string with any separaters') #input to try- "1, 3 4::78'9080
separators = ""
for char in num:
    if not char.isnumeric():      #isnumeric returns true if the var stores a number
        separators=separators+char

print(separators)

values = "".join(char if char not in separators else " " for char in num).split()  #code that returns numerics
print(sum([int(val) for val in values])) #edited to return sum

# Note: in lang like c++ or java, for loops work differently 
# as they work with a starting and ending value with a variable being incremented each time around the loop whereas,
# in python the approch is much more flexible although similar effect from those lang can be achieved by iterating a loop over a range in python.

# Ranges-
#ranges with for loop-

for i in range(1,12): #similar to slicing it doesn't iterate for the 12th time(end val) 
  print("i is now {}".format(i)) #prints 1 to 11
  
for i in range(10,0,-2): #similar to slicing it has step values as well
  print(i) # prints no. 10 to 1 with a step of 2

for i in range(10): #will take 0 as the default start value and run ten times
  print(i) #prints no.  0 to 9
  
#Challenge*********
#write the prog to print all no. from 0 to 100, divisible by 7, (without using if)

#sol1
for i in range(0,101,7):
  print(i)
#sol2
for in in range(101)[::7]: #it uses slicing
  print(i)

# Nested for loop-
for i in range(1,13):  #i is not defined outside this loop
    for j in range(1,13): #j is not defined outside this loop
        print("{0:02} times {1:02} is {2:03} ".format(i,j,i*j))
    print("------------------------")

#mini challenge: what if?
#case1: print("------") line is given indentation of 4 more space
#solution-
for i in range(1,13):
    for j in range(1,13):
        print("{0:02} times {1:02} is {2:03} ".format(i,j,i*j))
        print("------------------------") #here in case1, line will be drawn after every record

#case2: print("------") line is given no indentation
#solution-
for i in range(1,13):
    for j in range(1,13):
        print("{0:02} times {1:02} is {2:03} ".format(i,j,i*j))
print("------------------------") #here in case2, line will be drawn only once at the very last

# CONTINUE and BREAK keywords-
