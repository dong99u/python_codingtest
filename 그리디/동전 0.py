import sys
input = sys.stdin.readline

n, k = map(int, input().split())

coins = []
for _ in range(n):
    coins.append(int(input()))

answer = 0
for coin in coins[::-1]:
    while k >= coin:
        answer += (k // coin)
        k %= coin

print(answer)