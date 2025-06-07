c_amt, target = map(int, input().split())
cards = list(map(int, input().split()))

# 역순 정렬 후, target 보다 작을 때까지 가장 큰 합 구함
cards.sort(reverse=True)

def calc_max(cards):
    sum = 0
    for i in range(c_amt):
        for j in range(i + 1, c_amt):
            for k in range(j + 1, c_amt):
                sum_temp = cards[i] + cards[j] + cards[k]
                if sum < sum_temp <= target:    # 기존 값보다 큼
                    sum = sum_temp
    return sum

print(calc_max(cards))