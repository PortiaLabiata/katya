def cycle_shift(a, n):
    for i in range(0, n-1):
        a[i], a[i+1] = a[i+1], a[i]

def cycle_shift_M(a, n, m):
    for i in range(0, m):
        cycle_shift(a, n)
