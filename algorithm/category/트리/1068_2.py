import sys
input = sys.stdin.readline

def dfs(v):
    global answer
    visited[v] = True
    cnt = 0
    for next in graph[v]:
        if not visited[next] and next != delete_node:
            cnt += 1
            dfs(next)

    if cnt == 0:
        answer += 1

n = int(input())
graph = [[] for _ in range(n)]
arr = list(map(int, input().split()))
visited = [False] * n

for idx, num in enumerate(arr):
    if num == -1:
        root = idx
    else:
        graph[idx].append(num)
        graph[num].append(idx)

delete_node = int(input())

answer = 0

if delete_node == root:
    print(0)
else:
    dfs(root)
    print(answer)