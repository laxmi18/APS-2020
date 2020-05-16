def isDivBy9(n): 
    if (n == 0 or n == 9): 
        return True
    if (n < 9): 
        return False
    return isDivBy9((int)(n>>3) - (int)(n&7)) 
for i in range(100): 
    if (isDivBy9(i)): 
        print(i, " ", end ="") 