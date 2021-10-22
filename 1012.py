l1 = input().split(" ")

a, b, c = l1
PI = 3.14159

areaT = (float(a)*float(c))/2
areaC = PI*(float(c)*float(c))
areaTrap = ((float(a)+float(b))*float(c))/2
areaQ = float(b)*float(b)
areaR = float(a)*float(b)

print("TRIANGULO: %.3f" %areaT)
print("CIRCULO: %.3f" %areaC)
print("TRAPEZIO: %.3f" %areaTrap)
print("QUADRADO: %.3f" %areaQ)
print("RETANGULO: %.3f" %areaR)
