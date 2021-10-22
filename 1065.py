c = 0

for i in range(1, 6):
    x = int(input())
    if x % 2 == 0:
        c += 1

print("%d valores pares" %c)