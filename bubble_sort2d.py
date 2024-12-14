def print_array(a, n, m):
    for i in range(n):
        for j in range(m):
            print(a[i][j], end = ' ')
        print()
    print()

def bubble_sort2d(a, n, m):
    print_array(a, n, m)
    for k in range(0, n*m):
        for i in range(0, n):
            for j in range(0, m-1):
                if a[i][j] > a[i][j+1]:
                    a[i][j], a[i][j+1] = a[i][j+1], a[i][j]
                    print_array(a, n, m)
            if i < n-1:
                if a[i][m-1] > a[i+1][0]:
                    a[i][m-1], a[i+1][0] = a[i+1][0], a[i][m-1]
                    print_array(a, n, m)
