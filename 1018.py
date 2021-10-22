v = int(input())
print(v)

c = v/100
c1 = v%100
cinq = c1/50
cinq1 = c1%50
v = cinq1/20
v1 = cinq1%20
dez = v1/10
dez1 = v1%10
cinc = dez1/5
cinc1 = dez1%5
d = cinc1/2
d1 = cinc1%2
um = d1/1
um1 = d1%1

print("%d nota(s) de R$ 100,00" %c)
print("%d nota(s) de R$ 50,00" %cinq)
print("%d nota(s) de R$ 20,00" %v)
print("%d nota(s) de R$ 10,00" %dez)
print("%d nota(s) de R$ 5,00" %cinc)
print("%d nota(s) de R$ 2,00" %d)
print("%d nota(s) de R$ 1,00" %um)
      
