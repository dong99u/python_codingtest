def solution(s):
    s = s[2:-2].split('},{')
    s.sort(key=len)
    answer = []

    for elem in s:
        nums = elem.split(',')
        for num in nums:
            if num not in answer:
                answer.append(int(num))

    return answer

if __name__ == '__main__':
    print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))