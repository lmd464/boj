n, k = map(int, input().split())

# Permutation
P = 1
for i in range(n, n-k, -1):
    P *= i

# Factorial
F = 1
for i in range(k, 0, -1):
    F *= i

print(int(P / F))