maya = input().split()
res = 0

for position, number in enumerate(maya[::-1]):
    if number != '@':
        res += (number.count('.') + number.count('|')*5) * 20**position

print(res)
