import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n = int(input())
visited = [False] * n
tree = [[] for _ in range(n)]
parents = list(map(int, input().split()))

delete_node = int(input())

answer = 0
root = -1

for child in range(n):
    parent = parents[child]
    if parent == -1:
        root = child  # 루트 찾기
    else:
        tree[parent].append(child)

def dfs(v):
    visited[v] = True
    for child in tree[v]:
        dfs(child)

if delete_node == root:
    print(0)
else:
    dfs(delete_node)

