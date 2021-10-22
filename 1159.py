x = 1000

while x != 0:
    x = int(input())
    s = 0
    i = 1
    if x != 0:
        while i <= 5:
            if x % 2 == 0:
                s += x
                x += 1
                i += 1
            else:
                x += 1
        print(s)

    elif x == 0:
        break




