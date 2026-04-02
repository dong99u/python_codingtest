import sys

input = sys.stdin.readline

INF = float('inf')

n = int(input())
arr = list(map(int, input().split()))
total_sum = sum(arr)

memo = {}


dp = [0] * (M + 1)

    result = INF
    result = min(result, min(backtrack(idx + 1, acc + arr[idx]), backtrack(idx + 1, acc)))

    memo[state] = result

    return result


answer = backtrack(0, 0)

print(answer)