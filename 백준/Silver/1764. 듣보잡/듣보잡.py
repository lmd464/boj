import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
dd = {}
bd = {}
for _ in range(N):
    dd[input().strip()] = 1    # 중복 없음
for _ in range(M):
    bd[input().strip()] = 1

# dd, bd 모두 길이가 50만까지 가능 -> for 중첩 불가
# 하나를 해시맵으로 하고, 개수 일치 확인 -> 존재여부 판단 시, O(N)이 아니라 O(1)
# -> O(N) * O(1)
ddbd = []
for d in dd:
    if bd.get(d, 0) == 1:   # 없으면 0 저장
        ddbd.append(d)
ddbd.sort()
print(len(ddbd))
for out in ddbd:
    print(out)