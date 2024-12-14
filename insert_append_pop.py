x = []
for i in range(0, 100000):
    x.insert(0, i)

while len(x) != 0:
    x.pop()
