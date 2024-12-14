p = int(input())
a = 2

if (a**(p-1) - 1) % p == 0 or p == 2:
    print('YES')
else:
    print('NO')
