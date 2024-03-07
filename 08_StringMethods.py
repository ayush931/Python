names = "Mango"
print (names [:]) # It will print the complete string.
print (len (names)) # It will print the length of the string.
print (names [0 : 5]) # It will print upto the second last index.

# Result of both print will be same.
print (names [0 : - 3])
print (names [0 : len(names) - 3])

print (names [-3 : -1])

nm = "Ayush"
print (nm [-4 : -2])