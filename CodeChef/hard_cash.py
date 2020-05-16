try:
    t = int(input())
    result=[]
    for i in range(t):
        nk = list(map(int,input().split()))
        n = nk[0]
        k = nk[1]
        a = []
        for j in range(n):
            d = int(input())
            a.append(d)
        r = []
        for j in range(n):
            rem = a[j] % k
            r.append(rem)
        s = sum(r)
        if s<k:
            result.append(s)
        else:
            x = []
            y = r[:]
            c = 0
            while sum(x) < sum(y):
                x.append(r[c])
                y.remove(r[c])
                c += 1
#                print("------")
#                print(sum(x))
#                print(sum(y))
            #print(sum(r[:c]))
            if k == 2:
                p = (sum(r[:c])) - (sum(r[c:]))
#            p = sum(r) - k
            else:
                p = (sum(r[:c])) - (k-((sum(r[c:])%k)))
            result.append(p)
    for i in range(t):
        print(result[i])
                    
except Exception:
    pass 