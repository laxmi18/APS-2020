n = int(input())
k = int(input())
c = [[]]
for i in range(n):
    for j in range(min(i,k)):
        if j == 0 or i == j:
            c[i][j] = 1
        else:
            c[i][j] = c[i-1][j-1] + c[i-1][j]
print(c[n][k])