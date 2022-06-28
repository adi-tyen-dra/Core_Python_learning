#flow of program and decision making
name = input("what is your name? ")
age = input("how old are you {}? ".format(name))
print("he says he's {} years old".format(age)) #input func by default always return str so age here is str
# to make it int we use int func as follows
age = int(input("how old are you {}? ".format(name))) #due to int func use only int val otherwise it'll throw error
print("he says he's {} years old now".format(age)) # here the age is int 

#to check their authority to vote
if age>=18:
    print("you are old enough to vote")
    print("please put an X in the box")
else:
    print("you aren't old enough to vote, please come back in {} years ".format(18-age))

print()
#this can be achieved in a converse format aswell-

if age<18:
    print("you aren't old enough to vote, please come back in {} years ".format(18-age))
else:
    print("you are old enough to vote")
    print("please put an X in the box")
