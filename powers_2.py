n = int(input())
for i in range(1, 15):
    if n == 2**i:
        print('YES')
        break
else:
    print('NO')
