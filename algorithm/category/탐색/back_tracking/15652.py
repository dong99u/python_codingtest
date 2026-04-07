n, m = map(int, input().split())

result = []

def dfs(curr_num):
    if len(result) == m:
        print(*result)
        return

    for i in range(curr_num, n + 1):
        result.append(i)
        dfs(i)
        result.pop()

dfs(1)