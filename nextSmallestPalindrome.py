
def generateNextPalindromeUtil (num, n) : 

	mid = int(n/2 ) 

	leftsmaller = False

	i = mid - 1

	j = mid + 1 if (n % 2) else mid 
 
	while (i >= 0 and num[i] == num[j]) : 
		i-=1
		j+=1
	if ( i < 0 or num[i] < num[j]): 
		leftsmaller = True
	while (i >= 0) : 
	
		num[j] = num[i] 
		j+=1
		i-=1
	if (leftsmaller == True) : 
	
		carry = 1
		i = mid - 1
		if (n%2 == 1) : 
		
			num[mid] += carry 
			carry = int(num[mid] / 10 ) 
			num[mid] %= 10
			j = mid + 1
		
		else: 
			j = mid  
		while (i >= 0) : 
		
			num[i] += carry 
			carry = num[i] / 10
			num[i] %= 10
			num[j] = num[i] # copy mirror to right 
			j+=1
			i-=1
def generateNextPalindrome(num, n ) : 

	print("\nNext palindrome is:") 
	if( AreAll9s( num, n ) == True) : 
	
		print( "1") 
		for i in range(1, n): 
			print( "0" ) 
		print( "1") 
	else: 
	
		generateNextPalindromeUtil ( num, n ) 
		printArray (num, n) 
def AreAll9s(num, n ): 
	for i in range(1, n): 
		if( num[i] != 9 ) : 
			return 0
	return 1 
def printArray(arr, n): 

	for i in range(0, n): 
		print(int(arr[i]),end=" ") 
	print() 
if __name__ == "__main__": 
	num = [9, 4, 1, 8, 7, 9, 7, 8, 3, 2, 2] 
	n = len(num) 
	generateNextPalindrome( num, n ) 