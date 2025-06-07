N, K = map(int, input().split())
li = []
for i in range(N):
    li.append(i + 1)

# 제거
removed = []
curr_idx = -1
for _ in range(N):
    curr_idx = (curr_idx + K) % len(li)
    r = li.pop(curr_idx)
    curr_idx -= 1
    removed.append(str(r))

output = "<" + ", ".join(removed) + ">"
print(output)