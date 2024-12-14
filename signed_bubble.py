n = int(input())
a = [int(i) for i in input().split()]

for i in range(len(a)):
    for k in range(1, len(a)):
        if a[k] < 0:
            for j in range(k-1, -1, -1):
                if a[j] < 0:
                    break
            if a[k] > a[j]:
                a[k], a[j] = a[j], a[k]
                print(*a)
        else:
            for j in range(k-1, -1, -1):
                if a[j] >= 0:
                    break
            if a[k] < a[j]:
                a[k], a[j] = a[j], a[k]
                print(*a)
