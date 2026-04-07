n, m = map(int, input().split())

visited = [False] * (n + 1)
result = []
def dfs(length):
    if length == m:
        for elem in result:
            print(elem, end=' ')
        print()

    for i in range(1, n + 1):
        if visited[i]:
            continue

        visited[i] = True
        result.append(i)

        dfs(length + 1)

        result.pop()
        visited[i] = False

dfs(0)
