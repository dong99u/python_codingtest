import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

arr.sort(key=lambda x: (x[1], x[0]))

answer = 0
prev_end = -1
for s, e in arr:
    if s >= prev_end:
        answer += 1
        prev_end = e

print(answer)

