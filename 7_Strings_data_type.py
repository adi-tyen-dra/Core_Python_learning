#extra: Square brackets are used for 4 reasons in python, indexing, slicing,,

#indexing and negative indexing-

         #01234567890123
parrot = "Norwegion Blue"
print(parrot)
print(parrot[3]) #gives the fourth character of the string that is w because counting for string characters usually starts from 0

 ##MINI CHALLENGE##
# =>using the above var to print "we win" with all char in separate line using indexing then repeat the challeng using negative index
#my solution-
print(parrot + "\n" + parrot[3] + "\n" + parrot[4] + parrot[9] + "\n" + parrot[3] + "\n" + parrot[6] + "\n" + parrot[8])
print(parrot + "\n" + parrot[-11] + "\n" + parrot[-10] + "\n" + parrot[-5] + "\n" + parrot[-11] + "\n" + parrot[-8] + "\n" + parrot[-6])
# negative index of a char = (length of the string) - (char's positive index)

#Slicing

#slicing comprises of start, stop and a step value 
#firstly looking at slicing without step value
# Note: the char where the slicing stops isn't included in the end result
a = "hello there, how are you?"
print(a[0:3]) # start=0; stop=3 so, "ans = hel"
print(a[5:7]) # here start = 5 and stop = 7 so "ans = <blank>t"
print(a[:5]) # another way to specify the start of sclicing at index of first char, "ans = hello"
print(a[7:]) # another way to specify the end of slicing at index of last char+1, "ans = here, how are you?"
