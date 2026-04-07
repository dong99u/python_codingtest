import sys
input = sys.stdin.readline

n = int(input())

nums = []
for _ in range(n):
    nums.append(int(input()))

for i in range(n - 1):
    for j in range(n - 1 - i):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]

for num in nums:
    print(num)