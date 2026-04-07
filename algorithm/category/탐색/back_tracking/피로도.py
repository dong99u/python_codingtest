import sys
sys.setrecursionlimit(10 ** 6)

def solution(k, dungeons):
    n = len(dungeons)
    visited = [False] * n
    answer = 0

    def dfs(left, count):
        nonlocal answer
        answer = max(answer, count)

        for i in range(n):
            if not visited[i] and left >= dungeons[i][0]:
                visited[i] = True
                dfs(left - dungeons[i][1], count + 1)
                visited[i] = False

    dfs(k, 0)

    return answer

if __name__ == '__main__':
    print(solution(80, [[80,20],[50,40],[30,10]]))