def solution(N):
    answer = []

    def backtrack(sum, selected_nums, start):
        if sum > 10:
            return
        if sum == 10:
            answer.append(selected_nums[:])
            return

        for i in range(start, N + 1):
            selected_nums.append(i)
            backtrack(sum + i, selected_nums, i + 1)
            selected_nums.pop()


    backtrack(0, [], 1)
    return answer


if __name__ == '__main__':
    print(solution(5))