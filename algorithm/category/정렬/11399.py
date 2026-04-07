import sys
input = sys.stdin.readline

n = int(input())

A = list(map(int, input().split()))

for i in range(1, n):
    val = A[i]
    j = i - 1

    while j >= 0 and A[j] >= val:
        A[j + 1] = A[j]
        j -= 1

    A[j + 1] = val

S = [0] * n
S[0] = A[0]

for i in range(1, n):
    S[i] = S[i - 1] + A[i]

print(sum(S))