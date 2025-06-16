def solution(k, dungeons):
    visited = [False] * len(dungeons)
    answer = 0
    def dfs(curr, cnt):
        nonlocal answer
        answer = max(answer, cnt)

        for i in range(len(dungeons)):
            if visited[i] == True:
                continue
            if curr < dungeons[i][0]:
                continue

            visited[i] = True
            dfs(curr - dungeons[i][1], cnt + 1)
            visited[i] = False

    dfs(k, 0)

    return answer


if __name__ == '__main__':
    print(solution(80, [[80,20],[50,40],[30,10]]))