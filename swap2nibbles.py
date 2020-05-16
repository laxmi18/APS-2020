def swapNibbles(x): 
	return ( (x & 0x0F)<<4 | (x & 0xF0)>>4 ) 
x = 100
print(swapNibbles(x)) 