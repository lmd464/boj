nums = []
while True:
    num_temp = input()
    if num_temp == '0':
        break
    nums.append(num_temp)


def is_palindrome(n):
    for i in range(len(n)):
        # 길이가 홀수일 경우, 중앙에 도달 시 알아서 만족
        if i == len(n) - 1 - i:
            return True
        # 비교
        if num[i] != num[len(n) - 1 - i]:
            return False
    return True

for num in nums:
    print("yes") if is_palindrome(num) else print("no")
