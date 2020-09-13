string = input()

str_ar = string.split(' ')

a = int(str_ar[0])
b = int(str_ar[1])

c = a * a - b * b
d = 10 ** 6 + 7

x = (c % d + d) % d
print(x)