input()
nums = list(map(int, input().split()))

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

prime_cnt = 0
for num in nums:
    if is_prime(num):
        prime_cnt += 1

print(prime_cnt)