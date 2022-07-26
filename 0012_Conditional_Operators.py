# CONDITIONAL OPERATORS

# > greater than
# < less than
# >= greater than or equal to
# <= less than or equal to
# != not equal to
# == equal to

# guessing game with two attempts
ans = 5
print("please enter a number between 1 to 10")
guess = int(input())
# if ans > guess:
#     print("try guessing higher")
#     if ans == guess:
#         print("you've guessed correctly")
# elif ans < guess:
#     print("try guessing lower")
#     if ans == guess:
#         print("you've guessed correctly")
# else:
#     print("bravo you did it!")

# below is the efficient form of code using appropriate conditional operators
if ans != guess:  # this line
    if ans > guess:
        print('guess higher')
    if ans < guess:
        print('guess lower')
    guess = int(input())
    if guess == ans:
        print('good job you did it')
    else:
        print("sorry you didn't make it")
else:
    print("bravo you got it in the first go")

# MINI CHALLENGE
# change "this line" to "if ans == guess:" and make appropriate changes to the program to get same output

# my solution
if ans == guess:
    print("bravo you got it in the first go")
else:
    if ans > guess:
        print('guess higher')
    if ans < guess:
        print('guess lower')
    guess = int(input())
    if guess == ans:
        print('good job you did it')
    else:
        print("sorry you didn't make it")

# 'AND' AND 'OR' CONDITIONALS

# AND gives true for a pair of conditions only if both are true else false
# OR gives true for a pair of conditions if at least one of the condition is true else false
# note: python stops checking condition in:
# AND if one "false" is found 
# OR if one true is found
# example code-
num = int(input())
if num >= 1 and num <= 10:  # it is underlined as ide suggests simplified chained comparison
    print('and condition is satisfied')
else:
    print('and condition is not satisfied')
if num > 20 or num % 2 == 0:
    print('or condition is satisfied')
else:
    print('or condition is not satisfied')

# Simplified chained comparison appears to suggest that the comparison statement can be simplified by chaining together
# In above case  "num >= 1 and num <= 10" can be changed to "1 <= num <= 10" giving the same output
