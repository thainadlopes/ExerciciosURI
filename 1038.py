prod = input().split(" ")

cod, qtd = prod

if int(cod) == 1:
    t = int(qtd)*4.00
elif int(cod) == 2:
    t = int(qtd)*4.50
elif int(cod) == 3:
    t = int(qtd)*5.00
elif int(cod) == 4:
    t = int(qtd)*2.00
elif int(cod) == 5:
    t = int(qtd)*1.50

print("Total: R$ %.2f" %t)
