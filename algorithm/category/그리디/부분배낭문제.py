def solution(items, weight_limit):
    values = []

    for idx, (weight, value) in enumerate(items):
        values.append((idx, value / weight))

    values.sort(key=lambda x: -x[1])

    answer = 0

    for idx, per in values:
        weight = items[idx][0]
        value = items[idx][1]

        if weight <= weight_limit:
            answer += value
            weight_limit -= weight
        else:
            answer += weight_limit * per
            break


    return round(answer, 2)

if __name__ == '__main__':
    print(solution([[10, 19], [7, 10], [6, 10]], 15))
    print(solution([[10, 60], [20, 100], [30, 120]], 50))