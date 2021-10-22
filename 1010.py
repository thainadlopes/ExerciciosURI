linha1 = input().split(" ")
linha2 = input().split(" ")

cod, numP, valorU = linha1
cod2, numP2, valorU2 = linha2

total = (int(numP)*float(valorU)) + (int(numP2)*float(valorU2))

print("VALOR A PAGAR: R$ %.2f" %total)
