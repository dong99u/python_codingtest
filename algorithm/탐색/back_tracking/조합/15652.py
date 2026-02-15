import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def dfs(start_idx, cnt, selected):
    if cnt == m:
        print(*selected)
        return

    for i in range(start_idx, n + 1):
        dfs(i, cnt + 1, selected + [i])

n, m = map(int, input().split())

dfs(1, 0, [])