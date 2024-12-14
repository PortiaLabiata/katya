n = int(input())
a = [True for i in range(0, n+1)]
a[0] = a[1] = False

for i in range(2, n+1):
    if not a[i]: continue
    for j in range(i+i, n+1, i):
        if i != j: a[j] = False
res = [i for i in range(0, n+1) if a[i]]
print(' '.join([str(i) for i in res]))
