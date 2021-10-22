x = input().split()

a, b, c = x

a = float(a)
b = float(b)
c = float(c)

if a == 0.0 or (b ** 2 - 4 * a * c) < 0:
    print('Impossivel calcular')
else:
    d = (b**2 - (4*a*c))
    d1 = d ** (1/2)
    t1 = (- b + d1)/(2*a)
    t2 = (- b - d1)/(2*a)
    print("R1 = %.5f" %t1)
    print("R2 = %.5f" %t2)