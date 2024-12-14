babel = input().split('.')
res = 0

for position, number in enumerate(babel[::-1]):
    res += (number.count('v') + number.count('<')*10)*60**position

print(res)
