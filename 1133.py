x = int(input())
y = int(input())

while (x < y):
    x += 1
    if (x % 5 == 2 or x % 5 == 3 and x != y):
        print(x)
