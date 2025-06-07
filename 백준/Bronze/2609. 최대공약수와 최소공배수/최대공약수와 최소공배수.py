a, b = map(int, input().split())

# 유클리드 호제법(a>b) : gcd(a,b) = gcd(b,r) 반복, 한쪽이 0이 되면 다른쪽이 gcd
# 최소공배수(LCM) : a * b == gcd * lcm

def gcd(a, b):
    # a > b 맞춰줌
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return a * b // gcd(a, b)

print(gcd(a, b))
print(lcm(a, b))