from sys import exit
x = int(input())

i = 2
while i**2 <= x:
    if x % i == 0:
        print(0)
        exit()
    i += 1

print(1)
