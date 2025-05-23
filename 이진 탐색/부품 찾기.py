import sys

def binary_search(arr, target, start, end):
    if start > end:
        return 'no'
    mid = (start + end) // 2

    if arr[mid] == target:
        return 'yes'
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, end)
    else:
        return binary_search(arr, target, start, mid - 1)

n = int(input())
arr1 = list(map(int, input().split()))

m = int(input())
arr2 = list(map(int, input().split()))

arr1.sort()

answer = []
for i in arr2:
    answer.append(binary_search(arr1, i, 0, len(arr1) - 1))

print(answer)