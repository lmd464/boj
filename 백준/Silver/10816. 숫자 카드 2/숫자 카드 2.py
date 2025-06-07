N = input()
cards = list(map(int, input().split()))

M = input()
nums = list(map(int, input().split()))


# 모든 카드 순차 탐색하며 개수를 dict에 저장
count = {}
for card in cards:
    if card in count:
        count[card] += 1
    else:
        count[card] = 1

printlist = []
for num in nums:
    if num in count:
        printlist.append(str(count[num]))
    else:
        printlist.append(str(0))
print(" ".join(printlist))
