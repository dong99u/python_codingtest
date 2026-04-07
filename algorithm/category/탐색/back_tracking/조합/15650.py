def print_selected():
    for num in selected:
        print(num, end=' ')
    print()

def dfs(curr_num, cnt):
    if cnt == m:
        print_selected()
        return

    for num in range(curr_num, n + 1):
        selected.append(num)
        dfs(num + 1, cnt + 1)
        selected.pop()

n, m = map(int, input().split())

selected = []

dfs(1, 0)