import sys
input = sys.stdin.readline

def dfs(start_idx, depth):
    if depth == 6:
        results.append(selected[:])
        return

    for i in range(start_idx, n):
        selected.append(nums[i])
        dfs(i + 1, depth + 1)
        selected.pop()


while True:
    input_list = list(map(int, input().split()))
    k = input_list[0]
    if k == 0:
        break
    nums = input_list[1:]
    n = len(nums)

    results = []
    selected = []
    dfs(0, 0)

    for row in results:
        print(*row)

    print()