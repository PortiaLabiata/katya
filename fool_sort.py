a = [int(i) for i in input().split()]
i = 0
while i < len(a)-1:
    if a[i] > a[i+1]:
        a[i], a[i+1] = a[i+1], a[i]
        i = 0
        print(*a)
        continue
    i += 1
