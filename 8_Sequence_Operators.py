# python 3 has five sequence types-
# strings, lists, turple, range, bytes & bytearray
# sequence is defined to be the ordered set of items
# eg- string- 
str1 ="hello World!" # is a collection of 12 items each of which are chars.
# list-  
lis1 = [ "computer", "monitor","keyboard","mouse"] # is a collection of 4 items each of which is a string
#sequence are ordered hence we can use indexing to access the individual elements of the sequence as follows-
print(lis1[1][::3]) #will produce "mir" as 1 of lis1 = monitor then [::3] of monitor string gives "mir"

# conclusion: the operators discussed will be applicable to all of the sequence types, exception: concantenation is not applicable to all sequence types

#concantenation and multiplication aren't applicable on ranges

string1 = "hello "
string2 = "there "
string3 = "how "
string4 = "are "
string5 = "you "
print(string1 + string2 + string3 + string4 + string5) #concantenation of 5 strings 
#another way
print("hello " "there " "how " "are " "you") #give the same result as above (plus isn't necessary in this form)

print("hello "*5) #string multiplication also valid and produces the string "hello " five times in python 
# print("hello "*5+4) will give error as we are trying to add an int val to str which doesn't make any sence to python
print("hello "*5+"4") #here we replaced int 4 with str 4 so 4 becomes the part of str
print("hello "*(5+4)) #operator precedance here 5+4 will be evaluated first and the result will be multiplied to the str

#Subset verification

print("he" in string1) #true
print("er" in string2) #true
print("us" in string3) #false
print("hmm" in "zmmmhummkumdum") #false
