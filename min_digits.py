n = int(input())
digits = []
nzeros = 0
while n > 0:
    if n % 10 == 0:
        nzeros += 1
    else:
        digits.append(n % 10)
    n //= 10
digits.sort()
digits = [digits[0]] + [0]*nzeros + digits[1:]
print(*digits, sep='')
