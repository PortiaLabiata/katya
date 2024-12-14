def merge(l, r):
    i = j = 0
    n, m = len(l), len(r)
    c = [None]*(n + m)
    k = 0
    while i < n or j < m:
        if j == m or (i < n and l[i] < r[j]):
            c[k] = l[i]
            i += 1
            k += 1
        else:
            c[k] = r[j]
            j += 1
            k += 1
    return c

def merge_sort(a, depth=1, part='left'):
    print('depth:', depth, '|', 'part:', part, '|', 'array:', a)
    if len(a) == 1:
        return
    left = a[:len(a)//2]
    right = a[len(a)//2:]
    merge_sort(left, depth+1, 'left')
    merge_sort(right, depth+1, 'right')
    a[:] = merge(left, right)
    print('depth:', depth, '|', 'part:', part, '|', 'after merge:', a)
