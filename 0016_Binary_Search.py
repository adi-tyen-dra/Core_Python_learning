#Binary search is the most effecient way possible to search for an item in an odered collection of items.
#it works on the principle of dividing the search collection into half and checking the mid point for the item each time it fails to search the item
#eg- if a given no. is to be searched between a set of 1 to 1000 following would be the steps
#step0-> order the entire collection
#step1-> check for mid point=> lower limit + ((higher limit - lower limit)//2)       =>  1+((1000-1)//2)=500        #so try 500, lets say the no. is greater
#step2-> this time we know that no.>500 so narrow the range, same formula            =>  501+((1000-501)//2)=750    #so try 750, lets say the no. is smaller
#step2-> this time we know that no.<750 so narrow the range, same formula            =>  501+((749-501))//2)=625    #so try 625, and so on...
#following this method the no. would be found in at most 10 guesses in this case.
#no. of guess can be easily figured out, 2^10 = 1024 so in a range of 1023 no. at most 10 gusses are needed 


low = 1
high = 1000
print("please think of a no.")
int("please hit enter")
while True:
    guess = low + (high-low)//2
    hi_lo = input("my guess is {} should i guess high or low"
                  "enter either h, l or c respectively"
                  .format(guess)).casefold()
if hi_lo == "h":
    #guess higher, lower limit = current guess +1
elif hi_lo == "l":
    #guess lower, higher limit = current guess -1
else:
    print(please enter h, l or c)

