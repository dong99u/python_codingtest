import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = []

for _ in range(n):
    coins.append(int(input()))

counts = 0

for coin in coins[::-1]:
    while k >= coin:
        counts += k // coin
        k %= coin

print(counts)