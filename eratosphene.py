def eratosphene(N):
    a = [True] * N
    a[0] = a[1] = False
    i = 2
    while i**2 <= N:
        if not a[i]:
            i += 1
            continue
        for j in range(i**2, N, i):
            a[j] = False
        i += 1
    res = [i for i in range(N) if a[i]]
    return res

print(eratosphene(10))
