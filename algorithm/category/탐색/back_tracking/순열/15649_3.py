import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def dfs(cnt, selected):
    if cnt == m:
        print(*selected)
        return

    for i in range(1, n + 1):
        if not visited[i]:
            visited[i] = True
            dfs(cnt + 1, selected + [i])
            visited[i] = False



n, m = map(int, input().split())

visited = [False] * (n + 1)

dfs(0, [])