INT_BITS = 32
def rightRotate(n, d): 
	return (n >> d)|(n << (INT_BITS - d)) & 0xFFFFFFFF
n = 16
d = 2

print("Right Rotation of",n,"by",d,"is",end=" ") 
print(rightRotate(n, d)) 