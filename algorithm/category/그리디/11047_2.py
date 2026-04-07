import sys
input = sys.stdin.readline

n, k = map(int, input().split())

coins = []
for _ in range(n):
    coins.append(int(input()))

answer = 0
for coin in reversed(coins):
    if coin > k:
        continue
    answer += k // coin
    k %= coin

print(answer)
