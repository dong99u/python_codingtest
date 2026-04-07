from bisect import bisect_left
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
find_nums = list(map(int, input().split()))

arr.sort()

for num in find_nums:
    idx = bisect_left(arr, num)
    if idx < len(arr) and arr[idx] == num:
        print(1)
    else:
        print(0)

