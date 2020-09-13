n = input()

n = int(n) + 1
fib1 = fib2 = 1

i = 0
while i < n - 2:
    fib_sum = fib1 + fib2
    fib1 = fib2
    fib2 = fib_sum
    i = i + 1

d = 10 ** 6 + 3

x = (fib2 % d + d) % d
print(x)