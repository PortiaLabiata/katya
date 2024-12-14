def cycle_shift(a, n):
    for _ in range(0, n):
        for i in range(0, len(a)-1):
            a[i], a[i+1] = a[i+1], a[i]

def cycle_shift_M(a, n, m):
    for i in range(0, m):
        cycle_shift(a, n)
a = [1, 2, 3, 4]
cycle_shift(a, 1)
print(a)
