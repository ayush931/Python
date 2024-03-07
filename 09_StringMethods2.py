# Strings are immutable

a = "ayush"
print (a.upper()) # It will convert to Upper Case and will form a new string.

b = "AYUSH"
print (b.lower())

c = "!!!Ayush !!!!!!!!! Aman"
print (c.rstrip('!')) # It will delete all the given item from last
print (c.strip('!')) # It will delete the given item from all over the string.

print (a.replace('ayush', 'Aman')) # It will repalce ayush with Aman.

print (c.split(" ")) # It will form a list from the separated items in the string.

blogHeading = "introduction TO jS"
print (blogHeading.capitalize())

str1 = "Welcome to the Console!!!"
print (len(str1))
print (len(str1.center(50))) # It align the string to the centre

name = "Ayush, Aman, Ankit, Ayush"
print (name.count("Ayush"))

str1 = "Welcome to the Console !!!"
print (str1.endswith("!!!"))

str1 = "Welcome to the Console !!!"
print (str1.endswith("to", 4, 10))

str1 = "He's name is Ayush. He is an Honest man."
print (str1.find("iss")) # In case of non availability, it will show -1.
print (str1.index("is")) # In case of non availability, it will throw an error.

str1 = "WelcomeToTheConsole"
print (str1.isalnum()) # It will show true when the string contains A to Z, a to z, 0 to 9.

str1 = "Welcome"
print (str1.isalpha()) # It will show true when the string contains A to Z, a to z.

str1 = "hello world"
print (str1.islower())

str1 = "We wish you a Merry Christmas \n"
print (str1.isprintable()) # It will give false because '\n' is not printable.

str2 = "     " # Using spacebar
print (str2.isspace())

str1 = "        " # Using tab
print (str1.isspace())

str1 = "World Health Organization"
print (str1.istitle()) # All character must starts with capital letter.

str2 = "To kill a Mocking bird"
print (str2.istitle())

str1 = "Python is a Interpreted Language"
print (str1.startswith("Python"))

str1 = "Python is a Interpreted Language"
print (str1.swapcase())

str1 = "His name is Ayush. Ayush is an honest man."
print (str1.title()) # It will make first word of all letter capital.