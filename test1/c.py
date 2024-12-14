n = int(input())

print('#'*(12*n+1+n))
for i in range(1, n+1):
    print('# ', end='')
    for j in range(1, n+1):
        if i * j < 10: k = f'0{i*j}'
        else: k = f'{i*j}'
        print(f'{i} x {j} = {k}', end='')
        if j < n: print(' | ', end='')
    print(' #')
print('#'*(12*n+1+n))

