# variable is basically just a way to give a meaningful name to an area of memory, 
# -into wich we can place certain values.
# when a var is created python allocates a certain area to it in memory 
# -and knows where to call it when the var is called.
# it also allocates the type of var based on the kind of val provided 
# -and allows only the relevent action wrt the var type.
# rules for python underscore-
# -> may start from an alphabet or underscore but not a num
# -> may contain num, underscore or alphabets
# -> case sensitive so, A_1 and a_1 are considered two different variable.
# var are first created when they are attached to a value using "=" sign.

name = "hela"
age = 24
print(name)
print(age)
print(type(name))  #checking the type of var
print(type(age))

# in output, python refers age and name as object of type int and str.
# in python, values bound to the var have a data type instead of var itself hence 
# -type of var may change when val with a different data type is rebounded to the var.

age = "24 years"  # the new val rebounded to age changes its data type.
print(type(age))
# Python's property of being dynamically-typed- if the type of a variable is checked during run-time.

# A strongly-typed programming language is one in which each type of data 
# -(such as integer, character, hexadecimal, packed decimal, and so forth) 
# -is predefined as part of the programming language and all constants or variables defined 
# -for a given program must be described with one of the data types.
# -hence python is a stronglytyped language.
