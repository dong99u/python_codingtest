import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def dfs(cnt, selected):
    if cnt == m:
        print(*selected)
        return

    for i in range(1, n + 1):
        dfs(cnt + 1, selected + [i])

n, m = map(int, input().split())

dfs(0, [])