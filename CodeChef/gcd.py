import math
def simplify(a,b):
    g = math.gcd(a,b)
    return (a//g,b//g)
def farey(n):
    # def gcd(a,b):
    #     while b: a,b = b,a%b
    #     return a
    fs = dict()
    for i in range(2,n+1):
        for i2 in range(2,i+1):
            if i2 < n and i != i2:
                r = simplify(i2,i)
                fs[float(i2)/i] = r
    for i in sorted(fs.keys()):
         print(fs[i])
    #print([fs[k] for k in sorted(fs.keys())])

# Usage:
farey(5)
# => [(1, 5), (1, 4), (1, 3), (2, 5), (1, 2), (3, 5), (2, 3), (3, 4), (4, 5)]
