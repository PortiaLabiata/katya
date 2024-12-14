n = int(input())
res = []

while n > 0:
    k = n % 60
    res.append('<'*(k // 10) + 'v'*(k % 10))
    n //= 60

print('.'.join(res[::-1]))
