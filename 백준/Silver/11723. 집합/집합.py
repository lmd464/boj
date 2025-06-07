import sys
input = sys.stdin.readline

M = int(input())
set_li = []

for _ in range(M):
    comm = input().strip()

    if comm.startswith("all") or comm.startswith("emp"):
        if comm == "all":
            set_li = [x for x in range(1, 21)]
        elif comm == "empty":
            set_li = []

    else:
        c, x = comm.split()
        x = int(x)
        if c == "add":
            # 중복 X
            if set_li.count(x) == 0:
                set_li.append(x)
        elif c == "remove":
            if set_li.count(x) == 1:
                set_li.remove(x)
        elif c == "check":
            if set_li.count(x) == 1:
                print(1)
            else:
                print(0)
        elif c == "toggle":
            if set_li.count(x) == 1:
                set_li.remove(x)
            else:
                set_li.append(x)








