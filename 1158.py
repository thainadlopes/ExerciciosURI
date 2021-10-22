n = int(input())

for i in range(1, n+1):
    v = input().split()
    x, y = v
    x = int(x)
    y = int(y)
    s = 0
    j = 1
    while j <= y:
        if x % 2 != 0:
            s += x
            x += 1
            j += 1

        if x % 2 == 0:
            x += 1
    print(s)



