# the basic form is 
# while <condition>: 
#     execute block of code.
# The condition can be anything that can evaluate to True or False, 
# and so long as the condition is True, the code in the loop will be executed,
# this block of code must have a way to make the condition false or break out of the loop else the loop will run infinitely.
# When the condition becomes False, the loop terminates.

# a basic for loop
for i in range(10):  # no condition or initialization for i
    print("i is now {}".format(i))
  
# while loop counter part for the same for loop
i=0  # initialization for i
while i<10:  # condition for i
    print("i is now {}".format(i))
    i+=1 #(i=i+1) but this format is preferable #works as a terminating condition otherwise while will run infinitely
   
# application of while loop's infinitive behaviour
directions = ["north","south","east","west"]
chosen_direction = ""
while chosen_direction not in directions:
  chosen_direction = input("please choose a valid direction") # the loop will not be terminated until a valid direction is chosen
print("you came out of it")
  
# basic while loop features
# In case of for loop the loop will repeat for each item in a predetermined sequence, 
# whereas with a while loop you don't need to know how many times the loop will execute.
# application example- 
# we don't know the amount of data that is to be read from a source this is while loop can help and terminate itself as soon as the data input ends

# BREAK in while loop

directions = ["north","south","east","west"]
chosen_exit = ""
while chosen_exit not in directions:
  chosen_exit = input("please choose a valid direction")
  if chosen_exit.casefold() == "quit":
    print("game over")
    break
print("you came out of it")
  
#break challenge---
# Modify the code inside this loop to stop when i is greater than zero and exactly divisible by 11
#code-
# for i in range(0, 100, 7):
#    print(i)

#sol-
for i in range(0, 100, 7):
    print(i)
    if i > 0 and i % 11 == 0:
        break

#continue challenge---
# print no. 0 to 20 not divisible by 3 or 5
# sol with continue
for i in range(0,20):
    if i % 3 == 0 or i % 5 == 0:
        continue
    print(i)
#sol without continue
for i in range(0,20):
    if i % 3 != 0 and i % 5 != 0:
      print(i)
