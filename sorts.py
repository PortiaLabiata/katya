

def is_sorted(a: list) -> bool:
    for i in range(1, len(a)):
        if a[i] < a[i-1]: return False
    return True

print(is_sorted([1,2,3]))
