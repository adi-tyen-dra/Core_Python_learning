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
