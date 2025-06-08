nums = map(int, input().split())
res = 0
for num in nums:
    res += (num ** 2)
res = res % 10
print(res)