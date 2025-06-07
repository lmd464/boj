# N 세로, M 가로
N, M = map(int, input().split())

board = []
for _ in range(N):
    board.append(list(input()))

# 비교할 체스판 보드를 만들기 위해 행 제작
white_row = []
black_row = []
for i in range(M):
    if i % 2 == 0:
        white_row.append('W')
        black_row.append('B')
    else:
        white_row.append('B')
        black_row.append('W')

# 행들을 합쳐 완전한 보드 만들기
white_board = []
black_board = []
for i in range(N):
    if i % 2 == 0:
        white_board.append(white_row)
        black_board.append(black_row)
    else:
        white_board.append(black_row)
        black_board.append(white_row)

# 실제 보드와 차이 나는 개수 : 초기값 최대
W_miss = 64
B_miss = 64

# 주어진 타일에서, 완성된 체스보드와 최대한으루 매칭되는 N*M 타일 슬라이싱해가며 찾음
for row in range(N - 8 + 1):
    for col in range(M - 8 + 1):

        # 8*8로 자른 타일 : board[row:row+8][col:col+8] 안됨
        temp_board = [row[col:col+8] for row in board[row:row+8]]

        # 완성된 체스보드와 비교
        W_miss_temp = 0
        B_miss_temp = 0
        for temp_row in range(8):
            for temp_col in range(8):
                # B시작 보드, W시작 보드와 각각 비교
                if temp_board[temp_row][temp_col] != white_board[temp_row][temp_col]:
                    W_miss_temp += 1
                elif temp_board[temp_row][temp_col] != black_board[temp_row][temp_col]:
                    B_miss_temp += 1
        W_miss = min(W_miss_temp, W_miss)
        B_miss = min(B_miss_temp, B_miss)
        
print(min(W_miss, B_miss))