import sys
input = sys.stdin.readline
import heapq

N = int(input().strip())
min_pq = []
for _ in range(N):
    x = int(input().strip())
    # 가장 작은 값 출력
    if x == 0:
        if len(min_pq) > 0:
            print(heapq.heappop(min_pq))
        else:   # 비어있으면 0 출력
            print(0)
    else:
        heapq.heappush(min_pq, x)