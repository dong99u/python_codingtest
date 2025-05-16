from collections import defaultdict


def solution(N, stages):
    # 스테이지별 도전자 수를 구함
    challengers = [0] * (N + 2)

    for stage in stages:
        challengers[stage] += 1

    # 스테이지별 실패한 사용자 수 계산
    fails = {}
    total_count = len(stages)

    for i in range(1, N + 1):
        if challengers[i] == 0:
            fails[i] = 0

        else:
            fails[i] = challengers[i] / total_count
            total_count -= challengers[i]

    result = sorted(fails, key=lambda x: fails[x], reverse=True)
    return result




if __name__ == '__main__':
    print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
