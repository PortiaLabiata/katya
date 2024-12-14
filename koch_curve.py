import turtle

def f(l, n):
    if n == 1:
        turtle.forward(l)
    else:
        f(l/3, n-1)
        turtle.left(60)
        f(l/3, n-1)
        turtle.right(120)
        f(l/3, n-1)
        turtle.left(60)
        f(l/3, n-1)

turtle.tracer(False)
turtle.goto(-350, 0)
f(700, 6)
turtle.mainloop()
