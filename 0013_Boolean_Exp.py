# True and False
day = "saturday"
temperature = 30
raining = False  # assign values first then use in expression else error

# precedence of conditional operator- not>>and>>or

if day == "saturday" and temperature > 27 or not raining:  # (day == "saturday" and temperature > 27) or (not raining)
    # because of precedence
    print("go out")
else:
    print("go in")

# truthy values-
if 0:  # 0 of any kind is evaluated as false hence else will be executed
    print("hehe")  # underlined cuz its unreachable code
else:
    print("hoho")

name = input("please enter your name")
if name:  # an empty var will be evaluated as false but if val is there then true;
    # -now we may check if user entered something or not
    print("hello {} sir".format(name))
else:
    print("hi man don't you have a name")

# Usage of in-
parrot = "norwegian blue"
check = input("enter a char or a str to check in parrot ")
if check in parrot:  # case sensitive
    print('yes "{}" is there in "{}"'
          .format(check, parrot))
else:
    print('nope "{}" doesnt need "{}"'
          .format(parrot, check))
print()

# usage of not in-
activity = input("what would you like to do today")
if "cinema" not in activity.casefold():  # case fold avoids case-sensitive issues turning entire string to lower case
    print("but i wish to go to cinema")
else:
    print("lets go")

# some important methods-
# str.capitalize()
# Return a copy of the string with its first character capitalized and the rest lowercase.
# str.casefold()
# Return a case-folded copy of the string. Case folded strings may be used for case less matching.
# str.lower()
# Returns a lowercase copy of the string.
# -doesn't work on alphabets from different languages this is where case fold is helpful
# str.upper()
# Returns an uppercase copy of the string.

# MINI Challenge
# write a small program to ask for a name and an age. When both values have been entered,
# check if the person is the right age to go on an 18-30 holiday.
# They must be over 18 and under 31. If they are, welcome them to the holiday, otherwise print 'a',
# message refusing them entry. Our programs expect valid input. a person of 18 years is considered over 18

name = input("please enter your name ")
if name:
    age = int(input("please enter your age in numerics "))
    if 18 <= age < 31:
        print("congratulations {} you are eligible for holiday package"
              .format(name))
    else:
        print("Sorry {} you aren't eligible for the package"
              .format(name))
else:
    print("you haven't entered your name the program is dismissed")
