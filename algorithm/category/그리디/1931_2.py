import sys
input = sys.stdin.readline

n = int(input())

A = []

for _ in range(n):
    s, e = map(int, input().split())
    A.append((s, e))

A.sort(key=lambda x: (x[1], x[0]))
count = 0
end = -1

for i in range(n):
    if A[i][0] >= end:
        end = A[i][1]
        count += 1

print(count)