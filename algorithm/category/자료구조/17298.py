# import sys
# from collections import deque
#
# input = sys.stdin.readline
#
# n = int(input())
# A = list(maps(int, input().split()))
#
# s = deque()
# answers = [0] * n
#
# for x in range(n - 1, -1, -1):  # 뒤에서부터
#     # 1. 스택 정리: 현재 원소 이하인 것들 제거
#     while s and A[x] >= s[-1]:
#         s.pop()
#
#     # 2. 오큰수 결정
#     if len(s) == 0:
#         answers[x] = -1
#     else:
#         answers[x] = s[-1]
#
#     # 3. 현재 원소를 스택에 추가
#     s.append(A[x])
#
# print(*answers)

import sys
input = sys.stdin.readline

n = int(input())
ans = [0] * n
A = list(map(int, input().split()))
s = []

for i in range(n):
    while s and A[s[-1]] < A[i]:
        ans[s.pop()] = A[i]
    s.append(i)

while s:
    ans[s.pop()] = -1

print(*ans)

