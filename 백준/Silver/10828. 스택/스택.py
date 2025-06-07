import sys
input = sys.stdin.readline

N = int(input())
stack = []
for _ in range(N):
    s = input().strip()
    if s.startswith("push"):
        comm, param = s.split()
    else:
        comm = s

    if comm == "push":
        stack.append(param)

    elif comm == "pop":
        if len(stack) > 0:
            print(stack.pop())
        else:
            print(-1)

    elif comm == "size":
        print(len(stack))

    elif comm == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    elif comm == "top":
        if len(stack) > 0:
            print(stack[-1])
        else:
            print(-1)

