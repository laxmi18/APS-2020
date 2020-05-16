t = int(input())
result = []
i=1
while(t>0):
    n, c=map(int, input().split())
    a = list(map(int, input().rstrip().split()))
    a.sort()
    cnt = 0
    s = 0
    for i in range(n):
        s += a[i]
        if s<=c:
            cnt+=1
    print("Case #",end=i)
    t -=1
    i+=1