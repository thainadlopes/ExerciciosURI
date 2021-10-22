n = int(input())

for i in range(1, n+1):
    x = input().split()
    a, b, c = x
    a = float(a)
    b = float(b)
    c = float(c)

    s = a*2 + b*3 + c*5
    m = s/10
    print("%.1f" %m)