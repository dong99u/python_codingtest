T = int(input())
INF = 1e9

for test_case in range(1, T + 1):
    answer = INF

    n, m = map(int, input().split())

    answer_code_time = list(map(int, input().split()))
    slow_code_time = list(map(int, input().split()))

    answer_code_time.sort()
    slow_code_time.sort()

    min_answer_time = answer_code_time[0]
    max_answer_time = answer_code_time[-1]
    min_slow_time = slow_code_time[0]

    if max_answer_time > min_slow_time:
        print("#%d" % test_case)
        print(-1)
        continue

    for time in range(max_answer_time, min_slow_time):
        if time / 2 >= min_answer_time:
            answer = min(answer, time)

    print("#%d" % test_case)
    if answer == INF:
        print(-1)
    else:
        print(answer)
