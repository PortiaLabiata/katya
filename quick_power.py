
def quick_sqr(x: float, n: int) -> float:
    ''' quick x**n '''
    if n == 0: return 1
    if n % 2 == 0:
        return quick_sqr(x**2, n//2)
    return x * quick_sqr(x, n - 1)

if __name__ == '__main__':
    print(quick_sqr(2, 10))
