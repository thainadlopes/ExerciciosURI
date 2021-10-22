y = 0
s = 0

for x in range(1, 7):
    a = float(input())

    if a > 0:
        y += 1
        s += a

print("%d valores positivos" %y)
m = s/y
print("%.1f" %m)

