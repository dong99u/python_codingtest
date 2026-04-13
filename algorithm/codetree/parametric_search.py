import sys; input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

def is_valid(k):
    count = 0
    for num in arr:
        count += num // k

    return count >= m

def search():
    left, right = 1, max(arr)
    result = 0
    while left <= right:
        mid = (left + right) // 2

        if is_valid(mid):
            result = max(result, mid)
            left = mid + 1

        else:
            right = mid - 1

    return result

print(search())

