import math
coorda = input().split(' ')
coordb = input().split(' ')
coordc = input().split(' ')
skalprab = int(coorda[0])*int(coordb[0]) + int(coorda[1])*int(coordb[1])
skalprac = int(coorda[0])*int(coordc[0]) + int(coorda[1])*int(coordc[1])
skalprcb = int(coordb[0])*int(coordc[0]) + int(coordb[1])*int(coordc[1])
cb = math.sqrt((int(coordc[0])-int(coordb[0]))**2 + (int(coordc[1])-int(coordb[1]))**2)
ac = math.sqrt((int(coordc[0])-int(coorda[0]))**2 + (int(coordc[1])-int(coorda[1]))**2)
ab = math.sqrt((int(coordb[0])-int(coorda[0]))**2 + (int(coordb[1])-int(coorda[1]))**2)
maxstor = max(cb,ab,ac)
if (maxstor==cb):
    cosa=skalprcb/(ab*ac)
elif (maxstor==ab):
    cosa=skalprab/(cb*ac)
else:
    cosa=skalprac/(cb*ab)
if (cosa>0):
    print("ACUTE")
elif (cosa<0):
    print("OBTUSE")
else:
    print("RIGHT")