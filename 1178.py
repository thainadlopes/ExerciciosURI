x = []
n = float(input())

for i in range(100):
    x = n
    print('N[{}] = {:.4f}'.format(i, x))
    n /= 2

