import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

answer = 0
for k in range(n):
    find = arr[k]
    left, right = 0, n - 1

    while left < right:
        if arr[left] + arr[right] == find:
            if left != k and right != k:
                answer += 1
                break
            elif left == k:
                left += 1
            elif right == k:
                right -= 1
        elif arr[left] + arr[right] < find:
            left += 1
        else:
            right -= 1

print(answer)