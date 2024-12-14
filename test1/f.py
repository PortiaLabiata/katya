from math import inf
n = int(input())
a = []
m = -inf
while n != 0:
    a.append(n)
    m = max(m, n)
    n = int(input())

print(a.count(m))
