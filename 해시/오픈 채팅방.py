from collections import defaultdict
def solution(records):
    answer = []

    user_dict = defaultdict(str)

    for record in records:
        record = record.split(' ')
        if record[0] == 'Enter' or record[0] == 'Change':
            user_dict[record[1]] = record[2]

    for record in records:
        record = record.split(' ')
        if record[0] == 'Enter':
            answer.append(user_dict[record[1]] + '님이 들어왔습니다.')
        elif record[0] == 'Leave':
            answer.append(user_dict[record[1]] + '님이 나갔습니다.')

    return answer


if __name__ == '__main__':
    print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))