from collections import defaultdict

def solution(answers):
    students_answers = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]

    answers_count = defaultdict(int)

    for i in range(3):
        for j in range(len(answers)):
            k = j % len(students_answers[i])
            if students_answers[i][k] == answers[j]:
                answers_count[i + 1] += 1

    answer = []
    max_answer_count = max(answers_count.values())

    for k, v in answers_count.items():
        if v == max_answer_count:
            answer.append(k)

    return answer

if __name__ == '__main__':
    print(solution([1, 3, 2, 4, 2]))