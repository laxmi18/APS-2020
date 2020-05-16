
def nextSparse(x): 
	
	bin = [] 
	while (x != 0): 
		bin.append(x & 1) 
		x >>= 1

	bin.append(0) 
	n = len(bin) 
	last_final = 0

	for i in range(1,n - 1): 
 
		if ((bin[i] == 1 and bin[i - 1] == 1
			and bin[i + 1] != 1)): 
				
			# Make the next bit 1 
			bin[i + 1] = 1

			for j in range(i,last_final-1,-1): 
				bin[j] = 0
			
			last_final = i + 1

	ans = 0
	for i in range(n): 
		ans += bin[i] * (1 << i) 
	return ans 
if __name__=='__main__': 
	x = 38
	print("Next Sparse Number is",nextSparse(x)) 
