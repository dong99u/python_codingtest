def solution(n, stations, w):
    answer = 0
    coverage = 2 * w + 1

    position = 1
    station_idx = 0

    while position <= n:
        if station_idx < len(stations) and position >= stations[station_idx] - w:
            position = stations[station_idx] + w + 1
            station_idx += 1
        else:
            answer += 1
            position += coverage

    return answer


if __name__ == '__main__':
    print(solution(11, [4, 11], 1))
    print(solution(16, [9], 2))