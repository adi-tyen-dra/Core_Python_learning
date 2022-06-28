#flow of program and decision making
name = input("what is your name? ")

age = input("how old are you {}? ".format(name))
print("he says he's {} years old".format(age)) #input func by default always return str so age here is str

age = int(input("how old are you {}? ".format(name))) # to make it int we use int func as follows; val other than int will throw error here
print("he says he's {} years old now".format(age)) # here the age is int 

#IF-ELSE Statement-
#to check their authority to vote; 
if age>=18:
    print("you are old enough to vote")
    print("please put an X in the box")
else:
    print("you aren't old enough to vote, please come back in {} years ".format(18-age))

print()
#above this can be achieved in a converse format aswell proving that the order of statement doesn't matter-

if age<18:
    print("you aren't old enough to vote, please come back in {} years ".format(18-age))
else:
    print("you are old enough to vote")
    print("please put an X in the box")

#ELIF- ELSE-IF Statement, order of the statement does matter here

if age < 18:
    print("you aren't old enough to vote, please come back in {} years ".format(18-age))
elif age >= 200:
    print("false age, please enter a real age") #if above statement is false then check for this otherwise don't
else:
    print("you are old enough to vote")
    print("please put an X in the box")

#converse of this statement won't give us the same result as order is important here
#Note: ctrl+forward slash can comment out multiple lines at once in most py ide

