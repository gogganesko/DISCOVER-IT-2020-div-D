import math

data = []
with open("input.txt") as f:
    for line in f:
        data.append([int(x) for x in line.split()])

n = data[0][0]
k = data[0][1]
a = data[1]
b = data[2]

af = a[0]
al = a[len(a) - 1]
a.insert(0, af)
a.append(al)
out = ''

for el in b:
    answ = ''
    l = 0
    r = n + 2
    while (l + 1 < r):
        m = (l + r) / 2
        m = math.floor(m)
        if(len(a) == m):
            break
        if(el > a[m]):
            l = m
        elif(el < a[m]):
            r = m
        else:
            answ = 'YES'
            out = out + 'YES' + '\n'
            break
    if(answ == ''):
        out = out + 'NO' + '\n'

output = open('output.txt', 'w')
output.write(out)
output.close()