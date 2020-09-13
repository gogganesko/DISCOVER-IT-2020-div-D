n = int(input())
d = 10 ** 6 + 3
fac = 1
while n > 1:
    fac *= n
    n -= 1
    x = (fac % d + d) % d
print(x)