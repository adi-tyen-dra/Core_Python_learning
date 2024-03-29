# STRING REPLACEMENT FIELD: FORMATTING

for i in range(1, 13):   # a loop from 1 to 12
    print("No. {0:2} squared = {1:3} and cubed = {2:4}"
          .format(i, i**2, i**3))
    
# here the digit after colon specifies the defined space for the value; its purpose is to align the data well

# specifying the alignment for the values- > means right align, < means left align and ^ means center align

for i in range(1, 13):  # a loop from 1 to 12
    print("No. {0:<2} squared = {1:>3} and cubed = {2:^4}"
          .format(i, i**2, i**3))
print()

# in case of integer or float when fl.v is specified and 
# -no. is shorter than the extra white space can be replaced by 0 as follows 
# note: rule is only applicable for the left side of int part where significance of digit is 0
# in case of int no. people use d, (similar to f in float but its presence doesn't make difference in most cases)
print("{0:07.3f} + {1:03} = {2:02d}"
      .format(1.234, 2, 3))  # ans- 001.234 + 002 = 03

print()
# the formatting technique can also be used to justify the decimal digit precision after the no. along with field val

# if field val < default float val (15) + no. of int digits + point place 
# -then it prints the val of given with default float val
# in this case 12 < 15+1+1 
print("pi is approximately {0:12}"
      .format(22/7))

# if field val > default float val (15) + no. of int digits + point place 
# -then the normal field arrangement would be done
# in this case 20 > 15+1+1
print("pi is approximately {0:20}"
      .format(22/7))

# floating point has been specified but the field val isn't so,
# -the no. will show 6 as default float val with given float val as field val
# in this case field val = 12 (no. given for float val) with float val = 6 (default)
# note: in this case field val could have been any given no. while the float val would remain default
print("pi is approximately {0:12f}"
      .format(22/7))

# here both val provided but fe.v < fl.v so fl.v is given precedence and fe.v is ignored
print("pi is approximately {0:12.20f}"
      .format(22/7))

# here in all two case both val provided and fe.v > fl.v, so it is carried out without any issue
print("pi is approximately {0:52.50f}"
      .format(22/7))
print("pi is approximately {0:57.54f}"
      .format(22/7))

# answer for above:
# pi is approximately 3.142857142857143
# pi is approximately    3.142857142857143
# pi is approximately     3.142857
# pi is approximately 3.14285714285714279370
# pi is approximately 3.14285714285714279370154144999105483293533325195312
# pi is approximately  3.142857142857142793701541449991054832935333251953125000

# note: in case of ordered value we don't have to specify the order and can still use after colon formatting
for i in range(1, 13):  # a loop from 1 to 12
    print("No. {} squared = {} and cubed = {:4}"
          .format(i, i**2, i**3))

# STRING REPLACEMENT FIELD: F STRINGS
# another way of formatting; follows the same rules as normal formatting but with a minor change in syntax

print(f"pi is approximately {22/7:20.16f}")
pi = 22/7
print(f"pi is approximately {pi:30.28f}")

# STRING REPLACEMENT FIELD: INTERPOLATION (PYTHON 2)
# might be removed from newer versions; its use in python 3 is not recommended
age = 20
major = "years"
print("my age is %d %s and %d %s" % (age, major, 6, "months"))
# for float val along with precision-
print("val of pie is %60.50f" % (22/7))
