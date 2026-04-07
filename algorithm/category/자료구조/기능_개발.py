from collections import deque
import math

def solution(progresses, speeds):
    q = deque()
    n = len(progresses)

    answer = []

    for i in range(n):
        q.append(math.ceil((100 - progresses[i]) / speeds[i]))

    prev = q[0]
    count = 1
    for i in range(1, n):
        if prev > q[i]:
            count += 1
        else:
            answer.append(count)
            count = 1
            prev = q[i]

    answer.append(count)
    return answer


if __name__ == '__main__':
    print(solution([93, 30, 55], 	[1, 30, 5]))
    print(solution())