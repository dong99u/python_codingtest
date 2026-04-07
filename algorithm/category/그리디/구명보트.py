def solution(people, limit):
    people.sort()

    n = len(people)

    i = 0
    j = n - 1
    answer = 0

    while i <= j:
        if people[i] + people[j] <= limit:
            i += 1
        j -= 1

        answer += 1

    return answer

if __name__ == '__main__':
    print(solution([70, 50, 80, 50], 100))