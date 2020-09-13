n, m = map(int, input().split())
adj = [[0]*n for _ in range(n)]

for it in range(m):
    r, c = map(int, input().split())
    adj[r-1][c-1] = adj[c-1][r-1] = 1

s = ''
for ad in adj:
    for a in ad:
        s = s + str(a) 
    s = s + '\n'
s = s[:-1]
print(s)