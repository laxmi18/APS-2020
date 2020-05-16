def myXOR(x, y): 
	res = 0 
	for i in range(31, -1, -1):  
		b1 = x & (1 << i) 
		b2 = y & (1 << i) 
		b1 = min(b1, 1) 
		b2 = min(b2, 1) 
		xoredBit = 0
		if (b1 & b2): 
			xoredBit = 0
		else: 
			xoredBit = (b1 | b2) 
		res <<= 1; 
		res |= xoredBit 
	return res 

x = 3
y = 5
print("XOR is", myXOR(x, y)) 