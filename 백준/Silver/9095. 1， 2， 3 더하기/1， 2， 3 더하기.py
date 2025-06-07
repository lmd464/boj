T = int(input())

dp = [0] * 11   # n = 1 ~ 10, 0은 안씀
dp[1] = 1
dp[2] = 2   # 2, 1+1
dp[3] = 4   # 3, 2+1, 1+2, 1+1+1

# 2xN 타일링과 똑같음. 숫자의 순서를 구별함.
# 1 시작 : 나머지 dp[n-1]
# 2 시작 : 나머지 dp[n-2]
# 3 시작 : 나머지 dp[n-3] ..
# 맨 앞에 1, 2, 3 놓는 경우를 총합 -> dp[n-1] + dp[n-2] + dp[n-3]
for _ in range(T):
    num = int(input())
    for i in range(4, num + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    print(dp[num])