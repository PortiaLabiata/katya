def factor(x):
    d = 2
    while x != 1:
        while x % d == 0:
            x = x//d
            print(d)
        d += 1

n = int(input())
factor(n)
