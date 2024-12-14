def hoar_sort(a, depth=1, part='left'):
    print('depth:', depth, 'part:', part, 'array before:', a)
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
    print('depth:', depth, 'part:', part, 'array after:', a)
