#I love democracy!
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

n = int(input())
ks = [int(i) for i in input().split()]
hoar_sort(ks)
l = n // 2 + 1
s = 0
for v in ks[:l]:
    s += (v // 2 + 1)

print(s)
