try:
    t=int(input())
    for i in range(t):
        n=int(input())
        p=list(map(int,input().split()))
        p.sort()
        p.reverse()
        s=0
        i=0
        while len(p)>0:
            a=p[0]-i
            if a>0:
                s+=a
            p.remove(p[0])
            i+=1
        print(s)
except Exception:
    pass