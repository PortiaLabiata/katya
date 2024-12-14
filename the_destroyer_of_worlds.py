n = int(input())

if n == 1:
    print(2)
    exit(0)

counter = [[[ 0 for _ in range(2)] for _ in range(2)] for _ in range(n + 1)]
counter[2][0][0], counter[2][1][0], counter[2][0][1], counter[2][1][1] = 1, 1, 1, 1

for i in range(3, n + 1):
    counter[i][0][0] = counter[i - 1][0][0] + counter[i - 1][1][0]
    counter[i][0][1] = counter[i - 1][0][0] + counter[i - 1][1][0]
    counter[i][1][0] = counter[i - 1][0][1] + counter[i - 1][1][1]
    counter[i][1][1] = counter[i - 1][0][1]

print(counter[n][0][0] +
      counter[n][1][0] +
      counter[n][0][1] +
      counter[n][1][1])
