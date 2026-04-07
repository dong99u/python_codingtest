import sys

input = sys.stdin.readline

N = int(input()) # 5
nums = input().rstrip() # 54321

nums_list = []

for num in nums:
    nums_list.append(int(num))

print(sum(nums_list))