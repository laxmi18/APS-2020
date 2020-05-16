#!/bin/python3

import os
import sys

#
# Complete the primeCount function below.
#
def primeCount(n):
    prime = [0] * (n + 1); 
    i = 2; 
    
    c = set
    c.
    while (i * i <= n):  
        if (prime[i] > 0): 
            for j in range(2 * i, n + 1, i): 
                prime[j] += 1; 
        i += 1; 
  
        prime[i] = 1; 
#    print(prime)
    return max(prime); 

if __name__ == '__main__':
 #   fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        result = primeCount(n)
        print(result)

 #       fptr.write(str(result) + '\n')

#    fptr.close()
