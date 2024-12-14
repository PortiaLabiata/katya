def radix_sort(a, n=2):
    MAX_VALUE = max(a)
    l = 0
    b = (1 << n) - 1
    aux = [list() for _ in range(0, 1 << n)]
    while 1 << l < MAX_VALUE:
        for array in aux:
            array.clear()
        for element in a:
            aux[element & (b >> l)].append(element)
            #print(b >> l, bin(element & (b >> l)))
        a.clear()
        for array in aux:
            for i in array:
                a.append(i)
        print(*a)
        b <<= n
        l += n

a = [int(i, 2) for i in input().split()]
radix_sort(a)
