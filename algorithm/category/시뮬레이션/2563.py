import sys
input = sys.stdin.readline

n = int(input())

board = [[0] * 100 for _ in range(100)]

arr = []
for _ in range(n):
    x1, y1 = map(int, input().split())
    arr.append((x1, y1))

for x1, y1 in arr:
    for i in range(x1, x1 + 10):
        for j in range(y1, y1 + 10):
            board[i][j] += 1

answer = 0
for i in range(100):
    for j in range(100):
        if board[i][j]:
            answer += 1

print(answer)