print("string enclosed by double quotes")
print('string enclosed by single quotes')
print("python's string are easy to use")   #single quotes used within string
print('here are the "quotes", we need')   #double quote used within string
print("hello"+'world'+"good day")   #concantenating string
greet = "namaste"
name = "adi"
print(greet+' '+name) #concantenation of strings makes more sence with variables
#unlike java, python has no difference between single and double quotes
#input function helps in taking input from the user keyboard
greet = 'sayonara'
name = input('please enter your name - ')   #here input is evaluated first and its result is assigned to name var
print(greet+' '+name)   #here greet and name are without "" as they are var instead of string, being used as arg for print func
