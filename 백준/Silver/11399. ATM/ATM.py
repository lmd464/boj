N = int(input())
P = sorted(list(map(int, input().split())))
s = 0
for i in range(N):
    s += sum(P[:i + 1])
print(s)