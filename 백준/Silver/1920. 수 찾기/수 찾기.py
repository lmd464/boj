import sys

N = int(sys.stdin.readline())
A = list(map(int, input().split()))
M = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))


# input 10000 이상이므로 이중 for문은 안된다 (1초에 1억번+)
# 이분탐색(정렬됨) - 재귀 or while(보편적)
# 중간보다 크면 오른쪽탐색, 작으면 왼쪽탐색
A.sort()
for num in nums:
    l, r = 0, len(A) - 1
    mid = 0
    found = False
    # == 는 대상 원소가 1개일 때이므오 필요함 (재귀는 X)
    while (l <= r):
        mid = (l + r) // 2

        if num < A[mid]:
            r = mid - 1
        elif num > A[mid]:
            l = mid + 1
        else:  # 찾음 - 못찾으면 이거 실행 안되고 while 자체에서 벗어남
            found = True
            break

    print(1) if found else print(0)