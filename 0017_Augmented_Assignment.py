#In python, augmented assignment is an efficient way of assigning values to variables incase binary operaters are involved.
#following are a few examples-
a = 23
a += 1 #instead of "a = a + 1"   gives 24
print(a)
a -= 4 #instead of "a = a - 4"   gives 20
print(a)
a *= 5 #instead of "a = a * 5"   gives 100
print(a)
a /= 5 #instead of "a = a / 5"   gives 20.0
print(a)
a = 15.0// 4 #instead of "a = a // 4"  gives 5.0
print(a)
a**= 2 #instead of "a = a ** 2"  gives
print(a)
a =9.0% 2 #instead of "a = a % 2"   gives 0.0
print(a)

#In case of lang like java and c++ the above statements are identical but python computes them differently
#Reason1-
#normal assignment- the same variable appears twice in the expression hence is computed twice so less effecient
#augmented assignment- the variable appears only once so the time in computation is saved hence more effecient
#Reason2-
#normal assignment- during assignment new variable is created and binded to the result of performing the calculation, then the original variable is destroyed.
#augmented assignment- you can perform the operation in-place where possible, modifying the original variable instead of creating a new one. 
#note- reason 2 incase of augmented assignment doesn't always happen and depends upon the type of var/obj but will happen wherever possible.
