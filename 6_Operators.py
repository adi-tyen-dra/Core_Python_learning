a = 12
b = 3

print(a + b)   #15
print(a - b)   #9
print(a * b)   #36
print(a / b)   #4.0
print(a // b)  #4 interger division rounded down towards -infinity
print(a % b)   #0 modulous gives the remainder after integer division

#usecase for integer division
print() #empty line

for i in range (1,4):   #loop prints integer till 3
  print(i)              #it only uses int values for ranges so in place of 4, a/b will give error while a//b will work fine
  
#an expression is a combination of operators, operands or other expressions that can be interprated to some valuea.
#here, leaving the a and b in line 1 and 2 (not being evaluated) along with i in line 14 (not being evaluated) rest all are expression

i = 1    #here as well i is not an expressionn as it is not being evaluated in line 23, 24, out
print(i)
i = 2
print(i)
i = 3
print(i)

# Operator precedance
