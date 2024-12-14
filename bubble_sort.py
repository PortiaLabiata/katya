a = [int(i) for i in input().split()]
for i in range(0, len(a)):
    j = 0
    while j < len(a)-1:
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            print(*a)
        j += 1
