def generate(m, done=''):
    if m == 0:
        print(done)
        return
    generate(m-1, done+'0')
    generate(m-1, done+'1')



generate(10)
