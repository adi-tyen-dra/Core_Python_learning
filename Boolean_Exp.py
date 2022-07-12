#True and False
day = "saturday"
temprature = 30
raining = False  #assign values firt then use in expression else error

#precedance of conditional operator- not>>and>>or

if day == "saturday" and temprature > 27 or not raining: # ~ (day == "saturday" and temprature > 27) or (not raining) because of precedance
    print("go out")
else:
    print("go in")

#truthy values-
if 0:   #0 of any kind is evaluated as false hence else will be executed
    print("hehe")
else:
    print("hoho")

name = input("please enter your name")
if name:    #an empty var will be evaluated as false but if val is there then true; now we may check if user entered something or not
    print("hello {} sir".format(name))
else:
    print("hi man don't you have a name")
     
#Usage of in-
parrot = "norwegion blue"
check = input("enter a char or a str to check in parrot ")
if check in parrot: #case sensitive
    print('yes "{}" is there in "{}"'.format(check,parrot))
else:
    print('nope "{}" doesnt need "{}"'.format(parrot,check))
print()

#usage of not in-
activity = input("what would you like to do today")
if "cinema" not in activity.casefold():   #to avoide case sensitive issues use casefold to turn entire string to lower case
    print("but i wish to go to cinema")
else:
    print("lets go")

#some important methods-
# str.capitalize()
# Return a copy of the string with its first character capitalized and the rest lowercased.
# str.casefold()
# Return a casefolded copy of the string. Casefolded strings may be used for caseless matching.
# str.lower()
# Returns a lowercase copy of the string. doesnt work on alphabets from different languages this is where casefold is helpful
# str.upper()
# Returns a uppercase copy of the string.
