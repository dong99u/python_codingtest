import sys

input = sys.stdin.readline

INF = float('inf')

n = int(input())
arr = list(map(int, input().split()))
total_sum = sum(arr)

memo = {}


def backtrack(idx, acc):
    state = (idx, acc)
    B = total_sum - acc
    if state in memo:
        return memo[state]
    if idx == n:
        if acc == 0 or acc == total_sum:
            return INF
        return abs(acc - B)

    result = INF
    result = min(result, min(backtrack(idx + 1, acc + arr[idx]), backtrack(idx + 1, acc)))

    memo[state] = result

    return result


answer = backtrack(0, 0)

print(answer)