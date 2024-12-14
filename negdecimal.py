n = int(input())
res = 0
position = 0

while n != 0:
    res += (n % 10) * (-10)**position
    n //= 10
    position += 1

print(res)
