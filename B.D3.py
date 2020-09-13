data = []
with open("input.txt") as f:
    for line in f:
        data.append([int(x) for x in line.split()])

n = data[0][0]
m = data[0][1]

mat = []

dp = []
for i in range(1, n+1, 1):
    mat.append(data[i])

for i in range(0, n, 1):
    x = []
    dp.append(x)
    for j in range(0, m, 1):
        dp[i].append(-100000000)

dp[n-1][m-1] = mat[n-1][m-1]
for i in range(n-1, -1, -1):
    for j in range(m-1, -1, -1):
        if(i == n-1 and j == m - 1):
            continue

        if(j+1 <= m-1):
            dp[i][j] = max(dp[i][j], dp[i][j+1] + mat[i][j])
        if(i+1 <= n-1):
            dp[i][j] = max(dp[i][j], dp[i+1][j] + mat[i][j])
        if(i+1 <= n-1 and j+1 <= m-1):
            dp[i][j] = max(dp[i][j], dp[i+1][j+1] + mat[i][j])

print(dp[0][0])