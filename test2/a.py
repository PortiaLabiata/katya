string = input()
sub = []
flag = False
for symbol in string:
    if flag:
        sub.append(symbol)
    if symbol == '\"':
        flag = not flag
print(*sub[:-1], sep='')
