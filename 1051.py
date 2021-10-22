v = float(input())

if v <= 2000.00:
    imp=0
    print("Isento")
if 2000.01 <= v <= 3000.00:
    r8 = v - 2000.00
    imp = r8 * 0.08

if 3000.01 <= v <= 4500.00:
    imp8 = 0.08 * 1000.00
    r18 = v - 3000.00
    imp = r18 * (18 / 100) + imp8

if v > 4500.00:
    imp8 = 0.08 * 1000.00
    imp18 = 0.18 * 1500.00
    r28 = v - 4500.00
    imp = imp18 + imp8 + r28 * 0.28

if v > 2000.00:
    imp = float(imp)
    print('R$ {:.2f}'.format(imp))

