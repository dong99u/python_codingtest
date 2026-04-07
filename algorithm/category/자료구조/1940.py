import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
nums = sorted(list(map(int, input().split())))

i, j = 0, n - 1
answer = 0
while i < j:
    sum_val = nums[i] + nums[j]

    if sum_val < m:
        i += 1
    elif sum_val > m:
        j -= 1
    else:
        answer += 1
        i += 1
        j -= 1

print(answer)

