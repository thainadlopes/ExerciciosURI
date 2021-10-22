n = float(input())

cem = n/100
cem1 = n%100
cinq = cem1/50
cinq1 = cem1%50
v = cinq1/20
v1 = cinq1%20
dez = v1/10
dez1 = v1%10
c = dez1/5
c1 = dez1%5
d = c1/2
d1 = c1%2

um = d1/1
um1 = d1%1
cinqM = um1/0.50
cinqM1 = um1%0.50
vM = cinqM1/0.25
vM1 = cinqM1%0.25
dezM = vM1/0.10
dezM1 = vM1%0.10
cM = dezM1/0.05
cM1 = dezM1%0.05
umM = cM1/0.01

print("NOTAS:")
print("%d nota(s) de R$ 100.00" %cem)
print("%d nota(s) de R$ 50.00" %cinq)
print("%d nota(s) de R$ 20.00" %v)
print("%d nota(s) de R$ 10.00" %dez)
print("%d nota(s) de R$ 5.00" %c)
print("%d nota(s) de R$ 2.00" %d)

print("MOEDAS:")
print("%d moeda(s) de R$ 1.00" %um)
print("%d moeda(s) de R$ 0.50" %cinqM)
print("%d moeda(s) de R$ 0.25" %vM)
print("%d moeda(s) de R$ 0.10" %dezM)
print("%d moeda(s) de R$ 0.05" %cM)
print("%d moeda(s) de R$ 0.01" %umM)
