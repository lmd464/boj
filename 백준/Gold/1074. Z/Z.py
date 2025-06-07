N, r, c = map(int, input().split())

# 행렬에 들어갈 숫자를 4진수 변환하면, 깊이별 Z탐색 인덱스와 대응된다.
# 그러니까 좌표 (r, c) 를 깊이별 Z 탐색 순서로 어떻게든 변환하면 된다.
# r, c -> 2진수 변환하고 이진수의 각 자리수를 r, c에서 가져오면
# r, c에 따른 깊이별 탐색 순서가 나옴.
# 행렬순서 -> Z순서로 변환함
z_order = [[0, 1],
           [2, 3]]

# 이진수로 만들고 padding
r_bin = bin(r)[2:]
c_bin = bin(c)[2:]
max_len = max(len(r_bin), len(c_bin))
r_bin = r_bin.zfill(max_len)
c_bin = c_bin.zfill(max_len)

# 이진수 -> Z-order로 변경
converted = []
for i in range(len(r_bin)):
    converted.append(z_order[int(r_bin[i])][int(c_bin[i])])

# Z-order를 그대로 4진수 변환하면 값 나옴
acc = 0
for i in range(len(converted) - 1, -1, -1):
    acc += (4 ** i) * converted[len(converted) - 1 - i]
print(acc)