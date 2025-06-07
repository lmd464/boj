T = int(input())

# 가장 최근에 연 괄호는 가장 먼저 닫혀야 함 -> 스택
for _ in range(T):
    ps = list(input())
    stack = []
    is_vps = False
    for p in ps:
        if len(stack) !=0 and stack[-1] == "(" and p == ")":
            stack.pop()
        else:
            stack.append(p)
    if len(stack) == 0:
        is_vps = True

    print("YES") if is_vps else print("NO")