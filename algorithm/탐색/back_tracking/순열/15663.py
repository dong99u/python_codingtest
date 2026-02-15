import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def dfs(cnt, selected):
    if cnt == m:
        selected = tuple(selected)
        if selected not in result:
            result.add(selected)
            print(*selected)

        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            dfs(cnt + 1, selected + [nums[i]])
            visited[i] = False

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

visited = [False] * n

result = set()

dfs(0, [])