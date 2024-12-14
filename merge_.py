def merge(left, right, key=lambda x: x):
    l = r = 0
    n, m = len(left), len(right)
    c = []
    while l < n and r < m:
        if r == m or (l < n and left[l] <= right[r]):
            c.append(left[l])
            l += 1
        else:
            c.append(right[r])
            r += 1
    return c

def merge_sort(a, key=lambda x: x):
    if len(a) == 1:
        return a
    left = a[:len(a)//2]
    right = a[len(a)//2:]
    merge_sort(left, key)
    merge_sort(right, key)
    a[:] = merge(left, right, key)
