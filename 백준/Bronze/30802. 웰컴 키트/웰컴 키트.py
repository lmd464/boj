import math
# 펜 : N // P, N % P
# 티셔츠 : ceil(size_amt / T) 누적

N = int(input())
size_amt_list = list(map(int, input().split()))
T, P = map(int, input().split())

T_res = 0
for size_amt in size_amt_list:
    T_res += math.ceil(size_amt / T)
P_multi_res = N // P
P_single_res = N % P

print(T_res)
print(str(P_multi_res) + " " + str(P_single_res))