a = [int(i,2) for i in input().split()]
m = max(a)
i = 0
aux = [list() for _ in range(0, 2)]
while 1 << i <= m:
    for array in aux:
        array.clear()
    for element in a:
        aux[(element & (1 << i)) >> i].append(element)
    a.clear()
    for array in aux:
        for element in array:
            a.append(element)
    print(*[bin(k)[2:] for k in a])
    i += 1
