# Conversion of one datatype to another is called typecasting.

a = "1"
b = "2"

# a = "1Ayush" It will show error

print (a + b) # It will give 12.
# It will concatenate the string.

print (int(a) + int(b))
# It will convert string into the integer.

string = "15"
number = 7

string_number = int(string) # throw an error if the string is not a valid number.
sum = number + string_number

print ("The sum of both the numbers is: ", sum)

#! Explicit TypeCasting:- We have to change the datatype of the variable.
#! Implicit TypeCasting:- It will automatically convert the datatype of the variable.

c = 1.9
d = 8

print (c + d) # It will automatically convert d from integer to float.