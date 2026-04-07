import sys
input = sys.stdin.readline

n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))

arr1.sort()

for i in range(m):
    find = False
    start = 0
    end = n - 1
    target = arr2[i]

    while start <= end:
        mid = (start + end) // 2

        if arr1[mid] > target:
            end = mid - 1
        elif arr1[mid] < target:
            start = mid + 1
        else:
            find = True
            break

    if find:
        print(1)
    else:
        print(0)
