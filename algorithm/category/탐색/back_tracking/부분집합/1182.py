n, s = map(int, input().split())
nums = list(map(int, input().split()))

def dfs(idx, sum_val, cnt):
    if idx == n:
        if cnt > 0 and sum_val == s:
            return 1
        return 0

    result = 0

    result += dfs(idx + 1, sum_val + nums[idx], cnt + 1)
    result += dfs(idx + 1, sum_val, cnt)

    return result


answer = dfs(0, 0, 0)

print(answer)

