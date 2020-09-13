import math
coorda = input().split(' ')
coordb = input().split(' ')
coordc = input().split(' ')
a = math.sqrt((int(coordc[0])-int(coordb[0]))**2 + (int(coordc[1])-int(coordb[1]))**2)
b = math.sqrt((int(coordc[0])-int(coorda[0]))**2 + (int(coordc[1])-int(coorda[1]))**2)
c = math.sqrt((int(coordb[0])-int(coorda[0]))**2 + (int(coordb[1])-int(coorda[1]))**2)
maxstor = max(a,b,c)
if (maxstor==a):
    cosa=(a**2-(b**2+c**2))/(2*b*c)
    if (cosa>0):
        print("ACUTE")
    elif (cosa<0):
        print("OBTUSE")
    else:
        print("RIGHT")
    break
if (maxstor==b):
    cosa=(a**2+ b**2+ c**2)/(2*a*c)
    if (cosa>0):
        print("ACUTE")
    elif (cosa<0):
        print("OBTUSE")
    else:
        print("RIGHT")
    break
if (maxstor==c):
    cosa=(a**2+ b**2+ c**2)/(2*a*b)
    if (cosa>0):
        print("ACUTE")
    elif (cosa<0):
        print("OBTUSE")
    else:
        print("RIGHT")
    break