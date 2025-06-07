N = int(input())
nums = list(map(int, input().split()))

# 중복 제거 후 정렬 (서로 다른 값만 셈 !!)
# 정렬된 값에 순서대로 인덱스를 붙이면, 인덱스가 압축된 값임
s = sorted(set(nums))
d = {}
for idx, val in enumerate(s):
    d[val] = idx    # num 값과 압축값 매핑

li = []
for num in nums:
    li.append(str(d[num]))
print(" ".join(li))