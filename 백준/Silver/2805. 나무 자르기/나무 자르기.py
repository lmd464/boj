N, M = map(int, input().split())
trees = list(map(int, input().split()))
trees.sort()
# 자른 높이 - H가 작을 수록 cut이 커짐
def cut(H):
    res = 0
    for tree in trees:
        if H < tree:
            res += tree - H
    return res

# 나무는 선형탐색(N:100만) - cut(), H는 이분탐색(10억+)
# 어떤 범위를 이분탐색? -> H 범위 : 탐색 범위는 0 ~ 나무최대높이
# 최대 H 찾기 & cut(H) >= M
l, r = 0, trees[-1]
H_res = 0
while l <= r:
    mid = (l + r) // 2
    cut_mid = cut(mid)
    # 충분히 자름 (H가 충분히 작음), 우측 구간에서 더 큰 H(mid) 찾아야함
    if cut_mid >= M:
        l = mid + 1
        H_res = mid
    # 덜 자름, 좌측으로 가야 함
    elif cut_mid < M:
        r = mid - 1
print(H_res)

'''
# 첫번째 풀이 : 시간초과
# 이중 for 불가 
# -> H는 이분탐색으로 바꿔야 함

cut = 0     # 자른 나무 총 길이
complete = False    # 최종 H 결정 여부
res_H = 0   # 최종 H
# H : 나무 최고높이부터 시작, tree는 선형탐색
for H in range(max(trees), -1, -1):
    for idx in range(N):
        if trees[idx] > H:
            trees[idx] -= 1
            cut += 1
        if cut >= M:
            complete = True
            res_H = H
    if complete:
        break
print(res_H)
'''