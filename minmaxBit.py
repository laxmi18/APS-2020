def min(x, y): 
    return y ^ ((x ^ y) & -(x < y)) 
def max(x, y): 
    return x ^ ((x ^ y) & -(x < y))  
x = 15
y = 6
print("Minimum of", x, "and", y, "is", end=" ") 
print(min(x, y)) 
print("Maximum of", x, "and", y, "is", end=" ") 
print(max(x, y)) 