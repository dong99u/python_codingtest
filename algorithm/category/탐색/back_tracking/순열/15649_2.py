def dfs(cnt):
    if cnt == m:
        print(' '.join(map(str, result)))
        return

    for i in range(1, n + 1):
        if not visited[i]:
            visited[i] = True
            result.append(i)
            dfs(cnt + 1)

            visited[i] = False
            result.pop()


n, m = map(int, input().split())

visited = [False] * (n + 1)
result = []

dfs(0)