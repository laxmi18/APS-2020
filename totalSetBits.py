def countSetBits(n): 
    bitCount = 0 
  
    for i in range(1, n + 1): 
        bitCount += countSetBitsUtil(i) 
  
    return bitCount 
def countSetBitsUtil(x): 
  
    if (x <= 0): 
        return 0
    return (0 if int(x % 2) == 0 else 1) +  countSetBitsUtil(int(x / 2)) 
if __name__=='__main__':  
    n = 4
    print("Total set bit count is", countSetBits(n))