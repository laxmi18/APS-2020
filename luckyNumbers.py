
def isLucky(n):
    next_pos = n
    if isLucky.counter > n:
        return 1
    if n % isLucky.counter == 0:
        return 0
    next_pos = next_pos - next_pos/isLucky.counter
    isLucky.counter += 1
    return isLucky(next_pos)

isLucky.counter = 2
x=5
if isLucky(x):
    print("Luckynumber")
else:
    print("NotLucky")