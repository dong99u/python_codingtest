from collections import defaultdict

def solution(id_list, reports, k):
    answer = []
    mail_count = defaultdict(int)
    sue_dict = defaultdict(set)

    for id in id_list:
        mail_count[id] = 0

    for report in reports:
        report = report.split(' ')

        reporter = report[0]
        reportee = report[1]

        sue_dict[reportee].add(reporter)

    for key, value in sue_dict.items():
        if len(value) < k:
            continue

        for reporter in value:
            mail_count[reporter] += 1

    for id in id_list:
        answer.append(mail_count[id])

    return answer


if __name__ == '__main__':
    print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))

