x = int(input())

for i in range(1, x+1):
    n = int(input())

    s = 0
    j = 1
    while j <= n:
        if n % j == 0:
            s += 1
        j += 1
    if s > 2:
        print('{} nao eh primo'.format(n))
    else:
        print('{} eh primo'.format(n))

