n = int(input())

for i in range(1, n+1):
    x = int(input())
    i = 1
    s = 0
    while i < x:
        if x % i == 0:
            s += i

        i += 1

    if s == x:
        print("%d eh perfeito" %x)
    else:
        print("%d nao eh perfeito" %x)

