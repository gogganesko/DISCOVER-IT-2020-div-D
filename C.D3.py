n = int(input())
list_x = [1]

i = 1
while i != n:
    if(i * 3 <= n):
        i = i * 3
    elif(i * 2 <= n):
        i = i * 2
    else:
        i = i + 1
    list_x.append(int(i))
    
answ = str(len(list_x) - 1) + '\n'
for k in list_x:
    answ = answ + str(k) + ' '

print(answ)

#####

n = int(input())

list_x = [1]

i = 1
z = 0
answ = '1 '
while i != n:
    if(i * 3 <= n):
        i = i * 3
    elif(i * 2 <= n):
        i = i * 2
    else:
        i = i + 1
    list_x.append(int(i))
    z += 1
    answ = answ + str(i) + ' '
answ = str(z) + '\n' + answ 

print(answ)
