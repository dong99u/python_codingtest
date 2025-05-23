from collections import deque
import math

def solution(progresses, speeds):
    d = deque()
    n = len(progresses)

    for i in range(n):
        d.append(math.ceil((100 - progresses[i]) / speeds[i]))

    count = 1
    answer = []

    prev = d[0]
    for i in range(1, n):
        if prev < d[i]:
            answer.append(count)
            count = 1
            prev = d[i]
            continue

        count += 1

    answer.append(count)

    return answer

if __name__ == '__main__':
    print(solution([93, 30, 55], 	[1, 30, 5]))




