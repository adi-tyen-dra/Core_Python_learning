# PEP-8
# it's a document that provides guidelines and best practices on how to write Python code.
# The primary focus of PEP 8 is to improve the readability and consistency of Python code.

# there are numerous rules and guidelines regarding numerous topics that can be accessed through the website
# for instance, a guideline states that the code lines in python mustn't exceed 72 characters for consistency.
# note: 
# this entire repository of python codes follows convention of 120 characters instead of 72
# most of the pep8 rules have been followed while making these files though 
# -we must refer to the original document for valuable insights

# REFACTORING

# it's a process of optimising the structure of the code (might be to comply with pep8)
# -without affecting its functionality.
# certain IDEs, including intellij, provide features to facilitate this process.
# for eg- following is a code snippet, notice that the var are defined in camel case
# -so using refactoring we will change the var names wrt to pep8

split_string = "this string is \nprinted in \nmore than\n one\nline"
print(split_string) 

tabbed_string = "12345678\t2345678\t345678\t4"
another_tabbed = "helloooo\thellooooo\th"
print(tabbed_string)
print(another_tabbed)

another_string = 'The pet shop owner said, "No, no \'e\'s uhm..., he\'s sleeping"'
print(another_string)

# above snippet has three var with camel case structure, appropriate for java, 
# -this structure is not prescribed for python hence using refactoring:

split_string = "this string is \nprinted in \nmore than\n one\nline"
print(split_string)

tabbed_string = "12345678\t2345678\t345678\t4"
another_tabbed = "helloooo\thellooooo\th"
print(tabbed_string)
print(another_tabbed)

another_string = 'The pet shop owner said, "No, no \'e\'s uhm..., he\'s sleeping"'
print(another_string)

# steps followed (in IntelliJ IDE):
# right-click on the variable in the ide
# select render from the dialog box that appeared
# select rename from the new dialog box that appeared
# rename the variable

# Benefits:
# this will rename the variable everywhere it appeared so, ideal for large files



