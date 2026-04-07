def solution(s):
    answer = []

    for binary_str in s:
        stack = []
        count_110 = 0

        for char in binary_str:
            stack.append(char)

            if len(stack) >= 3 and stack[-3:] == ['1', '1', '0']:
                stack.pop()
                stack.pop()
                stack.pop()
                count_110 += 1

        remaining = ''.join(stack)

        insert_pos = 0
        for i in range(len(remaining) - 1, -1, -1):
            if remaining[i] == '0':
                insert_pos = i + 1
                break

        result = remaining[:insert_pos] + '110' * count_110 + remaining[insert_pos:]
        answer.append(result)

    return answer

if __name__ == '__main__':
    print(solution(["1110","100111100","0111111010"]))