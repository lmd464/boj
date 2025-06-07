num = int(input())
'''
DP(Bottom up) : 1부터 올라감
dp[i : 3배수] = dp[i // 3] + 1
dp[i : 2배수] = dp[i // 2] + 1
dp[i] = dp[i - 1] + 1
dp[0], dp[1] = 0
dp[2], dp[3] = 1

초기값에서 거슬러 올라가며 배열에 각각 저장하고 이를
이용하여 다음 값을 구함
1을 빼는 경우는 조건이 없으므로 항상 수행 하고,
2배수, 3배수인 경우엔 비교하여 더 작은 쪽을 저장함.
'''

dp = [0, 0, 1, 1]   # dp[0 ~ 3] : 미리 저장
for i in range(4, num + 1):
    dp.append(dp[i - 1] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)

print(dp[num])