def solution(people, limit):
    people.sort()

    weight = 0
    answer = 1
    for person in people:
        if weight + person >= limit:
            answer += 1
            weight = person
            continue
        weight += person

    return answer


if __name__ == '__main__':
    print(solution([70, 50, 80, 50], 100))
    print(solution([70, 80, 50], 100))