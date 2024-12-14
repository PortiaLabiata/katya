def split_barrier(a, barrier):
    aux1, aux2, aux3 = [], [], []
    for v in a:
        if v < barrier:
            aux1.append(v)
        elif v > barrier:
            aux3.append(v)
        else:
            aux2.append(v)
    a[:] = aux1 + aux2 + aux3
