n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

selected = []
def print_selected():
    for num in selected:
        print(num, end=' ')
    print()

def dfs(curr_idx, cnt):
    if cnt == m:
        print_selected()
        return

    for i in range(curr_idx, n):
        selected.append(arr[i])
        dfs(i + 1, cnt + 1)
        selected.pop()

dfs(0, 0)

