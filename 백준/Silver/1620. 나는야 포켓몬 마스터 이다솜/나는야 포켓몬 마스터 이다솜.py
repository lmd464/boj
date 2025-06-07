N, M = map(int, input().split())
enc = {}
enc_rev = {}
for i in range(1, N + 1):
    inp = input()
    enc[i] = inp
    enc_rev[inp] = i


for _ in range(M):
    i = input()
    if i.isnumeric():
        print(enc[int(i)])
    elif i.isalpha():
        print(enc_rev[i])