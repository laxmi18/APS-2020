# cook your dish here
try:   
    t = int(input())
    result = []
    for i in range(t):
        nm=input().split()
        n = int(nm[0])
        m = int(nm[1])
        f = list(map(int, input().rstrip().split()))
        p = list(map(int, input().rstrip().split()))
        res = []
        c=0
        flag = []
        for i in range(m):
            flag.append(0)
        for i in range(1,m+1):
            for j in range(n):
                if f[j] == i:
                    c += p[j]
                    flag[i-1]=1
            if c==0 and flag[i-1]==0:
                pass
            else:
                res.append(c)
            c=0
        result.append(min(res))
    for i in range(t):
        print(result[i])
except Exception:
    pass