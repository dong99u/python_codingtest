def merge_sort(arr):
    """
    병합 정렬 - 기본 버전
    """
    # 기저 조건: 원소가 1개 이하면 이미 정렬됨
    if len(arr) <= 1:
        return arr

    # 1. 분할 (Divide)
    mid = len(arr) // 2
    left = arr[:mid]      # 왼쪽 절반
    right = arr[mid:]     # 오른쪽 절반

    # 2. 정복 (Conquer) - 재귀적으로 정렬
    left = merge_sort(left)
    right = merge_sort(right)

    # 3. 결합 (Combine) - 병합
    return merge(left, right)


def merge(left, right):
    """
    정렬된 두 배열을 하나로 병합
    """
    result = []
    i = j = 0

    # 두 배열을 비교하며 작은 것부터 추가
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # 남은 원소들 추가
    result.extend(left[i:])
    result.extend(right[j:])

    return result


# 테스트
arr = [5, 3, 8, 1, 2, 7, 4, 6]
print("정렬 전:", arr)
sorted_arr = merge_sort(arr)
print("정렬 후:", sorted_arr)
