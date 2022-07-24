# \ is the escape character which exhibit special meaning when used with another character.
str1 = "this string is \nprinted in \nmore than\n one\nline"   # \n--> brings the cursor to new line
print(str1)

str2_1 = "12345678\t2345678\t345678\t4"   # \t--> brings a fixed whitespace between text
str2_2 = "helloooo\thellooooo\th"    # \t provides fixed space between the first char of string and the string after it
# -if the no. of char increases more than no. of spaces then space is counted from next char
# -at position= old_char_position + space
print(str2_1)
print(str2_2)

str3 = 'The pet shop owner said, "No, no \'e\'s uhm..., he\'s sleeping"'
# \' to esc single quote in a string enclosed by ''
print(str3)

str4 = "The pet shop owner said, \"No, no 'e's uhm..., he's sleeping\""
# \" to esc double quote in a string enclosed by ""
print(str4)

# using triple quotes to enclose string is a better alternative of above two cases
# -it avoids escape char and improves readability of string
str5 = """The pet shop owner said, "No, no 'e's uhm..., he's sleeping" """   # notice that no escape char is required
print(str5)

str6 = """this
line has been
split over multiple
lines"""   # triple quotes allows this
print(str6)
str6_1 = """this \
line has been \
split over multiple \
lines but fixed"""   # esc char esc the end of line combining the parts of string
# -it essentially helps in avoiding the use of \ with ' or " and supports readability
print(str6_1)

str7 = "C:\\user\\timmy\\notes.txt"   # here \helps esc \ itself
print(str7)
# un-preferable alternative to inc \ in sentence
str7 = r"C:\user\timmy\notes.txt"
print(str7)

