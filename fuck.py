from sys import exit
n = int(input())
if n == 0: print('NO'); exit()
if n == 2: print('YES'); exit()
n //= 2
r = n % 2
while not r and n:
    r = n % 2
    n //= 2
if n != 0: print('NO')
else: print('YES')
