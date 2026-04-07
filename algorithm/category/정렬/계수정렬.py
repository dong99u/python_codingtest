def solution(s):
    arr = [0] * 26

    for alphabet in s:
        idx = ord(alphabet) - ord('a')
        arr[idx] += 1

    answer = ''

    for i in range(len(arr)):
        for j in range(arr[i]):
            alpha = chr(i + ord('a'))
            answer += alpha

    return answer


if __name__ == '__main__':
    print(solution('hello'))
    print(solution('algorithm'))