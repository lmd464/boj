from collections import deque

com_amt = int(input())
conn_amt = int(input())
graph = {i: [] for i in range(1, com_amt + 1)}
for conn in range(conn_amt):
    temp = list(map(int, input().split()))
    graph[temp[0]].append(temp[1])
    graph[temp[1]].append(temp[0])

queue = deque()
visited = []
def bfs(start):
    queue.append(start)
    while queue:
        node = queue.popleft()
        if node in visited:
            continue
        visited.append(node)
        #print(node)
        for n in graph.get(node):
            queue.append(n)

bfs(1)
print(len(visited) - 1)