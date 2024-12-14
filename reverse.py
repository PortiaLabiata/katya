def reverse_array(arr, n):
    for i in range(0, n//2):
        arr[i], arr[n-i-1] = arr[n-i-1], arr[i]
