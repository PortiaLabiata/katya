from operator import itemgetter

months = {'January':1, 'February':2, 'March':3, 'April':4, 'May':5, 'June':6, 'July':7, 'August':8, 'September':9,
          'October':10, 'November':11, 'December':12}

def selection_sort(a, k=lambda x: x):
    for i in range(0, len(a)):
        f = lambda x: k(a.__getitem__(x))
        amin = min(list(range(i, len(a))), key=f)
        if k(a[amin]) < k(a[i]):
            a[i], a[amin] = a[amin], a[i]

n = int(input())
dates = []
for i in range(0, n):
    s = input().split()
    t = [int(j) for j in s[3].split(':')]
    dates.append((int(s[0]), s[1], int(s[2]), t[0], t[1]))

selection_sort(dates, k=itemgetter(4))
selection_sort(dates, k=itemgetter(3))
selection_sort(dates, k=itemgetter(0))
selection_sort(dates, k=lambda x: months[x[1]])
selection_sort(dates, k=itemgetter(2))

for date in dates:
    s = f'{date[0]} {date[1]} {date[2]} {date[3]}:'
    if date[4] < 10:
        s += '0' + str(date[4])
    else:
        s += str(date[4])
    print(s)
