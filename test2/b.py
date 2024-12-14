string = input()
digits = ['0', '2', '4', '6', '8']
c = 0
for symbol in string:
    if symbol in digits:
        c += 1
print(c)
