def solution(arr1, arr2):
    answer = []

    pointer1, pointer2 = 0, 0

    while pointer1 < len(arr1) and pointer2 < len(arr2):
        if arr1[pointer1] < arr2[pointer2]:
            answer.append(arr1[pointer1])
            pointer1 += 1
        else:
            answer.append(arr2[pointer2])
            pointer2 += 1

    if pointer1 < len(arr1):
        answer.append(arr1[pointer1])
    else:
        answer.append(arr2[pointer2])

    return answer

if __name__ == '__main__':
    print(solution([1, 3, 5], [2, 4, 6]))