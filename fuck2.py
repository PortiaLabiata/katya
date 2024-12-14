from sys import exit
nprev = None
n = int(input())
if not n: print(-1); exit()
nprev = n
n = int(input())
s = 0
while n:
    if nprev % 2 != 0:
        s += n
    nprev = n
    n = int(input())

if not s: print(-1)
else: print(s)

