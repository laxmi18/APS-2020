# cook your dish here
try:
    t = int(input())
    result = []
    for i in range(t):
        n, p = map(int,input().split())
        d = list(map(int, input().rstrip().split()))
        r = [p % d[j] for j in range(n)]
        count = 0
        for j in range(n):
            if r[j] == 0:
                count += 1
        if count == n:
            result.append("NO")
        else:
            s = 0
            j = 0
            d.reverse()
            r.reverse()
            ex = [0 for i in range(n)]
            while True:
                if r[j] != 0:
                    s = s + d[j]
                    ex[j] += 1
                j += 1
                if j > (len(r)-1):
                    j = 0
                    #continue
                if s > p:
                    break
            string = "YES"
            ex.reverse()
            for i in range(n):
                string = string + " " + str(ex[i])
            result.append(string)
    for i in range(t):
        print(result[i])
except Exception:
    pass