def selection_sort(a, k=lambda x: x):
    for i in range(0, len(a)):
        f = lambda x: k(a.__getitem__(x))
        amin = min(list(range(i, len(a))), key=f)
        if k(a[amin]) < k(a[i]):
            a[i], a[amin] = a[amin], a[i]

def sum_of_digits(n):
    i = 0
    s = 0
    while 10**i <= n:
        s += n % 10
        n //= 10
    return s

n = int(input())
a = []
for i in range(0, n):
    a.append(int(input()))
selection_sort(a)
selection_sort(a, sum_of_digits)
print(*a, sep='\n')
