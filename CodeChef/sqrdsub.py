# cook your dish here
try:
    t=int(input())
    for i in range(t):
        n=int(input())
        a=list(map(int,input().split()))
        tmp=1 
        c=0
        for i in range(n):
            tmp=1
            for j in range(i,n):
                tmp*=a[j]
                if tmp%2!=0 or tmp%4==0:
                    c+=1 
        print(c)
except Exception:
    pass