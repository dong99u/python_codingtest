import sys
INF = sys.maxsize

n = int(input())
arr = list(map(int, input().split()))
operators = list(map(int, input().split()))

min_val = INF
max_val = -INF


def dfs(index, curr_result):
    global min_val, max_val

    if index == n:
        min_val = min(min_val, curr_result)
        max_val = max(max_val, curr_result)
        return

    for i in range(4):
        if operators[i] > 0:
            operators[i] -= 1

            if i == 0:
                new_result = curr_result + arr[index]
            elif i == 1:
                new_result = curr_result - arr[index]
            elif i == 2:
                new_result = curr_result * arr[index]
            else:
                if curr_result < 0:
                    new_result = -(-curr_result // arr[index])
                else:
                    new_result = curr_result // arr[index]

            dfs(index + 1, new_result)

            operators[i] += 1

dfs(1, arr[0])

print(max_val)
print(min_val)
