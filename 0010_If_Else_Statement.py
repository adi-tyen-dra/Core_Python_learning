import random  # importing a module named random

# flow of program and decision-making
name = input("what is your name? ")

age = input("how old are you {}? "
            .format(name))
print("he says he's {} years old"
      .format(age))  # input func by default always return str so age here is str

age = int(input("how old are you {}? "
                .format(name)))  # to make it int we use int func as follows; val other than int will throw error here
print("he says he's {} years old now"
      .format(age))  # here the age is int 

# IF-ELSE Statement-
# to check their authority to vote; 
if age >= 18:
    print("you are old enough to vote")
    print("please put an X in the box")
else:
    print("you aren't old enough to vote, please come back in {} years "
          .format(18-age))

# above this can be achieved in a converse format as well proving that the order of statement doesn't matter-

if age < 18:
    print("you aren't old enough to vote, please come back in {} years ".format(18-age))
else:
    print("you are old enough to vote")
    print("please put an X in the box")

# ELIF- ELSE-IF Statement, order of the statement does matter here

if age < 18:
    print("you aren't old enough to vote, please come back in {} years ".format(18-age))
elif age >= 200:
    print("false age, please enter a real age")  # if above statement is false then check for this otherwise don't
else:
    print("you are old enough to vote")
    print("please put an X in the box")

# converse of this statement won't give us the same result as order is important here
# Note: ctrl+forward slash can comment out multiple lines at once in most py ide
# 
# guessing game
# sample 1, answer fixed
ans = 5
print("please enter a number between 1 to 10")
guess = int(input())
if ans > guess:
    print("try guessing higher")
elif ans < guess:  # checked only when "if" is false
    print("try guessing lower")
else:  # checked only when both "if" and "elif" are false
    print("bravo you did it!")

# if-elif is used when at an instance only one of them can be true
# if-if is used when at an instance both can be true

# adding a second guess option
ans = 5
guess = int(input("please enter a number between 1 to 10"))
if ans > guess:
    print("try guessing higher")
    if ans == guess:
        print("you've guessed correctly")
elif ans < guess:
    print("try guessing lower")
    if ans == guess:
        print("you've guessed correctly")
else:
    print("bravo you did it!")

# Challenge: Address the following two issues with the guessing game:
# 1-> let the answer be random at every attempt
# 2-> let their be infinite attempts instead of two until the user guessed the number
# 3-> provide an exit option if the user enters 0
# solution-

# when a builtin func is available in an external module/package 
# -we must import it and use dot notation to use it in our program
# it is suggested to import all modules and packages needed, 
# -in the beginning of code though python allows inbetween import as well

highest_limit = 10  # specified separately so that in case of change 
# -there is no need to change it at different places inside the code
answer = random.randint(1, highest_limit)  # using randint func from random module, 
# -it produces random no. within the given inclusive range
print(answer)  # TODO: delete after testing
guess = 0  # initializing to any no. not in the range to enter once inside the loop
print("please enter your guess between 1 to {}"
      .format(highest_limit))
print("incase of exit please enter 0")
while guess != answer:
    guess = int(input("->"))
    if guess == 0:  # exit statement
        print("sorry to see you go")
        break
    elif guess == answer:
        print("you've guessed it, no. was indeed {}".format(guess))
        break
    elif guess > answer:
        print("please try lower ")
    else:
        print("please try higher ")

# Note: the TODO comment is highlighted differently in intellij ide 
# -and helps the coder to keep a track of certain actions that might be needed in code
