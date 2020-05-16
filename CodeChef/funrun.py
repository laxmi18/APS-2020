try:
    t=int(input())
    for i in range(t):
        n=int(input())
        a=list(map(int,input().split()))
        b=list(map(int,input().split()))
        ma = max(a)
        mb = max(b)
        if ma > mb or mb > ma:
            print("YES")
        else:
            print("NO")
except Exception:
    pass