N = int(input())
a = []
for i in range(0, N):
    a.append(int(input()))

M = int(input())
n = 0
for i in range(0, N):
    if a[i] > a[M]: n += 1
print(n)
