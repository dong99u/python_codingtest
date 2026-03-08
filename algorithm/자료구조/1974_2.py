import sys
input = sys.stdin.readline

n = int(input())

nums = []
for _ in range(n):
    nums.append(int(input()))

j = 0
stack = []
answer = []
valid = True
for i in range(1, n + 1):
    if i <= nums[j]:
        stack.append(i)
        answer.append('+')
    else:
        while nums[j] < i:
            k = stack.pop()
            if k != nums[j]:
                valid = False
                break
            answer.append('-')
            j += 1
        stack.append(i)
        answer.append('+')

        if not valid:
            break

while stack:
    k = stack.pop()
    if k != nums[j]:
        valid = False
        break
    answer.append('-')
    j += 1

if valid:
    for elem in answer:
        print(elem)
else:
    print('NO')
