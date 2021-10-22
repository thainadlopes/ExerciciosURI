pos = 0
neg = 0
imp = 0
par = 0

for x in range(1, 6):
    a = float(input())

    if a > 0 and a % 2 == 0:
        pos += 1
        par += 1
    if a > 0 and a % 2 != 0:
        pos += 1
        imp += 1

    if a < 0 and a % 2 == 0:
        neg += 1
        par += 1
    if a < 0 and a % 2 != 0:
        neg += 1
        imp += 1

    if a == 0:
        par += 1

print("%d valor(es) par(es)" %par)
print("%d valor(es) impar(es)" %imp)
print("%d valor(es) positivo(s)" %pos)
print("%d valor(es) negativo(s)" %neg)


