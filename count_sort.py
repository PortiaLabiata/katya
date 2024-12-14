a = [int(i) for i in input().split()]
aux = [0 for i in range(0, max(a)+1)]
for i in a:
    aux[i] += 1
    print(*aux)

for i in range(0, len(aux)):
    print((f'{i} '*aux[i]), end='')

