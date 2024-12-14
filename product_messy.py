string = input()
product = 1
current = []
processing_number = False
order = 1

for symbol in string:
    if symbol.isnumeric():
        processing_number = True
        current.append(int(symbol))
    elif processing_number:
        processing_number = False
        product *= sum([current[len(current)-i-1]*10**i for i in range(0, len(current))])
        current = []

if current != []:
    product *= sum([current[len(current)-i-1]*10**i for i in range(0, len(current))])
print(product)
