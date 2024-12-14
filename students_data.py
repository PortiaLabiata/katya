from operator import itemgetter

n = int(input())
database = dict.fromkeys(list(range(0, n)), None)
for key in database:
    database[key] = []
entry = input()
while entry != '#':
    id_s, result = [int(i) for i in entry.split()]
    database[id_s].append(result)
    entry = input()

for key in database:
    database[key].sort(reverse=True)

res = sorted(database.items(), key=itemgetter(0))
res.sort(key=lambda x: sum(x[1]), reverse=True)
for i in range(0, len(res)):
    print(*res[i][1], end=' ')
