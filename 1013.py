import math

valor = input().split(" ")

a, b, c = valor

maiorAB = (int(a)+int(b)+abs(int(a)-int(b)))/2

maiorABC = (int(maiorAB)+int(c)+abs(int(maiorAB)-int(c)))/2

print("%d eh o maior" %maiorABC)
