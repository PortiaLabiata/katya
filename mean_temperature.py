n = int(input())
m = 0
k = 0

for i in range(1, n+1):
    age, height, weight, temp = [float(i) for i in input().split()]
    if age >= 60 or abs(weight - (height - 100)) > 10:
        k += 1
        m = (m*(k - 1) + temp)/k

print(m)
