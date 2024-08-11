# WHILE LOOPS

# the basic form is 
# while <condition>: 
#     execute block of code.
# The condition can be anything that can evaluate to True or False, 
# and so long as the condition is True, the code in the loop will be executed,
# this block of code must have a way to make the condition false or break out of the loop
# -else the loop will run infinitely.
# When the condition becomes False, the loop terminates.

# a basic for loop
for i in range(10):  # no condition or initialization for i
    print("i is now {}"
          .format(i))

# while loop counterpart for the same for loop
i = 0  # initialization for i
while i < 10:  # condition for i
    print("i is now {}".format(i))
    i += 1  # (i=i+1) but this format is preferable 
    # works as a terminating condition otherwise while will run infinitely

# application of while loop's infinitive behaviour
directions = ["north",
              "south",
              "east",
              "west"]
chosen_direction = ""
while chosen_direction not in directions:
    chosen_direction = input("please choose a valid direction") 
    # loop doesn't terminates until a valid direction is chosen
print("you came out of it")

# basic while loop features
# In case of for loop the loop will repeat for each item in a predetermined sequence, 
# whereas with a while loop you don't need to know how many times the loop will execute.
# application example: 
# we don't know the amount of data that is to be read from a source 
# -this is where while loop can help and terminate itself as soon as the data input ends

# BREAK IN WHILE LOOP

directions = ["north",
              "south",
              "east",
              "west"]
chosen_exit = ""
while chosen_exit not in directions:
    chosen_exit = input("please choose a valid direction")
    if chosen_exit.casefold() == "quit":
        print("game over")
        break
print("you came out of it")

# MINI CHALLENGE
# Modify the code inside this loop to stop when 'i' is greater than zero and exactly divisible by 11
# code
# for i in range(0, 100, 7):
#    print(i)

# sol-
for i in range(0, 100, 7):
    print(i)
    if i > 0 and i % 11 == 0:
        break

# CONTINUE CHALLENGE
# print no. 0 to 20 not divisible by 3 or 5
# sol with continue
for i in range(0, 20):
    if i % 3 == 0 or i % 5 == 0:
        continue
    print(i)
# sol without continue
for i in range(0, 20):
    if i % 3 != 0 and i % 5 != 0:
        print(i)

# WHILE LOOP WITH ELSE BLOCK

# notice that the direction adventure game above prints the end message 
# -even when the user comes out of the loop by quitting that not needed
# -now that can be fixed using the loop-else block

directions = ["north",
              "south",
              "east",
              "west"]
chosen_exit = ""
while chosen_exit not in directions:
    chosen_exit = input("please choose a valid direction")
    if chosen_exit.casefold() == "quit":
        print("game over")
        break
else:
    print("you came out of it")  #only prints the message if loop terminates normaly
   
# CHALLENGE
# write a program to print a number of options, and allow the user to select an
# -option from the list. The options should be numbered from 1 to 9, although you can use less than nine options too.
# -Make sure that there are at least four options with zero to exit the program. So the program should continue looping,
# -allowing the user to choose one of the options each time, and the loop should terminate when the user chooses zero.
# -If the user makes a valid choice, the program should print a short message and the message should include
# -the value that they typed. Don't print a different message for each choice.
# -The only thing that should change is the number they typed.
# -Although you could print out the description, Now if their choice isn't one of the options in the menu,
# -nothing should be printed (although you can still see their input on the screen). As an optional extra,
# -modify the program so that the menu is printed again,
# -If they choose an invalid option.
# -Be careful with that one.
# -You may start off by duplicating the code to print the menu, but it's possible to write the program without
# -duplicating the print lines.

# my solution
choice = " "  # no initialization problem; helps to enter the first loop 
while choice not in range(0, 6):  # loop1, choice not in valid range
    choice = int(input("please choose one of the following options by no.\n"
                       "1.\tlearn python\n"
                       "2.\tlearn dsa\n"
                       "3.\tlearn data science\n"
                       "4.\tlearn dbms\n"
                       "5.\tlearn ml\n"
                       "0.\texit\n"))
    while choice in range(0, 6):  # loop2, choice in valid range
        if choice == 0:  # if executed, it brings us out of both loop 
            # first loop is terminated due to break statement
            # second loop is terminated because choice == 0 doesn't satisfy first loop's condition
            print("the program is terminated")
            break
        print("you have selected {} as your choice"  # for valid range other than 0, next choice is asked for
              .format(choice))
        choice = int(input("please enter your next choice"))  # if choice within valid range, loop2 repeats
        # if choice not in valid range, loop2 breaks and execution returns to loop1 again asking for choice with menu
        
# provided solution

choice = " " 
while choice != "0": 
    if choice in "12345":
        print("you chose {}"
              .format(choice))
    else:
        print("please choose one of the following options by no.\n"
              "1.\tlearn python\n"
              "2.\tlearn dsa\n"
              "3.\tlearn data science\n"
              "4.\tlearn dbms\n"
              "5.\tlearn ml\n"
              "0.\texit\n")
        choice = input()
