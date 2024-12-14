n = int(input())
output = []
position = 1

while n > 0:
    output.append(f'{str(n % 10)}*10^{position-1}')
    position += 1
    n //= 10

print(' + '.join(output[::-1]))
