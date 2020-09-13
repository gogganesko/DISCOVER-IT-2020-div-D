data = []
with open("input.txt") as f:
    for line in f:
        data.append([int(x) for x in line.split()])

n = data[0][0]
a = data[1]

steps = [1, 2]

dp = []
dp.append(0)

for i in range(1, n+1, 1):
    dp.append(10000000)
    m = 10000000
    
    if(i - 1 >= 0):
        m = min(m, dp[i-1] + a[i-1])
    if(i - 2 >= 0):
        m = min(m, dp[i-2] + a[i-1])
    dp[i] = m

print(dp[n])
