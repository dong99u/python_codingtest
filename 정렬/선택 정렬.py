def solution(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

if __name__ == '__main__':
    arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
    print(*solution(arr))