maior = 0
for i in range(1, 101):
    x = int(input())

    if x > maior:
        maior = x
        pos = i

print(maior)
print(pos)