n, m = map(int, input().split())

result = []

def dfs(length):
    if length == m:
        print(*result)
        return

    for i in range(1, n + 1):
        result.append(i)
        dfs(length + 1)
        result.pop()

dfs(0)