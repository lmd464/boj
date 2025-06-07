def dfs(row, col, visited, graph):
    stack = [(row, col)]
    while stack:
        # pop -> visit처리 -> 인접 push
        top = stack.pop()
        if visited[top[0]][top[1]]:
            continue
        visited[top[0]][top[1]] = True
        # 인접 탐색
        for dr, dc in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            nr, nc = top[0] + dr, top[1] + dc
            if 0 <= nr < row_len and 0 <= nc < col_len and ground[nr][nc] == 1:
                stack.append((nr, nc))


T = int(input())
for _ in range(T):
    col_len, row_len, cab_count = map(int, input().split())

    # 격자 밭 구성 후, 좌표에 배추 넣음
    ground = [[0 for _ in range(col_len)] for _ in range(row_len)]
    for _ in range(cab_count):
        x, y = map(int, input().split())
        ground[y][x] = 1

    visited = [[False for _ in range(col_len)] for _ in range(row_len)]
    # 인접 판별
    count = 0
    for r in range(row_len):
        for c in range(col_len):
            if not visited[r][c] and ground[r][c] == 1:
                dfs(r, c, visited, ground)
                count += 1

    print(count)









