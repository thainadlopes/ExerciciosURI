s = 0
i = 0
while i < 2:
    n = float(input())
    if n < 0 or n > 10:
        print("nota invalida")
    if n >= 0 and n <= 10:
        i += 1
        s += n

m = s/2
print("media = %.2f" %m)