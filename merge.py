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
