import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
N_nums = list(map(int, input().strip().split()))
# N, M : 10만 -> O(N^2) 불가

sum_prev = [0] * (N + 1)    # 누적합 배열
sum_prev[0] = 0             # 0번 인덱스 안씀
for i in range(1, N + 1):  # s[1] ~ s[n]까지 누적합을 sum[n]에 저장
    #sum_prev[i] = sum(N_nums[:i])
    sum_prev[i] = N_nums[i - 1] + sum_prev[i - 1]   # 이전항까지의 누적합 + 현재합

for _ in range(M):
    i, j = map(int, input().strip().split())
    res = sum_prev[j] - sum_prev[i - 1]     # j까지의 함에서, i-1 까지의 합 구함
    print(res)

