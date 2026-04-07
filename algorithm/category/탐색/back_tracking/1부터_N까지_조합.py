def solution(N):
    if N <= 3:
        return []

    arr = [i for i in range(N + 1)]
    visited = [False] * (N + 1)

    answer = []
    def dfs(num, result):
        if sum(result) > 10:
            return
        if sum(result) == 10:
            answer.append(result)
            return

        for i in range(num, N + 1):
            if visited[i]:
                continue

            visited[i] = True
            dfs(i, result + [i])

            visited[i] = False

    dfs(1, [])

    return answer


if __name__ == '__main__':
    print(solution(5))
    print(solution(2))
    print(solution(7))