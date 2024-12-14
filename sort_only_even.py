from math import inf

def selection_sort(a, k=lambda x: x):
    for i in range(0, len(a)):
        f = lambda x: k(a.__getitem__(x))
        amin = min(list(range(i, len(a))), key=f)
        if k(a[amin]) < k(a[i]) and k(a[amin]) != inf and k(a[i]) != inf:
            a[i], a[amin] = a[amin], a[i]

n = int(input())
a = []
for i in range(0, n):
    a.append(int(input()))
selection_sort(a, k=lambda x: x if x % 2 == 0 else inf)
print(*a)
