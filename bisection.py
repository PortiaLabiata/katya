def find_root(f, a, b, tol):
    l = a; r = b
    while r - l > tol:
        m = (l + r)/2
        if f(m) <= 0:
            l = m
        else:
            r = m
    return r
