def solution(arr1, arr2):

    pointer1 = pointer2 = 0

    answer = []

    while pointer1 <= len(arr1) - 1 and pointer2 <= len(arr2) - 1:
        if arr1[pointer1] < arr2[pointer2]:
            answer.append(arr1[pointer1])
            pointer1 += 1
        elif arr1[pointer1] > arr2[pointer2]:
            answer.append(arr2[pointer2])
            pointer2 += 1

    while pointer1 <= len(arr1) - 1:
        answer.append(arr1[pointer1])
        pointer1 += 1

    while pointer2 <= len(arr2) - 1:
        answer.append(arr2[pointer2])
        pointer2 += 1

    return answer


if __name__ == '__main__':
    print(solution([1, 3, 5], [2, 4, 6]))
    print(solution([1, 2, 3], [4, 5, 6]))