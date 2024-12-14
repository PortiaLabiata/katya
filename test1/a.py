a = int(input())
b = int(input())
c = int(input())
d = int(input())
x = int(input())
f = s = False

if a + x == b: f = True
if c * x == d: s = True

if f and s: print(5)
elif f or s: print(4)
elif x == 1024: print(3)
else: print(2)
