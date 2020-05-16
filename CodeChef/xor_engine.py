try:
    def bitset(x):
        y = x ^ (x >> 1); 
        y = y ^ (y >> 2); 
        y = y ^ (y >> 4); 
        y = y ^ (y >> 8); 
        y = y ^ (y >> 16);  
        if (y & 1): 
            return 1; 
        return 0;
    t=int(input())
    for i in range(t):
        n,q=map(int,input().rstrip().split())
        a = list(map(int,input().rstrip().split()))
        odd = 0
        even = 0
        for j in range(n):
            if bitset(a[j]):
                odd +=1
            else:
                even += 1
        for j in range(q):
            p = int(input())
            if (bitset(p)):
                print(odd,even)
            else:
                print(even,odd)
except Exception:
    pass

## Program to find the 
## parity of a given number 
#
### Function to find the parity 
##def findParity(x): 
##	y = x ^ (x >> 1); 
##	y = y ^ (y >> 2); 
##	y = y ^ (y >> 4); 
##	y = y ^ (y >> 8); 
##	y = y ^ (y >> 16); 
##
##	# Rightmost bit of y holds 
##	# the parity value if (y&1) 
##	# is 1 then parity is odd 
##	# else even 
##	if (y & 1): 
##		return 1; 
##	return 0; 
##
### Driver code 
##if(findParity(9) == 0): 
##	print("Even Parity"); 
##else: 
##	print("Odd Parity\n"); 
##
##if(findParity(13) == 0): 
##	print("Even Parity"); 
##else: 
##	print("Odd Parity"); 
##	
### This code is contributed by mits 


# Python3 program to illustrate Compute the 
# parity of a number using XOR 

# Generating the look-up table while 
# pre-processing 
#def P2(n, table): 
#	table.extend([n, n ^ 1, n ^ 1, n]) 
#def P4(n, table): 
#	return (P2(n, table), P2(n ^ 1, table), 
#			P2(n ^ 1, table), P2(n, table)) 
#def P6(n, table): 
#	return (P4(n, table), P4(n ^ 1, table), 
#			P4(n ^ 1, table), P4(n, table)) 
#def LOOK_UP(table): 
#	return (P6(0, table), P6(1, table), 
#			P6(1, table), P6(0, table)) 
#
## LOOK_UP is the macro expansion to 
## generate the table 
#table = [0] * 256
#LOOK_UP(table) 
#
## Function to find the parity 
#def Parity(num) : 
#
#	# Number is considered to be 
#	# of 32 bits 
#	max = 16
#
#	# Dividing the number o 8-bit 
#	# chunks while performing X-OR 
#	while (max >= 8): 
#		num = num ^ (num >> max) 
#		max = max // 2
#
#	# Masking the number with 0xff (11111111) 
#	# to produce valid 8-bit result 
#	return table[num & 0xff] 
#
## Driver code 
#if __name__ =="__main__":
#    result = []
#    t=int(input())
#    for i in range(t):
#        n,q=map(int,input().rstrip().split())
#        a = list(map(int,input().rstrip().split()))
#        for j in range(q):
#            p = int(input())
#            res = [0,0]
#            for k in range(n):
#                #b = p ^ a[k]
#                if Parity(a[k]):
#                    res[0]+=1
#                else:
#                    res[1] +=1
#            result.append(res)
#    for item in result:
#        print(item[0],item[1]) 


# This code is contributed by 
# Shubham Singh(SHUBHAMSINGH10) 
