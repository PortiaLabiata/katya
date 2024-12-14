from operator import itemgetter
n = int(input())
movies = dict()

for _ in range(0, n):
    vote = input()
    if vote not in movies.keys():
        movies[vote] = 1
    else:
        movies[vote] += 1

ms = sorted(list(movies.items()), key=itemgetter(1), reverse=True)
for i in ms:
    print(*i)
