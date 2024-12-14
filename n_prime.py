def is_prime(x):
    i = 2
    while i**2 <= x:
        if x % i == 0: return False
        i += 1
    return True

n = int(input())
j = 1
k = 2
while j < n:
    k += 1
    if is_prime(k): j += 1

print(k)
