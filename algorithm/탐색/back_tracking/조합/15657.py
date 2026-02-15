import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def dfs(start_idx, cnt, selected):
    if cnt == m:
        print(*selected)
        return

    for i in range(start_idx, n):
        dfs(i, cnt + 1, selected + [nums[i]])


n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

dfs(0, 0, [])

