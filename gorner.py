from sys import exit
number = input().upper()
base = int(input())
res = 0

for symbol in number:
    if '0' <= symbol <= '9':
        x = ord(symbol) - ord('0')
    elif 'A' <= symbol <= 'Z':
        x = ord(symbol) - ord('A') + 10
    else:
        print(f'Ошибка! Символ {symbol} в системе счисления {base}')
        exit()
    res = res * base + x

print(res)
