import sys 
def isKthBitSet(x, k): 
	if ((x & (1 << (k - 1))) !=0): 
		return True
	else: 
		return False
def isPalindrome(x): 
	l = 1 
	r = 2 * 8 
	while (l < r): 
		if (isKthBitSet(x, l) != isKthBitSet(x, r)): 
			return False
		l += 1
		r -= 1
	
	return True

if __name__ =='__main__': 
	x = 1 << 15 + 1 << 16
	print(int(isPalindrome(x))) 
	x = 1 << 31 + 1
	print(int(isPalindrome(x))) 