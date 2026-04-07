n, m = map(int, input().split())

arr = []
visited = [False] * (n + 1)

def dfs(depth):
    if depth == m:
        print(*arr)
        return

    for i in range(1, n + 1):
        if visited[i]:
            continue

        visited[i] = True
        arr.append(i)

        dfs(depth + 1)

        arr.pop()
        visited[i] = False

dfs(0)