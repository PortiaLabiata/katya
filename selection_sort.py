a = [int(i) for i in input().split()]
for i in range(0, len(a)):
    amin = min(list(range(i, len(a))), key=a.__getitem__)
    if a[amin] < a[i]:
         a[i], a[amin] = a[amin], a[i]
         print(*a)
