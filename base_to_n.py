x = int(input())
n = int(input())
res = ''

while x != 0:
    res += str(x % n)
    x //= n

print(res[::-1])
