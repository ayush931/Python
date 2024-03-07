# In Python everything is an object.

a = 1
b = True    
c = "Ayush" 
d = None    
e = 1.5     
f = complex (8, 2)

# It will show the datatype.

print (type(a))  # Integer
print (type(b))  # Boolean
print (type(c))  # String
print (type(d))  # NoneType
print (type(e))  # Float
print (type(f))  # Complex

a1 = 15
print (a + a1) # It will add a and a1.

# List and Tuple are the collection of items.

list1 = [8, 2.3, [-4, 5], ["apple", "banana"]] # It is mutable (changeable).
print (list1) 

tuple1 = (("Parrot", "Sparrow"), ("Lion", "Tiger")) # It is immutable (not changeable).
print (tuple1)

# Dictionary is a collection of key value pair.

dict1 = {"name": "Ayush", "age": 23, "canVote": True}
print (dict1)