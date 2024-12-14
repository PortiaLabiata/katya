a = [int(i) for i in input().split()]
for i in range(1, len(a)):
    j = i
    while j > 0 and a[j] < a[j-1]:
        a[j], a[j-1] = a[j-1], a[j]
        j -= 1
        print(*a)
