N = int(input())

dp = [-1 for _ in range(N+1)]
if N >= 3:
    dp[3] = 1
if N >= 5:
    dp[5] = 1

# min(dp[i-3]+dp[3], dp[i-5]+dp[5]) (dp[i-x] != -1)
for i in range(6, N+1):
    li = []
    if dp[i-3] != -1:
        li.append(dp[i-3] + dp[3])
    if dp[i-5] != -1:
        li.append(dp[i-5] + dp[5])
    if li:
        dp[i] = min(li)
    else:
        dp[i] = -1
print(dp[N])