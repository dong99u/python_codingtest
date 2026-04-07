n, m = map(int, input().split())

result = []
visited = [False] * (n + 1)

def dfs(curr_num):
    if len(result) == m:
        print(*result)
        return

    for i in range(curr_num + 1, n + 1):
        if visited[i]:
            continue

        visited[i] = True
        result.append(i)

        dfs(i)

        result.pop()
        visited[i] = False

dfs(0)