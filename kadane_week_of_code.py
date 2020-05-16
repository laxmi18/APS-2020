minint = -2147483648 

def kadane(a,n):
    global s,e
    mx = minint
    tmax = 0
    b = 0
    for i in range(len(a)):
        tmax = tmax + a[i]
        if mx < tmax:
            mx = tmax
            s = b
            e = i
        if tmax < 0:
            tmax = 0
            b = i + 1
    return mx
n = int(input())
a = list(map(int, input().rstrip().split()))
print(kadane(a,n))
for i in range(e,s-1,-1):
    a.remove(a[i])
    #print(a)
print(kadane(a,n))