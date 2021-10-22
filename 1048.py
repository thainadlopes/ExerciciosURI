sal = float(input())

if sal <= 400.00:
    r = sal*0.15
    nsal = sal + r
    p=15

if 400.01 <= sal <= 800.00:
    r = sal*0.12
    nsal = sal + r
    p=12

if 400.01 <= sal <= 800.00:
    r = sal*0.10
    nsal = sal + r
    p=10

if 400.01 <= sal <= 800.00:
    r = sal*0.07
    nsal = sal + r
    p=7

if sal > 2000.00:
    r = sal*0.04
    nsal = sal + r
    p=4

print("Novo salario: %.2f" %nsal)
print("Reajuste ganho: %.2f" %r)
print("Em percentual: %d%%" %p)