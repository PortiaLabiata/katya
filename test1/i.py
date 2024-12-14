n = int(input())
m = []
for i in range(0, n):
    m.append(input().split())

for i in range(0, n):
    for j in range(0,n):
        print(m[j][i], end=' ')
    print()
