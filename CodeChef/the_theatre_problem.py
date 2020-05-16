try:
    t = int(input())
    result = []
    cost = [100,75,50,25]
    movie = ['A', 'B', 'C', 'D']
    time = ['12', '3', '6', '9']
    for i in range(t):
        n = int(input())
        if n == 0:
            result.append(-400)
        else:
            request = []
            for j in range(n):
                request.append(list(input().split()))
            m = [[0, 0, 0, 0],
                 [0, 0, 0, 0],
                 [0, 0, 0, 0],
                 [0, 0, 0, 0]]
            for item in request:
                for i in range(4):
                    for j in range(4):
                        if item[0] == movie[i] and item[1] == time[j]:
                            m[i][j] += 1
            row_count = [0,0,0,0]
#        col_count = [0,0,0,0]
#        for i in range(4):
#            for j in range(4):
#                if m[i][j] == 0:
#                    row_count[i] += 1
#                    col_count[j] += 1
#        print(row_count)
#        print(col_count)
            f = []
            while len(f) < 4:
                pre = m[0][0]
                col_count = [0,0,0,0]
                for i in range(4):
                    for j in range(4):
                        if m[i][j] == 0:
                        #row_count[i] += 1
                            col_count[j] += 1
#            print(col_count)
                x = 0
                y = 0
                for i in range(4):
                    for j in range(4):
                        if m[i][j] > pre:
                            pre = m[i][j]
                            x = i
                            y = j
                for j in range(4):
                    if j != y and m[x][j] != 0 and col_count[j] == 3:
                        pre = m[x][j]
                        y = j
                f.append(pre)
                for i in range(4):
                    m[i][y] = 0
                    for j in range(4):
                        m[x][j] = 0
#            print(m)
            
#        print(f)
            res = 0
            for i in range(4):
                if f[i] == 0:
                    res = res - 100
                else:
                    res = res + (cost[i]*f[i])
            result.append(res)
    for i in range(t):
        print(result[i])
    print(sum(result))
        
except Exception:
    pass