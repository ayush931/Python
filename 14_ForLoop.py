name = "Ayush"
for char in name:
    print (char)
    if (char == "y"):
        print ("This is something special")
        
colors = ["Red", "Green", "Blue", "Yellow"]
for color in colors:
    print (color)
    for i in color:
        print (i)
        
# Range

for k in range(2001): # Print from 0 to n-1 (2000)
    print (k)
    
for l in range (2001):
    print (l + 1)
    
for k in range (1, 9):
    print (k) # Print from 1 to 8
    
for k in range (1, 12, 3): # Last range will give the gap between the series.
    print (k)