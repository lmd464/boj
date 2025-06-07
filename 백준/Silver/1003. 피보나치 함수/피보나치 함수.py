T = int(input())

# fib(n)에서의 출력 횟수 C(N) = C(n-1) + C(n-2)
# n = 0 : 0출력 1번, 1출력 0번
# n = 1 : 0출력 0번, 1출력 1번
# n = 2 : (n = 1인 경우) + (n = 0인경우)
count = [[0, 0] * x for x in range(41)]     # 0 <= n <= 40
count[0] = [1, 0]
count[1] = [0, 1]
for _ in range(T):
    N = int(input())
    for i in range(2, N + 1):
        count[i][0] = count[i - 1][0] + count[i - 2][0]
        count[i][1] = count[i - 1][1] + count[i - 2][1]

    print(str(count[N][0]) + " " + str(count[N][1]))
