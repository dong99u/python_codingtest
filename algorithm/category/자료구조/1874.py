from collections import deque

n = int(input())

s = deque()
nums = [] # 맞춰야할 수열

for _ in range(n):
    nums.append(int(input()))

answer = []

pointer = 0

for i in range(1, n + 1):
    s.append(i)
    answer.append('+')
    while pointer < n and len(s) != 0 and nums[pointer] == s[-1]:
        s.pop()
        answer.append('-')
        pointer += 1

if len(s) == 0:
    for num in answer:
        print(num)

else:
    print('NO')