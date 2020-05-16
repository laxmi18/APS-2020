# def CountPair(L,R):
#     x=(R-L+1)
#     print(x//2)
# if __name__=='__main__':
#     L,R=1,10
#     CountPair(L,R)
import math
#lambda c:[i for i in range(c)if math.gcd(c,i)<2]
# n=int(input())
# l=set()
# for i in range(2,n+1):
#     for j in range(i+1,n+1):
#         a=set()
#         if math.gcd(i,j)<2:
#             a.add(i)
#             a.add(j)
#         l.add(a)
    
# print(l)
# def coprime(A,B):
#     return len([(x,y) for x in range(1,A+1) for y in range(x+1,B+1) if math.gcd(x,y) == 1])
# print(coprime(1,5))
# from collections import deque

# def coprimes():
#     tree = deque([[2, 1], [3, 1]])
#     while True:
#         m, n = tree.popleft()
#         yield m, n
#         tree.append([2 * m - n, m])
#         tree.append([2 * m + n, m])
#         tree.append([m + 2 * n, n])
#     print(tree)
# coprimes()
from gmpy2 import lcm
from itertools import combinations
 
for a, b in combinations(range(2, 101), 2):
	if lcm(a, b)==a*b:
		print('({}, {}), '.format(a,b), end=' ')