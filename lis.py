global dp

def forward(arr, n):
    global dp
    if n == 1:
        return 1
    end = 1
    for i in range(1, n):
        res = forward(arr, i)
        if arr[i-1] < arr[n-1] and res+1 > end:
            end = res + 1
    dp = max(dp, end)

    return end

def lis(arr):
    global dp
    n = len(arr)
    dp = 1
    forward(arr, n)
    return dp

if __name__ == '__main__':
    arr = [10, 22, 9, 33, 21, 50, 41, 60]
    n = len(arr)
    print("Length of lis is", lis(arr))
