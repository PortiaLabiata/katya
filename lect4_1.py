import doctest
def euclid(a, b):
    ...

def is_prime(x: int) -> bool:
    '''
    A very inefficient function to determine if number is prime
    '''
    if type(x) is not int or x < 2: return False
    i = 2
    while i < x:
        if x % i == 0: return False
        i += 1
    return True

def is_prime2(x: int) -> bool:
    '''
    Slightly more efficient version of previous function
    >>> [i for i in range(10) if is_prime(i) ]
    [2, 3, 5, 7]
    '''
    if type(x) is not int or x < 2: return False
    i = 2
    while i**2 <= x:
        if x % i == 0: return False
        i += 1
    return True

def append_wrapper(a, b=[]) -> list:
    b.append(a)
    return b

def append_wrapper2(a, b=None) -> list:
    if b is None: b = []
    b.append(a)
    return b

if __name__ == '__main__':
    print(append_wrapper2(1))
    print(append_wrapper2(2, []))
    print(append_wrapper2(3))
