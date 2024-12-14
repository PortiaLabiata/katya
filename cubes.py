from sys import exit
from math import copysign
n = int(input())

for a in range(1, n):
    d = copysign((abs(n - a**3))**(1/3), n - a**3)
    if abs(d - round(d, 1)) < 10**-12:
        print(*sorted([a, int(round(d, 1))]))
        exit()

print('impossible')
