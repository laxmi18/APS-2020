CHARBIT = 8; 
SIZE_INT = 8;
def getAbs(n): 
    mask = n >> (SIZE_INT * CHARBIT - 1); 
    return ((n + mask) ^ mask); 
n = -6; 
print("Absolute value of",n,"is",getAbs(n)); 