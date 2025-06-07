nums = list(map(int, input().split()))
while 0 not in nums:
    diag = nums.pop(nums.index(max(nums)))
    if diag ** 2 == nums[0] ** 2 + nums[1] ** 2:
        print("right")
    else:
        print("wrong")
    nums = list(map(int, input().split()))