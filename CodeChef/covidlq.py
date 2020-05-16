try:
    t=int(input())
    for i in range(t):
        n=int(input())
        a=list(map(int,input().split()))
        l=[]
        for i in range(n):
            if a[i]==1:
                l.append(i)
        f=0
        for i in range(1,len(l)):
            if l[i]-l[i-1]<6:
                f=1
                break
        if f==0:
            print("YES")
        elif f==1:
            print("NO")
except Exception:
    pass