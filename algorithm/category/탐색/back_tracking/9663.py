def check(row):
    col = board[row]
    for i in range(row):
        if board[i] == col:
            return False

    if diag1[row + col]:
        return False
    if diag2[row - col + n - 1]:
        return False

    return True


def dfs(row_idx):
    global answer

    if row_idx == n:
        answer += 1
        return

    for col in range(n):
        board[row_idx] = col
        if not check(row_idx):
            continue
        diag1[row_idx + col] = True
        diag2[row_idx - col + n - 1] = True
        dfs(row_idx + 1)

        board[row_idx] = -1
        diag1[row_idx + col] = False
        diag2[row_idx - col + n - 1] = False


n = int(input())
board = [-1] * n
diag1 = [False] * (2 * n + 1) # 오른쪽 위 대각 row + col
diag2 = [False] * (2 * n + 1) # 왼쪽 위 대각 row - col + n - 1

answer = 0
dfs(0)

print(answer)