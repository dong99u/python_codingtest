import sys

input = sys.stdin.readline

n = int(input())
nums = sorted(list(map(int, input().split())))

answer = 0

for k in range(n):
    find = nums[k]
    i = 0
    j = n - 1
    while i < j:
        if nums[i] + nums[j] == find:
            if i != k and j != k:
                answer += 1
                break
            elif i == k:
                i += 1
            elif j == k:
                j -= 1
        elif nums[i] + nums[j] < find:
            i += 1
        else:
            j -= 1

print(answer)

