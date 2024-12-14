from sys import exit

def hoar_sort(a, depth=1, part='left'):
    if len(a) == 1 or len(a) == 0:
        return
    barrier = a[0]
    aux1, aux2, aux3 = [], [], []
    for v in a:
        if v < barrier:
            aux1.append(v)
        elif v > barrier:
            aux3.append(v)
        else:
            aux2.append(v)
    hoar_sort(aux1, depth+1, 'left')
    hoar_sort(aux3, depth+1, 'right')
    a[:] = aux1 + aux2 + aux3

n, m = [int(i) for i in input().split()]
x = [int(i) for i in input().split()]
y = [int(i) for i in input().split()]

hoar_sort(x)
hoar_sort(y)
i = j = 0
while i < n - 1:
    if x[i] == x[i+1]:
        x.pop(i+1)
        n -= 1
    else:
        i += 1

while j < m - 1:
    if y[j] == y[j+1]:
        y.pop(j+1)
        m -= 1
    else:
        j += 1

if m != n:
    print('No')
    exit()
for i in range(0, m):
    if x[i] != y[i]:
        print('No')
        break
else:
    print('Yes')
