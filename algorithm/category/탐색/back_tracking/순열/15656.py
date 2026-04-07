import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def dfs(cnt, selected):
    if cnt == m:
        print(*selected)
        return

    for i in range(n):
        dfs(cnt + 1, selected + [nums[i]])


n, m = map(int, input().split())

nums = list(map(int, input().split()))
nums.sort()

dfs(0, [])

