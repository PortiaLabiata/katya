def _merge(l, r, key=lambda x: x):
    i = j = 0
    n, m = len(l), len(r)
    c = [None]*(n + m)
    k = 0
    while i < n or j < m:
        if j == m or (i < n and key(l[i]) <= key(r[j])):
            c[k] = l[i]
            i += 1
            k += 1
        else:
            c[k] = r[j]
            j += 1
            k += 1
    return c

def _mass(molecule):
    weights = {'C': 12, 'H': 1, 'N': 14, 'O': 16}
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    m = 0
    i = 0
    while i < len(molecule):
        atom = molecule[i]
        mul = ''
        i += 1
        while i < len(molecule) and (molecule[i] in digits):
            mul += molecule[i]
            i += 1

        if mul == '':
            mul = '1'
        m += weights[atom]*int(mul)
    return m

def merge_by_molweight(l, r):
    return _merge(l, r, key=_mass)
