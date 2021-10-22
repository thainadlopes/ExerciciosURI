x=[0,0,0,0,0,0,0,0,0,0]
n = int(input())

for i in range(len(x)):
    x[i] = n
    print('N[{}] = {}'.format(i, x[i]))
    n *= 2
