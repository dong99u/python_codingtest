n, m = map(int, input().split())

selected = []
answer = []

visited = [False] * n

def dfs(cnt):
    if cnt == m:
        answer.append(selected[:])
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            selected.append(i + 1)
            dfs(cnt + 1)
            selected.pop()
            visited[i] = False

dfs(0)

for ans in answer:
    for i in ans:
        print(i, end=' ')
    print()
