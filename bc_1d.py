n = int(input())
k = int(input())
c = []
c.append(1)
for i in range(1,n+1):
    c.append(0)
for i in range(n):
    for j in range(min(i,k),1):
        print(j)
        c[j] += c[j-1]
#        print(c[j])
print(c)