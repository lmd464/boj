import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())

visited = set()
def dfs(start):
    stack = [start]
    while stack:
        p = stack.pop()
        if p in visited:
            continue
        visited.add(p)
        for nei in graph[p]:
            if nei not in visited:
                stack.append(nei)


graph = {i + 1: [] for i in range(N)}
for _ in range(M):
    x, y = map(int, input().strip().split())
    graph[x].append(y)
    graph[y].append(x)

# 연결요소 수 == dfs 미방문 개수
count = 0
for node in graph:
    if node not in visited:
        dfs(node)
        count += 1
print(count)
