import sys
input = sys.stdin.readline

def dfs(n, source, mid, target):
    if n == 0:
        return

    dfs(n - 1, source, target, mid)
    results.append((source, target))
    dfs(n - 1, mid, source, target)


n = int(input())

results = []

dfs(n, 1, 2, 3)

print(len(results))
for elem in results:
    print(*elem)