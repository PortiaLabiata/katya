def hoar_sort(a):
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
    hoar_sort(aux1)
    hoar_sort(aux3)
    a[:] = aux1 + aux2 + aux3

n = int(input())
a = [int(i) for i in input().split()]
hoar_sort(a)
a = a[::-1]
print(sum(a[:n//2]) - sum(a[n//2:]))
