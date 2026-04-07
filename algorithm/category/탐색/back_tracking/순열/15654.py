n, m = map(int, input().split())

nums = list(map(int, input().split()))

nums.sort()

selected = []
answer = []

visited = set()

def dfs(cnt):
    if cnt == m:
        answer.append(selected[:])
        return

    for i in range(n):
        if nums[i] not in visited:
            selected.append(nums[i])
            visited.add(nums[i])
            dfs(cnt + 1)
            visited.remove(nums[i])
            selected.pop()

dfs(0)

for ans in answer:
    for a in ans:
        print(a, end=' ')
    print()