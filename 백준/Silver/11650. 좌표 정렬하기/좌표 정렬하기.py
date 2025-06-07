import sys

N = int(sys.stdin.readline())
points = []
for _ in range(N):
    points.append(list(map(int, sys.stdin.readline().split())))

points.sort(key=lambda x: (x[0], x[1]))

for point in points:
    print(str(point[0]) + " " + str(point[1]))