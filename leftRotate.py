INT_BITS = 32
def leftRotate(n, d): 
	return (n << d)|(n >> (INT_BITS - d)) 
n = 16
d = 2

print("Left Rotation of",n,"by"
	,d,"is",end=" ") 
print(leftRotate(n, d)) 