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

print(a+b/3-4*12) #ans=-35 this is because python follows mathematical format to solve arithmetic expressions
print((a+(b/3))-(4*12)) #the expression is equivalent to the upper one
print(((a+b)/3)-4)*12) #ans=12 as the brackets are introduced the way of solving the expression changes
#precedance=> brackets > exponential > division=multiplication > additio=substraction 
#if operators have equal precedance then the one found first from the left is simplified first 
#expression can also be breaken down into smaller units for convenience in case of larger values

