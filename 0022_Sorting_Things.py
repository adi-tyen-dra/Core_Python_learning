# SORTING THINGS

# sorted() function different from sort() method

pan_gram = "the quick brown fox jumps over the lazy dog"

letters = sorted(pan_gram)  # sorted function
print(letters)  # returns all the char in the sequence in sorted manner

# sorted function example
num = [2.3, 9.5, 6.5, 5.0, 1.0, 9.4]
sorted_nums = sorted(num)  # returns a newly created sorted list which is assigned to "sorted_nums" var
print(sorted_nums)  # sorted list
print(num)  # unlike sort() method, a new list is created here hence num remains unchanged
# note: sorted() function returns the newly created sorted version of target sequence

# sort method example 
number = [ 1, 3, 2, 9, 6, 8]
another_number = number
number.sort()  # the list gets sorted
print(number)  # the orignal list is changed and no new list is created
print(another_number)  # this displays sorted list as it is assigned the orignal list which changed
# note: sort() method changes the orignal list without creating any copy
# -moreover, it doesn't return anything so assigning it to a var will give error

# SORTING THINGS IN CASE INSENSITIVE MANNER

print(sorted("The lazy brown Fox jumped over the quick Dog",
             key=str.casefold))
# works both with sort and sorted
