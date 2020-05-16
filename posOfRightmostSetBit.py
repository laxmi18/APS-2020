import math 

def getFirstSetBitPos(n): 

	return math.log2(n&-n)+1

n = 12
print(int(getFirstSetBitPos(n))) 