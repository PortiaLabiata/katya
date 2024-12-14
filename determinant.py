m = []
n = int(input())
for i in range(0, n):
    m.append([int(i) for i in input().split()])

d = 0
def det(m, n):
    global d
    if n == 1:
        return m[0]
    if n == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]
    m2 = m.copy()
    m2.pop(0)
    for i in range(0, n):
        m3 = m.copy()
        for row in m3:
            del row[i]
        det += (-1)**i*det(m3, n-1)

det(m, n)
print(d)
