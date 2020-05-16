t = int(input())
for i in range(t):
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    a = list(map(int,input().rstrip().split()))
    r = []
    for j in range(n):
        rem = a[j] % k
        r.append(rem)
    result = []
    if sum(r) < k:
        result.append(sum(r))
    else:
        x = []
        y = r[:]
        c = 0
        while sum(x) < sum(y):
            x.append(r[c])
            y.remove(r[c])
            c += 1
        if k == 2:
            p = (sum(r[:c])) - (sum(r[c:]))
        else:                               
            p = (sum(r[:c])) - (k-((sum(r[c:])%k)))
        result.append(p)
for i in range(t):
    print(result[i])