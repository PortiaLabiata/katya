from operator import itemgetter

text = input()
letters = {}
for symbol in text:
    if symbol == ' ':
        continue
    if symbol in letters.keys():
        letters[symbol] += 1
    else:
        letters[symbol] = 1

for letter, count in sorted(letters.items(), key=itemgetter(0)):
    print(letter, count)
