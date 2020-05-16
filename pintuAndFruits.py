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
        for i in range(1,m+1):
            for j in range(n):
                if f[j] == i:
                    c += p[j]
            res.append(c)
            c=0
        for i in reversed(range(m)):
            if res[i] == 0:
                res.remove(res[i])
        result.append(min(res))
    for i in range(t):
        print(result[i])
except Exception:
    pass