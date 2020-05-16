def smallest(x, y, z): 
    c = 0
      
    while ( x and y and z ): 
        x = x-1
        y = y-1
        z = z-1
        c = c + 1
  
    return c 
  
x = 12
y = 15
z = 5
print("Minimum of 3 numbers is", smallest(x, y, z)) 