import math as m
def kFactor(n,k):
    a = list()  
    while n % 2 == 0: 
        a.append(2) 
        n = n // 2
    for i in range(3, m.ceil(m.sqrt(n)), 2): 
        while n % i == 0: 
            n = n / i; 
            a.append(i) 
    if n > 2: 
        a.append(n) 
    if len(a) < k: 
        return 0
    return 1
for _ in range(int(input())):
    x,k=map(int,input().split())
    print(kFactor(x,k))