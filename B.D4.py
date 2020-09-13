c = list(map(int, input().split(' ')))
X = (c[0] - c[2]) * (c[5] - c[3]) - (c[1] - c[3]) * (c[4] - c[2])
if (X == 0 and (c[0] >= c[2] and c[0] <= c[4]) or (c[0] <= c[2] and c[0] <= c[4])):
	if((c[1] >= c[3] and c[1] <= c[5]) or (c[1] <= c[3] and c[1] >= c[5])):
		print('YES')
	else:
		print('NO')
else:
	print('NO')