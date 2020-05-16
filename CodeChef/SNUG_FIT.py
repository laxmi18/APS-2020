try:
    t = int(input())
    d = []
    for i in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        a.sort()
        b.sort()
        c = 0
        for j in range(n):
            c = c + min(a[j],b[j])
        d.append(c)
    for i in range(len(d)):
        print(d[i])
except Exception:
    pass