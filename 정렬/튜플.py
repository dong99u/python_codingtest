def solution(s):
    s = s[2:-2].split('},{')
    s = sorted(s, key=len)
    answer = []

    for elem in s:
        numbers = elem.split(',')
        for number in numbers:
            if int(number) not in answer:
                answer.append(int(number))

    return answer


if __name__ == '__main__':
    print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))